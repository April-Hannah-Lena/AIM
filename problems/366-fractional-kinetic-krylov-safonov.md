# 366. Hölder regularity for nondivergence kinetic jump equations

**Area:** Kinetic transport; anomalous velocity diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $`d\ge1`$, $`s\in(0,1)`$ and $`0<\lambda\le\Lambda`$. Let $`K(t,x,v,w)`$ be measurable, even in $`w`$, and satisfy

```math
\lambda|w|^{-d-2s}\le K(t,x,v,w)\le\Lambda|w|^{-d-2s}.
```

Suppose bounded $`f:[0,1]\times B_1\times\mathbb R^d\to\mathbb R`$ solves, classically on $`(0,1]\times B_1\times B_1`$,

```math
\partial_tf+v\cdot\nabla_xf=\mathop{\mathrm{PV}}\nolimits\int_{\mathbb R^d}[f(t,x,v+w)-f(t,x,v)]K(t,x,v,w)\,dw+h,
```

where $`h`$ is bounded there. Must there be $`\alpha>0`$ and $`C`$, depending only on $`d,s,\lambda,\Lambda`$, for which

```math
\|f\|_{C^\alpha((1/2,1)\times B_{1/2}\times B_{1/2})}\le C(\|f\|_{L^\infty([0,1]\times B_1\times\mathbb R^d)}+\|h\|_{L^\infty((0,1]\times B_1\times B_1)})?
```

Here $`C^\alpha`$ uses ordinary Euclidean distance. In particular, do not assume interchange symmetry $`K(t,x,v,w)=K(t,x,v+w,-w)`$ or continuity of the coefficients.

## Application

This is a model regularity question for kinetic transport with nonlocal velocity diffusion. The estimate would bound variation of a bounded solution in position, velocity and time using its amplitude, the forcing and the stated kernel bounds, without requiring smooth coefficients.

## References

1. L. Silvestre, [*Regularity estimates and open problems in kinetic equations*](https://arxiv.org/abs/2204.06401), proceedings survey (2022), §8.2, Conjecture 8.2.
2. C. Imbert and L. Silvestre, [*The weak Harnack inequality for the Boltzmann equation without cut-off*](https://arxiv.org/abs/1608.07571), Journal of the European Mathematical Society 22 (2020), 507–592, §1.1 and Theorem 1.6, including its cancellation assumptions.
3. F. Anceschi, G. Palatucci and M. Piccinini, [*Harnack inequalities for kinetic integral equations*](https://cvgmt.sns.it/media/doc/paper/6687/Anceschi-Palatucci-Piccinini_revised.pdf), revised paper, §2, symmetric-kernel framework.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using fractional kinetic Krylov–Safonov, merely measurable nondivergence kernels, and Conjecture 8.2. The newer Harnack work uses symmetry between the two velocity arguments, a stronger and different condition than evenness about the current velocity. The September 2026 announcement [arXiv:2609.15534](https://arxiv.org/abs/2609.15534) addresses second-order local kinetic diffusion; that does not supply the displayed jump-kernel estimate. No matching result under just the stated conditions was located.
