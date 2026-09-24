# 192. Pathwise uniqueness at the three-quarter Hölder threshold

**Area:** Stochastic reaction–diffusion equations

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\sigma:\mathbb R\to\mathbb R`$ satisfy $`|\sigma(a)-\sigma(b)|\le C|a-b|^{3/4}`$ for all $`a,b`$, and let $`u_0`$ be bounded and continuous. On $`\mathbb R`$, consider the Itô–Walsh mild equation

```math
u(t,x)=(p_t*u_0)(x)+\int_0^t\!\int_{\mathbb R}p_{t-s}(x-y)\sigma(u(s,y))\,W(ds,dy),
```

where $`p_t(x)=(2\pi t)^{-1/2}e^{-x^2/(2t)}`$ and $`W`$ is space–time white noise.

Must any two adapted continuous mild solutions with the same $`u_0`$ and the same noise be indistinguishable, in the class satisfying

```math
\sup_{0\le t\le T,\ x\in\mathbb R}e^{-a|x|}|u(t,x)|<\infty
\quad\text{almost surely for every }a,T>0?
```

The coefficient may vanish and solutions may have either sign.

## Application

Noise coefficients with limited smoothness arise in population-density and branching models. The endpoint would identify the sharp regularity at which a stochastic diffusion law determines its trajectory from its driving noise.

## References

- [Leonid Mytnik and Edwin Perkins, *Pathwise uniqueness for stochastic heat equations with Hölder continuous coefficients: the white noise case* (2011)](https://arxiv.org/abs/0809.0248), Theorem 1.2.
- [Carl Mueller, Leonid Mytnik and Edwin Perkins, *Nonuniqueness for a parabolic SPDE with three-quarter-minus-epsilon Hölder diffusion coefficients* (2014)](https://arxiv.org/abs/1201.2767), discussion immediately after Theorem 1.1.
- [Yi Han, *Stochastic heat equation with nondegenerate Hölder diffusion coefficient: uniqueness below the three-fourth threshold* (August 2026 preprint)](https://arxiv.org/abs/2608.01279), §1 and its distinction between weak and pathwise uniqueness.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2014 paper explicitly leaves the endpoint open. Han's August 2026 theorem assumes a uniformly nonvanishing coefficient and proves uniqueness in law, not pathwise uniqueness; it does not settle this general endpoint. The signed solution class is intentional: nonnegative special models have additional structure.

Search topics checked on 2026-09-08: stochastic heat critical 3/4 pathwise uniqueness open; Holder diffusion uniqueness 2026 Han.
