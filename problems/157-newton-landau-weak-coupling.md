# 157. The nonlinear Landau limit of weakly interacting particles

**Area:** Kinetic theory and collisional relaxation

## Problem statement

Let $\Phi\in C_c^\infty(\mathbb R^3)$ be nonzero, nonnegative, radial and nonincreasing in radius. Put $\epsilon=N^{-1/3}$ and periodize $\Phi_\epsilon(x)=\sum_{n\in\mathbb Z^3}\Phi((x+n)/\epsilon)$ on the unit torus. Start $N$ independent particles with uniform positions and a smooth positive rapidly decaying velocity probability density $f_0$. Evolve

$$
\dot X_i=V_i,\qquad \dot V_i=-\sqrt\epsilon\sum_{j\ne i}\nabla\Phi_\epsilon(X_i-X_j).
$$

Prove or disprove convergence as $N\to\infty$ of the one-particle velocity marginal $f_N(t)$, weakly and uniformly on each interval $[0,T]$ where a classical solution $f$ exists, to

$$
\partial_t f(v)=\nabla_v\cdot\int_{\mathbb R^3}a(v-w)[f(w)\nabla_v f(v)-f(v)\nabla_w f(w)]\,dw,\quad f(0)=f_0,
$$

$$
a(z)=\frac12\int_{\mathbb R}\int_{\mathbb R^3}\nabla\Phi(y)\otimes\nabla\Phi(y+sz)\,dy\,ds.
$$

Uniform weak convergence means $\sup_{0\le t\le T}|\int\psi\,df_N(t)-\int\psi(v)f(t,v)\,dv|\to0$ for every $\psi\in C_b(\mathbb R^3)$. The tensor has the form $c_\Phi|z|^{-1}(I-z\otimes z/|z|^2)$ for $z\ne0$. The particle hierarchy may not be truncated.

## Applied significance

This would derive collisional velocity diffusion from many weak deflections of interacting particles, rather than assuming molecular chaos at the kinetic level.

## References

1. Raphael Winter, *Convergence to the Landau equation from the truncated BBGKY hierarchy in the weak-coupling limit*, Journal of Differential Equations 283 (2021), 1–36. [Paper](https://arxiv.org/abs/1905.05021). Introduction, equations (1.1)–(1.5), explicitly describe the unresolved full limit and the weak-coupling scaling.

2. Juan J. L. Velázquez and Raphael Winter, *From a non-Markovian system to the Landau equation*, Communications in Mathematical Physics 361 (2018), 239–287. [Paper](https://arxiv.org/abs/1707.07544). Derivation from a closed intermediate equation; not from the full Newtonian system.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

The cited introduction labels the full nonlinear weak-coupling derivation open. Searches for “weak coupling Landau derivation Newton particles 2026” and “nonlinear Landau full BBGKY weak coupling limit” found truncated-hierarchy and linear tagged-particle theorems. This finite-volume homogeneous formulation retains all particle interactions. A Boltzmann-to-Landau grazing-collision limit starts from an already kinetic equation and does not establish it.
