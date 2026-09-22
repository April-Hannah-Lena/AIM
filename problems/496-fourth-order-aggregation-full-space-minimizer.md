# 496. Full-space minimizers for subcritical fourth-order aggregation energy

**Area:** Variational PDEs; aggregation and phase separation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every $d\ge2$, $\chi>0$ and $1<m<2+2/d$, define
$$
\mathcal E_m(\rho)=\frac12\int_{\mathbb R^d}|\nabla\rho|^2\,dx
-\frac{\chi}{m-1}\int_{\mathbb R^d}\rho^m\,dx
$$
on
$$
\mathcal A=\{\rho\in H^1(\mathbb R^d):\rho\ge0,\ \int\rho=1,\ \int|x|^2\rho(x)\,dx<\infty\}.
$$
Is $\inf_{\rho\in\mathcal A}\mathcal E_m(\rho)$ attained in $\mathcal A$? No external confining potential, prescribed support, or symmetry constraint is imposed. Translates of a minimizer are identified when discussing the lack of compactness, but the problem asks only for existence, not uniqueness or a formula.

## Application

The energy balances concentration-promoting attraction against the cost of spatial variation in an aggregate density. Attainment would justify an equilibrium shape at fixed total mass without adding an artificial confining potential or prescribing the support. It would give a variational foundation for the fourth-order aggregation model, while leaving dynamical convergence to that equilibrium as a separate question.

## References

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Theorem 2.1 and §3. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The source proves a lower energy bound in this subcritical range and treats critical optimizers, but explicitly leaves full-space subcritical minimizers open; the 2025 review repeats the gap. Searches on 2026-09-22 for this energy, the paper title, and subcritical minimizer existence found no later matching attainment result. Compact-domain minimizers, critical Gagliardo–Nirenberg optimizers, and minimizers with quadratic confinement have different compactness assumptions. This stationary variational problem is distinct from uniqueness of the associated time-dependent PDE.
