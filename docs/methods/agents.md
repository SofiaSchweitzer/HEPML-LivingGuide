# LLMs & agents

## Overview

Large language models and agentic systems are the most recent arrival, and the one
whose eventual role in particle physics is least clear. Proposed uses span assisting
analysis code, navigating software and documentation, extracting structured
information from the literature, and — most ambitiously — running parts of an analysis
autonomously. The claims outrun the evidence at present, which makes benchmarks
unusually important here: without them, this area risks accumulating demonstrations
rather than results. It is included in the Guide because the community is
investing in it seriously, not because the case is settled.

## Recommended starting points

- **Toward a Community Roadmap for High Energy Physics and Artificial Intelligence in China and Beyond**, Cai et al. (2026) ([arXiv:2605.03474](https://arxiv.org/abs/2605.03474)) — *a community roadmap covering where agents are expected to fit*
- **Building an AI-native Research Ecosystem for Experimental Particle Physics: A Community Vision**, Aarrestad et al. (2026) ([arXiv:2602.17582](https://arxiv.org/abs/2602.17582)) — *the AI-native research ecosystem vision paper, which is the most concrete statement of the ambition*

## Curated paper list

!!! note "This list is a seed, not a curated selection"
    A few landmark papers are listed to give the section a starting shape.
    A proper curated list — thematically grouped, with an annotation on every
    entry — is what this section still needs. See [Contribute](../contribute.md).

### Agents operating physics tools

- **Agents of Discovery**, Diefenbacher et al. (2025) ([arXiv:2509.08535](https://arxiv.org/abs/2509.08535)) — *an agent system aimed at the discovery task itself rather than at automating a known analysis*
- **HEPTAPOD: Orchestrating High Energy Physics Workflows Towards Autonomous Agency**, Menzo et al. (2025) ([arXiv:2512.15867](https://arxiv.org/abs/2512.15867)) — *orchestration across a multi-step workflow rather than a single tool, which is where the interesting failures live: an agent that operates one program correctly can still lose the thread across a chain of them*
- **MadAgents**, Plehn et al. (2026) ([arXiv:2601.21015](https://arxiv.org/abs/2601.21015)) — *agents driving a Monte Carlo generator: the theory-side counterpart, where the tool being operated has a well-defined interface and the correctness of the result can be checked against the physics*
- **AI Agents Can Already Autonomously Perform Experimental High Energy Physics**, Moreno et al. (2026) ([arXiv:2603.20179](https://arxiv.org/abs/2603.20179)) — *an orchestrated set of agents mimics full experimental analysis, from crafting the setup to emulating different stages of collaboration review to final paper writing*
- **AgentRivet: an automated system for producing Rivet routines from journal publications**, Costa et al. (2026) ([arXiv:2606.13535](https://arxiv.org/abs/2606.13535)) — *generates the missing Rivet routines from published papers, with automated code and physics review in the loop. The concrete case for agents in this field: only 39% of measurements currently have public Rivet routines, so the task is real, bounded, and its output is checkable*

### Evaluation

- **Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction**, Faroughy et al. (2026) ([arXiv:2605.13950](https://arxiv.org/abs/2605.13950)) — *a benchmark built on reproducing published analyses, so the target is a known answer rather than a subjective judgment of output quality*
- **Automating High Energy Physics Data Analysis with LLM-Powered Agents**, Gendreau-Distler et al. (2025) ([arXiv:2512.07785](https://arxiv.org/abs/2512.07785)) — *a diphoton cross-section measurement on ATLAS Open Data with quantitative metrics: success rate, error distribution, API calls and cost per task, across several model families. Reports what these systems actually cost and how often they fail, which most of this literature does not*
- **A Scientific Human-Agent Reproduction Pipeline**, Birk et al. (2026) ([arXiv:2604.18752](https://arxiv.org/abs/2604.18752)) — *evaluation with the human kept in the loop, which is the realistic deployment mode and a different question from full autonomy*

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

- Pre-training and representations are under [Foundation models](foundation-models.md).
