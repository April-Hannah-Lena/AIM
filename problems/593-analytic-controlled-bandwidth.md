# 593. Logarithmic controlled bandwidth for locally analytic functions

**Area:** Numerical approximation and oscillatory quadrature

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $f:[-1,1]\to\mathbb C$ be nonzero and extend holomorphically to an open complex neighborhood of $[-1,1]$. Set $M=\|f\|_{L^\infty([-1,1])}$ and use the Fourier convention

$$
\widehat g(\xi)=\frac1{2\pi}\int_{\mathbb R}g(x)e^{-i\xi x}\,dx.
$$

For $0<\varepsilon<1$, let $c_f(\varepsilon)$ be the infimum of $c>0$ for which there exists a Schwartz function $g\in\mathcal S(\mathbb R)$ satisfying

$$
\mathop{\mathrm{supp}}\nolimits\widehat g\subset[-c,c],\qquad
\|f-g\|_{L^\infty([-1,1])}\le\varepsilon M,
$$

and

$$
\|g\|_{L^\infty(\mathbb R)}\le4M,\qquad
\|\widehat g\|_{L^\infty(\mathbb R)}\le4M,\qquad
\|\widehat g'\|_{L^\infty(\mathbb R)}\le4M.
$$

Prove or disprove the Chen–Serkh–Bremer conjecture that there are constants $C_f<\infty$ and $\varepsilon_f>0$ such that

$$
c_f(\varepsilon)\le C_f\log(1/\varepsilon)
\qquad(0<\varepsilon<\varepsilon_f).
$$

The constants may depend on $f$ and its neighborhood of analyticity, but not on $\varepsilon$. All three global norm bounds are part of the problem.

## Application

Controlled bandlimited approximations enter error bounds for the adaptive Levin method for oscillatory integrals. The proposed logarithmic bandwidth would sharpen the dependence of these estimates on the requested accuracy for integrands known to be analytic only near the integration interval.

## References

1. S. Chen, K. Serkh and J. Bremer, [On the adaptive Levin method](https://doi.org/10.1007/s00211-024-01443-6), *Numerische Mathematik* **156** (2024), 1927–1985. Section 2.3, Definition 1, equation (42) and the following conjecture, pages 1936–1937.
2. [Author manuscript](https://www.math.toronto.edu/~bremer/papers/levin.pdf); [arXiv:2211.13400](https://arxiv.org/abs/2211.13400).

## Status review

For a smooth extension, the source proves $c_f(\varepsilon)\le C_{m,f}\varepsilon^{-1/m}$ for every fixed positive integer $m$. It records the logarithmic bound when the extension is bounded and analytic throughout a horizontal strip containing the real axis, and conjectures the stated local-analyticity version. Rapid polynomial approximation on the finite interval alone does not establish the required global bounds.

The current author manuscript retains the conjecture, and the arXiv record has no revision after January 2024. Searches through the date above found no matching solution or announcement in the literature, arXiv, public GitHub, indexed Zenodo or native Palomar. Native Zenodo access returned HTTP 403. No equivalent catalogue entry was found.
