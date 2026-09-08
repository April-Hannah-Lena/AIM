# 156. Tagged-particle thermalization with an interacting background

**Area:** Kinetic theory and plasma relaxation

## Problem statement

Fix $\beta>0$ and a smooth even potential $V$ on the unit torus $\mathbb T^3$ with nonnegative Fourier coefficients. Evolve particles $0,\ldots,N$ by $\dot X_j=V_j$, $\dot V_j=-N^{-1}\sum_{l\ne j}\nabla V(X_j-X_l)$. Initially particle $0$ has uniform position and velocity density $f^\circ\in C_c^\infty(\mathbb R^3)$; independently of particle $0$, the joint background density of particles $1,\ldots,N$ is proportional to

$$
\exp\left[-\frac\beta2\sum_{j=1}^N|v_j|^2-\frac\beta{2N}\sum_{j\ne l}V(x_j-x_l)\right].
$$

Must the velocity law $f_N(\tau)$ of particle $0$ at time $N\tau$ converge as $N\to\infty$, weakly and uniformly on compact $\tau$ intervals, to the solution of $\partial_\tau f=\operatorname{div}_v(A(v)(\nabla_v f+\beta vf))$, $f(0)=f^\circ$? With $M(v)=(\beta/2\pi)^{3/2}e^{-\beta|v|^2/2}$, define

$$
A(v)=\int_{\mathbb R^3}\sum_{k\in2\pi\mathbb Z^3\setminus\{0\}}\frac{\pi\widehat V(k)^2(k\otimes k)\delta(k\cdot(v-w))}{|\varepsilon(k,k\cdot v)|^2}M(w)\,dw,
$$

$$
\varepsilon(k,\omega)=1+\widehat V(k)\lim_{a\downarrow0}\int_{\mathbb R^3}\frac{k\cdot\nabla M(w)}{\omega-k\cdot w-ia}\,dw.
$$

Uniform weak convergence means $\sup_{0\le\tau\le T}|\int\psi\,df_N(\tau)-\int\psi(v)f(\tau,v)\,dv|\to0$ for every $T<\infty$ and $\psi\in C_b(\mathbb R^3)$. Here $\widehat V(k)=\int_{\mathbb T^3}V(x)e^{-ik\cdot x}dx$ and $\delta$ is the one-dimensional Dirac distribution.

## Applied significance

This asks whether the slow thermalization of a tagged charge emerges from deterministic interactions, including collective screening by the background.

## References

1. Mitia Duerinckx and Laure Saint-Raymond, *Lenard–Balescu correction to mean-field theory* (2021). [Paper](https://arxiv.org/abs/1911.10151). Introduction and main result justify a shorter-time correction to mean-field dynamics.

2. Mitia Duerinckx and Corentin Le Bihan, *Lenard-Balescu thermalization: rigorous derivation from a toy model* (2025), §1.1, equations (1.1)–(1.3). [Author text](https://mitia.duerinckx.web.ulb.be/publications-DLB25.pdf). Source of the full-particle question and the screened diffusion tensor.

3. Thierry Bodineau and Pierre Le Bris, *Linear Landau equation as a limit of a tagged particle in mean field interaction with a free gas* (2026). [Paper](https://arxiv.org/abs/2602.16440). Main theorem treats a free background gas in dimensions at least four.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

The November 2025 source explicitly leaves the full particle derivation open and proves a truncated-hierarchy model instead. Searches for “tagged particle Lenard Balescu 2026” and “Lenard Balescu thermalization full particle derivation” also found the February 2026 free-gas theorem. Its background particles do not interact as those above do; it therefore does not settle the screened limit.
