# Contributing

This collection contains distinct, precise research problems with an applied motivation and a traceable literature status. [README.md](README.md) provides the overview, [CATALOG.md](CATALOG.md) lists open targets, and [RESOLVED.md](RESOLVED.md) lists solved, claimed, and otherwise retired entries. Corrections to an existing statement or its status are especially useful. Further additions exclude numerical linear algebra; the surviving original problems, now numbered 001–292, and their review dates are preserved unless separately reviewed.

## Volunteer review

To request review, provide a short packet with the exact target, a fixed version of the argument, its main steps and new contributions, known gaps, relevant reproduction evidence, and a specific question. Propose a bounded task, such as checking one reduction, and agree the expected time commitment. Prepare the argument for review rather than asking volunteers to reconstruct it from a stream of automated output.

Review is voluntary: people may decline, limit its scope, or stop. Obtain permission before naming a reviewer and describe the work they actually checked. A limited check does not imply endorsement of the whole argument. Follow the [status and evidence rules](#status-and-evidence) when assigning mathematical labels.

## Adding or revising a problem

1. Identify a source that explicitly poses the problem or clearly states that the requested case is unresolved. Prefer the author's paper, a scholarly monograph, a research survey, or an expert-maintained problem list.
2. State the mathematical question in full: the objects, parameter ranges, quantifiers, normalization, hypotheses, and requested conclusion. Define notation that is not standard for the intended research audience. Say when the entry is a narrower case or energy formulation of a broader conjecture.
3. Include an **Application** section. Where a clear application is supported by the cited sources or follows directly from the statement, explain the connection and what resolving the conjecture would enable. Distinguish established uses, prospective consequences, and indirect theoretical connections. If no clear direct application is identified, say so explicitly and, if useful, describe the mathematical significance instead. Do not invent or stretch an application to fill the section. Mathematical physics, PDEs, continuum mechanics, imaging, control, stochastic models, and foundational tools for these subjects are within scope. Follow the expansion's exclusion of numerical linear algebra when proposing further additions.
4. Give a short bibliography with direct, stable links and a verified chapter, section, theorem, or problem number when available. Distinguish a preprint from a published article. Two versions of one work are not independent confirmations.
5. Search for later proofs and counterexamples using the name of the problem, its mathematical formulation, the source's authors, and relevant synonyms. Read the hypotheses of any candidate resolution. Record the search date, topics, relevant partial results, and any conflicting claims.
6. Update the corresponding row in `data/*.json`, run the catalogue commands below, and explain any changes of scope. Do not count a solved problem, several parameter values of one question, or a restatement of another entry merely to maintain the count.

## Reporting a resolution

Include the current problem ID and repository commit, a link to the proof or counterexample, and an explanation of why its hypotheses and conclusion match the entry. A title, abstract, search-engine snippet, or lack of citations alone is insufficient to adjudicate a disputed proof. Record the proof source, date, and the kind and scope of review actually performed.

Use the [status and evidence rules](#status-and-evidence) below. A partial result leaves the unresolved target in the open catalogue, with the remaining question explained on its page.

Unless the repository owner explicitly requests complete removal, for a complete resolution or matching claim placed on hold, move the entry out of the active collection into `research/`, preserving its original statement, application, and status record. Remove its row from `data/`, repair incoming links, and add its title, status, review date, reason, and record path to `catalogue.json` as described below. Regenerate the indexes to list it in [RESOLVED.md](RESOLVED.md). A replacement must have a distinct statement and its own sources, and receives a new ID.

## Status and evidence

Use exactly one canonical metadata value: `Open`, `Partially resolved`, `Solution claimed`, `Solved`, `Lean verified`, `Needs verification`, or `Withdrawn`. The [README legend](README.md#problem-status) gives their meanings and badges. Place the matching badge in the page's `Status` field near the top, before the first section; the generator uses the same badge in each index row. Update metadata and the page together.

- **Open / Partially resolved:** Keep these entries in `data/`. Mark Partial only for substantive proved cases within the full displayed target. Include nonempty `**Known cases:**` and `**Remaining target:**` notes in its Status review section. A weaker bound or a result for a different model is insufficient. Existing results can justify Partial; the label need not represent a new discovery. Open does not assert the absence of partial results; it is the default until an in-scope partial classification is documented.
- **Solution claimed:** Cite the complete claim and compare its hypotheses with the exact target. Independent proof review is still outstanding.
- **Solved:** Cite a published resolution or a complete argument with a documented independent audit. Identify the reviewer, whether human or AI, and what was reviewed. An informal audit does not establish formal verification.
- **Lean verified:** Supply the evidence below for a complete resolution. Formalized lemmas or special cases alone do not qualify.
- **Needs verification / Withdrawn:** Record the unresolved statement/status issue or the reason for withdrawal. Neither label asserts that the problem has been solved.

Only Open and Partial count as open targets, once each. All other statuses belong in the retained archive unless the repository owner explicitly requests complete removal. Preserve the original statement and sources for archived entries; place archive identifiers after the active sequence and update references when renumbering. Change `last_checked` only when a new literature or evidence review actually occurs; formatting and label migrations do not renew a literature check.

### Lean verification evidence

For `Lean verified`, set `verification_record` in the retained metadata to a local Markdown evidence record and link that record from the problem's status review. Include:

1. An immutable proof-source revision, the Lean version, and pinned dependency versions.
2. The theorem names and a comparison of their assumptions and conclusions with the full original target, including any definitions or reductions needed for that comparison.
3. Reproduction commands and a dated successful verification log. Say whether checks were run here or an external verification record was reviewed.
4. Transitive axiom output for each target theorem. Only `propext`, `Classical.choice`, and `Quot.sound` (or a subset) are acceptable; reject `sorryAx`, unproved custom axioms, and extra trust in native execution.

A successful build alone is insufficient. Recheck the evidence when its source revision changes. These categories follow the [NLA repository's status model](https://github.com/ajt60gaibb/OpenProblemsInNLA#problem-status).

## Repository format

Each `problems/NNN-slug.md` has **Area**, **Status**, **Last checked**, and the sections **Problem statement**, **Application**, **References**, and **Status review**. The Application section must contain an explanation or an explicit statement such as “No direct application is identified in this entry.” Such a statement is acceptable; an empty heading or unexplained placeholder is not. Retained problem records in `research/` use the same format. Protect mathematics from Markdown processing as shown below. The JSON files hold index metadata; the Markdown pages hold the mathematical content.

Use fenced code blocks labelled `math` for display equations and dollar-backtick delimiters for inline equations. Plain dollar delimiters allow Markdown to consume TeX escapes and interpret underscores or asterisks before MathJax sees them. In particular, Markdown turns `\left\{` into the invalid `\left{`. These protected forms are supported by [GitHub's math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions):

````markdown
An inline set is $`\left\{x,y\right\}`$.

```math
\left\{x\in\mathbb R:x>0\right\}
```
````

For named operators, use core TeX such as `\mathop{\mathrm{Per}}\nolimits(E)`; retain a space after a command when its operand begins with a letter. The catalogue check rejects unprotected math, unmatched delimiters, and unsupported operator-name macros throughout the Markdown files, including research notes.

From the repository root, using Python 3.10 or later:

```sh
python3 scripts/catalogue.py --write
python3 scripts/catalogue.py --check
```

The write command rebuilds `README.md`, `CATALOG.md`, and `RESOLVED.md`; edit the metadata or the rendering functions in `scripts/catalogue.py` rather than the generated files. The check validates catalogue structure, allowed statuses, page/metadata agreement, required application content, local links, and freshness of all three documents. For Lean verified entries it also requires a nonempty local verification record. It does not run Lean, verify proofs, assess the substance of an application or evidence record, certify open status, or check availability of external websites. Keep the README citation and [CITATION.cff](CITATION.cff) consistent when updating citation details.

For complete math-rendering QA, use the optional pinned dependencies below. They stay in a temporary environment; the ordinary catalogue commands require only the Python standard library.

```sh
python3 -m venv /tmp/aim-math-check
/tmp/aim-math-check/bin/pip install -r scripts/requirements-math.txt
npm install --prefix /tmp/aim-math-check --ignore-scripts --no-save mathjax-full@3.2.2
NODE_PATH=/tmp/aim-math-check/node_modules /tmp/aim-math-check/bin/python scripts/check_math.py
```

This check runs every Markdown file through GitHub's `cmark-gfm` parser, verifies that every equation survives with its TeX unchanged, and renders the resulting expressions with MathJax. It fails on lost equations, altered escapes, or MathJax error output. Compiling TeX extracted directly from the source does not test the preceding Markdown stage.

### IDs, subject membership and publication batches

`catalogue.json` (schema version 2) declares the ordered subject groups and the publication batches. A group's `key` names its existing `data/KEY.json` file. Its `title` supplies the heading in `CATALOG.md` and the subject links in the README. Each active row has `id`, `title`, `area`, `file`, `status`, and `last_checked`; membership comes from the containing file, independently of ID. New IDs can therefore appear in any subject group.

Allocate problem IDs only after admission, after the largest current identifier. Active entries must be consecutively numbered from 001. Append every admitted ID to exactly one named publication batch. Batches record publication history, not subject ranges; membership must follow each problem when numbering changes.

For an owner-requested complete removal, delete the page and metadata, remove retained copies and incoming references, remove its batch membership, and renumber the remaining active entries consecutively. Do not reserve deleted identifiers or retain removal records. Update filenames, headings, metadata, indexes, queue records, research references and batch memberships together. If an entry is archived rather than deleted, keep its statement and evidence in `research/` and put archive identifiers after the active sequence. The validator rejects gaps, duplicate IDs, stale reservations, unindexed pages and unregistered metadata. IDs can change after deletions; citations should include the repository commit and problem title.

Run `python3 scripts/test_catalogue.py` when changing the catalogue machinery. The integrity tests operate on temporary copies and remove their fixtures automatically.
