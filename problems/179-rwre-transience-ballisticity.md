# 179. Does directional transience imply ballistic transport in an iid medium?

**Area:** Diffusion and transport in random environments

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

At each $`x\in\mathbb Z^3`$, sample independently an identically distributed probability vector $`(\omega_x(e))_{|e|_1=1}`$. Assume a deterministic $`\kappa>0`$ satisfies $`\omega_x(e)\ge\kappa`$ almost surely for every direction $`e`$. Given the environment, start $`X_0=0`$ and use transition probabilities $`P_\omega(X_{n+1}=x+e\mid X_n=x)=\omega_x(e)`$. Write $`P`$ for the joint law of environment and walk. For any unit vector $`\ell`$, does

```math
P(X_n\cdot\ell\longrightarrow+\infty)=1
```

imply the existence of a deterministic $`v`$ with $`v\cdot\ell>0`$ and $`P(X_n/n\to v)=1`$?

## Application

The statement asks whether persistent transport through an independently disordered medium must have positive macroscopic velocity, or can be slowed to zero by traps.

## References

- [David Campos and Alejandro F. Ramírez, *Ellipticity criteria for ballistic behavior of random walks in random environment* (2014)](https://doi.org/10.1007/s00440-013-0527-7), Conjecture 1.1.
- [Enrique Guerra and Alejandro F. Ramírez, *A proof of Sznitman's conjecture about ballistic RWRE* (2020)](https://arxiv.org/abs/1809.02011), abstract and main theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Guerra–Ramírez prove equivalence of several quantitative ballisticity conditions, while explicitly distinguishing transience-implies-ballisticity. Their title therefore does not resolve this entry. The dimension is fixed at three and uniform ellipticity is essential to the intended question.

Search topics checked on 2026-09-08: uniformly elliptic iid RWRE directional transience ballisticity conjecture 2025 2026.
