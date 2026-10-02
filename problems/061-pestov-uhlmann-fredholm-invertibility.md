# 061 — Invertibility of the Pestov–Uhlmann reconstruction operator

**Area:** Integral geometry and computational tomography

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`(M,g)`$ be a smooth compact oriented simple Riemannian surface: its boundary is strictly convex and any two points are joined by a unique geodesic depending smoothly on its endpoints. On its unit tangent bundle $`SM`$, let $`X`$ generate geodesic motion, $`V`$ generate rotation in each unit circle, and $`X_\perp=[X,V]`$. For a smooth function $`f`$ on $`M`$, solve $`Xu^f=-f`$ with zero values at the incoming boundary of $`SM`$. Put

```math
Wf(x)=\frac1{2\pi}\int_{S_xM}X_\perp u^f(x,v)\,dS_x(v).
```

The smoothing operator $`W`$ extends to $`L^2(M;\mathbb C)`$. Is $`\mathrm{Id}+W^2`$ invertible on that space for every such surface? Equivalently, does $`\ker(\mathrm{Id}+W^2)=\{0\}`$ always hold?

## Application

Invertibility would justify a Fredholm reconstruction formula for geodesic tomography beyond geometries close to constant curvature.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions* (Cambridge University Press, 2023), §15.1, problem 3. [Open problems chapter](https://doi.org/10.1017/9781009039901.018).
2. François Monard, *Numerical Implementation of Geodesic X-Ray Transforms and Their Inversion*, SIAM Journal on Imaging Sciences **7** (2014), 1335–1357. [DOI](https://doi.org/10.1137/130938657), [preprint](https://arxiv.org/abs/1309.6042).

## Status review

**Known cases:** Invertibility follows for simple metrics near constant curvature, where the error operator has sufficiently small norm.

**Remaining target:** Invertibility of the displayed reconstruction operator for every smooth simple surface.

**Literature check:** Open in cited literature; no later resolution located

The book explicitly asks whether this Fredholm operator is invertible for every simple surface. Monard describes the operator and numerical reconstruction; a small error-operator norm yields invertibility near constant curvature, but does not cover arbitrary simple metrics. Searches on 2026-09-08: "Pestov Uhlmann invertibility 2025 2026" and "Pestov Uhlmann W operator invertibility solved". No general resolution was located.
