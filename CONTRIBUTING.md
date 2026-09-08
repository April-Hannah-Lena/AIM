# Contributing

This collection contains 200 distinct, precise research problems with an applied motivation and a traceable literature status. Corrections to an existing statement or its status are especially useful. The expansion (101–200) focuses on applied mathematics and the established subject areas, excluding numerical linear algebra; the original 001–100 remain available.

## Adding or revising a problem

1. Identify a source that explicitly poses the problem or clearly states that the requested case is unresolved. Prefer the author's paper, a scholarly monograph, a research survey, or an expert-maintained problem list.
2. State the mathematical question in full: the objects, parameter ranges, quantifiers, normalization, hypotheses, and requested conclusion. Define notation that is not standard for the intended research audience. Say when the entry is a narrower case or energy formulation of a broader conjecture.
3. Explain the applied connection in a short paragraph. Mathematical physics, PDEs, continuum mechanics, imaging, control, stochastic models, and foundational tools for these subjects are within scope. Follow the expansion's exclusion of numerical linear algebra when proposing further additions.
4. Give a short bibliography with direct, stable links and a verified chapter, section, theorem, or problem number when available. Distinguish a preprint from a published article. Two versions of one work are not independent confirmations.
5. Search for later proofs and counterexamples using the name of the problem, its mathematical formulation, the source's authors, and relevant synonyms. Read the hypotheses of any candidate resolution. Record the search date, topics, relevant partial results, and any conflicting claims.
6. Update the corresponding row in `data/*.json`, run the catalogue commands below, and explain any changes of scope. Do not count a solved problem, several parameter values of one question, or a restatement of another entry merely to maintain the count.

## Reporting a resolution

Include a link to the proof or counterexample and explain why its hypotheses match the entry. A title, abstract, search-engine snippet, or lack of citations alone is insufficient to adjudicate a disputed proof. Move a resolved entry out of the active collection and record the reason in `research/`; preserve its history and identifier through version control. A replacement must have a distinct statement and its own sources.

## Repository format

Each `problems/NNN-slug.md` has **Area**, **Status**, **Last checked**, and the sections **Problem statement**, **Applied significance**, **References**, and **Status review**. Use GitHub-compatible dollar delimiters for mathematics. The JSON files hold index metadata; the Markdown pages hold the mathematical content.

From the repository root, using Python 3.10 or later:

```sh
python3 scripts/catalogue.py --write
python3 scripts/catalogue.py --check
```

The check validates catalogue structure and local links. It does not verify proofs, certify open status, or check availability of external websites.
