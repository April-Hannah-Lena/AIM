# 468. Hölder continuity for parabolic SPDEs with merely bounded transport noise

**Area:** Stochastic parabolic PDEs; passive scalar transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

On $\mathbb T^d$, $d\ge2$, consider the scalar Itô equation
$$du=\nabla\cdot(a\nabla u)\,dt+\sum_{k\ge1}(b_k\cdot\nabla u)\,dW^k_t,\qquad u(0)=u_0,$$
where the Brownian motions are independent, $u_0\in C^\infty(\mathbb T^d)$ is deterministic, and the coefficients are progressively measurable in $(t,\omega)$ and measurable in $x$. Assume fixed deterministic bounds
$$|a|+\Big(\sum_k|b_k|^2\Big)^{1/2}\le M,\qquad
\eta^\top\Big(a-\tfrac12\sum_kb_k\otimes b_k\Big)\eta\ge\nu|\eta|^2\quad(\eta\in\mathbb R^d),$$
with $M<\infty$ and $\nu>0$. Use the variational solution in $C([0,T];L^2)\cap L^2(0,T;H^1)$, defined by testing against smooth spatial functions and integrating the stochastic terms in the Itô sense.

With no spatial regularity imposed on $a$ or $b$, does the solution have a modification such that, almost surely, for every $0<\tau<T<\infty$ there is a $\gamma=\gamma(\omega,\tau,T)>0$ with
$$u\in C^{\gamma/2,\gamma}([\tau,T]\times\mathbb T^d)?$$
Here the seminorm uses the denominator $|t-r|^{\gamma/2}+\operatorname{dist}(x,y)^\gamma$. The assertion concerns joint continuity on one probability-one event, not continuity almost surely at each separately fixed point.

## Application

This would justify pointwise concentration fields in diffusion models advected by spatially rough random velocities.

## References

1. A. Agresti, M. Sauerbrey and M. Veraar, *A stochastic flow approach to De Giorgi–Nash–Moser estimates for SPDEs with smooth transport noise* (2025 preprint, manuscript dated August 2026), Theorem 1.1, §1.2 and §4. [Full manuscript](https://arxiv.org/html/2511.12692v1).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The first open question in §1.2 asks to remove the spatial regularity of the transport coefficients while retaining boundedness and stochastic parabolicity. The source proves Hölder regularity for sufficiently smooth transport fields and explains why earlier pointwise-probability continuity does not imply the requested simultaneous pathwise regularity. Searches on 2026-09-22 for rough-transport stochastic De Giorgi estimates and later work of the authors found no matching theorem. The random exponent is allowed here; this is distinct from obtaining a deterministic exponent for smooth noise.
