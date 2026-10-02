# 485. Global attraction for complex-balanced reaction–diffusion with boundary equilibria

**Area:** Reaction–diffusion PDEs; chemical equilibration

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`\Omega\subset\mathbb R^d`$ be smooth, bounded and connected, with $`|\Omega|=1`$. A finite mass-action network consists of reactions $`y_r\to y'_r`$ in $`\mathbb N_0^N`$ and rates $`k_r>0`$. Put $`z^y=\prod_i z_i^{y_i}`$ and

```math
f(z)=\sum_r k_r z^{y_r}(y'_r-y_r),\qquad S=\mathop{\mathrm{span}}\nolimits\{y'_r-y_r\}_r.
```

Assume complex balance: some $`c_*\in(0,\infty)^N`$ satisfies, for every complex $`y`$,

```math
\sum_{r:y_r=y}k_r c_*^{y_r}=\sum_{r:y'_r=y}k_r c_*^{y_r}.
```

For arbitrary diffusion constants $`d_i>0`$, consider

```math
\partial_tu_i=d_i\Delta u_i+f_i(u),\qquad\partial_\nu u_i=0.
```

Let $`u_0`$ be smooth, strictly positive and boundary-compatible, and suppose its classical solution exists globally and satisfies $`\sup_{t\ge0}\|u(t)\|_{L^\infty}<\infty`$. Let $`c_\infty`$ be the unique positive equilibrium with $`\int_\Omega u_0-c_\infty\in S`$.

Must $`\|u(t)-c_\infty\|_{L^1(\Omega)}\to0`$ as $`t\to\infty`$, even when the same stoichiometric class contains equilibria with zero components? No uniform positive lower bound on $`u`$ is assumed, and the diffusion constants need not be large or nearly equal.

## Application

This asks whether bounded spatially varying chemical concentrations always relax to the predicted positive equilibrium, despite possible equilibria representing extinction of some species.

## References

1. L. Desvillettes, K. Fellner and B. Q. Tang, *Trend to equilibrium for reaction-diffusion systems arising from complex balanced chemical reaction networks*, SIAM J. Math. Anal. **49** (2017), 2666–2709, §3 and Remark 3.6. [Article](https://doi.org/10.1137/16M1073935); [author manuscript](https://imsc.uni-graz.at/fellnerk/preprints/DFT.pdf).
2. K. Fellner and B. Q. Tang, *Convergence to equilibrium of renormalised solutions to nonlinear chemical reaction-diffusion systems*, Z. Angew. Math. Phys. **69**, 54 (2018), discussion of boundary equilibria. [Author manuscript](https://imsc.uni-graz.at/fellnerk/preprints/FTRenorm.pdf).
3. T. L. Nguyen and B. Q. Tang, *Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria*, Z. Angew. Math. Phys. **77**, 199 (2026), Introduction. [Article](https://doi.org/10.1007/s00033-026-02847-0).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The SIAM paper explicitly leaves general systems with boundary equilibria open. The 2018 and July 2026 papers explain why the absence-of-boundary-equilibria theory does not settle this regime. Searches on 2026-09-22 also found convergence for selected networks, a single reversible reaction with bounded solutions, near-equilibrium data, and sufficiently large diffusivity; these restrictions do not imply the statement for arbitrary complex-balanced networks and diffusion constants. The question assumes global boundedness to separate asymptotic selection from global existence. It is a spatial PDE problem; catalogue problem 276 concerns general weakly reversible ODE persistence without complex balance.
