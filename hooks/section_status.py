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
def _authors_line(section: dict, depth_prefix: str) -> str:
    authors = section.get("authors") or []
    if not authors:
        return (f"*Unclaimed — this section has no named author yet. "
                f"See [Contribute]({depth_prefix}contribute.md).*")
    parts = []
    for a in authors:
        name = a.get("name", "Unknown")
        orcid = a.get("orcid")
        # Link the name to its ORCID where one is given, so credit for a
        # section resolves to a person rather than to a string.
        label = f"[{name}](https://orcid.org/{orcid})" if orcid else name
        aff = a.get("affiliation")
        parts.append(f"{label} ({aff})" if aff else label)
    return "; ".join(parts)


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

    lines = [
        '!!! abstract "Section status"',
        f"    **Contributor:** {_authors_line(section, depth_prefix)}",
        "",
        f"    **Last reviewed:** {reviewed if reviewed else '—'}",
        "",
        f"    **Status:** {_STATUS_TEXT.get(status, status)}",
    ]
    block = "\n".join(lines)

    if state == "stale":
        interval = section.get("review_interval_months") or _CONFIG.get(
            "default_review_interval_months", 12
        )
        block += (
            "\n\n"
            '!!! warning "This section may be out of date"\n'
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
