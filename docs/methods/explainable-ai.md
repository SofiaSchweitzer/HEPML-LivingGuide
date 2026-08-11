# Explainable AI & interpretability

## Overview

A network that tags jets better than any cut-based selection is useful. A network
whose reasoning you can state in a sentence is knowledge. The gap between those two
is what this section is about, and it is why the topic keeps coming back in a field
whose stated goal is understanding rather than prediction.

The two words are not synonyms, and the distinction is worth learning before reading
anything else here. *Interpretability* concerns the structural transparency of a model, 
meaning whether you can understand or approximate how it works inside. 
*Explainability* concerns its scientific content, meaning whether you can map what
it does onto physics you already know. A symbolic expression is interpretable, while
knowing that a tagger uses the same soft radiation pattern as a known observable is 
an explanation.

The practical toolkit divides along a related line. **Attribution** methods take a
trained network as given and ask which inputs drove a decision: Shapley values and
their SHAP approximations, layer-wise relevance propagation, saliency maps,
permutation importance. They are model-agnostic, cheap to bolt onto an existing
analysis, and they answer "which variables mattered". **Distillation** methods
instead replace the network with something a physicist can read, usually a closed-form
expression found by symbolic regression. They are expensive and do not always succeed,
but when they do the output is an equation you can differentiate, publish, and argue
about.

Particle physics has a structural advantage here that most machine-learning
application domains lack. We usually know what the answer ought to look like. The
learned function should respect Lorentz symmetry, factorize in the soft and collinear
limits, and reduce to a known observable in some corner of phase space. That gives
interpretability a target more precise than "a human finds this plausible", and it
means an explanation can be *wrong* in a checkable way. Several papers here work by
projecting a network onto a basis of known observables and asking how much of its
discrimination power survives.

## Recommended starting points

- **Interpretable machine learning in Physics**, Grojean et al. (2022) ([arXiv:2203.08021](https://arxiv.org/abs/2203.08021)) — *the Nature Reviews Physics comment, and the shortest route into Shapley values as they are actually used in collider analyses*
- **Explainable AI for High Energy Physics**, Neubauer & Roy (2022) ([arXiv:2206.06632](https://arxiv.org/abs/2206.06632)) — *a Snowmass letter of interest, a few pages mapping xAI techniques onto HEP problems*
- **Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl**, Cranmer (2023) ([arXiv:2305.01582](https://arxiv.org/abs/2305.01582)) — *the tool most symbolic-regression work in HEP is built on; read it before running it*
- **Interpretable Machine Learning in Physics: A Review**, Wetzel et al. (2025) ([arXiv:2503.23616](https://arxiv.org/abs/2503.23616)) — *physics-wide rather than HEP-specific, and the best single place to see how the same methods are used in other subfields*
- **Interpreting "Interpretability" and Explaining "Explainability" in Machine Learning in Physics**, Gambhir et al. (2026) ([arXiv:2606.26228](https://arxiv.org/abs/2606.26228)) — *read this first: it separates the two words the rest of the literature uses interchangeably, and gives the trade-offs each one costs you*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

- **What is the Machine Learning?**, Chang et al. (2017) ([arXiv:1709.10106](https://arxiv.org/abs/1709.10106)) — *an early attempt to ask what a jet classifier had actually learned, by planing away known variables and seeing what discrimination remained*
- **Mapping Machine-Learned Physics into a Human-Readable Space**, Faucett et al. (2020) ([arXiv:2010.11998](https://arxiv.org/abs/2010.11998)) — *projects a black-box tagger onto a basis of interpretable observables, turning "what did it learn" into a quantitative question*
- **Explainable AI for ML jet taggers using expert variables and layerwise relevance propagation**, Agarwal et al. (2020) ([arXiv:2011.13466](https://arxiv.org/abs/2011.13466)) — *layer-wise relevance propagation applied to taggers, and a worked example of attribution on a realistic HEP architecture*
- **Discovering Symbolic Models from Deep Learning with Inductive Biases**, Cranmer et al. (2020) ([arXiv:2006.11287](https://arxiv.org/abs/2006.11287)) — *the symbolic-distillation method: sparsify a GNN's messages, then symbolically regress them. The worked physics example is cosmological rather than collider, but the technique is what later HEP work builds on*
- **Back to the Formula — LHC Edition**, Butter et al. (2021) ([arXiv:2109.10414](https://arxiv.org/abs/2109.10414)) — *symbolic regression on matrix-element information, producing optimal LHC observables in closed form; the collider counterpart to the entry above*
- **Boosted top tagging and its interpretation using Shapley values**, Bhattacherjee et al. (2022) ([arXiv:2212.11606](https://arxiv.org/abs/2212.11606)) — *Shapley values applied end to end to a top tagger, and a concrete answer to what the attribution actually buys you*

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

- Architectures whose symmetry structure is itself a form of interpretability are under [Equivariant & geometric architectures](equivariant-geometric.md).
- Knowing when a model should not be trusted is the complementary problem, under [Uncertainty quantification & calibration](uncertainty.md).
- Taggers and classifiers that these methods are usually applied to are under [Reconstruction](../applications/reconstruction.md).
