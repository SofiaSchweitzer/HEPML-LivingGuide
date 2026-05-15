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
and update the **Last updated** field. If your contribution is substantial, you
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
   and Cross-references. See [Anomaly detection](applications/anomaly-detection.md)
   for a worked template.
3. **Submit a pull request.** Include your name, affiliation, and a date stamp.
4. **Get credited.** Authors of section-level contributions are listed by name on
   the section they wrote, providing a concrete and citable record.

### What makes a good section

- **Opinionated.** Curation requires choices. Explain why a paper is in the list,
  not just that it exists.
- **Annotated.** Every entry should have at least a sentence of context. A bare
  link is a search result, not a guide entry.
- **Scoped.** Three to six starting points; a manageable curated list (often
  fewer than 30 entries). If you find yourself listing everything, you have
  drifted back into the old Living Review model.
- **Honest about boundaries.** If a topic spans two sections, cross-reference
  rather than duplicating.

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
