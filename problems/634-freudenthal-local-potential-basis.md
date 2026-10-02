# 634. Local potential bases on Freudenthal meshes

**Area:** Finite elements and multigrid methods

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Partition $`\Omega=(0,1)^3`$ into $`N^3`$ congruent cubes, where $`N\ge1`$ and $`h=1/N`$. Subdivide every cube with lower corner $`a`$ into the six tetrahedra

```math
a+h\mathop{\mathrm{conv}}\nolimits\{0,e_{\sigma(1)},e_{\sigma(1)}+e_{\sigma(2)},(1,1,1)\},\qquad \sigma\in S_3.
```

Call this mesh $`\mathcal T_h`$. For an integer $`k\ge5`$, define the potential space

```math
\Sigma_{h,k}=\{w\in[C^0(\overline\Omega)]^3:
w|_T\in[\mathbb P_{k+1}(T)]^3\ (T\in\mathcal T_h),\quad
\mathop{\mathrm{curl}}\nolimits w\in[C^0(\overline\Omega)]^3\}.
```

Here $`\mathbb P_r`$ denotes polynomials of total degree at most $`r`$. No boundary condition is imposed. For each mesh vertex $`v`$, including boundary vertices, let $`\omega_v`$ be the union of the closed tetrahedra containing $`v`$.

Does $`\Sigma_{h,k}`$ always have a basis whose every member is supported in some $`\omega_v`$? Equivalently, prove or disprove

```math
\Sigma_{h,k}=\sum_v\{w\in\Sigma_{h,k}:\mathop{\mathrm{supp}}\nolimits w\subseteq\omega_v\}
\qquad(N\ge1,\ k\ge5).
```

This is the local-support assertion in Conjecture 2(b) of [1]; a uniform bound on decomposition norms is a further question.

## Application

Curls of local potentials supply divergence-free corrections for multigrid solvers in incompressible flow and nearly incompressible elasticity.

## References

1. P. E. Farrell, L. Mitchell and L. R. Scott, [Two conjectures on the Stokes complex in three dimensions on Freudenthal meshes](https://doi.org/10.1137/22M1533943), *SIAM Journal on Scientific Computing* **46** (2024), A629–A644. Section 3.3, Conjecture 2(b); [arXiv version 2](https://arxiv.org/abs/2211.05494v2), p. 12 and Appendix A.
2. S. Ding, P. Ming, H. Yu and Q. Zhu, [The Scott–Vogelius element is inf-sup stable on Freudenthal meshes for $`k\ge4`$](https://arxiv.org/abs/2609.25690), preprint, 22 September 2026.

## Status review

The source provides numerical evidence for local support. Its separate inf-sup conjecture has an announced proof in [2], concerning a bounded right inverse of divergence. That assertion does not construct the potential-space basis requested here. Current targeted literature, arXiv, GitHub, Zenodo and Palomar checks found no matching resolution of this local-basis target. Zenodo search omitted a known inf-sup announcement; that announcement was checked directly, so negative index results are not treated as exhaustive. No equivalent catalogue entry was found.
