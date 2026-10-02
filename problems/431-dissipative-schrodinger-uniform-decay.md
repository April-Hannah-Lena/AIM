# 431. Classical attenuation versus uniform semiclassical local decay

**Area:** Dissipative Schrödinger PDEs and high-frequency propagation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`V_1,V_2\in C^\infty(\mathbb R^d;\mathbb R)`$, $`V_2\ge0`$, $`V_2\not\equiv0`$, and assume that for some $`\rho>0`$,

```math
|\partial^\beta V_j(x)|\le C_\beta\langle x\rangle^{-\rho-|\beta|}\quad(j=1,2).
```

Set $`P_h=-h^2\Delta+V_1-ihV_2`$, $`S_h(t)=e^{-itP_h/h}`$, and let $`x(t;y,\eta)`$ be the position component of the Hamiltonian flow of $`|\xi|^2+V_1(x)`$ starting at $`(y,\eta)`$. Fix $`s>0`$. Suppose

```math
\lim_{t\to\infty}\sup_{(y,\eta)\in\mathbb R^{2d}}\langle x(t;y,\eta)\rangle^{-s}\exp\!\left(-2\int_0^tV_2(x(\tau;y,\eta))\,d\tau\right)\langle y\rangle^{-s}=0.
```

Must there exist $`h_0>0`$ such that

```math
\lim_{t\to\infty}\sup_{0<h\le h_0}\|\langle x\rangle^{-s}S_h(t)\langle x\rangle^{-s}\|_{L^2\to L^2}=0?
```

The conclusion includes the zero-energy threshold and does not insert an energy cutoff.

## Application

This asks whether the decay predicted by attenuated geometric rays guarantees decay of waves uniformly as their wavelength tends to zero. Zero-energy propagation is the obstacle to using standard high-frequency arguments.

## References

1. X. P. Wang, [Uniform time-decay of semigroups of contractions](https://nsa.fjfi.cvut.cz/problems/01_ESF_2010/2010-12/2010-12_ESF_Wang.pdf), ESF problem 2010-12, equations (1)–(2), and the final paragraph on the zero threshold.
2. J. Royer, [Limiting absorption principle for the dissipative Helmholtz equation](https://doi.org/10.1080/03605302.2010.490287), *Communications in PDE* **35** (2010), 1458–1489, introduction and the semiclassical resolvent theorem; [preprint](https://arxiv.org/abs/0905.0355).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Wang explicitly asks whether the classical condition suffices. Searches for uniform semiclassical dissipative decay, Royer’s limiting absorption results, and later Wang threshold estimates through the review date found no theorem under precisely this global dynamical condition. Decay for each fixed h, or estimates away from zero energy, do not yield the displayed uniform limit.
