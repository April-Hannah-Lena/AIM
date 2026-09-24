# 229. One cubic NLS trajectory with unbounded Sobolev norm

**Area:** Nonlinear wave turbulence

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On $`\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2`$, does there exist $`u_0\in C^\infty(\mathbb T^2;\mathbb C)`$ such that the global solution of

```math
i\partial_tu+\Delta u=|u|^2u,\qquad u(0)=u_0,
```

satisfies

```math
\limsup_{t\to\infty}\|u(t)\|_{H^2(\mathbb T^2)}=\infty?
```

Here $`\|u\|_{H^2}^2=\sum_{k\in\mathbb Z^2}(1+|k|^2)^2|\widehat u(k)|^2`$. A single fixed initial datum and its entire forward trajectory must realize the unbounded growth.

## Application

This would rigorously demonstrate an indefinitely continuing transfer toward fine spatial scales in a basic conservative nonlinear-wave model, despite conservation of mass and energy.

## References

- Filippo Giuliani and Marcel Guardia, [*Arnold diffusion in Hamiltonian systems on infinite lattices*](https://diposit.ub.edu/bitstreams/4cd40dfd-10f5-4876-8b7d-b46751475686/download) (2023 manuscript), §1.4: explicitly distinguishes the open cubic-NLS question from proved lattice diffusion.
- Sebastian Herr and Beomjong Kwak, [*Global well-posedness of the cubic nonlinear Schrödinger equation on $`\mathbb T^2`$*](https://doi.org/10.1007/s00222-026-01418-4) (2026), introduction and main theorem: recent global existence at low regularity, a different issue from long-time Sobolev growth.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “cubic NLS torus single orbit unbounded Sobolev growth”, “weak turbulence two torus proof 2025 2026”, and the 2026 global-well-posedness result. Arbitrarily large finite growth factors obtained by choosing different data do not provide the single orbit requested here. Results on waveguides with a noncompact factor or modified nonlinearities also differ.
