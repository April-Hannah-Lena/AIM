# Contributing

This collection contains distinct, precise research problems with an applied motivation and a traceable literature status. [README.md](README.md) provides the overview, [CATALOG.md](CATALOG.md) lists open targets, and [RESOLVED.md](RESOLVED.md) lists solved, claimed, and otherwise retired entries. Corrections to an existing statement or its status are especially useful. Further additions exclude numerical linear algebra; the original 001–300 and their review dates are preserved unless separately reviewed.

## Adding or revising a problem

1. Identify a source that explicitly poses the problem or clearly states that the requested case is unresolved. Prefer the author's paper, a scholarly monograph, a research survey, or an expert-maintained problem list.
2. State the mathematical question in full: the objects, parameter ranges, quantifiers, normalization, hypotheses, and requested conclusion. Define notation that is not standard for the intended research audience. Say when the entry is a narrower case or energy formulation of a broader conjecture.
3. Explain the applied connection in a short paragraph. Mathematical physics, PDEs, continuum mechanics, imaging, control, stochastic models, and foundational tools for these subjects are within scope. Follow the expansion's exclusion of numerical linear algebra when proposing further additions.
4. Give a short bibliography with direct, stable links and a verified chapter, section, theorem, or problem number when available. Distinguish a preprint from a published article. Two versions of one work are not independent confirmations.
5. Search for later proofs and counterexamples using the name of the problem, its mathematical formulation, the source's authors, and relevant synonyms. Read the hypotheses of any candidate resolution. Record the search date, topics, relevant partial results, and any conflicting claims.
6. Update the corresponding row in `data/*.json`, run the catalogue commands below, and explain any changes of scope. Do not count a solved problem, several parameter values of one question, or a restatement of another entry merely to maintain the count.

## Reporting a resolution

Include the permanent problem ID, a link to the proof or counterexample, and an explanation of why its hypotheses and conclusion match the entry. A title, abstract, search-engine snippet, or lack of citations alone is insufficient to adjudicate a disputed proof. Record the proof source, date, and the kind and scope of review actually performed.

Use **Solution claimed** for a matching complete resolution awaiting independent proof review. Use **Solved** only when a published result or a documented independent review supports a resolution of the exact target; identify that evidence in the record. An informal audit does not establish formal verification. A partial result leaves the unresolved target in the open catalogue, with the remaining question explained on its page.

For a complete resolution or matching claim placed on hold, move the entry out of the active collection into `research/`, preserving its original statement and permanent ID. Remove its row from `data/`, repair incoming links, and add its title, status, reason, and record path to `catalogue.json` as described below. Regenerate the indexes to list it in [RESOLVED.md](RESOLVED.md). A replacement must have a distinct statement and its own sources, and receives a new ID.

## Repository format

Each `problems/NNN-slug.md` has **Area**, **Status**, **Last checked**, and the sections **Problem statement**, **Applied significance**, **References**, and **Status review**. Use GitHub-compatible dollar delimiters for mathematics. The JSON files hold index metadata; the Markdown pages hold the mathematical content.

From the repository root, using Python 3.10 or later:

```sh
python3 scripts/catalogue.py --write
python3 scripts/catalogue.py --check
```

The write command rebuilds `README.md`, `CATALOG.md`, and `RESOLVED.md`; edit the metadata or the rendering functions in `scripts/catalogue.py` rather than the generated files. The check validates catalogue structure, local links, and freshness of all three documents. It does not verify proofs, certify open status, or check availability of external websites. Keep the README citation and [CITATION.cff](CITATION.cff) consistent when updating citation details.

### IDs, subject membership and publication batches

`catalogue.json` (schema version 1) declares the twelve ordered subject groups and the publication batches. A group's `key` names its existing `data/KEY.json` file. Its `title` supplies the heading in `CATALOG.md` and the subject links in the README. The metadata row fields are unchanged; membership comes from the containing file, independently of ID. New IDs can therefore appear in any subject group.

Allocate permanent IDs only after admission, in a single integration pass above the largest active or retired identifier. Append every admitted ID to exactly one named batch's `ids` array in the manifest. Batches record publication history, not subject ranges; their counts and review-date ranges are derived from active metadata. Existing pages keep their IDs and paths.

Never reuse an ID. If an entry is retired after a sourced correction, move its page into `research/`, repair incoming links, and add a `retired` record with `id`, `reason`, and a local `record` path. Include `title` and `status` for readable archive listings: `Solved`, `Solution claimed`, or `Retired` for another reason. Legacy records without these optional fields display as `Entry NNN` under other retained entries; a missing status never implies a solution. Here `retired` means outside the active catalogue, not necessarily solved. Keep its batch membership. The validator requires every issued ID to be either active or explicitly retired and rejects reuse, silent gaps, unindexed pages, and unregistered metadata files. Retirement decisions do not count as new problems.

Run `python3 scripts/test_catalogue.py` when changing the catalogue machinery. The integrity tests operate on temporary copies and remove their fixtures automatically.
