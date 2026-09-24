# 448. The Weinstock inequality for convex domains in a sphere

**Area:** Elliptic boundary spectra and shape optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`n\ge3`$ and let $`\Omega`$ be a smooth geodesically convex domain whose closure is contained in an open hemisphere of the unit sphere $`S^n`$. Define its first nonzero Steklov eigenvalue by

```math
\sigma_1(\Omega)=\inf\left\{\frac{\int_\Omega|\nabla u|^2\,dV}{\int_{\partial\Omega}u^2\,dS}:u\in H^1(\Omega),\ \int_{\partial\Omega}u\,dS=0,\ \int_{\partial\Omega}u^2\,dS>0\right\}.
```

Let $`B\subset S^n`$ be a geodesic ball of radius less than $`\pi/2`$ with $`|\partial B|=|\partial\Omega|`$. Is $`\sigma_1(\Omega)\le\sigma_1(B)`$, with equality only when $`\Omega`$ is a geodesic ball? Equivalently, the spectrum comes from $`\Delta u=0`$ in $`\Omega`$ and $`\partial_\nu u=\sigma u`$ on its boundary.

## Application

Steklov modes describe harmonic bulk fields coupled to boundary dynamics. This inequality would identify the shape with the fastest first boundary relaxation mode under a fixed boundary-area constraint in a curved medium.

## References

1. B. Colbois, A. Girouard, C. Gordon and D. Sher, [Some recent developments on the Steklov eigenvalue problem](https://doi.org/10.1007/s13163-023-00480-3), *Revista Matemática Complutense* **37** (2024), 1–161, Open Question 4.27.
2. D. Bucur, V. Ferone, C. Nitsch and C. Trombetti, [Weinstock inequality in higher dimensions](https://doi.org/10.4310/jdg/1620272940), *Journal of Differential Geometry* **118** (2021), 1–21, Theorem 3.1; [preprint](https://arxiv.org/abs/1710.04587).
3. C. Gao, Y. Wei and R. Zhou, [Weinstock inequalities for outward-minimizing domains](https://arxiv.org/abs/2608.11841), preprint (2026), Theorems 1.1–1.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The Euclidean convex theorem is known. August 2026 results establish hyperbolic versions, including the broader outward-minimizing class, but their theorems do not concern the sphere. Review-date searches for spherical convex Weinstock inequalities located no solution. Spherical counterexamples to volume-normalized inequalities use a different constraint; this statement fixes boundary area and an open hemisphere.
