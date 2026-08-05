# Triggering

## Overview

The LHC produces collisions far faster than any system can record, so a trigger
decides within microseconds what to keep. Everything discarded is gone permanently,
which makes this the most consequential selection in the experiment and an unusually
demanding place to deploy machine learning: latency is fixed by hardware, models run
on FPGAs or ASICs, and the resource budget is measured in look-up tables. The
resulting literature is concerned less with accuracy than with accuracy achievable
under hard constraints — quantisation, pruning, and architectures chosen for what
synthesises well.

## Recommended starting points

- **Review of Machine Learning for Real-Time Analysis at the Large Hadron Collider experiments ALICE, ATLAS, CMS and LHCb**, Boggia et al. (2025) ([arXiv:2506.14578](https://arxiv.org/abs/2506.14578)) — *a review of machine learning for real-time analysis at the LHC*
- **Fast convolutional neural networks on FPGAs with hls4ml**, Aarrestad et al. (2021) ([arXiv:2101.05108](https://arxiv.org/abs/2101.05108)) — *fast convolutional networks on FPGAs with hls4ml — the practical starting point*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **Fast inference of deep neural networks in FPGAs for particle physics**, Duarte et al. (2018) ([arXiv:1804.06913](https://arxiv.org/abs/1804.06913)) — *made sub-microsecond neural network inference on FPGAs practical, and introduced the toolchain the field now uses*
- **Compressing deep neural networks on FPGAs to binary and ternary precision with HLS4ML**, Ngadiuba et al. (2020) ([arXiv:2003.06308](https://arxiv.org/abs/2003.06308)) — *binary and ternary precision networks, pushing the compression limit*
- **LHC physics dataset for unsupervised New Physics detection at 40 MHz**, Govorkova et al. (2021) ([arXiv:2107.02157](https://arxiv.org/abs/2107.02157)) — *trigger-level anomaly detection posed as a concrete dataset problem*

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

- The algorithms are under [Anomaly detection](anomaly-detection.md).
- Architecture cost trade-offs are under [Equivariant & geometric architectures](../methods/equivariant-geometric.md).
