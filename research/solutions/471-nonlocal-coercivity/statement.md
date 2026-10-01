# 471. Does directional ellipticity force a fractional energy bound?

**Area:** Nonlocal diffusion PDEs; coercivity of interaction energies

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $`n\ge2`$, $`0<s<1`$, $`\lambda>0`$ and $`\Lambda>1`$. Let $`K(x,z)=K(z,x)\ge0`$ be measurable and suppose, for almost every $`x`$, every $`r>0`$ and every unit $`e`$,

```math
r^{2s}\int_{B_{2r}(x)\setminus B_r(x)}K(x,z)dz\le\Lambda,
```



```math
r^{2s-2}\int_{B_{\Lambda r}(x)\setminus B_r(x)}|e\cdot(x-z)|^2K(x,z)dz\ge\lambda.
```

Must there be a $`c=c(n,s,\lambda,\Lambda)>0`$ such that every $`v\in C_c^\infty(\mathbb R^n)`$ satisfies

```math
\iint_{\mathbb R^n\times\mathbb R^n}|v(x)-v(z)|^2K(x,z)\,dx\,dz
\ge c\iint_{\mathbb R^n\times\mathbb R^n}\frac{|v(x)-v(z)|^2}{|x-z|^{n+2s}}\,dx\,dz?
```

No regularity of $`K`$ in the base point and no lower bound on the measure of directions carrying a pointwise kernel lower bound are assumed.

## Application

The inequality would turn local directional information about long-range interactions into a global dissipation estimate for heterogeneous media and kinetic diffusion.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. J. Chaker and L. Silvestre, *Coercivity estimates for integro-differential operators*, Calc. Var. PDE **59**, 106 (2020). [Article](https://doi.org/10.1007/s00526-020-01764-y).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book poses this precise coercivity question immediately after Open Question 2.1 in §2.8.1 and explains its link to divergence-form regularity. Searches on 2026-09-22 checked coercivity under annular second-moment bounds and later work on singular kernels. Known results require additional thickness or energy-comparability assumptions. This entry concerns the symmetric quadratic form, unlike the separate nondivergence-form pointwise equation.
