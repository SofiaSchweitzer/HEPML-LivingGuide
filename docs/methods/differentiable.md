# Differentiable programming

## Overview

Differentiable programming makes an entire analysis chain — simulation,
reconstruction, selection, statistical inference — differentiable end to end, so that
gradients of the final objective with respect to upstream choices are available. The
payoff is optimization of things that were previously tuned by hand or by scan:
detector geometry, selection cuts, even the simulator's own parameters. 
This is among the smallest and youngest areas in the Guide, and correspondingly 
the one where a good section would add the most.

## Recommended starting points

- **New directions for surrogate models and differentiable programming for High Energy Physics detector simulation**, Adelmann et al. (2022) ([arXiv:2203.08806](https://arxiv.org/abs/2203.08806)) — *the Snowmass contribution on surrogate models and differentiable programming for HEP*
- **Toward the end-to-end optimization of particle physics instruments with differentiable programming**, Dorigo et al. (2022) ([arXiv:2203.13818](https://arxiv.org/abs/2203.13818)) — *white paper on the use of differential programming for detector optimization*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **VegasFlow: accelerating Monte Carlo simulation across multiple hardware platforms**, Carrazza & Cruz-Martinez (2020) ([arXiv:2002.12921](https://arxiv.org/abs/2002.12921)) — *reimplementing Monte Carlo integration inside a machine-learning framework, which buys GPU execution and, as a by-product, gradients — the pragmatic route into differentiable programming for code that already exists*
- **Differentiable Matrix Elements with MadJax**, Heinrich et al. (2022) ([arXiv:2203.00057](https://arxiv.org/abs/2203.00057)) — *MadJax: differentiable matrix elements, making the theory end of the chain differentiable*
- **Branches of a Tree: Taking Derivatives of Programs with Discrete and Branching Randomness in High Energy Physics**, Kagan et al. (2023) ([arXiv:2308.16680](https://arxiv.org/abs/2308.16680)) — *taking derivatives of programs with discrete and branching structure — the central technical obstacle*
- **Progress in End-to-End Optimization of Detectors for Fundamental Physics with Differentiable Programming**, Aehle et al. (2023) ([arXiv:2310.05673](https://arxiv.org/abs/2310.05673)) — *progress on end-to-end optimization of detectors, the most ambitious application*
- **Differentiable MadNIS-Lite**, Heimel et al. (2024) ([arXiv:2408.01486](https://arxiv.org/abs/2408.01486)) — *gradients through the sampler itself, so the integration channels and the network are optimized together rather than the network being trained against a fixed sampler*

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

- Inference-aware objectives are under [Uncertainty quantification](uncertainty.md).
- Simulator surrogates are under [Simulation & fast emulation](../applications/simulation.md).
