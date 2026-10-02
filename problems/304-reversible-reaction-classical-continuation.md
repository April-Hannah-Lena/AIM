# 304. Global classical continuation for a reversible mass-action reaction

**Area:** Chemical reaction–diffusion / continuum biology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $`I,J,n\ge1`$ be integers and let $`\Omega\subset\mathbb R^n`$ be a bounded connected domain with smooth boundary. Consider distinct chemical species undergoing one reversible reaction

```math
\sum_{i=1}^{I}\alpha_i A_i\ \rightleftarrows\ \sum_{j=1}^{J}\beta_j B_j,
\qquad \alpha_i,\beta_j\in\{1,2,\ldots\}.
```

For concentrations $`a=(a_1,\ldots,a_I)`$ and $`b=(b_1,\ldots,b_J)`$, set

```math
R(a,b)=k_+\prod_{i=1}^{I}a_i^{\alpha_i}
       -k_-\prod_{j=1}^{J}b_j^{\beta_j},\qquad k_+,k_->0.
```

Fix arbitrary constant diffusivities $`d_i,e_j>0`$ and solve

```math
\partial_t a_i-d_i\Delta a_i=-\alpha_i R(a,b),\qquad
\partial_t b_j-e_j\Delta b_j=\beta_j R(a,b)
```

in $`(0,\infty)\times\Omega`$, with $`\partial_\nu a_i=\partial_\nu b_j=0`$ on the boundary, where $`\nu`$ is the outward normal. The initial concentrations are arbitrary nonnegative smooth functions on $`\overline\Omega`$ satisfying these boundary conditions.

Must the unique local nonnegative classical solution extend to every finite time? Equivalently, can finite-time concentration blowup be excluded for every such reaction, domain, set of coefficients and initial state? The required bound is

```math
\sup_{0\le t\le T}\left(\sum_{i=1}^{I}\|a_i(t)\|_{L^\infty(\Omega)}
+\sum_{j=1}^{J}\|b_j(t)\|_{L^\infty(\Omega)}\right)<\infty
\quad\text{for each }T<\infty.
```

Here classical means continuous to the initial data and continuously differentiable in time and twice in space for positive times, satisfying the equations and boundary conditions pointwise. Bounds may depend on $`T`$, the data and all coefficients. No upper bound on reaction order, smallness of the initial data, or closeness of diffusivities is assumed. This is the single-reaction, disjoint-species version of the broader chemical reaction-network regularity question; its parameter cases count as one entry.

## Application

This models a closed reaction vessel containing diffusing chemical or biochemical species. Forward and backward mass-action rates couple local concentrations, while species move at different rates. A positive answer would justify using the classical concentration equations through any finite observation interval, even for large spatially uneven initial concentrations and higher-order reactions. Integrated mass and entropy estimates alone do not give the pointwise concentration control needed for that conclusion.

## References

- Julian Fischer, [*Weak–strong uniqueness of solutions to entropy-dissipating reaction–diffusion equations*](https://arxiv.org/abs/1703.00730), *Nonlinear Analysis* 159 (2017), 181–207. The arXiv text §1, equations (1)–(3), explicitly states the smooth global-existence question; Theorems 3 and 7 distinguish renormalized existence from conditional uniqueness.
- Klemens Fellner and Bao Quoc Tang, [*Explicit exponential convergence to equilibrium for nonlinear reaction–diffusion systems with detailed balance condition*](https://imsc.uni-graz.at/fellnerk/preprints/FTfinal.pdf), *Nonlinear Analysis* 159 (2017), 145–180, equations (1.12)–(1.14), Theorem 1.2 and Remark 1.1 in the author text. These give the no-flux model and its renormalized-solution theory.
- Klemens Fellner, Jeff Morgan and Bao Quoc Tang, [*Global classical solutions to quadratic systems with mass control in arbitrary dimensions*](https://www.numdam.org/item/10.1016/j.anihpc.2019.09.003.pdf), *Annales de l’Institut Henri Poincaré C* 37 (2020), 281–307, Theorem 1.1 and Remark 1.1.
- Antonio Agresti, [*Delayed blow-up and enhanced diffusion by transport noise for systems of reaction-diffusion equations*](https://arxiv.org/abs/2207.08293), arXiv:2207.08293v4 (2023; accepted manuscript), §§1–1.2 and Theorem 1.2.
- Antonio Agresti, Michael Kniely and Bao Quoc Tang, [*Global classical solutions by transport noise for reaction-diffusion systems with entropy dissipation*](https://arxiv.org/html/2608.13332v1), August 2026 preprint, §§1, 1.3, Theorem 3.4 and Proposition 6.5.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited sources distinguish global renormalized solutions from classical continuation. Quadratic reactions have global classical solutions in arbitrary dimensions; higher-order cases require further hypotheses. The August 2026 result concerns suitably chosen transport noise on a torus, and its deterministic result assumes sufficiently large diffusivities. These conclusions leave the arbitrary-coefficient deterministic question above unresolved.

The May 2026 Bouton–Desvillettes–Dietert [Theorem 1](https://arxiv.org/pdf/2605.23709) provides a new proof for a quadratic four-species system in dimensions at most three. Porous-medium regularity results change the diffusion law. The evidence ledger records the precise comparisons and the limits of source access.

Known generic mass-control blowup examples require a separate scope check. Pierre’s [2021 author statement](https://math.univ-cotedazur.fr/u/delarue/GE2MI_MPierre1.pdf), PDF pp. 57–63, uses prescribed Dirichlet data, or explicitly space/time-dependent reactions for its no-flux adaptation. Hopf–Tang’s [2026 specialist discussion](https://www.wias-berlin.de/preprint/3263/wias_preprints_3263.pdf), printed p. 4, still distinguishes these examples from the entropy-dissipating setting. The original Pierre–Schmitt journal PDF required login; the author restatement and later discussion were used instead.

Searches on 2026-09-17 covered reversible mass-action classical existence, smooth continuation, blowup, counterexamples, recent results, version histories and corrections. The separate adversarial self-pass A16 checked additional diffusion-closeness and low-dimensional results; none covers the full statement. See the [evidence ledger](../research/expansion-2026-09/candidates/reversible-reaction-classical-continuation.json).

Related entries [273](272-reaction-network-positive-recurrence.md) and [274](273-reaction-network-persistence.md) concern stochastic molecule counts and spatially homogeneous ODE persistence, respectively; neither asks for PDE continuation.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration.
