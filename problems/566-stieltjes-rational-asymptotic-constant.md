# 566. Sharp asymptotic constant for rational approximation of fractional inverse powers

**Area:** Rational approximation and numerical analysis

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix $`0<a<b<\infty`$ and $`0<\gamma<1`$. Let

```math
E_{n-1,n}(a,b;\gamma)=\inf_{p,q}\max_{x\in[a,b]}\left|x^{-\gamma}-\frac{p(x)}{q(x)}\right|,
```

where $`p,q`$ are real polynomials with $`\deg p\le n-1`$, $`\deg q\le n`$, and $`q`$ has no zeros on $`[a,b]`$.

Put

```math
k=\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a},\qquad
K(k)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-k^2\sin^2\theta}},\qquad
\mu(k)=\frac{\pi K(\sqrt{1-k^2})}{2K(k)}.
```

Prove or disprove the Braess–Hackbusch conjecture

```math
\lim_{n\to\infty} e^{2n\mu(k)}E_{n-1,n}(a,b;\gamma)
=4(ab)^{-\gamma/2}\sin(\pi\gamma).
```

The interval and exponent are fixed as $`n\to\infty`$. The target is absolute uniform error, with no restriction on poles outside the approximation interval.

## Application

Rational approximations of fractional inverse powers are used to approximate fractional diffusion operators and related matrix functions. A sharp leading constant would turn a known asymptotic convergence rate into a more precise degree-versus-accuracy prediction.

## References

1. D. Braess and W. Hackbusch, [On the approximation of Stieltjes functions by exponential sums and rational functions with applications to partial differential equations](https://doi.org/10.1007/s00211-025-01523-1), *Numerische Mathematik* **158** (2026), 455–490. Conjecture 4.8, equation (4.20); Section 4.1 defines $`\mu`$.
2. [Author-hosted revised preprint](https://files-www.mis.mpg.de/mpi-typo3/preprints/2024/preprint2024_10.pdf), revised November 2025.

## Status review

The source establishes the exponential rate and provides numerical evidence for this more precise leading constant. Its relative-error theorem for the square root is a different approximation problem, and the classical asymptotic result on an infinite interval does not prove the stated finite-interval formula.

Checks through 24 September 2026 found no matching proof or announcement. The published text, author preprint, current institute publication list, arXiv-indexed searches, public GitHub searches and Palomar were checked. Zenodo's API was inaccessible; its indexed search returned no matching result. No equivalent catalogue entry was found. Detailed checks are in the accompanying numerical-journal review.
