# Unfolding & simulation-based inference

## Overview

Particle physics has excellent simulators and no tractable likelihood. Everything in
this section follows from that. Traditional analysis bridges the gap by binning a small
number of summary statistics, which is statistically lossy and forces the analyst to
decide in advance what to summarize. Simulation-based inference — also called
likelihood-free inference — instead uses machine learning to construct the likelihood,
the likelihood ratio, or the posterior directly from simulated samples.

Unfolding is the same problem viewed from the other end. It removes detector
distortions so a measurement can be compared with predictions, or reused years later
against theories that did not exist when the data were taken. Classical methods invert
a binned response matrix, while learned methods do it unbinned and in many dimensions at
once.

The particle-physics contribution to this cross-disciplinary field is distinctive.
Because the simulator's internals are accessible, quantities such as the joint
likelihood ratio of the latent process can be extracted and used as training targets —
"mining gold" — giving sample efficiency far beyond what a black-box simulator would
allow. That is why methods developed here are of interest well outside the field.

Not all inference in HEP is simulation-based. Weakly supervised searches infer a signal
from data alone, without trusting a simulation to model the background; that work lives
under [Anomaly detection](anomaly-detection.md).

## Recommended starting points

- **The frontier of simulation-based inference**, Cranmer et al. (2019) ([arXiv:1911.01429](https://arxiv.org/abs/1911.01429)) — *the standard cross-disciplinary review of simulation-based inference; the single best entry point*
- **Simulation-based inference methods for particle physics**, Brehmer et al. (2020) ([arXiv:2010.06439](https://arxiv.org/abs/2010.06439)) — *the particle-physics-specific treatment, closer to how these methods are actually deployed*
- **The Landscape of Unfolding with Machine Learning**, Huetsch et al. (2024) ([arXiv:2404.18807](https://arxiv.org/abs/2404.18807)) — *a survey of ML unfolding methods and how they relate to each other*
- **A Practical Guide to Unbinned Unfolding**, Canelli et al. (2025) ([arXiv:2507.09582](https://arxiv.org/abs/2507.09582)) — *a practical guide to unbinned unfolding, closer to implementation than the surveys*
- **simulation-based-inference.org** ([website](https://simulation-based-inference.org)) — *a living cross-disciplinary guide to SBI maintained outside HEP, with a searchable bibliography; the best place to see how the methods here connect to cosmology, neuroscience and epidemiology.*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Approximating Likelihood Ratios with Calibrated Discriminative Classifiers**, Cranmer et al. (2015) ([arXiv:1506.02169](https://arxiv.org/abs/1506.02169)) — *the foundational result that a calibrated classifier approximates the likelihood ratio — the idea nearly everything else here rests on*
- **Constraining Effective Field Theories with Machine Learning**, Brehmer et al. (2018) ([arXiv:1805.00013](https://arxiv.org/abs/1805.00013)) — *mining gold: exploiting simulator internals to make likelihood-ratio estimation dramatically more sample-efficient*
- **MadMiner: Machine learning-based inference for particle physics**, Brehmer et al. (2020) ([arXiv:1907.10621](https://arxiv.org/abs/1907.10621)) — *MadMiner, the reference implementation for collider EFT inference*
- **OmniFold: A Method to Simultaneously Unfold All Observables**, Andreassen et al. (2020) ([arXiv:1911.09107](https://arxiv.org/abs/1911.09107)) — *OmniFold: iterative, unbinned, simultaneously multi-dimensional unfolding by reweighting; the method most experiments have adopted*
- **Invertible Networks or Partons to Detector and Back Again**, Bellagente et al. (2020) ([arXiv:2006.06685](https://arxiv.org/abs/2006.06685)) — *conditional invertible networks learn the detector map and its inverse together, so unfolding becomes sampling from a per-event posterior over parton-level configurations rather than a single point estimate*

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

- The shared machinery is under [Density estimation & likelihood ratios](../methods/density-ratio.md).
- Inference without a trusted simulator is under [Anomaly detection](anomaly-detection.md).
- Systematics and coverage are under [Uncertainty quantification](../methods/uncertainty.md).
- Gradients through the simulator are under [Differentiable programming](../methods/differentiable.md).
