# 051 — Recover both Lamé moduli from static boundary measurements

**Area:** Inverse elasticity / nondestructive testing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected smooth domain. For smooth coefficients $`\lambda,\mu`$ satisfying $`\mu>0`$ and $`3\lambda+2\mu>0`$ on $`\overline\Omega`$, set

```math
\varepsilon(u)=\tfrac12(\nabla u+\nabla u^T),\qquad
\sigma_{\lambda,\mu}(u)=\lambda(\nabla\cdot u)I+2\mu\varepsilon(u).
```

For each boundary displacement $`f\in H^{1/2}(\partial\Omega;\mathbb R^3)`$, let $`u`$ solve $`\nabla\cdot\sigma_{\lambda,\mu}(u)=0`$ with trace $`f`$, and define the traction map $`\Lambda_{\lambda,\mu}f=\sigma_{\lambda,\mu}(u)\nu`$.

Does equality of the full traction maps for two admissible coefficient pairs imply equality of both $`\lambda`$ and $`\mu`$ in $`\Omega`$? Both coefficients are arbitrary smooth spatial functions.

## Application

Boundary loading and displacement measurements are used to infer elastic defects and tissue stiffness. This asks whether they contain enough information to separate the two isotropic elastic moduli.

## References

1. V. Markaki, D. Kourounis and A. Charalambopoulos, *On the identification of Lamé parameters in linear isotropic elasticity via a weighted self-guided TV-regularization method*, Journal of Inverse and Ill-posed Problems **32** (2024), 213–231, introduction. [Paper](https://doi.org/10.1515/jiip-2021-0050).
2. R.-Y. Lai, *Uniqueness and stability of Lamé parameters in elastography*, Journal of Spectral Theory **4** (2014), 841–877. [Paper](https://doi.org/10.4171/JST/88).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Reference 1 states that even full-data global uniqueness is open and discusses results with shear modulus close to constant. Reference 2 reconstructs moduli from internal displacement fields, which are additional measurements. Dynamic elastic-wave theorems also use a different data set.

Searches on 2026-09-08 included `isotropic elasticity inverse boundary problem Lame parameters global uniqueness open 2025 2026` and `Lamé parameters open three inverse uniqueness`. No unrestricted static three-dimensional theorem was located. The solved two-dimensional Lamé problem is not the target here.
