# 237. Global optimality of the Abrikosov triangular lattice

**Area:** Superconductivity and Coulomb crystallization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\mathcal A_1$ consist of planar vector fields $E$ satisfying, distributionally,
$$\operatorname{div}E=2\pi\left(\sum_{p\in\Lambda}\delta_p-1\right),\qquad\operatorname{curl}E=0,$$
where $\Lambda\subset\mathbb R^2$ is locally finite and $\sup_{R\geq1}\#(\Lambda\cap[-R,R]^2)/R^2<\infty$. The fields are locally square-integrable away from the points. Fix smooth cutoffs $0\leq\chi_R\leq1$, equal to one on $[-R+1,R-1]^2$, supported in $[-R,R]^2$, with uniformly bounded gradient. Define
$$W(E)=\limsup_{R\to\infty}\frac1{4R^2}\lim_{\eta\downarrow0}\left[\frac12\int_{\mathbb R^2\setminus\bigcup_{p\in\Lambda}B(p,\eta)}\chi_R|E|^2\,dx+\pi\log\eta\sum_{p\in\Lambda}\chi_R(p)\right].$$
Let $\Lambda_\triangle=\sqrt{2/\sqrt3}\,[\mathbb Z(1,0)+\mathbb Z(1/2,\sqrt3/2)]$ and let $E_\triangle$ be the mean-zero periodic field in $\mathcal A_1$ associated to it. Is $W(E)\geq W(E_\triangle)$ for every $E\in\mathcal A_1$? No periodicity is required of competitors.

## Application

The energy describes the microscopic arrangement of vortices in type-II superconductors and point charges in a neutralizing background. Global optimality would derive the observed triangular pattern without assuming a lattice in advance.

## References

- Sylvia Serfaty, [*Ginzburg–Landau vortices, Coulomb gases, and Abrikosov lattices*](https://doi.org/10.1016/j.crhy.2014.06.001) (2014), Theorem 1 and Conjecture 1: optimality among lattices and the open global extension.
- Simona Rota Nodari and Sylvia Serfaty, [*Renormalized energy equidistribution and local charge balance in 2D Coulomb systems*](https://math.nyu.edu/~serfaty/REG_V12.pdf) (2013 manuscript), §1.1, Definitions 1, 3 and 4: precise admissible fields and renormalized-energy normalization; the introduction states the unresolved crystallization question.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “Abrikosov triangular lattice global renormalized energy minimizer proof 2025 2026” and “Coulomb crystallization Sandier Serfaty conjecture solved”. Located lattice optimality, local charge-balance and equidistribution results, not unrestricted global crystallization. The target is optimal energy, with no uniqueness claim: changing finitely many points need not change a thermodynamic energy density.
