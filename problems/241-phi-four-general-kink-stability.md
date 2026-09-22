# 241. Asymptotic stability of the phi-four kink without odd symmetry

**Area:** Nonlinear scalar fields

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $H(x)=\tanh(x/\sqrt2)$ and consider $\phi_{tt}-\phi_{xx}=\phi-\phi^3$ on $\mathbb R_t\times\mathbb R_x$. Does there exist $\varepsilon>0$ such that every initial datum
$$\|\phi(0)-H\|_{H^1}+\|\phi_t(0)\|_{L^2}<\varepsilon$$
has the following asymptotics? There exist $c_\infty\in(-1,1)$ and $a\in C^1([0,\infty))$ with $a'(t)\to c_\infty$ such that, writing $H_c(y)=H(y/\sqrt{1-c^2})$, for every $R>0$,
$$\|\phi(t,a(t)+\cdot)-H_{c_\infty}\|_{H^1(-R,R)}+\|\phi_t(t,a(t)+\cdot)+c_\infty H'_{c_\infty}\|_{L^2(-R,R)}\longrightarrow0.$$
No parity condition is imposed on either perturbation. The derivative in the second term is the physical time derivative before shifting coordinates.

## Application

The kink is a model of a persistent interface between two phases. The question asks whether its internal oscillation and emitted radiation decay locally under arbitrary small disturbances.

## References

- Michał Kowalczyk, Yvan Martel and Claudio Muñoz, [*Kink dynamics in the $\phi^4$ model: asymptotic stability for odd perturbations in the energy space*](https://doi.org/10.1090/jams/870) (2017), §1 and main theorem: the proved odd-perturbation result and the underlying equation.
- Michał Kowalczyk and Yvan Martel, [*Kink dynamics under odd perturbations for (1+1)-scalar field models with one internal mode*](https://arxiv.org/abs/2203.04143) (2022 preprint), abstract and main theorem: robust extensions retaining odd symmetry.
- Claudio Muñoz, [*The asymptotic stability of kinks in scalar field models*](https://indico.ictp.it/event/11210/overview) (ICTP lecture, 9 December 2025), lecture abstract: explicitly identifies general energy-space perturbations of the phi-four kink as unresolved.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “phi4 kink asymptotic stability general perturbations 2025 2026”, “moving phi4 kink asymptotic stability”, and recent internal-mode results. Orbital stability controls distance to the family but does not prove the displayed local convergence. The cited newer scalar-field theorem still assumes odd perturbations.
