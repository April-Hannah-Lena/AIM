# 183. Coexistence for every positive cyclic invasion rate

**Area:** Spatial ecology and evolutionary dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $`\mathbb Z^2`$, let $`\eta_t(x)\in\{1,2,3\}`$ and $`f_i(x,\eta)=\frac14\sum_{|y-x|_1=1}\mathbf1_{\{\eta(y)=i\}}`$. The only transitions at a site are $`3\to1`$ at rate $`\beta_1f_1`$, $`1\to2`$ at rate $`\beta_2f_2`$, and $`2\to3`$ at rate $`\beta_3f_3`$. For every $`\beta_1,\beta_2,\beta_3>0`$, does this process possess a stationary probability measure $`\nu`$, invariant under lattice translations, such that

```math
\nu\bigl(\#\{x\in\mathbb Z^2:\eta(x)=i\}=\infty\text{ for every }i=1,2,3\bigr)=1?
```

All three populations must coexist in the same configuration almost surely; a mixture of the three constant absorbing configurations does not qualify.

## Application

Cyclic competition occurs in spatial ecological communities. The question asks whether spatial structure sustains all three populations even when invasion rates are very unequal.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, book manuscript of 2 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf), §4.5.1, Open Problem 4.5.2.
- [Rick Durrett and Simon A. Levin, *Spatial aspects of interspecific competition* (1998)](https://doi.org/10.1006/tpbi.1997.1338), the spatial model and simulations.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 book explicitly retains coexistence for arbitrary positive cyclic rates as an open problem. Periodic orbits of the mean-field ODE and finite simulations do not construct a coexistence law for the infinite stochastic lattice system.

Search topics checked on 2026-09-08: Silvertown cyclic competition coexistence arbitrary rates; Durrett Levin rock paper scissors coexistence proof 2025 2026.
