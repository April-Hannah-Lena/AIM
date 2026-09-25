# AIM — Open Applied Problems

A sourced collection of precise mathematical research problems in spectral theory, operator theory, applied mathematics, and related fields. Each entry has a self-contained statement, a discussion of applications or mathematical significance, references, and a dated literature-status review. There are several motivations for starting this repository which have been formed after consultation with a wide number of mathematicians from different areas:
- We are a few weeks (if that) away from an AI company or hobbyists from looping over our literature and solving many of our precise conjectures, without much understanding. We would like our community to solve them first and digest the consequences. This also creates an environment where ECRs can (and should) gain credit for human digestion of proofs in a protected environment.
- Many precise conjectures can now be solved by the best AI models on the market. We are mourning just like you are.
- It seems wise to collect the solutions in one place because they are coming in fast.

If one of your favourite open problems is solved here, we strongly encourage you to improve the proof, write about it, and publish it. We only have three hopes: (1) You will reference this GitHub repository as a proof source (see below), (2) Add your preprint to the repository, and (3) Update any information about the problem in the repository. We have set up a website

https://mathematics-explained.com

to collect human digestion, explanation and extension of proofs from this repo. Please email the collaborators of this repo for any comments and suggestions.




**665 open targets** (548 open, 117 partial) · **0 solved entries** · **0 Lean verified** · **0 solution claims**. Counts reflect the statuses recorded in this collection.

**[Browse all 665 open targets →](CATALOG.md)** · **[Solved and claimed solutions →](RESOLVED.md)**

## Browse by subject

| Subject group | Open targets |
| --- | ---: |
| [Spectral theory and spectral geometry](CATALOG.md#spectral-theory-and-spectral-geometry) | 25 |
| [Operators, matrices and computation](CATALOG.md#operators-matrices-and-computation) | 39 |
| [Inverse problems, control and dynamics](CATALOG.md#inverse-problems-control-and-dynamics) | 28 |
| [PDEs, fluids and materials](CATALOG.md#pdes-fluids-and-materials) | 32 |
| [Probability, statistics and learning](CATALOG.md#probability-statistics-and-learning) | 46 |
| [Numerical analysis and scientific computing](CATALOG.md#numerical-analysis-and-scientific-computing) | 29 |
| [Geometry and topology](CATALOG.md#geometry-and-topology) | 79 |
| [Combinatorics, optimization and information theory](CATALOG.md#combinatorics-optimization-and-information-theory) | 26 |
| [Waves, quantum systems and spectral geometry](CATALOG.md#waves-quantum-systems-and-spectral-geometry) | 32 |
| [Imaging, control, geometry and dynamics](CATALOG.md#imaging-control-geometry-and-dynamics) | 30 |
| [Fluids, kinetic theory and continuum mechanics](CATALOG.md#fluids-kinetic-theory-and-continuum-mechanics) | 48 |
| [Stochastic growth, populations and statistical mechanics](CATALOG.md#stochastic-growth-populations-and-statistical-mechanics) | 31 |
| [Many-body physics, quantum information and wave analysis](CATALOG.md#many-body-physics-quantum-information-and-wave-analysis) | 33 |
| [Nonlinear waves, fluids and kinetic equations](CATALOG.md#nonlinear-waves-fluids-and-kinetic-equations) | 33 |
| [Diffusion, materials and variational problems](CATALOG.md#diffusion-materials-and-variational-problems) | 59 |
| [Applied geometry, control and information](CATALOG.md#applied-geometry-control-and-information) | 49 |
| [Stochastic dynamics, reaction networks and applied optimization](CATALOG.md#stochastic-dynamics-reaction-networks-and-applied-optimization) | 46 |

## Reading the collection

Each [problem page](problems/) records its assumptions and quantifiers, an **Application** section, references, a status label, and its last review date. The Application section describes a supported use where one is clear, labels indirect connections, or states that no direct application has been identified. Active problems are numbered consecutively from 001. Complete deletion closes the gap: subsequent entries and their links are renumbered, and deleted numbers are not reserved. Cite the repository commit alongside an ID because numbering can change.

The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may imply one another; the count does not assert logical independence. Further additions exclude numerical linear algebra (NLA).

## Problem status

The same labels appear on problem pages and index rows. Only Open and Partial count as open targets; each problem counts once.

| Status | Meaning | Counted as open? |
| --- | --- | --- |
| 🔵 OPEN | The target is unresolved in the literature checked for the entry. | Yes |
| 🟡 PARTIAL | Some substantive cases of the stated target are proved; the page identifies what remains. | Yes |
| 🟠 SOLUTION CLAIMED | A source claims a complete resolution; independent proof review is outstanding. | No |
| ✅ SOLVED | A publication or documented independent audit supports a complete resolution. | No |
| 🏆 LEAN VERIFIED | A complete resolution has reviewed Lean kernel-checking evidence and matches the original target. | No |
| ⚪ NEEDS VERIFICATION | A statement or status issue requires further review. | No |
| ⚫ WITHDRAWN | The entry was removed for a documented reason; its ID and original statement are retained. | No |

An informal audit, including an AI audit, does not establish Lean verification. Formal proofs of special cases do not settle the whole target. See the [status and evidence requirements](CONTRIBUTING.md#status-and-evidence) and the [resolution archive](RESOLVED.md).

## What “open” means here

An open target is unresolved in its cited literature, and targeted searches found no later resolution of its exact statement as of the entry's review date. Partial results and restrictions are explained on its page. These bounded checks cannot guarantee that no proof exists, and adding a batch does not revalidate earlier entries.

See the [research methodology](research/METHODOLOGY.md), [source maps and exclusion records](research/README.md), and [publication batches](CATALOG.md#publication-batches) for the evidence behind the catalogue.

## Contributing

Suggestions, references, corrections, and resolution reports are welcome through [GitHub issues](https://github.com/MColbrook/AIM/issues) and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for admission criteria, status updates, and catalogue maintenance. A resolution report should link to the proof or counterexample and explain how it matches the exact target.

## Citing this collection

If you use this collection, please cite:

```bibtex
@misc{aim2026openproblems,
  author = {{Colbrook, Matthew J., George Stepaniants, and Alex Townsend}},
  title  = {{AIM — Open Applied Problems}},
  year   = {2026},
  url    = {https://github.com/MColbrook/AIM},
  note   = {GitHub repository}
}
```

Machine-readable citation metadata is available in [CITATION.cff](CITATION.cff). Include your access date or the commit used when referring to a particular version. For an individual problem, give its ID and the repository commit and cite the original sources listed in the entry as well. When using a solution, also cite its authors and the proof source linked from the status record.
