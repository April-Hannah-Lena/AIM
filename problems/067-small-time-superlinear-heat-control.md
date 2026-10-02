# 067 — Small-time global control of a slightly superlinear heat equation

**Area:** Nonlinear PDE control

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega\subset\mathbb R^d`$ be a bounded connected $`C^2`$ domain and $`\omega\subset\Omega`$ a nonempty open control region. For every exponent $`\alpha\in[3/2,2)`$, every $`T>0`$, and every $`y_0\in L^\infty(\Omega)`$, determine whether there is $`v\in L^\infty((0,T)\times\omega)`$ such that

```math
\partial_t y-\Delta y+|y|\log^\alpha(2+|y|)=\mathbf1_\omega v,\qquad
y|_{\partial\Omega}=0,\quad y(0)=y_0,
```

has a bounded weak solution on $`[0,T]`$ with $`y(T)=0`$. The time $`T`$ is prescribed independently of the initial state; negative initial data are allowed.

## Application

The question concerns whether a localized actuator can suppress a potentially blowing-up reaction in any prescribed positive time.

## References

1. Enrique Fernández-Cara and Enrique Zuazua, *Null and Approximate Controllability for Weakly Blowing Up Semilinear Heat Equations*, Annales de l'Institut Henri Poincaré C, Analyse Non Linéaire **17** (2000), 583–616. [DOI](https://doi.org/10.1016/S0294-1449(00)00117-7).
2. Kévin Le Balc'h, *Global Null-Controllability and Nonnegative-Controllability of Slightly Superlinear Heat Equations*, Journal de Mathématiques Pures et Appliquées (2020). [DOI](https://doi.org/10.1016/j.matpur.2019.10.009), [preprint](https://arxiv.org/abs/1810.12232).

## Status review

**Known cases:** Uniform sufficiently-large-time null controllability is established for the displayed nonlinearity.

**Remaining target:** Null controllability for arbitrary initial states in every prescribed positive time, including arbitrarily short times.

**Literature check:** Open in cited literature; no later resolution located

Fernández-Cara–Zuazua leave a gap in logarithmic growth exponents for small-time global null control. Le Balc'h resolves uniform sufficiently-large-time null control for the displayed nonlinearity, and small-time control to a nonnegative state, while leaving arbitrary-small-time null control open. Searches on 2026-09-08: "semilinear heat 3/2 2025 controllability" and "Global null-controllability small time 2025 Le Balc". No resolution of the prescribed-time assertion was located.
