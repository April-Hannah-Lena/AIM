# 071 — A strictly convex function on every simple manifold

**Area:** Geometric tomography

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`(M,g)`$ be a smooth compact Riemannian manifold of dimension $`n\ge3`$ with boundary. Assume it is simple: the boundary is strictly convex, and any two points are joined by a unique geodesic depending smoothly on its endpoints. Must there exist $`\rho\in C^\infty(M;\mathbb R)`$ and a constant $`c>0`$ such that

```math
\mathop{\mathrm{Hess}}\nolimits_g\rho(x)(v,v)\ge c\,g_x(v,v)
\qquad\text{for every }x\in M,\ v\in T_xM?
```

Here $`\mathop{\mathrm{Hess}}\nolimits_g\rho(v,v)=g(\nabla_v\nabla\rho,v)`$. No condition that $`\rho`$ be constant on the boundary is imposed.

## Application

Strictly convex level sets allow recovery of an unknown medium successively from the boundary inward in geodesic and elastic-wave tomography.

## References

1. Joonas Ilmavirta, Teemu Saksala and Lili Yan, *Rigidity of Homogeneous Lamé Systems* (2026 preprint), introduction, p. 3. [Preprint](https://arxiv.org/abs/2602.08860), [author PDF](https://users.jyu.fi/~jojapeil/pub/homogeneous-lame-rigidity.pdf).
2. Plamen Stefanov, Gunther Uhlmann and András Vasy, *Local and Global Boundary Rigidity and the Geodesic X-Ray Transform in the Normal Gauge*, Annals of Mathematics **194** (2021), 1–95. [DOI](https://doi.org/10.4007/annals.2021.194.1.1).

## Status review

**Literature check:** Open in cited literature; no later resolution located

The 2026 paper explicitly identifies existence of a strictly convex function on every simple manifold as a major open problem. The 2021 reconstruction theory uses convexity hypotheses but does not derive them from simplicity in general. Searches on 2026-09-08: "simple manifolds strictly convex function open" and "simple manifold convex function 2026 solved". No general existence theorem or simple counterexample was located.
