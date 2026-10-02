# 210. Sharp local smoothing for the three-dimensional wave equation

**Area:** Wave propagation; dispersive estimates

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a Schwartz function $`f`$ on $`\mathbb R^3`$, let

```math
u(t,x)=e^{it\sqrt{-\Delta}}f(x),\qquad \widehat u(t,\xi)=e^{it|\xi|}\widehat f(\xi).
```

For every $`3\le p<\infty`$ and $`\varepsilon>0`$, is there a constant $`C_{p,\varepsilon}`$ such that, for every $`\lambda\ge1`$ and every $`f`$ with Fourier support in $`\{\lambda\le|\xi|\le2\lambda\}`$,

```math
\left(\int_1^2\int_{\mathbb R^3}|u(t,x)|^p\,dx\,dt\right)^{1/p}\le C_{p,\varepsilon}\lambda^{1-3/p+\varepsilon}\|f\|_{L^p(\mathbb R^3)}?
```

## Application

This measures the additional regularity gained by averaging a propagating wave over time. It constrains persistent wave focusing and supports estimates for nonlinear wave equations with rough initial data.

## References

1. David Beltran, Jonathan Hickman, and Christopher D. Sogge, [Sharp local smoothing estimates for Fourier integral operators](https://arxiv.org/abs/1812.11616), survey (2019). Section 2.3, Conjecture 2.4, gives the Euclidean half-wave conjecture and distinguishes it from manifold and general Fourier-integral-operator versions.
2. Tainara Borges, Benjamin Foster, Yumeng Ou, and Eyvindur Palsson, [Nonempty interior of pinned distance and tree sets](https://doi.org/10.1016/j.aim.2026.110917), *Adv. Math.* (2026). Section 2.3, Conjecture 12, and the discussion following Theorem 3 retain the open three-dimensional threshold.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 application explicitly treats the three-dimensional critical estimate as conjectural. General Fourier-integral-operator theorems have different admissible exponents, and the proved two-dimensional wave result does not cover this dimension. The arbitrarily small loss $`\varepsilon`$ is part of the statement.

**Search audit:** Queries: “local smoothing conjecture Euclidean wave R3 2026”, “local smoothing rough wave equations 2608.01440”; checked its conjectured endpoint discussion rather than interpreting “sharp” as the full Euclidean range. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
