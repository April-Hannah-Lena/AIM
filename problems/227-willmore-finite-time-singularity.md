# 227. Finite-time singularity formation for unconstrained Willmore flow

**Area:** Membrane bending and geometric evolution

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Does there exist a smooth closed connected orientable surface $\Sigma$ and a smooth immersion $f_0:\Sigma\to\mathbb R^3$ whose maximal smooth unconstrained Willmore flow has finite lifetime $T<\infty$?

Precisely, for the induced metric $g$, second fundamental form $A$, mean curvature $H=\operatorname{tr}_g A$ and trace-free part $A^\circ=A-(H/2)g$, consider
$$\partial_t f\cdot\nu=-\big(\Delta_gH+H|A^\circ|^2\big),\qquad f(0)=f_0,$$
with compatible curvature and normal conventions, and arbitrary tangential reparametrization. Seek an evolution that cannot be smoothly extended past a finite $T$, equivalently with curvature becoming unbounded as $t\uparrow T$. There are no area, volume or spontaneous-curvature terms in this flow.

## Application

Willmore energy models bending of thin membranes. A finite-time singularity would identify a failure of smooth bending relaxation even without external loading or area penalties.

## References

- Uwe F. Mayer and Gieri Simonett, [*A numerical scheme for axisymmetric solutions of curvature-driven free boundary problems, with applications to the Willmore flow*](https://ems.press/content/serial-article-files/36255) (2002), §8.5: numerical singular examples and the open finite-time question.
- Simon Blatt, [*A singular example for the Willmore flow*](https://www.instmath.rwth-aachen.de/Preprints/blatt20080715.pdf) (2008 preprint; 2009 publication), introduction and main theorem: singular behavior at finite or infinite time, without distinguishing the two.
- Pak Tung Ho and Juncheol Pyo, [*Solitons to the Willmore flow*](https://doi.org/10.1515/ans-2023-0150) (2024 online), introduction: later discussion of the finite-time question and special solutions.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “unconstrained Willmore flow finite time singularity proof 2025 2026”, “Blatt singular example finite infinite time”, and “Willmore soliton singularity”. Located results for constrained Willmore or Helfrich flows include additional terms. Blatt’s result allows infinite-time degeneration and therefore does not answer the finite-lifetime question.
