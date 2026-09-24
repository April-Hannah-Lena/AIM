# 060 — Classify noninjectivity sets of spherical mean tomography

**Area:** Integral geometry / thermoacoustic imaging

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $f\in C_c(\mathbb R^d)$, $d\geq3$, define
$$
Rf(x,r)=\int_{S^{d-1}}f(x+r\omega)\,d\omega,\qquad r>0.
$$
A set $S\subset\mathbb R^d$ is a noninjectivity set if some nonzero $f\in C_c(\mathbb R^d)$ satisfies $Rf(x,r)=0$ for all $x\in S$ and $r>0$.

Prove or disprove that every noninjectivity set is contained in
$$
(a+\{x:h(x)=0\})\cup V,
$$
where $a\in\mathbb R^d$, $h$ is a nonzero homogeneous harmonic polynomial of positive degree, and $V$ is a real algebraic set of dimension at most $d-2$. Harmonic means $\Delta h=0$. This is the necessity direction of the higher-dimensional Agranovsky–Quinto classification conjecture.

## Application

Spherical means describe ideal constant-speed photoacoustic data. Noninjectivity sets identify detector arrangements on which a nonzero source can be completely invisible.

## References

1. M. Agranovsky, *Ruled nodal surfaces of Laplace eigenfunctions and injectivity sets for the spherical mean Radon transform in $\mathbb R^3$*, Journal of Spectral Theory **7** (2017), 1039–1099, Conjecture 3.2. [Paper](https://ems.press/journals/jst/articles/15151); [preprint](https://arxiv.org/abs/1504.01250).
2. P. Kuchment and L. Kunyansky, *Mathematics of thermoacoustic tomography*, European Journal of Applied Mathematics **19** (2008), §8.2.2. [Survey](https://www.cambridge.org/core/journals/european-journal-of-applied-mathematics/article/mathematics-of-thermoacoustic-tomography/322F4C7F2A05EE3CD1BD2E6E45F80125).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Reference 1 states the higher-dimensional conjecture and proves results for real-analytically ruled surfaces in three dimensions. The complete planar classification and ruled-surface result do not cover arbitrary higher-dimensional sets.

Checked on 2026-09-08 with `spherical mean injectivity sets conjecture 2025 2026` and `Agranovsky Quinto noninjectivity sets homogeneous harmonic cone 2026`. No general classification theorem settling the displayed implication was located.
