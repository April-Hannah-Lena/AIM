# 381. Hard-sphere Boltzmann shock profiles at arbitrary Mach number

**Area:** Rarefied gas dynamics; kinetic shock layers

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every Mach number $\mathcal M>1$, set
$$\rho_-=T_-=1,\quad u_-=\sqrt{5/3}\,\mathcal M,\quad r=\frac{4\mathcal M^2}{\mathcal M^2+3},\quad\rho_+=r,\quad u_+=u_-/r,\quad T_+=\frac{(5\mathcal M^2-1)(\mathcal M^2+3)}{16\mathcal M^2}.$$
Let $M_\pm(v)=\rho_\pm(2\pi T_\pm)^{-3/2}\exp(-|v-u_\pm e_1|^2/(2T_\pm))$. Does there exist a nonnegative stationary planar profile $F(z,v)$ satisfying
$$v_1\partial_zF=Q(F,F),\qquad z\in\mathbb R,\ v\in\mathbb R^3,$$
$$Q(F,F)(v)=\int_{\mathbb R^3}\int_{\mathbb S^2}|(v-v_*)\cdot\omega|[F(v')F(v_*')-F(v)F(v_*)]\,d\omega\,dv_*,$$
where $v'=v-((v-v_*)\cdot\omega)\omega$ and $v_*'=v_*+((v-v_*)\cdot\omega)\omega$, such that $F(z,\cdot)\to M_\pm$ in $L^1((1+|v|^2)\,dv)$ as $z\to\pm\infty$? Require continuity into this weighted space, locally finite entropy and a distributional solution of the profile equation. The end states obey the monatomic ideal-gas Rankine–Hugoniot relations; their jump need not be small.

## Application

These profiles describe the internal molecular structure of a gas shock. Small-amplitude theory does not justify kinetic shock layers at the large Mach numbers occurring in rarefied high-speed flows.

## References

1. A. Pogan and K. Zumbrun, [*Center manifolds for a class of degenerate evolution equations and existence of small-amplitude kinetic shocks*](https://arxiv.org/abs/1612.05676), Journal of Differential Equations 264 (2018), 6752–6808, §1.3, discussion of large-amplitude kinetic shocks; DOI [10.1016/j.jde.2018.01.049](https://doi.org/10.1016/j.jde.2018.01.049).
2. R. E. Caflisch and B. Nicolaenko, [*Shock profile solutions of the Boltzmann equation*](https://doi.org/10.1007/BF01206009), Communications in Mathematical Physics 86 (1982), 161–194, weak-shock existence theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using large-amplitude and arbitrary-Mach hard-sphere Boltzmann shock existence. The 2018 primary paper explicitly identifies large-amplitude profiles as an unresolved problem. Its center-manifold construction, like the 1982 theorem, assumes weak shocks. Subsequent invariant-manifold localization and stability results concern profiles already known to exist or retain small amplitude. Numerical shock computations and Navier–Stokes shock profiles do not prove kinetic existence. No theorem covering every displayed Mach number was located.
