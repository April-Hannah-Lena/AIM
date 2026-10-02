# Status and source audit

Audit date: **1 October 2026**.

## Pinned target

Repository: https://github.com/MColbrook/AIM  
Inspected main commit: **aa776a01d7d48a79f93251af11fde9454b0aea95**.  
Commit check: https://github.com/MColbrook/AIM/commit/aa776a01d7d48a79f93251af11fde9454b0aea95

Problem 560, **Monotone variance in the Gaussian approximation to DrMMD flow**:

https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/560-drmmd-gaussian-variance-monotonicity.md

Raw pinned statement:

https://raw.githubusercontent.com/MColbrook/AIM/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/560-drmmd-gaussian-variance-monotonicity.md

The entry was labeled **Open**, with a recorded review date of 24 September 2026.
The target uses the fixed-target integral operator, the normalized witness, and
all finite positive regularization parameters. It does not assert Gaussian
invariance of the unrestricted transport flow.

## Primary mathematical source

Zonghao Chen, Aratrika Mustafi, Pierre Glaser, Anna Korba, Arthur Gretton,
and Bharath K. Sriperumbudur. **(De)-regularized Maximum Mean Discrepancy
Gradient Flow.** Journal of Machine Learning Research 26(235), 2025, pp. 1–77.

Publisher: https://www.jmlr.org/papers/v26/24-1574.html  
Published PDF: https://www.jmlr.org/papers/volume26/24-1574/24-1574.pdf  
Current arXiv record: https://arxiv.org/abs/2409.14980  
Pinned HTML: https://arxiv.org/html/2409.14980v3

The published Appendix C, especially pages 71–72 and Lemma C.2 on page 74,
contains the variance discussion and the limiting-regime arguments. The current
arXiv record inspected during this audit lists version 3, dated 24 November 2025.
The finite-positive-regularization conjecture remains in that version.

The source's witness convention can contain a positive factor of two. The proof
in this package follows the repository's normalized witness exactly. A positive
constant changes the time scale but not the requested sign.

## Search for later resolutions

The original package reports the following targeted web searches:

- `"DrMMD" "variance" "monotonicity"`
- `"DrMMD" "conjecture"`
- `"560" "Gaussian" "DrMMD"`
- variants involving Gaussian variance, de-regularized MMD, and monotonicity.

These searches and the current source record did not reveal a matching later
proof or counterexample. This is a dated search result, not a guarantee that no
unindexed resolution exists. The result here was not taken from a discovered
later resolution.

During submission preparation, Codex rechecked the publisher and arXiv records
and searched for DrMMD variance monotonicity and a finite-regularization proof.
No matching later resolution was found in those results. The separate repository
audit covered open and closed submissions and is recorded in
`repository_submission_check.txt`.

## Evidence convention

https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/CONTRIBUTING.md

The repository distinguishes an unreviewed complete claim from an independently
audited or published solution. This package fits **Solution claimed**. Separate Codex AI reviewers checked the mathematics and computation during
submission preparation. No human peer review or proof-assistant verification
has occurred. Repository duplicate checks are recorded separately in
`repository_submission_check.txt`.
