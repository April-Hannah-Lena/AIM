# 382. Large-data weak solutions for three-dimensional stress-diffusive Oldroyd-B flow

**Area:** Viscoelastic fluids; polymer rheology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^3$ be smooth and bounded and let $\nu,\mu>0$. Given smooth compatible $u_0$ with $\nabla\cdot u_0=0$, $u_0|_{\partial\Omega}=0$, and a smooth symmetric uniformly positive-definite tensor $\sigma_0$ with $\partial_n\sigma_0=0$, must there be a global distributional solution of
$$u_t+u\cdot\nabla u-\nu\Delta u+\nabla p=\nabla\cdot\sigma,\quad\nabla\cdot u=0,$$
$$\sigma_t+u\cdot\nabla\sigma-(\nabla u)\sigma-\sigma(\nabla u)^T-\mu\Delta\sigma+2(\sigma-I)=0$$
with $u=0$, $\partial_n\sigma=0$ on the boundary and the prescribed initial traces? Require, on each finite time interval, $u\in L^\infty_tL^2_x\cap L^2_tH_0^1$, $\sigma\in L^\infty_tL^2_x\cap L^2_tH^1_x$, $\sigma$ positive semidefinite almost everywhere, and the integrated inequality
$$E(t)+\nu\int_0^t\!\int_\Omega|\nabla u|^2+\int_0^t\!\int_\Omega(\operatorname{tr}\sigma-3)\le E(0),\qquad E(t)=\frac12\int_\Omega(|u|^2+\operatorname{tr}\sigma).$$
The momentum equation must contain exactly $\nabla\cdot\sigma$, with no additional stress-defect measure.

## Application

The conformation tensor tracks the average stretching of Hookean polymer molecules in a viscous solvent. Global weak existence is needed to justify the model after smooth-flow estimates cease to be available.

## References

1. T. Dębiec and E. Süli, [*On a Class of Generalised Solutions to the Kinetic Hookean Dumbbell Model for Incompressible Dilute Polymeric Fluids: Existence and Macroscopic Closure*](https://doi.org/10.1007/s00205-025-02115-x), Archive for Rational Mechanics and Analysis 249 (2025), article 43, equations (3)–(4), Definition 1.2 and Remark 1.4.
2. J. W. Barrett and S. Boyaval, [*Existence and approximation of a (regularized) Oldroyd-B model*](https://arxiv.org/abs/0907.4066), Mathematical Models and Methods in Applied Sciences 21 (2011), 1783–1837, two-dimensional stress-diffusive existence theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using three-dimensional diffusive Oldroyd-B large-data weak existence and exact stress closure. The 2025 paper identifies the missing stress compactness and provides generalized solutions with defects, together with conditional removal of those defects. Two-dimensional theorems and three-dimensional models with an additional quadratic elastic-energy term do not prove this assertion. The August 2026 creeping-flow result [arXiv:2608.25333](https://arxiv.org/abs/2608.25333) is two-dimensional and removes inertia. No matching three-dimensional theorem for the displayed constitutive law was located.
