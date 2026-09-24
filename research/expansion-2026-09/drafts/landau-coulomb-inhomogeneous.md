# Global classical solutions of the spatially inhomogeneous Landau–Coulomb equation

**Area:** Fluids, kinetic theory and continuum mechanics

**Status:** Open in cited literature; no later resolution located as of 2026-09-17.

**Last checked:** 2026-09-17

## Problem statement

Let $`x\in\mathbb T^3=(\mathbb R/\mathbb Z)^3`$ and $`v\in\mathbb R^3`$. Consider the classical Landau equation without an external or self-consistent force,

```math
\partial_t f+v\cdot\nabla_x f=Q(f,f),\qquad
Q(f,f)=\nabla_v\cdot\int_{\mathbb R^3}a(v-w)
\big[f(t,x,w)\nabla_v f(t,x,v)-f(t,x,v)\nabla_w f(t,x,w)\big]\,dw,
```

with Coulomb kernel

```math
a(z)=|z|^{-1}\left(I-\frac{z\otimes z}{|z|^2}\right),\qquad z\ne0.
```

Suppose $`f_0\ge0`$ is smooth and rapidly decreasing in velocity: for every $`m\ge0`$ and multi-indices $`\alpha,\beta`$,

```math
\sup_{x,v}\langle v\rangle^m|\partial_x^\alpha\partial_v^\beta f_0(x,v)|<\infty,
\qquad \langle v\rangle=(1+|v|^2)^{1/2}.
```

Assume also that $`f_0(x,v)\ge\delta`$ for every $`x`$ and $`|v|\le r`$, for some $`\delta,r>0`$. No smallness or closeness to a Maxwellian is imposed.

Does the local nonnegative classical solution with $`f(0)=f_0`$ always extend to all $`t\ge0`$, continuously at $`t=0`$, smoothly for $`t>0`$, with

```math
\sup_{0\le t\le T}\|\langle v\rangle^m f(t)\|_{L^\infty_{x,v}}<\infty
\quad\text{for every finite }T\text{ and every }m\ge0?
```

This asks whether the maximal classical existence time is infinite in a precise nice-data class supported by the local theory of Henderson–Snelson–Tarfulea. Uniqueness within that local classical class is already known; the unresolved issue is global continuation.

## Applied significance

The Coulomb Landau operator describes collisional redistribution of charged-particle velocities in a plasma. The question tests whether an initially smooth kinetic density can develop a finite-time singularity far from equilibrium, where perturbative stability theory does not apply.

## References

- C. Henderson, S. Snelson and A. Tarfulea, [*Local solutions of the Landau equation with rough, slowly decaying initial data*](https://www.numdam.org/item/10.1016/j.anihpc.2020.04.004.pdf), *Annales de l’Institut Henri Poincaré C* 37 (2020), 1345–1377, §1, Definition 1.1 and Theorems 1.2–1.4.
- W. Golding, C. Henderson and L. Silvestre, [*Pointwise bounds and obstructions to blowup for the Landau and Boltzmann equations*](https://arxiv.org/html/2605.20426v1), arXiv:2605.20426v1, May 19, 2026, §§1.1–1.2, Theorem 1.3, and §3.3 (preprint).
- S. Snelson and C. Solomon, [*A continuation criterion for the Landau equation with very soft and Coulomb potentials*](https://arxiv.org/html/2309.15690v2), *Archive for Rational Mechanics and Analysis* 250 (2026), 20, DOI 10.1007/s00205-026-02182-8, §1, Theorems 1.2–1.3 and Corollary 1.4; linked accepted manuscript dated February 18, 2026.
- N. Guillen and L. Silvestre, [*The Landau equation does not blow up*](https://arxiv.org/html/2311.09420v2), *Acta Mathematica* 234 (2025), 315–375, §1, Theorems 1.1–1.2 (spatially homogeneous equation).
- W. Golding and C. Henderson, [*Global smooth solutions to the inhomogeneous Landau–Fermi–Dirac equation*](https://arxiv.org/html/2608.31071v1), arXiv:2608.31071v1, August 31, 2026, Theorem 1.4 (quantum equation; preprint).
- J. Bedrossian, J. Chen, M. P. Gualdani, S. Ji, V. Vicol and J. Yang, [*Finite time singularities in the Landau equation with very hard potentials*](https://arxiv.org/pdf/2602.05981v1), arXiv:2602.05981v1, February 5, 2026, Theorem 1.1 (different potentials; preprint).

## Status review

The cited local theory gives existence and uniqueness for this data class. The 2026 continuation papers leave large-data inhomogeneous global regularity open. Their conditional bounds are not consequences of conservation of total mass and energy alone. Golding–Henderson–Silvestre explicitly include the periodic domain and Coulomb kernel.

Guillen–Silvestre's global theorem concerns spatially homogeneous solutions. The August 2026 quantum result uses Pauli factors and a density cap that degenerates in the classical limit. The February 2026 singularity construction instead requires potential exponent $`\gamma\in(\sqrt3,2]`$, whereas Coulomb interactions have $`\gamma=-3`$. These results do not decide the displayed problem.

Searches on September 17, 2026 also checked semiclassical limits, fuzzy collision operators, enhanced-reaction blowup and gravitational isotropic models. Their full relevant theorems were compared in the [evidence ledger](../candidates/landau-coulomb-inhomogeneous.json). Author versions supplied full text where publisher access or HTML parsing failed. The problem differs from the catalogue's Boltzmann regularity and homogeneous Landau particle-limit questions. A separated adversarial self-pass checked the equation, local solution class, periodic setting, continuation assumptions, indirect limits and duplicate boundaries; no matching resolution was located.
