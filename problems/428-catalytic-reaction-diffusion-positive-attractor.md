# 428. Positive equilibrium attraction for an irreversible catalytic reaction

**Area:** Reaction–diffusion PDEs / chemical kinetics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^n$ be a bounded connected smooth domain with $|\Omega|=1$, and let $d_1,d_2,d_3>0$. Consider the unique global bounded classical solution of
$$a_t-d_1\Delta a=b(c-a),\qquad b_t-d_2\Delta b=b(c-a),\qquad c_t-d_3\Delta c=-b(c-a),$$
with homogeneous Neumann boundary conditions. Assume $a_0,b_0,c_0\in C^2(\overline\Omega)$ are strictly positive and satisfy the Neumann compatibility conditions. Put
$$M_1=\int_\Omega(a_0+c_0),\qquad M_2=\int_\Omega(b_0+c_0),$$
and assume $M_2\le M_1<2M_2$. Is it true that
$$\lim_{t\to\infty}\left[\|a(t)-M_1/2\|_\infty+\|b(t)-(M_2-M_1/2)\|_\infty+\|c(t)-M_1/2\|_\infty\right]=0?$$

## Application

A catalyst can become depleted at a boundary equilibrium even when a positive chemical equilibrium exists. This model asks whether spatial diffusion and positive initial concentrations always sustain the catalyst and select the active equilibrium.

## References

1. T. L. Nguyen and B. Q. Tang, *Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria*, Zeitschrift für angewandte Mathematik und Physik 77 (2026), 199, equation (1.1), the conjecture after Table 1, Theorem 2.1 and §2.3. [DOI and full text](https://doi.org/10.1007/s00033-026-02847-0).
2. K. Fellner, J. Morgan and B. Q. Tang, *Uniform-in-time bounds for quadratic reaction-diffusion systems with mass dissipation in higher dimensions*, Discrete and Continuous Dynamical Systems, Series S 14 (2021), 635–651, main boundedness theorem. [DOI](https://doi.org/10.3934/dcdss.2020334).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The July 2026 paper proves boundedness, local stability of the positive equilibrium and instability of the boundary equilibrium, but states global attraction as a conjecture. Its printed nonnegative-data wording includes a stationary boundary equilibrium; the present formulation explicitly restricts to strictly positive data, removing that immediate obstruction. The irreversible network is not complex balanced, so the complex-balanced global-attractor question is distinct. Searches through 22 September 2026 located no resolution.
