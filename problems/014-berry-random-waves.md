# 014. Berry's random-wave conjecture as a local limit

**Area:** Quantum chaos and random waves

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $(M,g)$ be a closed negatively curved Riemannian surface. Let $u_j$ be any real Laplace eigenfunctions with $-\Delta_g u_j=\lambda_j u_j$, $\lambda_j\to\infty$, and $\int_Mu_j^2\,dV=\operatorname{Area}(M)$. Sample $x$ uniformly from $M$ and an orthonormal frame $e:\mathbb R^2\to T_xM$ uniformly in its orthogonal group. Define the random smooth function

$$F_j(y)=u_j\bigl(\exp_x(e y/\sqrt{\lambda_j})\bigr).$$

Do its laws converge, in the topology of smooth convergence on every compact subset of $\mathbb R^2$, to the centered real Gaussian field $F$ with covariance

$$\mathbb E[F(y)F(z)]=J_0(|y-z|)?$$

This is the normalized isotropic monochromatic random wave; $J_0$ is the Bessel function of order zero.

## Application

The random-wave model underpins statistical predictions for intensity, nodal patterns and interference in chaotic microwave and acoustic resonators.

## References

1. M. Ingremeau, [Local weak limits of Laplace eigenfunctions](https://arxiv.org/abs/1712.03431), Tunisian Journal of Mathematics 3 (2021), 481–515.
2. A. García-Ruiz, [A relation between two different formulations of the Berry's conjecture](https://arxiv.org/abs/2305.14906), preprint (2023), definitions and main equivalence theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Ingremeau gives a rigorous local-limit formulation and special deterministic examples, not a negative-curvature theorem. García-Ruiz proves equivalence of formulations. The update search found related random-wave and open-system results, but no proof of this universal local Gaussian limit. Frame randomization makes the formulation intrinsic.

**Search audit:** “Berry conjecture local weak limits negative curvature proof 2025 2026”; “Berry random wave conjecture Ingremeau”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
