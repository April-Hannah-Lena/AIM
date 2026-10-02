# 149. The unregularized Coulomb mean-field limit

**Area:** Kinetic theory and plasma physics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`K(x)=x/|x|^3`$ on $`\mathbb R^3\setminus\{0\}`$. Draw $`N`$ initial position–velocity pairs independently with a probability density $`f_0\in C_c^\infty(\mathbb R^6)`$, and evolve them by

```math
\dot X_i=V_i,\qquad \dot V_i=\frac1N\sum_{j\ne i}K(X_i-X_j).
```

Let $`f`$ be the classical solution with initial datum $`f_0`$ of $`\partial_t f+v\cdot\nabla_x f+(K*\rho_f)\cdot\nabla_v f=0`$, where $`\rho_f(x)=\int f(x,v)\,dv`$. For every $`T,\delta>0`$, prove or disprove

```math
\mathbb P\left(\sup_{0\le t\le T}W_1\left(\frac1N\sum_{i=1}^N\delta_{(X_i(t),V_i(t))},f(t)\,dx\,dv\right)>\delta\right)\longrightarrow0.
```

Here $`W_1`$ is the infimum of the mean Euclidean distance over couplings of the two probability measures. No particle-size regularization or force cutoff is allowed.

## Application

Collisionless plasma models replace individual charged-particle trajectories by a distribution evolving under a collective electric field. This limit would justify that replacement for actual point-charge interactions on fixed time intervals, without imposing an artificial short-distance force cutoff.

## References

1. Dustin Lazarovici and Peter Pickl, *A mean field limit for the Vlasov–Poisson system*, Archive for Rational Mechanics and Analysis 225 (2017), 1201–1231. [Paper](https://arxiv.org/abs/1502.04608). Introduction and main theorem identify the Coulomb obstruction and prove a cutoff result.

2. Megan Griffin-Pickering, *A probabilistic mean-field limit for the Vlasov–Poisson system for ions* (2026). [Publisher text](https://ems.press/content/serial-article-files/52877). Introduction reviews the unresolved point-charge issue; the theorem concerns regularized ionic dynamics.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches on 2026-09-08 for “uncut Coulomb mean field Vlasov Poisson 2026” and “Vlasov Poisson propagation chaos no cutoff solved” found regularized and conditional results. Lazarovici–Pickl use a cutoff of order $`N^{-1/3+\epsilon}`$. Neither that theorem nor the cited ionic limit proves the exact Newtonian particle statement above.
