# How to use this guide

The Living Guide is built around five commitments, taken directly from the
transition paper that introduced this resource:

1. **No claim of completeness.** Sections do not attempt to list every relevant
   paper. This is not a limitation — it is the point.
2. **Curation through community interest.** Sections exist because someone with
   expertise wrote them. Active subfields naturally attract more frequent updates.
3. **Annotation is required.** Every recommended paper or cluster of papers comes
   with a short explanation of what it establishes and how it relates to adjacent
   work. A list of links without context is a search result, not a guide.
4. **Complement INSPIRE-HEP and arXiv, do not compete with them.** Comprehensive
   bibliographic search already exists and works well. Finding papers is your
   job and the search engines' job; the Guide's job is telling you which few are
   worth reading first, and why. It provides what those tools do not: structured
   context and explicit guidance on where to start.
5. **Sustainability by design.** Sections are written as named, timestamped
   one-time contributions and remain stable until a new contribution updates them.
   A stale bibliography is merely incomplete; a stale guide is misleading, so every
   section displays when it was last reviewed and automatically carries a notice
   once that is more than **12 months** ago. You should never have to guess the
   vintage of a recommendation.

## Scope

The Guide covers machine learning for **particle physics**: collider physics and
phenomenology, formal and theoretical particle physics, lattice field theory, and
neutrino physics.

Nuclear and heavy-ion physics, astroparticle physics, cosmology, astronomical data
science, accelerator ML, and generic ML methodology with no particle-physics
content are deliberately out of scope — see [About](about.md) for the reasoning,
and [Related resources](resources/related.md) for where to go instead.

## What you'll find in each section

Each topical section follows a consistent structure:

| Element | Purpose |
|---|---|
| **Overview** | One to two paragraphs on the problem, why it matters in HEP, and how it connects to adjacent areas. |
| **Recommended starting points** | Three to six reviews, tutorials, or lecture notes, each with a one-sentence annotation. |
| **Curated paper list** | Foundational and representative papers, grouped thematically, each with a brief annotation. Not exhaustive by design. |
| **Benchmarks, datasets, and software** | Key references for reproducibility and comparison, where they exist. |
| **Contributor & vintage** | Who wrote the section, and when. |

## What you will *not* find

- A complete bibliography, or any attempt at one. For that, use INSPIRE-HEP,
  arXiv, or the [archived Living Review](archived-review.md). Those tools are
  good at finding papers and this resource is not trying to be.
- Peer review. Curation here is editorial, not adjudicative — inclusion is not an
  endorsement and exclusion is not a judgment of quality.
- Real-time freshness. Sections are timestamped. If a section is older than you'd
  like, the right response is to [contribute an update](contribute.md).

## A note on cross-cutting work

Many important papers sit at the intersection of an *application* (e.g. fast
calorimeter simulation) and a *method* (e.g. diffusion models). Where this is
the case, the paper is annotated in the section where it is most useful as an
entry point and **cross-linked** from the other. If you think a cross-link is
missing, please open an issue or a pull request.
