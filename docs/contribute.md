# Contribute

The Living Guide grows through community contributions. There are three ways to
contribute, in increasing order of effort.

## 1. Suggest a paper or flag an error

Open an [issue](https://github.com/iml-wg/HEPML-LivingGuide/issues) on GitHub, or
open a pull request that edits the relevant section directly. Use the **edit
this page** pencil icon at the top of any page to jump straight to the file on
GitHub.

A good paper suggestion includes:

- The section it belongs in (or "I'm not sure where this fits")
- One or two sentences on **why** it should be included — what it establishes,
  who it helps
- The arXiv link and a full citation if available

Pull requests are reviewed against the [editorial criteria](how-to-use.md) by
the maintainers before being merged. We do not expect this to require heavy
moderation — the criteria are clear and the resource is self-selective.

## 2. Update an existing section

If you have expertise in an area and notice that a section is out of date or
incomplete, please consider revising it. Open a pull request with your changes
and update `last_reviewed` in the section's registry file (`sections/<id>.yml`). If your contribution is substantial, you
will be added as a section contributor.

## 3. Write a new section

This is the most valuable form of contribution. If you work in an area that the
Guide does not yet cover — or only covers as a stub — please consider writing
the section.

### Process

1. **Open an issue first** announcing your intent to write the section. This
   prevents duplicate effort and lets the maintainers and community comment on
   scope.
2. **Use the standard structure.** Every section contains: Overview,
   Recommended starting points, Curated paper list, Benchmarks/datasets/software,
   and Cross-references. See [Simulation](applications/simulation.md)
   for a worked template.
3. **Submit a pull request.** Include your name, a date stamp, and your ORCID or
   INSPIRE id if you want to be findable.
4. **Get credited.** Authors of section-level contributions are listed by name on
   the section they wrote, providing a concrete and citable record.

### What makes a good section

- **Opinionated.** Curation requires choices. Explain why a paper is in the list,
  not just that it exists.
- **Annotated.** Every entry should have at least a sentence of context. A bare
  link is a search result, not a guide entry.
- **Scoped.** Three to six starting points and a manageable curated list (often
  fewer than 30 entries). If you find yourself listing everything, you have
  drifted back into the old Living Review model.
- **Honest about boundaries.** If a topic spans two sections, cross-reference
  rather than duplicating.

## Section metadata and the 12-month notice

Each section has a small registry file at `sections/<id>.yml` holding its authors,
its status, and the date it was last reviewed. Claiming a section means editing
four fields there — see `sections/simulation.yml` for a filled-in example:

```yaml
status: published          # stub -> draft -> published
authors:
  - name: Your Name
    orcid: 0000-0000-0000-0000   # optional
    inspire: 1234567             # optional
stewards: [yourgithubhandle]
last_reviewed: 2026-08-05
```

Names render as plain text with small ORCID and INSPIRE badges after them,
linking to your profiles. Give one, both, or neither. We do not list
affiliations, because they date faster than the sections do, and a persistent
identifier answers "who is this?" better than a job title does.

Your INSPIRE id is the number in your author page URL, so
`https://inspirehep.net/authors/1234567` means `inspire: 1234567`. The older
dotted form works too. ORCID iDs are checked against their check digit when the
site builds, so a mistyped one shows up as a warning rather than as a link to
somebody else.

The citation block at the foot of the page is generated from the same entry, as
is the status banner at the top — never write either by hand.

If `last_reviewed` is more than 12 months old, the page automatically displays a
notice telling readers the recommendations may no longer be current. This is not a
criticism of the authors but it is a statement to the reader about what they are
looking at. Confirming that a section still holds and bumping the date is itself a
real contribution, and clears the notice.

## Where a suggestion lands

Curation implies exclusion. Two things follow, and we would rather be explicit about
them:

- **Omission is not a judgment.** A paper left out of a curated list is not being
  called unimportant. The list is a reading order for newcomers, not a ranking.
- **Suggestions are redirected, not rejected.** Work that is relevant but not a good
  *first* read belongs in the section's **Further reading** list. That is the normal
  outcome for a good paper that is simply too specialized to be someone's entry
  point.

Self-suggestion is welcome and completely normal — please just mention it, and it
will be judged by exactly the same criteria as anything else.

## Local preview

To preview your changes locally before opening a pull request:

```bash
# Clone the repo
git clone https://github.com/iml-wg/HEPML-LivingGuide.git
cd HEPML-LivingGuide

# Install dependencies (Python 3.10+ recommended)
pip install -r requirements.txt

# Serve the site locally with live reload
mkdocs serve
```

Then open <http://127.0.0.1:8000> in your browser. Edits to `.md` files will
trigger automatic rebuilds.

## Code of conduct

All contributors are expected to follow the [Code of conduct](code-of-conduct.md).
