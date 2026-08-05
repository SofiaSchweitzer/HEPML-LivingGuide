# Uncertainty quantification & calibration

## Overview

A classifier that is confident and wrong is worse than useless in a measurement.
Particle physics has an unusually demanding relationship with uncertainty: results
carry systematic uncertainties that must be defensible to a collaboration and a
referee, and "the network said so" is not an error budget. Two distinct problems live
here. The first is estimating uncertainty on a network's output — the usual Bayesian,
ensemble and calibration machinery. The second, more particular to this field, is what
to do when the systematic is a property of the *simulation* the network trained on, so
a mismodelled input yields a confidently biased output. Inference-aware training,
which optimises the final measurement rather than a proxy classification loss, is the
main response.

## Recommended starting points

- **Dealing with Nuisance Parameters using Machine Learning in High Energy Physics: a Review**, Dorigo et al. (2020) ([arXiv:2007.09121](https://arxiv.org/abs/2007.09121)) — *on handling nuisance parameters with machine learning, which is the version of the problem that usually dominates*
- **Solving Simulation Systematics in and with AI/ML**, Viren et al. (2022) ([arXiv:2203.06112](https://arxiv.org/abs/2203.06112)) — *on solving simulation systematics in and with ML*
- **Uncertainty in Physics and AI: Taxonomy, Quantification, and Validation**, Haussmann et al. (2026) ([arXiv:2605.10378](https://arxiv.org/abs/2605.10378)) — *the orienting reference: sorts out what the various uncertainties actually are before getting to methods, and treats validation as a first-class problem rather than an afterthought. Read this first*
- **Deep-Learning Jets with Uncertainties and More**, Bollweg et al. (2020) ([arXiv:1904.10004](https://arxiv.org/abs/1904.10004)) — *Bayesian networks for jet tagging: the reference demonstration that a HEP classifier can report a per-event uncertainty, and that the number means something*
- **Learning to Pivot with Adversarial Networks**, Louppe et al. (2017) ([arXiv:1611.01046](https://arxiv.org/abs/1611.01046)) — *training a classifier to be independent of a nuisance parameter by adversarially removing the information. The founding method for the second problem in the Overview, and still the baseline everything else is measured against*
- **INFERNO: Inference-Aware Neural Optimisation**, De Castro & Dorigo (2019) ([arXiv:1806.04743](https://arxiv.org/abs/1806.04743)) — *optimize the expected uncertainty on the final measurement rather than a classification loss — the paper that made "inference-aware" a category*
- **Uncertainty Aware Learning for High Energy Physics**, Ghosh et al. (2021) ([arXiv:2105.08742](https://arxiv.org/abs/2105.08742)) — *a systematic comparison of the ways systematics can be folded into training, and what each actually buys*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Development of systematic uncertainty-aware neural network trainings for binned-likelihood analyses at the LHC**, CMS Collaboration (2025) ([arXiv:2502.13047](https://arxiv.org/abs/2502.13047)) — *systematic-uncertainty-aware network training for binned analyses, from CMS*
- **Precision calibration of calorimeter signals in the ATLAS experiment using an uncertainty-aware neural network**, ATLAS Collaboration (2024) ([arXiv:2412.04370](https://arxiv.org/abs/2412.04370)) — *calorimeter calibration in ATLAS with uncertainty handled explicitly*
- **FAIR Universe HiggsML Uncertainty Challenge Competition**, Bhimji et al. (2024) ([arXiv:2410.02867](https://arxiv.org/abs/2410.02867)) — *the FAIR Universe HiggsML uncertainty challenge, which poses the problem as a shared task*

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

- Inference machinery is under [Density estimation & likelihood ratios](density-ratio.md).
- Unbinned systematics are under [Unfolding & simulation-based inference](../applications/unfolding-inference.md).
