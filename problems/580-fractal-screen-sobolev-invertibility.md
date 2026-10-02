# 580. Full Sobolev invertibility range for Hausdorff-measure screen operators

**Area:** Boundary integral equations and numerical scattering

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`n\in\{1,2\}`$, $`n-1<d\le n`$, and let $`\Gamma\subset\mathbb R^n`$ be a nonempty compact $`d`$-set: for some $`c_1,c_2>0`$,

```math
c_1r^d\le\mathcal H^d(\Gamma\cap B_r(x))\le c_2r^d\qquad(x\in\Gamma,\ 0<r\le1).
```

Regard $`\Gamma\times\{0\}`$ as a sound-soft screen in $`\mathbb R^{n+1}`$. Put $`t_d=(d-n+1)/2`$ and fix a wavenumber $`k>0`$.

For $`s>0`$, define $`\mathbb H^s(\Gamma)`$ as the trace of $`H^{s+(n-d)/2}(\mathbb R^n)`$ on $`\Gamma`$, with its quotient norm. Set $`\mathbb H^0(\Gamma)=L^2(\Gamma,\mathcal H^d)`$ and $`\mathbb H^{-s}(\Gamma)=(\mathbb H^s(\Gamma))^*`$, using $`L^2`$ as the duality pivot.

Let $`\mathbb S_k`$ be the Hausdorff-measure single-layer operator, initially given for bounded densities by

```math
(\mathbb S_k\varphi)(x)=\int_\Gamma\Phi_k((x,0),(y,0))\varphi(y)\,d\mathcal H^d(y),
```

where $`\Phi_k(X,Y)=\tfrac{i}{4}H_0^{(1)}(k|X-Y|)`$ in two-dimensional space and $`\Phi_k(X,Y)=e^{ik|X-Y|}/(4\pi|X-Y|)`$ in three-dimensional space. Use its continuous extensions between the trace spaces above.

Prove or disprove Conjecture 4.8 of [1]: for every such screen and every $`|t|<t_d`$, the operator

```math
\mathbb S_k:\mathbb H^{t-t_d}(\Gamma)\longrightarrow\mathbb H^{t+t_d}(\Gamma)
```

is a bounded linear isomorphism. No self-similarity or separation assumption is imposed on the $`d`$-set.

## Application

The conjecture would establish the solution regularity required for nearly optimal convergence rates of Hausdorff-measure boundary element methods. These methods compute acoustic scattering directly on fractal screens, including screens of zero ordinary surface measure, rather than replacing them by smooth approximations.

## References

1. A. M. Caetano, S. N. Chandler-Wilde, A. Gibbs, D. P. Hewett and A. Moiola, [A Hausdorff-measure boundary element method for acoustic scattering by fractal screens](https://doi.org/10.1007/s00211-024-01399-7), *Numerische Mathematik* **156** (2024), 463–532. Section 2.4, equation (45), Conjecture 4.8 and Proposition 4.9, pages 470–472 and 485–488. [Preprint](https://arxiv.org/abs/2212.06594).
2. S. N. Chandler-Wilde, G. Claret, D. P. Hewett, A. Rozanova-Pierrat and S. Sadeghi, [Integral Equation Methods for Scattering by Multifractal Obstacles](https://arxiv.org/abs/2605.19540), 2026. Section 4.3, especially Proposition 4.10.

## Status review

**Known cases:** At $`t=0`$, coercivity gives invertibility for every screen in the statement. The full interval is known when $`\Gamma`$ is the closure of a bounded Lipschitz domain in its supporting hyperplane. For disjoint iterated-function-system attractors, [1] proves invertibility in some neighborhood $`|t|<\varepsilon`$ of zero.

**Remaining target:** Obtain the entire interval $`|t|<t_d`$ for arbitrary compact $`d`$-sets. The 2026 multifractal extension [2] still supplies only a possibly smaller neighborhood of zero under additional geometric hypotheses; its convergence results do not establish this conjecture.

Current literature, arXiv (including the 2026 follow-up), public GitHub, native Zenodo and Palomar checks found no full resolution or matching announcement. No equivalent catalogue problem was found.
