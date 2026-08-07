# Equivariant & geometric architectures

## Overview

Collider data are neither images nor sequences. An event is a variable-length set
of particles with no canonical ordering, carrying momenta that transform under the
Lorentz group, in a detector with its own geometry. Architectures respecting that
structure — permutation invariance, rotational or Lorentz equivariance, locality on a
graph — consistently outperform generic ones at equal size and often need far less
training data. The progression runs from images through sequences and trees to sets
and graphs, then to explicit symmetry constraints.

## Recommended starting points

- **The Machine Learning Landscape of Top Taggers**, Butter et al. (2019) ([arXiv:1902.09914](https://arxiv.org/abs/1902.09914)) — *the top-tagging comparison, the cleanest empirical read on what structure actually buys*
- **Symmetry Group Equivariant Architectures for Physics**, Bogatskiy et al. (2022) ([arXiv:2203.06153](https://arxiv.org/abs/2203.06153)) — *symmetry group equivariant architectures for physics, the dedicated review*
- **Graph Neural Networks in Particle Physics: Implementations, Innovations, and Challenges**, Thais et al. (2022) ([arXiv:2203.12852](https://arxiv.org/abs/2203.12852)) — *graph neural networks in particle physics, on implementations and innovations*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Energy Flow Networks: Deep Sets for Particle Jets**, Komiske et al. (2019) ([arXiv:1810.05165](https://arxiv.org/abs/1810.05165)) — *Energy Flow Networks: Deep Sets for jets, giving permutation invariance a physics-motivated form with a provable representation property*
- **ParticleNet: Jet Tagging via Particle Clouds**, Qu et al. (2020) ([arXiv:1902.08570](https://arxiv.org/abs/1902.08570)) — *ParticleNet: dynamic graph convolutions on particle clouds*
- **Equivariant Energy Flow Networks for Jet Tagging**, Dolan et al. (2021) ([arXiv:2012.00964](https://arxiv.org/abs/2012.00964)) — *equivariant Energy Flow Networks, adding explicit symmetry to the Deep Sets construction*
- **An Efficient Lorentz Equivariant Graph Neural Network for Jet Tagging**, Gong et al. (2022) ([arXiv:2201.08187](https://arxiv.org/abs/2201.08187)) — *LorentzNet: the paper that showed Lorentz equivariance could be made cheap enough to compete on speed as well as accuracy, which is what moved the idea out of proof-of-concept*
- **PELICAN: Permutation Equivariant and Lorentz Invariant or Covariant Aggregator Network for Particle Physics**, Bogatskiy et al. (2022) ([arXiv:2211.00454](https://arxiv.org/abs/2211.00454)) — *permutation and Lorentz symmetry imposed together, on pairwise invariants rather than on the four-vectors themselves. Competitive with far larger models, which is the cleanest evidence that symmetry substitutes for parameters*
- **Lorentz-Equivariant Geometric Algebra Transformers for High-Energy Physics**, Spinner et al. (2024) ([arXiv:2405.14806](https://arxiv.org/abs/2405.14806)) — *L-GATr: geometric algebra as the representation, which makes Lorentz equivariance a property of the data type rather than a constraint bolted onto the architecture, and scales to transformer size*
- **Lorentz Local Canonicalization: How to Make Any Network Lorentz-Equivariant**, Spinner et al. (2025) ([arXiv:2505.20280](https://arxiv.org/abs/2505.20280)) — *LLoCa, a general framework that renders any backbone network exactly Lorentz-equivariant*

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

- Symmetry-preserving generation is under [Generative models](generative.md).
- The scaling counter-argument is under [Foundation models](foundation-models.md).
- Cost-constrained deployment is under [Triggering](../applications/triggering.md).
