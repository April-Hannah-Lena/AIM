# 232. Finite-time growth of total variation in physical gas dynamics

**Area:** Nonlinear hyperbolic conservation laws

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Can finite-time blowup of total variation occur for an exact entropy solution of the polytropic $`p`$-system while its state remains bounded away from vacuum and concentration?

Specifically, determine whether there exist $`\gamma>1`$, $`T<\infty`$ and a distributional solution on $`[0,T)\times\mathbb R`$ of

```math
v_t-u_x=0,\qquad u_t+(v^{-\gamma})_x=0,
```

with initial data of finite total variation, with $`0<a\leq v\leq b<\infty`$ and $`|u|\leq M`$, such that for every $`T'<T`$,

```math
\mathop{\mathrm{ess\,sup}}_{t\leq T'}[\mathop{\mathrm{TV}}\nolimits v(t)+\mathop{\mathrm{TV}}\nolimits u(t)]<\infty,
```

but this bound diverges as $`T'\uparrow T`$. Require local $`L^1`$ continuity in time and the mechanical entropy inequality

```math
\partial_t\left(\frac{u^2}{2}+\frac{v^{1-\gamma}}{\gamma-1}\right)+\partial_x(uv^{-\gamma})\leq0.
```

Here $`v`$ is specific volume, $`u`$ is velocity, and $`\mathop{\mathrm{TV}}\nolimits`$ is spatial total variation on $`\mathbb R`$.

## Application

Finite total variation controls interacting shocks and rarefactions in one-dimensional gas dynamics. Its loss would challenge continuation methods used for large-amplitude flow beyond classical shock formation.

## References

- Alberto Bressan, Geng Chen and Qingtian Zhang, [*On finite time BV blow-up for the p-system*](https://arxiv.org/abs/1710.03382) (2017 preprint; 2018 publication), §1: the exact-solution question, necessary conditions, and approximate blowup constructions.
- Sam G. Krupa, [*Non-uniqueness and BV blowup for vacuously Liu-admissible solutions to p-system via computer-assisted proof*](https://doi.org/10.1007/s00021-026-01018-5) (2026), abstract and note 2: its construction does not obey the natural strictly convex entropy.
- Sam G. Krupa, [*The computational ansatz for convex integration of hyperbolic systems and a resolution of the Strong Trace Conjecture*](https://arxiv.org/abs/2609.09353) (8 September 2026 preprint), abstract: new constructions for a selected pressure law and obstructions for strictly convex pressure laws.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “p-system exact entropy finite time BV blowup 2026”, “polytropic pressure large BV”, and both recent Krupa papers. The April construction fails the mechanical entropy condition. The September preprint concerns a specially selected pressure law; its abstract separately gives obstructions when the pressure has positive second derivative. Neither establishes the displayed polytropic, entropy-admissible finite-time scenario. Approximate front-tracking growth is not an exact solution.
