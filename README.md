# HEP–ML Living Guide

[![Deploy site](https://github.com/iml-wg/HEPML-LivingGuide/actions/workflows/deploy.yml/badge.svg)](https://github.com/iml-wg/HEPML-LivingGuide/actions/workflows/deploy.yml)
[![Site](https://img.shields.io/website?url=https%3A%2F%2Fiml-wg.github.io%2FHEPML-LivingGuide%2F&label=site)](https://iml-wg.github.io/HEPML-LivingGuide/)

A community-curated field guide to machine learning for particle physics.

**Live site:** <https://iml-wg.github.io/HEPML-LivingGuide/>

This resource replaces the [HEP–ML Living Review](https://github.com/iml-wg/HEPML-LivingReview),
which is now frozen as an archival bibliography. The Guide curates rather than
enumerates: it offers structured entry points into the literature, annotated
recommendations of foundational works, and community-driven guidance for
researchers navigating a now mature and rapidly diversifying field. See the
[About](https://iml-wg.github.io/HEPML-LivingGuide/about/) page for the full
rationale.

## Repository layout

```
.
├── docs/                       # Site content
│   ├── index.md                # Landing page
│   ├── how-to-use.md           # Editorial principles
│   ├── applications/           # Sections organised by HEP application
│   ├── methods/                # Sections organised by ML method
│   ├── resources/              # Reviews, benchmarks, related resources
│   ├── about.md                # About the Guide
│   ├── archived-review.md      # Pointers to the archived Living Review
│   ├── contribute.md           # How to contribute
│   ├── code-of-conduct.md
│   ├── cite.md
│   ├── assets/                 # Logo, favicon, images
│   ├── javascripts/            # MathJax config
│   └── stylesheets/            # Custom CSS
├── mkdocs.yml                  # MkDocs configuration
├── requirements.txt            # Python dependencies for building the site
├── .github/workflows/deploy.yml  # CI: build + deploy to GitHub Pages
├── CONTRIBUTING.md             # Short contribution guide (full version on the site)
├── LICENSE                     # CC BY 4.0 for content; MIT for code
└── README.md                   # This file
```

## Local preview

```bash
git clone git@github.com:iml-wg/HEPML-LivingGuide.git
cd HEPML-LivingGuide
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the short version, or the
[Contribute](https://iml-wg.github.io/HEPML-LivingGuide/contribute/) page on the
site for full guidance.

## License

- **Content** (everything in `docs/`) is licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Code** (configuration, workflows, scripts) is licensed under the MIT License.

See [LICENSE](LICENSE) for the full text.

## Maintainers

- Claudius Krause — Marietta Blau Institute for Particle Physics
- Ramon Winterhalder — Università degli Studi di Milano & INFN
- Matthew Feickert — University of Wisconsin–Madison
- Benjamin Nachman — SLAC & Stanford

## Citation

See the [Cite us](https://iml-wg.github.io/HEPML-LivingGuide/cite/) page.
