# 439. Regular MEMS extremal states without an asymptotic curvature condition

**Area:** Semilinear elliptic PDEs and electrostatic microdevices

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`3\le d\le6`$, let $`\Omega\subset\mathbb R^d`$ be a bounded smooth domain, and let $`f\in C^2([0,1))`$ be positive, nondecreasing and convex, with $`f(t)\to\infty`$ as $`t\uparrow1`$ and $`\int_0^1 f(t)\,dt=\infty`$. Consider

```math
-\Delta u=\lambda f(u)\quad\hbox{in }\Omega,\qquad u=0\quad\hbox{on }\partial\Omega,\qquad0<u<1.
```

Let $`\lambda^*`$ be the supremum of parameters admitting a classical solution, let $`u_\lambda`$ be the pointwise minimal classical solution for $`0<\lambda<\lambda^*`$, and set $`u^*=\lim_{\lambda\uparrow\lambda^*}u_\lambda`$. Must $`\|u^*\|_{L^\infty(\Omega)}<1`$, without assuming $`\liminf_{t\uparrow1}f(t)f''(t)/f'(t)^2>1`$?

## Application

The value u=1 represents contact or touchdown in an electrostatic membrane model. The question asks whether low-dimensional extremal equilibria stay separated from contact for a broad class of singular force laws.

## References

1. X. Cabré, [Stable solutions to reaction-diffusion elliptic problems](https://arxiv.org/abs/2603.03161), lecture survey (2026), §3.5.3.
2. R. Bruera and X. Cabré, [Regularity of stable solutions to the MEMS problem up to the optimal dimension 6](https://arxiv.org/abs/2507.20916), preprint (2025), Theorem 1.3, Remark 1.4 and Appendix A.
3. F. Peng and S. Villegas, [Regularity of stable radial solutions to semilinear elliptic equations in MEMS problems](https://arxiv.org/abs/2602.21115), preprint (2026), main theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 theorem reaches dimensions 3–6 under the omitted curvature condition and needs no such condition in dimensions 1–2. The February 2026 Peng–Villegas result removes the condition for radial solutions on balls. The question here retains general smooth domains and no radial hypothesis; review-date searches located no corresponding unrestricted theorem.
