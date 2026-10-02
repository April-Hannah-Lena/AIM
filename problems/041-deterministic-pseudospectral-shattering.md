# 041. Deterministic pseudospectral shattering in nearly cubic time

**Area:** Eigenvalue computation and nonnormal operators

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $`n\ge2`$, $`A\in\mathbb C^{n\times n}`$ with $`\|A\|_2\le1`$, and $`0<\delta<1`$, construct a deterministic algorithm using $`O(n^3\log^c(n/\delta))`$ arithmetic operations that outputs $`E`$ with $`\|E\|_2\le\delta`$ such that $`B=A+E`$ has distinct eigenvalues and

```math
\frac{\kappa_V(B)}{\mathop{\mathrm{gap}}\nolimits(B)}\le C(n/\delta)^c.
```

Here $`\mathop{\mathrm{gap}}\nolimits(B)=\min_{i\ne j}|\lambda_i(B)-\lambda_j(B)|`$ and $`\kappa_V(B)=\inf\{\|V\|_2\|V^{-1}\|_2:B=VDV^{-1},\ D\text{ diagonal}\}`$. The constants $`C,c`$ must be universal. The task is to find the perturbation; a full diagonalization is not required.

## Application

Controlled eigenvector conditioning and eigenvalue separation enable reliable fast algorithms for general nonnormal eigenproblems. A deterministic construction would remove dependence on random perturbations.

## References

1. J. Banks, J. Garza-Vargas, A. Kulkarni and N. Srivastava, [Pseudospectral shattering, the sign function, and diagonalization in nearly matrix multiplication time](https://doi.org/10.1007/s10208-022-09577-5), Foundations of Computational Mathematics 23 (2023), 1959–2047. Randomized baseline.
2. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Problem 3.1 and equation (6).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 3.1 remains the cited deterministic challenge; no later resolution was located. The displayed bound there reverses n/δ typographically; the formulation here follows its preceding equation (6), which asks for polynomially bounded conditioning.

Searches included: `deterministic pseudospectral shattering 2026`; `deterministic shattering eigenvalue conditioning polynomial`; `pseudospectral shattering derandomization`. This is a documented literature check, not a certification that no solution exists.
