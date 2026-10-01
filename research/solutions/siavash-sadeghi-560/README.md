# AIM 560 — proposed affirmative resolution

**Gaussian variance monotonicity for de-regularized MMD**  
Prepared: 1 October 2026  
Contributor / submitter: **Siavash Sadeghi**  
Target: MColbrook/AIM, Problem 560, repository commit `aa776a01d7d48a79f93251af11fde9454b0aea95`

## Result

For the target `pi_s = N(0,s)`, Gaussian kernel `k(x,y) = exp(-(x-y)^2/2)`,
its integral operator `T_s` on `L^2(pi_s)`, and

```
h = T_s (T_s + lambda I)^(-1) (dN(0,v)/dpi_s - 1),
```

the proposed proof establishes

```
integral y h'(y) dN(0,v)(y) < 0
```

for **every `s > 0`, `lambda > 0`, and `0 < v < s`**. This includes the
repository's full target, which assumes `s > 2`.

The main argument proves negativity for every finite initial block of
Gaussian eigenmodes. Summation by parts then proves the sign for every bounded,
nonnegative, nonincreasing sequence of mode weights with a positive first weight,
including the DrMMD resolvent weights.

The scalar Gaussian moment variance therefore increases to `s` from any initial
variance in `(0,s)`. This is not a claim that the unrestricted transport flow
preserves Gaussian distributions.

## Read first

`aim560_proof.pdf` is the complete analytic argument. It includes the
operator normalization, eigenfunction calculation, finite-prefix lemma, convergence
of the series, the monotone-weight theorem, the scalar differential-equation
consequence, and the rigorous tail estimate used for certified examples.

`aim560_proof.tex` is the editable LaTeX source.

The universal proof does **not** depend on finite tests or numerical experiments.
The accompanying programs are supporting checks, not a proof-assistant certificate.

## Reproduce the exact checks

The exact script uses only the Python standard library; it performs no network
requests and no floating-point arithmetic in its mathematical checks. Python
3.10 or later is required by its type-annotation syntax. The current rerun uses Python 3.12.14; the original package used Python 3.13.5.

From this folder:

```sh
python3 verify_exact.py --json exact_certificates_reproduced.json
```

Expected summary:

```text
PASS: 2237 exact supporting checks
```

The checks include polynomial coefficient identities, a sum-of-squares identity,
representative mixed-derivative calculations, and outward-rounded enclosures of
seven **infinite** spectral sums. Their tails are bounded analytically; these are
not merely finite-sum approximations. `exact_certificates.json` and
`exact_checks.log` contain the recorded results.

## Reproduce the numerical cross-checks

Use an isolated Python 3.12 or later environment. The current checked environment
uses Python 3.12.14, NumPy 2.3.5, SciPy 1.18.1 and mpmath 1.3.0. These package
versions are pinned in `requirements.txt`; the original package used Python
3.13.5 and SciPy 1.17.0.

```sh
python3 -m venv .venv
```

Activate the environment using the command appropriate to your shell. For example,
on Linux/macOS:

```sh
. .venv/bin/activate
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python verify_numerics.py --json numerical_checks_reproduced.json
```

On Windows PowerShell, after activating `.venv\Scripts\Activate.ps1`:

```powershell
python -m pip install -r requirements.txt
$env:OPENBLAS_NUM_THREADS = "1"
python verify_numerics.py --json numerical_checks_reproduced.json
```

The numerical program compares the spectral formula with a direct Gaussian-kernel
Nystrom calculation at 256, 512 and 2,048 quadrature nodes. The direct calculation
solves the discretized integral operator and does not use the spectral reduction.
It is a separate computational route, **not** an independent mathematical review.
The 2,048-node stage may take appreciable CPU time and memory.

Recorded results:

- 12 direct-kernel comparisons at a portable tolerance of `2e-10`; the current
  measured maximum is recorded in `numerical_checks.log`.
- 6 closed-form endpoint comparisons at 70-digit precision; errors below `1e-60`.
- 363,810 finite-prefix sign checks, including eigenfunction degrees up to 400.

The script asserts a portable comparison tolerance of `2e-10`, rather than
requiring identical last digits. Its coarse-grid outputs are retained to expose
quadrature convergence. `numerical_checks.json` and `numerical_checks.log` record
the actual run. No numerical grid establishes the universal theorem.

The verifier explicitly rejects non-finite results and nonnegative integrals in
its valid test cases. Run the focused regression tests with:

```sh
python -m unittest -v test_verify_numerics.py
```

These tests cover 42 failure cases with inexpensive mocked computations.
`verification_checks.txt` records both normal and optimized-mode checks;
`ENVIRONMENT.txt` records the exact current dependency versions.

## Rebuild the PDF

A TeX installation with the packages listed in the source is required. Run twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim560_proof.tex
pdflatex -interaction=nonstopmode -halt-on-error aim560_proof.tex
```

## Review and repository status

This is an AI-generated research claim. Codex read the complete argument and
pinned target, and separate Codex AI reviewers checked the mathematics and
computational programs. No human peer review, journal acceptance or proof-assistant
verification is claimed. See `REVIEW_AND_CHECKS.txt` for review scope and limits. The appropriate requested repository status
under its evidence rules is **Solution claimed**, pending independent review,
not **Solved** or **Lean verified**. The package is prepared for submission through a pull request.

The target entry was labeled **Open** when inspected on 1 October 2026. A search
for the exact conjecture did not identify a later resolution, but cannot exclude
an unindexed or otherwise undiscovered result. See `status_and_sources.md` and the
`resolution_report.md` for the source audit and theorem-to-target match.

`SHA256SUMS.txt` gives integrity hashes of the delivered files other than itself.

## Submission contents

The proof, editable source, target report, scripts, regenerated check results,
review record and checksum manifest are submitted under
`research/solutions/siavash-sadeghi-560/`. The repository accepts a PR with the
pinned target, proof link, full-target comparison and reviewer disclosure.
This contribution proposes no catalogue or status change. The repository
duplicate-submission check is recorded in `repository_submission_check.txt`.
