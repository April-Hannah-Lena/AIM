# 380. Global weak flow of three-dimensional nematic directors without a hemisphere restriction

**Area:** Liquid crystals; coupled fluid and harmonic-map flow

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a smooth bounded domain. Given smooth compatible data $`u_0:\overline\Omega\to\mathbb R^3`$, $`\nabla\cdot u_0=0`$, $`u_0|_{\partial\Omega}=0`$, and $`d_0:\overline\Omega\to\mathbb S^2`$, does there always exist a global distributional solution of

```math
u_t+u\cdot\nabla u-\Delta u+\nabla p=-\nabla\cdot(\nabla d\odot\nabla d),\quad\nabla\cdot u=0,
```



```math
d_t+u\cdot\nabla d=\Delta d+|\nabla d|^2d,\qquad |d|=1,
```

with initial data $`(u_0,d_0)`$ and time-independent boundary values $`u=0`$, $`d=d_0`$? Here $`(\nabla d\odot\nabla d)_{ij}=\partial_i d\cdot\partial_jd`$. Require $`u\in L^\infty_tL^2_x\cap L^2_tH^1_{0,x}`$, $`d\in L^\infty_tH^1_x`$, $`\tau=d_t+u\cdot\nabla d\in L^2_{t,x}`$ on finite time intervals and

```math
\int_\Omega(|u(t)|^2+|\nabla d(t)|^2)+2\int_0^t\!\int_\Omega(|\nabla u|^2+|\tau|^2)\le\int_\Omega(|u_0|^2+|\nabla d_0|^2).
```

The displayed elastic stress must hold without a defect measure. No hemisphere or small-energy restriction is imposed on $`d_0`$.

## Application

This asks whether the standard unit-director description of a nematic fluid remains a consistent global weak model after defects form in three spatial dimensions.

## References

1. F. Lin and C. Wang, [*Global existence of weak solutions of the nematic liquid crystal flow in dimension three*](https://arxiv.org/abs/1408.4146), Communications on Pure and Applied Mathematics 69 (2016), 1532–1571, §1, equations (1.1)–(1.2) and Theorem 1.1; DOI [10.1002/cpa.21583](https://doi.org/10.1002/cpa.21583).
2. F. Lin and C. Wang, [*Recent developments of analysis for hydrodynamic flow of nematic liquid crystals*](https://arxiv.org/abs/1408.4138), Philosophical Transactions of the Royal Society A 372 (2014), 20130361, §2, three-dimensional existence discussion; DOI [10.1098/rsta.2013.0361](https://doi.org/10.1098/rsta.2013.0361).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using arbitrary-data three-dimensional weak existence for the unit-length simplified Ericksen–Leslie system. The Lin–Wang theorem assumes that the initial director lies in a hemisphere; this removes a concentration mechanism that remains uncontrolled here. Two-dimensional existence and tensor-order-parameter models change essential hypotheses. The 2026 [Chen–Hao–Lazar density-patch paper](https://doi.org/10.1016/j.jfa.2026.111356) studies a two-dimensional system, with conditional perturbative extensions in three dimensions. It does not establish the statement above. No unrestricted three-dimensional defect-free construction was located.
