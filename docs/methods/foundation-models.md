# Foundation models

## Overview

A foundation model is pre-trained on a large unlabelled corpus and then adapted to
many downstream tasks. The hope in particle physics is that the vast quantity of
unlabelled collider data — real and simulated — yields representations that transfer,
so individual analyses need less labeled data and less bespoke architecture
engineering. This is the newest and least settled area in the Guide, and it sits in
direct tension with the equivariant-architecture program: one says build the physics
in, the other says learn it from scale. Both have empirical support, and which wins
where is genuinely open rather than rhetorical.

## Recommended starting points

- **Building an AI-native Research Ecosystem for Experimental Particle Physics: A Community Vision**, Aarrestad et al. (2026) ([arXiv:2602.17582](https://arxiv.org/abs/2602.17582)) — *on building an AI-native research ecosystem for experimental particle physics*
- **Les Houches guide to reusable ML models in LHC analyses**, Araz et al. (2023) ([arXiv:2312.14575](https://arxiv.org/abs/2312.14575)) — *the Les Houches guide to reusable models, the practical prerequisite for any of this*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **OmniJet-alpha: The first cross-task foundation model for particle physics**, Birk et al. (2024) ([arXiv:2403.05618](https://arxiv.org/abs/2403.05618)) — *OmniJet-alpha, the first model in the field to demonstrate transfer across genuinely different tasks*
- **OmniLearn: A Method to Simultaneously Facilitate All Jet Physics Tasks**, Mikuni et al. (2024) ([arXiv:2404.16091](https://arxiv.org/abs/2404.16091)) — *OmniLearn, a complementary approach to multi-task jet physics*
- **Aspen Open Jets: Unlocking LHC Data for Foundation Models in Particle Physics**,  (2024) ([arXiv:2412.10504](https://arxiv.org/abs/2412.10504)) — *Aspen Open Jets: large-scale open collider data assembled specifically for pre-training*

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

- The opposing design philosophy is under [Equivariant & geometric architectures](equivariant-geometric.md).
- Agent-style applications are under [LLMs & agents](agents.md).
