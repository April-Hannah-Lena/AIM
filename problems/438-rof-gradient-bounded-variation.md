# 438. Bounded variation of gradients in the Rudin–Osher–Fatemi denoising model

**Area:** Variational elliptic PDEs and image denoising

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be a bounded smooth domain and $`f\in C^\infty(\overline\Omega)`$. Let $`U`$ be the unique minimizer over $`BV(\Omega)\cap L^2(\Omega)`$ of

```math
\mathcal E(u)=|Du|(\Omega)+\frac12\int_\Omega|u-f|^2\,dx,
```

where $`|Du|`$ is the total variation of the distributional gradient; no boundary values are prescribed. Must $`\nabla U\in BV(\Omega;\mathbb R^d)`$? Equivalently, must all distributional second derivatives of $`U`$ be finite Radon measures on $`\Omega`$?

## Application

This is the classical total-variation image-denoising model. A finite variation bound on the reconstructed gradient would control the complexity of transitions between flat and varying regions beyond the known Lipschitz regularity.

## References

1. H. Brezis, [Some of my favorite open problems](https://doi.org/10.4171/RLM/1008), *Rendiconti Lincei—Matematica e Applicazioni* (2023), §8, Open Problem 8.1.
2. H. Brezis, [Remarks on some minimization problems associated with BV norms](https://doi.org/10.3934/dcds.2019242), *Discrete and Continuous Dynamical Systems* **39** (2019), 7013–7029, Open Problem 1 and the one-dimensional theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2023 survey states the multidimensional question after the known global Lipschitz theorem. Searches through the review date for ROF gradient BV, Brezis minimizer Hessian measures, and higher regularity of total-variation denoising found no resolution. The affirmative one-dimensional result and regularity of other higher-order regularizers do not address this functional.
