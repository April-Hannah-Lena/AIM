# 081. Large-data global regularity for creeping-flow Oldroyd–B without stress diffusion

**Area:** Viscoelasticity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On the unit torus $`\mathbb T^2`$, let $`C_0`$ be an arbitrary smooth symmetric positive-definite $`2\times2`$ matrix field. Set all material constants to one. Does

```math
-\Delta u+\nabla p=\nabla\cdot C,\qquad \nabla\cdot u=0,\qquad \int_{\mathbb T^2}u\,dx=0,
```



```math
C_t+u\cdot\nabla C-(\nabla u)C-C(\nabla u)^T=-(C-I),\qquad C(0)=C_0
```

have a unique global smooth solution with $`C`$ positive definite? Pressure has zero mean. The velocity is determined by the elliptic Stokes equation at each time; there is no inertial term and no Laplacian acting on $`C`$. The question is for arbitrary large data.

## Application

This is a standard low-Reynolds-number model of polymeric fluids, where stress transport may become singular even though the velocity solves an elliptic equation.

## References

- [Peter Constantin and Weiran Sun, *Remarks on Oldroyd-B and related complex fluid models* (Communications in Mathematical Sciences, 2012)](https://doi.org/10.4310/CMS.2012.v10.n1.a3).
- [Yinghui Wang, Shihao Zhang and Zhuo Zhang, *Global well-posedness of strong solutions to the initial-boundary value problem for a two-dimensional stress-diffusive Oldroyd-B model in the creeping flow regime* (2026), abstract and §1](https://arxiv.org/abs/2608.25333).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 paper explicitly says that the non-diffusive creeping-flow problem remains open in two dimensions. Its large-data theorem retains stress diffusion. Small-data results or the introduction of diffusion cannot be used to mark the system above solved.

Searches run on 2026-09-08: `Oldroyd-B global regularity open 2025`; `Remarks on Oldroyd-B and related complex fluid models`. This is a literature search, not a proof that no solution exists.
