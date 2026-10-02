# 359. Global regularity of the planar noncorotational FENE fluid

**Area:** Polymer rheology; kinetic–fluid coupling

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`B=\{q\in\mathbb R^2:|q|<1\}`$, $`k>2`$, $`U(q)=-k\log(1-|q|^2)`$ and $`M(q)=Z^{-1}e^{-U(q)}`$, with $`\int_B M=1`$. On $`\mathbb R_x^2\times B_q`$, consider

```math
u_t+u\cdot\nabla_xu-\Delta_xu+\nabla_xp=\nabla_x\cdot\tau,\qquad\nabla_x\cdot u=0,
```



```math
\psi_t+u\cdot\nabla_x\psi=\nabla_q\cdot\bigl(\nabla_q\psi+\psi\nabla_qU-(\nabla_xu)q\psi\bigr),\qquad \tau=\int_B q\otimes\nabla_qU\,\psi\,dq.
```

Impose zero normal configuration flux at $`\partial B`$ and $`\int_B\psi(t,x,q)\,dq=1`$. For every smooth compatible initial datum with $`u_0`$ divergence free, $`\psi_0=M g_0`$, $`g_0>0`$, and $`u_0,g_0-1`$ smooth and compactly supported in $`x`$, must the local classical solution extend for all positive times? Require on each finite interval the usual strong norms $`u\in C_tH_x^s`$ and $`\psi-M\in C_tH_x^s(L_q^2(M^{-1}dq))`$ for every $`s`$, with smoothness for $`q\in B`$. There is no smallness assumption and no centre-of-mass diffusion in $`x`$.

## Application

The finite extensibility of polymer chains prevents infinite molecular elongation, but it is unknown whether it also prevents singular macroscopic stresses in arbitrary planar flows. The full velocity gradient transfers both rotation and stretching to the molecules.

## References

1. N. Masmoudi, [*Global existence of weak solutions to the FENE dumbbell model of polymeric flows*](https://arxiv.org/abs/1004.4015), Inventiones Mathematicae 191 (2013), 427–500; §7, “Regularity in 2D”; [author full text](https://math.nyu.edu/~masmoudi/Fene-global.pdf).
2. N. Masmoudi, [*Well-posedness for the FENE dumbbell model of polymeric flows*](https://doi.org/10.1002/cpa.20252), Communications on Pure and Applied Mathematics 61 (2008), 1685–1714, local theory and the small-data and corotational global theorems.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using planar noncorotational FENE global strong solutions and 2024–2026 large-data results. The cited weak-existence paper explicitly separates this smoothness problem from its own theorem. Global corotational results replace $`\nabla u`$ by its antisymmetric part, eliminating stretching. Recent results such as [arXiv:2408.00993](https://arxiv.org/abs/2408.00993) treat some large compressible data under quantitative restrictions, and near-equilibrium FENE results require small perturbations. No unrestricted theorem for the displayed noncorotational model was located.
