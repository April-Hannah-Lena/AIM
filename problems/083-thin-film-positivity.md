# 083. Preservation of strict positivity for the cubic thin-film equation

**Area:** Thin films and lubrication

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`h_0\in C^\infty(\mathbb T)`$ satisfy $`\min h_0>0`$, where $`\mathbb T=\mathbb R/\mathbb Z`$. For

```math
h_t+\partial_x(h^3\partial_x^3h)=0,\qquad h(0,x)=h_0(x),
```

does the positive classical solution extend to every finite time and satisfy

```math
\inf_{(t,x)\in[0,T]\times\mathbb T}h(t,x)>0
\quad\text{for every }T<\infty?
```

There are no disjoining-pressure, gravitational or stochastic terms. The question concerns strict positivity at every time, rather than nonnegative weak solutions or positivity at almost every time.

## Application

Cubic mobility is the no-slip lubrication model. A proof would exclude finite-time dry spots created solely by capillarity from an initially wet film.

## References

- [Benjamin Gess, Rishabh S. Gvalani, Florian Kunick and Felix Otto, *Thermodynamically consistent and positivity-preserving discretization of the thin-film equation with thermal noise* (2021 preprint; Mathematics of Computation, 2023), continuum touch-down discussion](https://arxiv.org/abs/2109.06083).
- [Florian Johannes Kunick, *Analysis and Numerics of Stochastic Gradient Flows* (doctoral thesis, Universität Leipzig, 2022), §3.10](https://d-nb.info/1296492575/34).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The thesis explicitly calls deterministic cubic-mobility positivity open and contrasts it with the proven higher-exponent case. The cited discretization preserves positivity at fixed discretization size; that does not prove a positive lower bound in the continuum limit. Searches through 2026 found no resolution for this deterministic cubic equation.

Searches run on 2026-09-08: `thin film positivity n=3 open`; `thin-film cubic mobility open positivity`. This is a literature search, not a proof that no solution exists.
