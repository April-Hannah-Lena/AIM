# Target audit: AIM 506

Contributor / submitter: **Siavash Sadeghi**.

Review date: 2 October 2026. This is a record of sources inspected and mathematical matching, not a claim of exhaustive literature coverage.

## Repository target and status

Problem: **506. Small-ball ratios for general symmetric product priors**.

Pinned revision: `aa776a01d7d48a79f93251af11fde9454b0aea95`.

Pinned source:
https://raw.githubusercontent.com/MColbrook/AIM/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/506-product-prior-small-ball-ratios.md

Main source also inspected:
https://raw.githubusercontent.com/MColbrook/AIM/main/problems/506-product-prior-small-ball-ratios.md

The page is labeled **Partial**, last checked 23 September 2026. The known cases do not establish the matching lower bound at every finite-energy center for every permitted reference density. The remaining target explicitly allows a counterexample. This claim addresses that remaining open general statement.

## Duplicate-claim checks

The current public repository audit found no matching AIM 506 submission.
It inspected all 12 indexed PRs (9 open, 3 closed), 10 available detailed PR
records, 2 discussion comments, no submitted reviews or inline comments,
82 changed-file records and 995 tracked main files. Four focused GitHub queries
for the problem number and subject returned no matches. The inspected main
commit matches the pinned revision above.

Full audit timestamp and scope are in `repository_submission_check.txt`.
Two unrelated closed index entries have unavailable detailed endpoints;
their retained titles, bodies and comments were checked. Private, deleted,
unsubmitted or unindexed work cannot be excluded. This is a bounded public
submission check, not a guarantee of mathematical novelty or priority.

## Primary mathematical source

B. Ayanbayev, I. Klebanov, H. C. Lie and T. J. Sullivan,
*Gamma-convergence of Onsager-Machlup functionals: II. Infinite product measures on Banach spaces*, Inverse Problems 38 (2022), 025006.

DOI: https://doi.org/10.1088/1361-6420/ac3f82

Published PDF:
https://wrap.warwick.ac.uk/161670/7/WRAP-convergence-Onsager-Machlup-functionals-II-Banach-spaces-2021.pdf

Author preprint: https://arxiv.org/abs/2108.04598
Version 3: 29 November 2021.

The published PDF's printed pages 6, 11 and 12 were visually inspected. The PDF has an extra cover page, so the zero-indexed PDF page numbers for these locations are also 6, 11 and 12.

Exact locations:
- Equation (3.1): weighted sequence-space norm.
- Assumption 4.1(A1)-(A3), printed page 6: the general measure assumptions.
- Definition 4.9, printed page 11: formal energy.
- Theorem 4.10, printed page 11: established upper bound and restricted lower bound.
- Conjecture 4.12, equation (4.15), printed page 12: the full target being disproved.

## Theorem-to-target match

| Target requirement | Counterexample verification |
|---|---|
| A weighted ell^p norm, 1 <= p < infinity | p = 2 and all norm weights alpha_k = 1 |
| Positive coordinate scales | gamma_k = 4^(-j) on block j |
| Center m in X | m = 0 |
| Independent scaled copies of one continuous even density | Independent Z_k, all with normalized density exp(-z^4) |
| Density strictly decreasing on nonnegative arguments | Immediate from the strict increase of z^4 for z >= 0 |
| Probability measure supported in X | E sum gamma_k^2 Z_k^2 <= 1/2 |
| Candidate h in X | norm(h)^2 = 1/7 |
| Finite formal energy | Q(h) = 1 |
| Contradiction to conjectured positive limit | Actual liminf = 0, whereas exp(-Q(h)) = exp(-1) > 0 |
| Positive denominator for every radius | Full support of the product measure, proved directly |

The density also satisfies optional smoothness and Fisher-information assumptions. However, sum_k (h_k/gamma_k)^2 is infinite. The lower bound in Theorem 4.10 therefore does not already apply at this center. The example targets the conjectured extension beyond that theorem.

## Scope of later-work search

Searches included combinations of the paper title/authors, Conjecture 4.12, small-ball ratios, quartic/exponential-fourth-power densities, product priors and counterexamples. The current repository review and the author's preprint were inspected. No matching published general resolution or counterexample was found in the consulted results.

An indexed discussion of a 'counterexample to Conjecture 4.12' was checked and concerned line-graph inertia, not this probability conjecture. Interacting Phi^4 field-measure results mentioned in the repository concern different measures/metrics, not the independent-coordinate law treated here. Neither is evidence of a solution to this target.

Searches are not exhaustive registry exports. No categorical priority claim is made.

## Evidence classification

Repository contributing rules:
https://raw.githubusercontent.com/MColbrook/AIM/aa776a01d7d48a79f93251af11fde9454b0aea95/CONTRIBUTING.md

The proposed mathematical disproof is complete as an analytic argument, but independent review remains outstanding. The appropriate submission classification is **Solution claimed**, not **Solved** or **Lean verified**. Supporting arithmetic checks are not an independent audit. The proof package is prepared for submission through a pull request; no catalogue status change is proposed. AI review scope and reproduction results are recorded in `REVIEW_AND_CHECKS.txt`.
