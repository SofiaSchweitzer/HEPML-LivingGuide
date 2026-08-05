# Phenomenology

## Overview

Phenomenology connects theory to measurement: extracting the parameters of the
Standard Model and its extensions from data, and turning theoretical input into
predictions that can be confronted with it. This section covers the *fitting and
interpretation* end of that work, including parton distribution functions and global fits,
BSM parameter scans and reinterpretation, and symbolic approaches that produce
formulae rather than opaque functions.

The machinery for *generating* predictions — scattering amplitudes, phase-space
integration, parton showers and event generation — lives in
[Simulation & fast emulation](simulation.md) instead. The boundary is between
producing a prediction and inferring a parameter from one, and it was drawn there
because the generation stages share an architecture and a set of failure modes with
detector simulation, which makes them more useful read together than split by
whether the physics is theoretical or experimental.

Fits are a natural home for machine learning because the objects being fitted are
functions, not numbers, and because the parameter spaces are large enough that
scanning them exhaustively is not an option.

## Recommended starting points

- **Modern Machine Learning and Particle Physics Phenomenology at the LHC**, Ubiali (2026) ([arXiv:2602.03728](https://arxiv.org/abs/2602.03728)) — *modern machine learning and LHC phenomenology, the closest thing to a dedicated review*
- **Lecture notes on Machine Learning applications for global fits**, Alda (2026) ([arXiv:2604.07520](https://arxiv.org/abs/2604.07520)) — *lecture notes on machine learning for global fits*
- **Parton distribution functions**, Forte et al. (2020) ([arXiv:2008.12305](https://arxiv.org/abs/2008.12305)) — *a review of parton distribution functions, for the physics context the ML work sits in*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **An open-source machine learning framework for global analyses of parton distributions**, Ball et al. (2021) ([arXiv:2109.02671](https://arxiv.org/abs/2109.02671)) — *an open-source ML framework for global parton distribution analyses, the reference implementation in the area*
- **Back to the Formula -- LHC Edition**, Butter et al. (2021) ([arXiv:2109.10414](https://arxiv.org/abs/2109.10414)) — *symbolic regression applied to LHC observables, producing formulae rather than black-box functions*
- **Deep Learning Analysis of Deeply Virtual Exclusive Photoproduction**, Grigsby et al. (2020) ([arXiv:2012.04801](https://arxiv.org/abs/2012.04801)) — *deep learning applied to deeply virtual exclusive photoproduction, representative of the extraction problems in this area*

## Benchmarks, datasets & software

*Not yet compiled for this section.*

## Open questions

*What is settled here, what is contested, and what remains unsolved? This is
the part a bibliography structurally cannot provide, and often the most
useful paragraph on the page.*

## Further reading

*Relevant work that is not an entry point — too specialized, too recent, or simply not where a newcomer should start. Suggestions that do not fit the curated list above belong here rather than being turned away.*

*Nothing listed yet.*

## Cross-references

- Amplitudes, phase-space sampling and event generation are under [Simulation & fast emulation](simulation.md).
- Parameter inference from data is under [Density estimation & likelihood ratios](../methods/density-ratio.md).
- Reinterpretation overlaps with [Anomaly detection](anomaly-detection.md) for model-agnostic searches.
