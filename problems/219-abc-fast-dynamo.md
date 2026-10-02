# 219. Fast dynamo action of the unit ABC flow

**Area:** Magnetohydrodynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On $`\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3`$, fix

```math
u=(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x).
```

For magnetic diffusivity $`\eta>0`$, let $`L_\eta B=\eta\Delta B+\nabla\times(u\times B)`$ on complex, mean-zero, divergence-free $`L^2`$ vector fields, with domain $`H^2`$ in that space. Write $`s(\eta)=\sup\{\mathop{\mathrm{Re}}\nolimits\lambda:\lambda\in\sigma(L_\eta)\}`$.

Prove or disprove that this fixed velocity field is a fast kinematic dynamo in the spectral sense:

```math
\liminf_{\eta\downarrow0}s(\eta)>0.
```

The velocity and its three coefficients remain fixed while diffusivity tends to zero.

## Application

This asks whether a standard model of three-dimensional chaotic advection amplifies a weak magnetic field at a rate that survives the high-conductivity limit.

## References

- Ismaël Bouya and Emmanuel Dormy, [*Revisiting the ABC flow dynamo*](https://arxiv.org/abs/1206.5186) (2012 preprint; 2013 publication), abstract and numerical growth-rate study: high-magnetic-Reynolds-number evidence.
- Massimo Sorella and David Villringer, [*A limsup fast dynamo on $`\mathbb T^3`$*](https://arxiv.org/html/2511.23024v2) (2025 preprint), abstract and §§2–3: the unresolved stronger fast-dynamo question and the distinction between fixed ABC flows and the constructed time-dependent flow.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “ABC fast dynamo rigorous proof”, “unit ABC spectral growth diffusivity 2025 2026”, and recent fast-dynamo constructions. The Sorella–Villringer result concerns a time-dependent Lipschitz velocity and a limsup formulation. It does not establish the positive liminf above for the fixed unit ABC field; finite-resolution growth-rate computations also do not establish that limit.
