# Pólya literature and convention audit — 2026-09-08

This is a source-scope audit, not independent verification of every cited proof. Primary publisher pages, author preprints and theorem statements were checked. No external computational certificate was executed. Searches found no full resolution for arbitrary bounded connected Lipschitz domains; the July 2026 balls paper explicitly describes that general problem as open.

## Exact normalization and endpoints

Put `p=d/2`, `a=omega_d*|Omega|/(2*pi)^d`. The repository's indexing is Dirichlet `lambda_1,lambda_2,...` and Neumann `mu_0=0,mu_1,...`, with multiplicity. Its target is

```math
\mu_k\le (k/a)^{1/p}\le\lambda_k\qquad(k\ge1).
```

FLPS 2023, Remark 1.1, uses `mu_1=0` and writes `mu_{n+1} <= (n/a)^{1/p} <= lambda_n`, so the statements agree exactly after shifting the Neumann index. Their counting variable is frequency: eigenvalues are compared with `lambda^2`, not `lambda`. [Publisher full text](https://link.springer.com/article/10.1007/s00222-023-01198-1).

For energy `E>=0`, an equivalent endpoint-safe form is

```math
N_D^{\le}(E)\le aE^p\le N_N^{<}(E).
```

Here the Neumann count includes the zero eigenvalue when `E>0`, and both counts use multiplicity. Elementary verification: if `m=N_N^<(E)`, then `mu_m>=E`, and the eigenvalue bound gives `aE^p<=m` when `m>=1`; the case `E=0` is trivial. Conversely, if `mu_k>(k/a)^{1/p}`, choose `E` strictly between these numbers: `N_N^<(E)<=k<aE^p`, a contradiction. Dirichlet equivalence follows by evaluating at eigenvalues. Using `N_N^<=` instead gives an equivalent family only when required for every energy and interpreted with the appropriate one-sided limits. In fact the target implies `N_N^<=(E)>aE^p` for every positive `E`: if its value is `m`, then `mu_m>E`, so `aE^p<m`.

## Existing special classes

1. **FLPS, Inventiones 234 (2023), 129–169.** Theorem 1.2 proves Dirichlet Pólya for balls in every integer dimension `d>=2`; Theorems 1.4–1.5 and Corollary 1.6 establish Neumann disks. Theorem 1.12 covers both conditions on every circular sector of aperture `(0,2*pi]`. Theorem 1.8 transfers a valid inequality to a congruent tile of a domain satisfying it. The Neumann disk proof uses an explicit finite frequency interval and rational/integer computation. These are external established results; no script was rerun in this audit. This paper does not prove Neumann balls for `d>=3` or arbitrary domains. [Full text](https://link.springer.com/article/10.1007/s00222-023-01198-1).

2. **FLPS, JLMS 113 (2026), e70425; first published 6 February 2026.** Theorem 1.1 covers all **planar concentric annuli** `r<|x|<1`, `0<r<1`, every positive frequency; scaling covers arbitrary radii. It is Dirichlet only, not arbitrary doubly connected domains or higher-dimensional shells. The proof combines analytic regions with a rigorous finite parameter-region certificate. Full final-version theorem statements were accessible, but certificate execution and all estimates were not audited. [Published article](https://doi.org/10.1112/jlms.70425), [final arXiv text](https://arxiv.org/html/2505.21737v2).

3. **FLPS, arXiv:2607.29305v1, 31 July 2026.** Announces Neumann Pólya for balls in every `d>=3`. Section 1 states the general-domain conjecture remains open. The radial equation uses derivatives of ultraspherical Bessel functions; ordinary derivative Bessel zeros alone are not the physical spectrum in higher dimensions. The proof combines weighted lattice estimates, dimension-dependent Rayleigh trial functions and certified rational computations for residual ranges in dimensions `3,...,12`; analytic bounds handle the unbounded dimension/frequency ranges. Full HTML was inspected at the theorem, strategy and certification-description level. No journal publication or independent full verification was established in this audit. [Full preprint](https://arxiv.org/html/2607.29305v1).

4. **Yutian Li, arXiv:2607.25958v3, revised 5 August 2026.** Independently announces both all-dimensional Neumann balls and an analytic replacement for the finite disk step. Its abstract explicitly counts eigenvalues **strictly below energy** and claims every `d>=2`, radius `R>0`, energy `E>=0`. It reports printed finite calculations for `2<=d<=6` and exact-rational ancillary certification of a compact two-parameter estimate for `d>=7`. Only abstract/version metadata were audited; this is an independent announcement, not an independently checked campaign proof. [Current preprint](https://arxiv.org/abs/2607.25958).

5. **Guo–Miao–Wang–Zhan, arXiv:2511.17050v2.** Gives quantitative improvements for disks, balls and cylinders, including Neumann circular cylinders in three dimensions of every radius and height. Remark 1.10 records inheritance of Neumann Pólya under product with a finite interval when the base already satisfies it. It does not cover arbitrary bases without that hypothesis or arbitrary domains. Full-text statements were inspected. [Preprint](https://arxiv.org/html/2511.17050v2).

## Current general advances and their limits

6. **Jiang–Lin, CPAM, first published 12 June 2026, DOI 10.1002/cpa.70058.** For each bounded Lipschitz domain and each `epsilon in (0,1)`, gives an explicit `Lambda(epsilon,Omega)` above which

```math
k\le(1+\epsilon)a\lambda_k^{d/2}.
```

This makes the **epsilon-loss** version finitely checkable for a specified domain. One cannot send `epsilon->0` at a fixed eigenvalue without controlling the epsilon-dependent threshold. Additional exact domain-class results exist, but this does not settle the full target. Publisher abstract and publication metadata were checked; the explicit threshold proof was not independently audited. [Published abstract](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpa.70058), [preprint](https://arxiv.org/abs/2507.04307).

7. **Frank–Larson, CPAM 79 (2026), 762–822, DOI 10.1002/cpa.70019.** Theorems 1.1 and 1.2 show that, for each fixed dimension, there exists a Riesz exponent `gamma<1` for which the sharp semiclassical inequalities hold uniformly over bounded open **convex** domains and all energies, separately for Dirichlet and Neumann. This is an improvement over the general `gamma>=1` theory. Neither `gamma=0` nor all Lipschitz domains is asserted. Their critical-exponent/dimensional-degeneration framework is potentially useful for a convex subcampaign, but promoting smoothed estimates to counting estimates needs new reasoning. Full published theorem statements were inspected. [Published full text](https://research.chalmers.se/publication/548922/file/548922_Fulltext.pdf).

8. **Frank–Larson, Inventiones 241 (2025), 999–1079.** Establishes two-term asymptotics for Riesz means of every **positive** order on bounded Lipschitz domains. Positive order excludes counting order zero. It cannot be substituted for unrestricted two-term counting Weyl asymptotics or an exact finite reduction. [Publisher source](https://link.springer.com/article/10.1007/s00222-025-01352-x).

9. **Frank–Larson–Pfeiffer, arXiv:2502.02388v2; JST publication available.** For arbitrary finite-measure open sets and `gamma>=1`, strengthens the semiclassical Riesz inequalities by factors `1-c exp(-c' sqrt(E)|Omega|^(1/d))` for Dirichlet and `1+c exp(...)` for Neumann. Constants depend on dimension; a more geometric form uses regularized inradius. These are still smoothed estimates. Theorem 1 and the basic hypotheses were inspected. [Full preprint](https://arxiv.org/html/2502.02388v2), [published PDF](https://ems.press/content/serial-article-files/52272).

10. **Gan–Jiang–Lin, Science China Mathematics, published 21 April 2026.** Publisher abstract reports improved Berezin–Li–Yau/Kröger inequalities yielding infinitely many Pólya-valid Dirichlet indices for `d>=3` and Neumann indices for `d>=5` (discrete Neumann spectrum). This does not mean all sufficiently large indices or all indices. Full text was unavailable here, so only this stated scope is recorded. [Publisher abstract](https://link.springer.com/article/10.1007/s11425-025-2522-x).

11. **Filonov, CPAM 78 (2025), 537–544.** Proves for bounded planar convex domains `N_N(E)>=|Omega|E/(2 sqrt(3) j_0^2)`, where `j_0` is the first positive zero of `J_0`. This improves the general Kröger coefficient `1/(8*pi)` to approximately `0.0499`, still below the conjectured `1/(4*pi)`. It is not a proof of planar convex Pólya. [Primary full preprint](https://arxiv.org/html/2309.01432v1), [publication](https://doi.org/10.1002/cpa.22231).

## Campaign implications

- Avoid spending initial campaigns reproving ball, sector or Dirichlet-annulus coverage unless extracting a genuinely useful new transferable lemma.
- Keep arbitrary Lipschitz and convex subproblems explicitly separate. Convexity may enable quantified intermediate statements but cannot be silently introduced into the target.
- In the planar Dirichlet problem, Faber–Krahn and Krahn–Szegő already control indices 1 and 2; index 3 is a meaningful unresolved endpoint to isolate. No broader low-index Neumann or dimension-dependent assertion is needed for this campaign decision.
- Do not infer unsmoothed inequalities by differentiating Riesz bounds, or exact Pólya from epsilon-loss tails. Quantifier control and endpoint recovery are the significant remaining issues.
- A finite numerical survey of domains or eigenvalues has no uniform infinite-domain implication. A successful certificate needs explicit domain-family reduction and a rigorous global tail argument.

## Concurrent-Sol addendum: the first two indices

**Source check.** Bucur–Henrot, *Acta Mathematica* 222 (2019), 337–361, Theorem 1, applies in every `d>=2` to bounded open “regular” sets, defined by compact embedding `H^1(Omega)->L^2(Omega)`, explicitly including Lipschitz sets. Connectedness is not assumed. Indexing is exactly `mu_0=0<=mu_1<=mu_2`, with multiplicities. Their theorem is equivalent to

```math
\mu_2(\Omega)\le\mu_1(B_{V/2}),\qquad V=|\Omega|,
```

where `B_v` denotes a ball of volume `v`. Equality requires two equal disjoint balls almost everywhere. Corollary 2 explicitly states Neumann Pólya at index 2 in every dimension. Their density extension involves relaxed eigenvalues and is unnecessary here. The introduction also records all-dimensional Szegő–Weinberger and Hong–Krahn–Szegő. [Primary PDF, pp. 1–4](https://arxiv.org/pdf/1801.07435), [published DOI](https://doi.org/10.4310/ACTA.2019.v222.n2.a2).

**Independent elementary check avoiding July 2026 ball results.** The coordinate trial function `x_1` on a centered radius-`R` ball has mean zero and Rayleigh quotient `(d+2)/R^2`. Moreover

```math
d+2\le4\Gamma(d/2+1)^{4/d}=4\pi^2/\omega_d^{4/d}.
```

For an elementary proof, set

```math
F(x)=\Gamma(x+1)^2\left(\frac2{x+1}\right)^x.
```

Then `F(1)=1`, `F(3/2)=9*pi/(10*sqrt(5))>1`, and

```math
\frac{F(x+1)}{F(x)}
=2(x+1)\left(1+\frac1{x+1}\right)^{-(x+1)}
>\frac{2(x+1)}e>1\quad(x\ge1).
```

Induction on the two parity classes proves the comparison for every integer `d>=2`. Thus the first ball Neumann bound needs only a Rayleigh test and elementary constants.

Szegő–Weinberger, Bucur–Henrot and scaling give the requested Neumann inequalities at `k=1,2`. Faber–Krahn and Hong–Krahn–Szegő reduce the corresponding Dirichlet inequalities to the first eigenvalue of balls; the 2023 published Dirichlet-ball theorem supplies that bound. Hence the concurrent Sol low-index chain is valid in every stated dimension, conditional only on these explicit established external theorems. It is known mathematics, not a new campaign resolution. This addendum expands the intentionally narrower earlier campaign bullet after checking the needed source.
