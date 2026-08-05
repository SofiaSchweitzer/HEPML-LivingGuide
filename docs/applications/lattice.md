# Lattice field theory

## Overview

The cost of sampling gauge configurations limits lattice calculations.
Markov chain Monte Carlo suffers critical slowing down near the continuum limit:
autocorrelation times grow, and topological sectors become effectively disconnected,
so more computing buys progressively less independent data. Flow-based sampling is
the most developed response. A normalizing flow is trained to map a simple
distribution to the target gauge measure and, combined with an accept/reject step,
gives *asymptotically exact* sampling rather than an approximation. Gauge symmetry
must be built into the architecture, so this section and equivariant architectures
are two views of similar work.

## Recommended starting points

- **Lecture Notes on Normalizing Flows for Lattice Quantum Field Theories**, Cheng et al. (2025) ([arXiv:2504.18126](https://arxiv.org/abs/2504.18126)) — *lecture notes on normalizing flows for lattice quantum field theories*
- **Machine-learning approaches to accelerating lattice simulations**, Lawrence (2025) ([arXiv:2502.02670](https://arxiv.org/abs/2502.02670)) — *a review of ML approaches to accelerating lattice simulations*
- **Snowmass 2021 Computational Frontier CompF03 Topical Group Report: Machine Learning**, Shanahan et al. (2022) ([arXiv:2209.07559](https://arxiv.org/abs/2209.07559)) — *the Snowmass computational-frontier report, for where this sits in the field's computing plans*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Flow-based generative models for Markov chain Monte Carlo in lattice field theory**, Albergo et al. (2019) ([arXiv:1904.12072](https://arxiv.org/abs/1904.12072)) — *introduced flow-based generative models for lattice field theory, in a scalar theory*
- **Equivariant flow-based sampling for lattice gauge theory**, Kanwar et al. (2020) ([arXiv:2003.06413](https://arxiv.org/abs/2003.06413)) — *extended this to gauge fields with the required equivariance — the foundational result for the area*
- **Reducing Autocorrelation Times in Lattice Simulations with Generative Adversarial Networks**, Urban et al. (2018) ([arXiv:1811.03533](https://arxiv.org/abs/1811.03533)) — *an earlier adversarial attempt at reducing autocorrelation times, useful as contrast*

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

- Symmetry machinery is under [Equivariant & geometric architectures](../methods/equivariant-geometric.md).
- Flow architectures are under [Generative models](../methods/generative.md).
