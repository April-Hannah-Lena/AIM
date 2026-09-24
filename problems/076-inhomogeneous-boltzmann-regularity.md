# 076. Large-data global smoothness for the spatially inhomogeneous Boltzmann equation

**Area:** Kinetic theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $`\mathbb T_x^3\times\mathbb R_v^3`$, consider

```math
\partial_t f+v\cdot\nabla_x f=Q(f,f),\qquad
Q(f,f)(v)=\int_{\mathbb R^3}\int_{\mathbb S^2}
|v-v_*|\,\big[f(v')f(v_*')-f(v)f(v_*)\big]\,d\sigma\,dv_*,
```

where $`v'=(v+v_*)/2+|v-v_*|\sigma/2`$ and
$`v_*'=(v+v_*)/2-|v-v_*|\sigma/2`$; all factors have the same $`(t,x)`$.
For every strictly positive smooth datum, rapidly decreasing with all derivatives in $`v`$ and bounded below by some $`a e^{-b|v|^2}`$ with $`a,b>0`$, does a unique global smooth solution exist? This fixes the angular-cutoff hard-sphere kernel and imposes no closeness to a Maxwellian.

## Application

The question asks whether the kinetic model underlying dilute-gas simulation remains regular far from thermodynamic equilibrium.

## References

- [Luis Silvestre, *Regularity estimates and open problems in kinetic equations* (2022), §3 on existence of solutions, including both cutoff and non-cutoff kernels](https://arxiv.org/abs/2204.06401).
- [Christopher Henderson, Stanley Snelson and Andrei Tarfulea, *Classical solutions of the Boltzmann equation with irregular initial data* (Ann. Sci. Éc. Norm. Supér., 2025), local large-data and global near-equilibrium results for the non-cutoff setting](https://arxiv.org/abs/2207.03497).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey separates unrestricted inhomogeneous smoothness from global renormalized solutions. The 2025 paper's global conclusion requires near-equilibrium data and concerns non-cutoff collisions. Searches for later large-data global theorems located results with additional restrictions, not this arbitrary-data hard-sphere assertion.

Searches run on 2026-09-08: `site.arxiv.org Boltzmann large data global classical solutions open problem 2025`; `site.arxiv.org Boltzmann large data open regularity`. This is a literature search, not a proof that no solution exists.
