# 385. Nonlinear Landau damping near a Maxwellian on the whole space

**Area:** Plasma kinetics; dispersive relaxation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Set $\mu(v)=(2\pi)^{-3/2}e^{-|v|^2/2}$. On $\mathbb R^3_x\times\mathbb R^3_v$, consider the repulsive Vlasov–Poisson system with neutralizing background

$$
\partial_tf+v\cdot\nabla_xf+E\cdot\nabla_vf=0,\qquad E=-\nabla_x\Phi,\qquad-\Delta_x\Phi=\int_{\mathbb R^3}(f-\mu)\,dv.
$$

Here $E$ is the Coulomb field that decays at spatial infinity. For $\lambda>0$ define the analytic localized norm

$$
\|h\|_{\mathcal A_\lambda}=\sum_{\alpha,\beta\in\mathbb N_0^3}\frac{\lambda^{|\alpha|+|\beta|}}{\alpha!\beta!}\left\|\langle x\rangle^4\langle v\rangle^6\partial_x^\alpha\partial_v^\beta h\right\|_{L^2_{x,v}},\qquad\langle z\rangle=(1+|z|^2)^{1/2}.
$$

Does every fixed $\lambda>0$ admit $\varepsilon_\lambda>0$ such that all initial data $f_0=\mu+h_0\ge0$ with $\int h_0\,dx\,dv=0$ and $\|h_0\|_{\mathcal A_\lambda}\le\varepsilon_\lambda$ generate a global classical solution satisfying $\|E(t)\|_{L^\infty_x}\to0$ as $t\to\infty$? This is a localized analytic formulation of the open nonlinear Maxwellian damping problem; no exponential time-decay rate is required.

## Application

Landau damping describes relaxation of the electric field in a collisionless plasma. Whole-space Maxwellian backgrounds have long-wavelength oscillations absent from the usual periodic stability argument.

## References

1. Y. Wang, M. Xiao and H. Xiong, [*Nonlinear Landau damping for the two-species screened Vlasov–Poisson system with large initial distributions*](https://arxiv.org/abs/2603.16767), preprint, version 3 (2026), §1.1, discussion of the unresolved unscreened whole-space Maxwellian problem.
2. A. D. Ionescu, B. Pausader, X. Wang and K. Widmayer, [*Nonlinear Landau damping for the Vlasov–Poisson system in $\mathbb R^3$: the Poisson equilibrium*](https://arxiv.org/abs/2205.04540), final version (2024), §1 and main theorem for an equilibrium with polynomial velocity tails.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using nonlinear whole-space Maxwellian Landau damping and recent Vlasov–Poisson stability results. The May 2026 version explicitly retains the Maxwellian problem. Whole-space nonlinear damping around the Poisson equilibrium uses polynomial tails, whereas the Maxwellian has Gaussian tails and a different low-frequency resonance structure. Screened interactions replace the Coulomb multiplier, and periodic analytic or Gevrey theorems have discrete spatial frequencies. Linear Maxwellian decay and weakly collisional models do not establish the displayed nonlinear collisionless assertion. No matching resolution was located.
