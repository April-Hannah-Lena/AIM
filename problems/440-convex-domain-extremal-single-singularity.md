# 440. A single blow-up point for singular extremal states on convex domains

**Area:** Semilinear elliptic PDEs and thermal ignition

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`d\ge10`$, let $`\Omega\subset\mathbb R^d`$ be bounded, smooth and convex, and let $`f\in C^\infty([0,\infty))`$ be positive, increasing and convex with $`f(t)/t\to\infty`$. For the Dirichlet problem

```math
-\Delta u=\lambda f(u)\quad\hbox{in }\Omega,\qquad u=0\quad\hbox{on }\partial\Omega,
```

let $`u_\lambda`$ be the minimal positive classical branch, $`\lambda^*`$ its maximal parameter, and $`u^*=\lim_{\lambda\uparrow\lambda^*}u_\lambda`$. Suppose $`u^*\notin L^\infty(\Omega)`$. Must the set

```math
\Sigma=\{x\in\overline\Omega:\ \mathop{\mathrm{ess\,sup}}_{\Omega\cap B_r(x)}u^*=\infty\ \hbox{for every }r>0\}
```

consist of exactly one point?

## Application

Minimal branches describe stable temperature or reaction equilibria up to an ignition threshold. The geometry of the singular set determines whether loss of boundedness is localized at one ignition site or several.

## References

1. H. Brezis, [Some of my favorite open problems](https://doi.org/10.4171/RLM/1008), *Rendiconti Lincei—Matematica e Applicazioni* (2023), §6, Open Problem 6.2.
2. H. Brezis and J. L. Vázquez, [Blow-up solutions of some nonlinear elliptic problems](https://sites.math.rutgers.edu/~brezis/PUBlications/152.pdf), *Revista Matemática de la Universidad Complutense de Madrid* **10** (1997), 443–469, §8, Problem 5.
3. B. Yu and Y. Zhou, [Singular Extremal Solutions on Thin Ellipsoids with Varying Nonlinearities](https://arxiv.org/abs/2609.06673), preprint (2026), Theorem 1.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2023 source explicitly asks whether convexity forces a single blow-up point. The September 2026 construction concerns particular thin ellipsoids and adapted nonlinearities; it does not classify singular sets for all convex domains and all the stated nonlinearities. Searches for multiple singular points of convex-domain extremal solutions found no general resolution. This question is separate from whether the exponential nonlinearity always has a singular extremal state, which is excluded from this collection.
