# Density estimation & likelihood ratios

## Overview

This is the single most reused idea in machine learning for particle physics: train a
classifier to separate two samples, and its output — suitably calibrated — approximates
the ratio of the two densities that produced them. Because a likelihood ratio is the
optimal test statistic, and because reweighting one sample into another is exactly a
ratio problem, that one result covers a remarkable amount of the field.

Three application areas that look unrelated are the same technique in different
clothing. In [simulation-based inference](../applications/unfolding-inference.md) the
ratio is between simulations at different parameter points, and it gives you a
likelihood. In unfolding, the ratio reweights simulation to data, iteratively, and it
gives you a measurement. In [anomaly detection](../applications/anomaly-detection.md)
the ratio is between a signal region and sidebands, and it gives you a search.

The complementary tool is explicit density estimation — normalizing flows and
diffusion models that provide a tractable likelihood rather than a ratio. The
distinction that matters in practice is that ratios are often easier to estimate
accurately than the densities themselves, since the hard normalization cancels, but
densities can be sampled from, and ratios cannot. Which you want depends on whether
you are measuring or generating.

The open problem across all of it is calibration. A classifier that ranks correctly
but is not calibrated gives a monotone function of the likelihood ratio rather than
the ratio itself, which is fine for a cut but fatal for an interval.

## Recommended starting points

- **The frontier of simulation-based inference**, Cranmer et al. (2019) ([arXiv:1911.01429](https://arxiv.org/abs/1911.01429)) — *the review that frames ratio estimation as the core of simulation-based inference*
- **Learning Likelihood Ratios with Neural Network Classifiers**, Rizvi et al. (2023) ([arXiv:2305.10500](https://arxiv.org/abs/2305.10500)) — *specifically on learning likelihood ratios with neural classifiers, and the practical pitfalls*
- **Modern Machine Learning for LHC Physicists**, Plehn et al. (2022) ([arXiv:2211.01421](https://arxiv.org/abs/2211.01421)) — *lecture notes covering classifiers, reweighting and density estimation in one place*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Approximating Likelihood Ratios with Calibrated Discriminative Classifiers**, Cranmer et al. (2015) ([arXiv:1506.02169](https://arxiv.org/abs/1506.02169)) — *the founding paper: a calibrated discriminative classifier approximates the likelihood ratio*
- **OmniFold: A Method to Simultaneously Unfold All Observables**, Andreassen et al. (2020) ([arXiv:1911.09107](https://arxiv.org/abs/1911.09107)) — *OmniFold, showing the same idea used iteratively as a reweighting scheme*
- **Anomaly Detection with Density Estimation**, Nachman et al. (2020) ([arXiv:2001.04990](https://arxiv.org/abs/2001.04990)) — *ANODE, using estimated densities in signal region and sidebands to construct a ratio for searches*
- **Classifying Anomalies THrough Outer Density Estimation (CATHODE)**, Hallin et al. (2021) ([arXiv:2109.00546](https://arxiv.org/abs/2109.00546)) — *CATHODE, which replaces the direct ratio with sampling from an interpolated density and outperforms it*

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

- Inference and unfolding applications are under [Unfolding & simulation-based inference](../applications/unfolding-inference.md).
- Searches built on ratios are under [Anomaly detection](../applications/anomaly-detection.md).
- Density estimators used for sampling are under [Generative models](generative.md).
- Calibration of the resulting statistics is under [Uncertainty quantification](uncertainty.md).
