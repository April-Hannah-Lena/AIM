# 156. The full set of zero-energy cubic-to-tetragonal strains

**Area:** Materials science and nonlinear elasticity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $`\alpha,\beta>0`$ with $`\alpha\ne\beta`$. Let $`U_1=\mathop{\mathrm{diag}}\nolimits(\alpha,\beta,\beta)`$, let $`U_2,U_3`$ be its other coordinate permutations, and set $`K=\bigcup_{i=1}^3 SO(3)U_i`$, where $`SO(3)`$ is the rotation group.

Determine $`K^{qc}`$ for every such pair $`\alpha,\beta`$: give necessary and sufficient conditions on a matrix $`F\in\mathbb R^{3\times3}`$ for membership. Here $`F\in K^{qc}`$ means that on $`Q=(0,1)^3`$ there are maps $`y_j\in W^{1,\infty}(Q;\mathbb R^3)`$ with $`y_j=Fx`$ on $`\partial Q`$, uniformly bounded gradients, and

```math
\int_Q\mathop{\mathrm{dist}}\nolimits(Dy_j(x),K)^2\,dx\longrightarrow0.
```

The requested characterization must decide general matrices, including non-diagonal ones.

## Application

This set gives all macroscopic strains that a tetragonal martensite can accommodate by fine mixtures of its stress-free crystal variants.

## References

1. John M. Ball, *Some Open Problems in Elasticity*, in *Geometry, Mechanics, and Dynamics* (2002), Problem 16 and equation (4.3). [Chapter](https://doi.org/10.1007/0-387-21791-6_1). Explicit three-well hull question.

2. John M. Ball and Myrto Galanopoulou, *Compatibility of Martensitic Microstructures in Polycrystals* (2026). [Paper](https://arxiv.org/abs/2607.12572). Introduction and the section on the Taylor set discuss partial hull information, including the positive diagonal matrices.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The source problem asks for the full quasiconvex hull. Searches for “cubic to tetragonal quasiconvex hull 2026” and the Ball–Galanopoulou title found a July 2026 treatment of special matrices and polycrystal compatibility. Its positive-diagonal characterization does not cover arbitrary $`F`$; no full characterization was located.
