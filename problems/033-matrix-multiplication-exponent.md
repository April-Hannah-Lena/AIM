# 033. Is the matrix-multiplication exponent two?

**Area:** Numerical linear algebra and algebraic complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Over $\mathbb C$, let $\omega$ be the infimum of all real $\tau$ for which two arbitrary $n\times n$ matrices can be multiplied using $O(n^\tau)$ scalar arithmetic operations. Determine whether $\omega=2$.

Equivalently, for every $\varepsilon>0$, is there an arithmetic algorithm, with constants allowed to depend on $\varepsilon$, using $O(n^{2+\varepsilon})$ operations for every $n$? Arithmetic is exact; bit complexity and numerical stability are separate requirements.

## Application

Matrix multiplication underlies dense factorizations, least squares, eigenvalue algorithms and many scientific computing kernels. Its exponent describes a fundamental asymptotic computational limit.

## References

1. P. Dutta, F. Gesmundo, C. Ikenmeyer et al., [Geometric complexity theory for product-plus-power](https://wrap.warwick.ac.uk/id/eprint/191761/1/1-s2.0-S0747717125000409-main.pdf), Journal of Symbolic Computation 132 (2026), 102458; introduction. Definition and tensor characterization.
2. E. Dupont et al., [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884), 2026. August upper-bound improvement.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The August 2026 result reports $\omega<2.371177$, which remains strictly above the conjectured value. No theorem establishing $\omega=2$ or a lower bound $\omega>2$ was located. A small improvement in the upper bound is not a resolution.

Searches included: `matrix multiplication exponent 2026`; `omega equals two matrix multiplication proof`; `Improving matrix multiplication exponent AlphaEvolve`. This is a documented literature check, not a certification that no solution exists.
