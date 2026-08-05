# Reconstruction

## Overview

Reconstruction turns detector signals into physics objects: tracks from hits, showers into energies, 
particles into jets, and jets into flavor labels. It is where machine learning entered collider physics 
earliest and where it is now most thoroughly deployed — almost every major experiment runs ML taggers 
in production. The problems share a structure that has shaped architectures across the field: inputs are 
variable-length, unordered, and geometric, so sets, graphs, and attention were adopted here earlier 
than in most other areas, replacing image- and sequence-based approaches. Tracking is the hardest instance, 
being a combinatorial problem at a scale where even good heuristics struggle.

## Recommended starting points

- **Exploring jets: substructure and flavour tagging in CMS and ATLAS**, Malara (2024) ([arXiv:2410.14330](https://arxiv.org/abs/2410.14330)) — *jet substructure and flavour tagging as practised in CMS and ATLAS*
- **The Machine Learning Landscape of Top Taggers**, Butter et al. (2019) ([arXiv:1902.09914](https://arxiv.org/abs/1902.09914)) — *the top-tagging comparison: many architectures measured on one task, still the cleanest empirical read on what structure buys*
- **Graph Neural Networks for Particle Tracking and Reconstruction**, Duarte et al. (2020) ([arXiv:2012.01249](https://arxiv.org/abs/2012.01249)) — *graph neural networks for tracking and reconstruction*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Energy Flow Networks: Deep Sets for Particle Jets**, Komiske et al. (2019) ([arXiv:1810.05165](https://arxiv.org/abs/1810.05165)) — *Energy Flow Networks: permutation invariance in a physics-motivated form, with a representation guarantee*
- **ParticleNet: Jet Tagging via Particle Clouds**, Qu et al. (2020) ([arXiv:1902.08570](https://arxiv.org/abs/1902.08570)) — *ParticleNet: dynamic graph convolutions on particle clouds, long the standard strong baseline*
- **Particle Transformer for Jet Tagging**, Qu et al. (2022) ([arXiv:2202.03772](https://arxiv.org/abs/2202.03772)) — *Particle Transformer, with the JetClass dataset that made large-scale comparison possible*

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

- Architectures are under [Equivariant & geometric architectures](../methods/equivariant-geometric.md).
- Real-time constraints are under [Triggering](triggering.md).
