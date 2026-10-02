# 422. Global L2 scattering for the planar hyperbolic cubic Schrödinger equation

**Area:** Dispersive PDEs and nonlinear wave envelopes

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For every $`u_0\in L^2(\mathbb R^2)`$, consider

```math
i\partial_tu+\partial_x^2u-\partial_y^2u+|u|^2u=0,\qquad u(0)=u_0.
```

Does its unique local solution extend to $`u\in C(\mathbb R;L^2)\cap L^4_{\mathrm{loc}}(\mathbb R\times\mathbb R^2)`$, depend continuously on $`u_0`$ on compact time intervals, and admit $`u_\pm\in L^2`$ satisfying

```math
\lim_{t\to\pm\infty}\|u(t)-e^{it(\partial_x^2-\partial_y^2)}u_\pm\|_{L^2}=0?
```

Uniqueness is in the displayed local spacetime class. This is the scalar hyperbolic equation; no additional nonlocal Davey–Stewartson term is present.

## Application

Opposite signs of dispersion arise in anisotropic wave-envelope models and optics. The question tests whether finite wave action always disperses despite the absence of a coercive gradient energy.

## References

1. J.-C. Saut and Y. Wang, [On the hyperbolic nonlinear Schrödinger equations](https://doi.org/10.1186/s13662-024-03811-w), *Advances in Continuous and Discrete Models* (2024), article 15, equation (1.12), §2.1, Conjecture 1.
2. B. Dodson, J. L. Marzuola, B. Pausader and D. P. Spirn, [The profile decomposition for the hyperbolic Schrödinger equation](https://doi.org/10.1215/ijm/1552442664), *Illinois Journal of Mathematics* **62** (2018), 293–320, introduction and mass-critical profile decomposition; [preprint](https://arxiv.org/abs/1708.08014).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The source explicitly separates this conjecture from the solved integrable defocusing DS-II system. Searches through the review date for hyperbolic cubic NLS global L2 scattering and subsequent Saut–Wang work found results on different product domains or restricted data, but no resolution for arbitrary planar L2 data.
