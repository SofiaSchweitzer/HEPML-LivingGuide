"""
Generate the section status banner, the staleness notice and the per-section
citation block from the registry in ``sections/``.

Why a hook rather than hand-written Markdown: a "last updated" line that a
contributor has to remember to edit is a line that will silently go stale, and
a stale guide is worse than a stale bibliography because it makes an implicit
claim about the current state of the field. Deriving it from a machine-readable
registry means the notice appears whether or not anyone remembers.

Registered in mkdocs.yml via:

    hooks:
      - hooks/section_status.py

No network access, no dependencies beyond PyYAML, which mkdocs already needs.
"""

from __future__ import annotations

import datetime as _dt
import logging
import re
from pathlib import Path

import yaml

log = logging.getLogger("mkdocs.hooks.section_status")

_ROOT = Path(__file__).resolve().parent.parent
_SECTIONS_DIR = _ROOT / "sections"

_BY_PAGE: dict[str, dict] = {}
_CONFIG: dict = {}


# --------------------------------------------------------------------------
# Registry
# --------------------------------------------------------------------------
def _load_registry() -> None:
    """Read sections/*.yml into memory.

    Author entries may carry `orcid` and `inspire`. An `affiliation` key is
    accepted but ignored: affiliations date faster than the sections do, and a
    persistent identifier answers "who is this?" better than a job does.
    """
    global _CONFIG, _BY_PAGE
    cfg_path = _SECTIONS_DIR / "_config.yml"
    _CONFIG = yaml.safe_load(cfg_path.read_text()) if cfg_path.exists() else {}
    _BY_PAGE = {}
    for path in sorted(_SECTIONS_DIR.glob("*.yml")):
        if path.name.startswith("_"):
            continue
        data = yaml.safe_load(path.read_text()) or {}
        page = data.get("page")
        if not page:
            log.warning("section registry %s has no 'page' key; skipping", path.name)
            continue
        src = page[len("docs/"):] if page.startswith("docs/") else page
        data["_src_path"] = src
        _BY_PAGE[src] = data


def on_config(config, **kwargs):
    _load_registry()
    log.info("section_status: loaded %d registry entries", len(_BY_PAGE))
    return config


# --------------------------------------------------------------------------
# Freshness
# --------------------------------------------------------------------------
def _months_between(then: _dt.date, now: _dt.date) -> int:
    return (now.year - then.year) * 12 + (now.month - then.month)


def _freshness(section: dict, today: _dt.date):
    """Return (state, months_old) with state in {never, fresh, stale}."""
    raw = section.get("last_reviewed")
    if not raw:
        return "never", None
    if isinstance(raw, _dt.datetime):
        raw = raw.date()
    if isinstance(raw, str):
        raw = _dt.date.fromisoformat(raw)
    interval = section.get("review_interval_months") or _CONFIG.get(
        "default_review_interval_months", 12
    )
    age = _months_between(raw, today)
    return ("stale" if age >= interval else "fresh"), age


# --------------------------------------------------------------------------
# Blocks
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Banner presentation
#
# Every string and separator the banner prints lives here, and every one of
# them can be overridden from `status_banner:` in sections/_config.yml. The
# point is that changing a delimiter or a label is a one-line YAML edit rather
# than a patch to this file, so it stays reviewable by people who do not read
# Python. Spacing is deliberately NOT here: it is CSS, and lives as custom
# properties in docs/stylesheets/extra.css.
# --------------------------------------------------------------------------
_BANNER_DEFAULTS = {
    "type": "abstract",          # Material admonition type
    "css_class": "hg-status",    # hook for the spacing rules in extra.css
    "title": "Section status",
    "labels": {
        "contributor": "Contributor",
        "contributors": "Contributors",
        "last_reviewed": "Last reviewed",
        "status": "Status",
    },
    "separators": {
        "label": ":",      # between a field label and its value
        "authors": " · ",  # between one author and the next
        "name_ids": " ",   # between a name and its first identifier icon
        "ids": " ",        # between two icons belonging to the same author
        "no_date": "—",    # stands in for a missing last_reviewed
    },
    "stale": {
        "type": "warning",
        "css_class": "hg-status-stale",
        "title": "This section may be out of date",
    },
}


def _banner() -> dict:
    """Merge `status_banner:` from _config.yml over the defaults, one level deep.

    One level is enough for the shape above and keeps a partial override doing
    the obvious thing: setting a single separator must not silently drop the
    other three.
    """
    merged = {k: (dict(v) if isinstance(v, dict) else v)
              for k, v in _BANNER_DEFAULTS.items()}
    for key, value in (_CONFIG.get("status_banner") or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key].update(value)
        else:
            merged[key] = value
    return merged


_ORCID_RE = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$")
_INSPIRE_RECID_RE = re.compile(r"^\d+$")
_INSPIRE_BAI_RE = re.compile(r"^([A-Za-z.-]+\.)+\d+$")


def _orcid_checksum_ok(orcid: str) -> bool:
    """Validate the ISO 7064 MOD 11-2 check digit of an ORCID iD.

    A mistyped digit still looks like an ORCID and still produces a link that
    resolves, just to somebody else. Checking here turns a silent
    misattribution into a build-time warning.
    """
    total = 0
    for ch in orcid.replace("-", "")[:-1]:
        total = (total + int(ch)) * 2
    expected = (12 - total % 11) % 11
    return ("X" if expected == 10 else str(expected)) == orcid[-1].upper()


def _orcid_url(orcid, name: str):
    orcid = str(orcid).strip()
    # A YAML iD written without quotes is still a string here because of the
    # dashes, but normalise anyway in case someone pastes the full URI.
    orcid = orcid.rsplit("/", 1)[-1]
    if not _ORCID_RE.match(orcid):
        log.warning("section registry: %r has a malformed ORCID %r; skipping the "
                    "icon. Expected 0000-0000-0000-0000.", name, orcid)
        return None, None
    if not _orcid_checksum_ok(orcid):
        log.warning("section registry: ORCID %s for %r fails its check digit. "
                    "It is probably a typo, and it will link to the wrong person.",
                    orcid, name)
    return f"https://orcid.org/{orcid}", orcid


def _inspire_url(value, name: str):
    """Accept either an INSPIRE author record id or a legacy BAI.

    The record id is the number in the profile URL (inspirehep.net/authors/1234567).
    The BAI is the older dotted form (J.R.Thaler.1), which the current site does
    not resolve as a path, so it is sent to the author search instead.
    """
    value = str(value).strip().rstrip("/").rsplit("/", 1)[-1]
    if _INSPIRE_RECID_RE.match(value):
        return f"https://inspirehep.net/authors/{value}", value
    if _INSPIRE_BAI_RE.match(value):
        return f"https://inspirehep.net/authors?q={value}", value
    log.warning("section registry: %r has an unrecognised INSPIRE id %r; skipping "
                "the icon. Expected a record id (1234567) or a BAI (J.R.Thaler.1).",
                name, value)
    return None, None


def _id_link(icon: str, url: str, label: str) -> str:
    """An icon-only link, with an accessible name because the icon has none.

    attr_list carries aria-label so screen readers announce the destination,
    and title so a sighted user gets the same information on hover.
    """
    return (f"[:academicons-{icon}:]({url})"
            f'{{ .hg-idlink .hg-idlink--{icon} aria-label="{label}" title="{label}" }}')


def _authors_line(section: dict, depth_prefix: str) -> str:
    authors = section.get("authors") or []
    if not authors:
        return (f"*Unclaimed — this section has no named author yet. "
                f"See [Contribute]({depth_prefix}contribute.md).*")
    parts = []
    for a in authors:
        name = a.get("name", "Unknown")
        # The name stays plain text and the identifiers hang off it as icons.
        # Linking the name itself made credit ambiguous: a reader could not tell
        # whether the link led to the person or to the section they wrote.
        ids = []
        if a.get("orcid"):
            url, shown = _orcid_url(a["orcid"], name)
            if url:
                ids.append(_id_link("orcid", url, f"ORCID iD {shown} for {name}"))
        if a.get("inspire"):
            url, shown = _inspire_url(a["inspire"], name)
            if url:
                ids.append(_id_link("inspire", url, f"INSPIRE-HEP profile for {name}"))
        sep = _banner()["separators"]
        unit = sep["name_ids"].join([name, sep["ids"].join(ids)]) if ids else name
        # Wrap each author so the CSS can tell "second icon of this author"
        # from "first icon of the next author". The `+` combinator skips text
        # nodes, so without a wrapper the separator between authors is
        # invisible to it and the next author's first icon inherits the tight
        # icon-to-icon gap.
        parts.append(f'<span class="hg-author">{unit}</span>')
    return _banner()["separators"]["authors"].join(parts)


_STATUS_TEXT = {
    "stub": "Stub — a starting point only. The curated list is not yet written.",
    "draft": "Draft — assembled from the archived Living Review, not yet written "
             "by a named expert. Treat the selection as provisional.",
    "published": "Published — written and signed by its authors.",
}


def _status_block(section: dict, today: _dt.date, depth_prefix: str) -> str:
    state, age = _freshness(section, today)
    status = section.get("status", "stub")
    reviewed = section.get("last_reviewed")

    cfg = _banner()
    lab, sep = cfg["labels"], cfg["separators"]
    n_authors = len(section.get("authors") or [])
    who = lab["contributors"] if n_authors > 1 else lab["contributor"]

    def field(label: str, value: str) -> str:
        return f"    **{label}{sep['label']}** {value}"

    # Each field is its own paragraph so the vertical rhythm is a CSS decision
    # rather than a hardcoded <br>. See --hg-status-row-gap in extra.css.
    rows = [
        field(who, _authors_line(section, depth_prefix)),
        field(lab["last_reviewed"], str(reviewed) if reviewed else sep["no_date"]),
        field(lab["status"], _STATUS_TEXT.get(status, status)),
    ]
    header = f'!!! {cfg["type"]} {cfg["css_class"]} "{cfg["title"]}"'
    block = "\n\n".join([header] + rows)

    if state == "stale":
        interval = section.get("review_interval_months") or _CONFIG.get(
            "default_review_interval_months", 12
        )
        block += (
            "\n\n"
            f'!!! {cfg["stale"]["type"]} {cfg["stale"]["css_class"]}'
            f' "{cfg["stale"]["title"]}"\n'
            f"    It was last reviewed {age} months ago, beyond the {interval}-month\n"
            "    review interval. The recommendations below reflect the state of the\n"
            "    field at that time and may no longer be current. If you work in this\n"
            f"    area, please consider [contributing an update]({depth_prefix}contribute.md)."
        )
    return block


_LATEX_SPECIALS = {
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}",
}


def _latex_escape(text: str) -> str:
    """Escape LaTeX specials so the generated BibTeX actually compiles.

    Several section titles contain an ampersand ("Simulation & fast emulation",
    "Unfolding & inference"), which is a column separator in LaTeX and produces
    a hard error if pasted unescaped into a .bib file.
    """
    return "".join(_LATEX_SPECIALS.get(c, c) for c in text)


def _citation_block(section: dict) -> str:
    authors = section.get("authors") or []
    if not authors:
        return ""
    names = " and ".join(a.get("name", "Unknown") for a in authors)
    reviewed = section.get("last_reviewed") or ""
    year = str(reviewed)[:4] if reviewed else "n.d."
    slug = section["_src_path"].removesuffix(".md")
    # The resource name goes in the title rather than in `note`, because many
    # bibliography styles drop `note` entirely — and a bare "Generative models"
    # in a reference list tells the reader nothing about what they are citing.
    # The review date goes in `note` so a citation identifies which vintage of a
    # living document was used.
    reviewed_str = str(reviewed) if reviewed else "undated"
    return (
        "\n\n---\n\n"
        "## Cite this section\n\n"
        "Sections are named, timestamped contributions and are citable in their own\n"
        "right. Please cite the section rather than only the Guide as a whole.\n\n"
        "```bibtex\n"
        f"@misc{{HEPMLGuide:{section['id']},\n"
        f"  author = {{{_latex_escape(names)}}},\n"
        f"  title  = {{{{The HEP--ML Living Guide: {_latex_escape(section['title'])}}}}},\n"
        f"  year   = {{{year}}},\n"
        f"  note   = {{Community-curated section, last reviewed {reviewed_str}}},\n"
        f"  url    = {{https://iml-wg.github.io/HEPML-LivingGuide/{slug}/}}\n"
        "}\n"
        "```\n"
    )


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------
def on_page_markdown(markdown: str, page, config, files, **kwargs):
    section = _BY_PAGE.get(page.file.src_path)
    if section is None:
        return markdown

    today = _dt.date.today()
    depth_prefix = "../" * page.file.src_path.count("/")
    lines = markdown.split("\n")

    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            break
    else:
        insert_at = 0

    block = _status_block(section, today, depth_prefix)
    out = lines[:insert_at] + ["", block, ""] + lines[insert_at:]
    return "\n".join(out) + _citation_block(section)
