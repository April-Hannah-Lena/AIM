# 055 — Recover an arbitrary sound speed from one incident direction

**Area:** Inverse scattering / acoustic tomography

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $\theta_0\in S^2$ and $R>0$. Let $c\in C^\infty(\mathbb R^3)$ be positive and equal to one outside $B_R$. For each $k>0$, solve

$$
(\Delta+k^2c(x)^{-2})u=0,\qquad
u=e^{ikx\cdot\theta_0}+u^s,
$$

with outgoing scattered field. Write
$u^s(r\omega)=r^{-1}e^{ikr}a_c(\omega,k)+O(r^{-2})$.

Does equality of $a_{c_1}(\omega,k)$ and $a_{c_2}(\omega,k)$ for all $\omega\in S^2$ and $k>0$ force $c_1=c_2$? Both speeds may be far from constant. Only one incoming plane-wave direction is used.

## Application

This tests whether broadband illumination from a single direction can identify an inhomogeneous acoustic propagation speed.

## References

1. S. Ma, L. Potenciano-Machado and M. Salo, *Fixed Angle Inverse Scattering for Sound Speeds Close to Constant*, SIAM Journal on Mathematical Analysis (2023). [Paper](https://doi.org/10.1137/22M147640X).
2. L. Oksanen, Rakesh and M. Salo, *Rigidity in fixed angle inverse scattering for Riemannian metrics* (2024; revised 2025), abstract. [Preprint](https://arxiv.org/abs/2410.06864).
3. L. Oksanen, Rakesh and M. Salo, *Fixed angle inverse scattering with non-constant velocity* (August 2026), abstract and main results. [Preprint](https://arxiv.org/abs/2608.13670).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Reference 2 explicitly states the general problem is open and distinguishes any admissible metric from the Euclidean metric. Reference 1 treats speeds near constant. The August 2026 paper uses finitely many waves together with complementary solutions and geometric hypotheses; these are stronger data or restrictions than the single-direction experiment stated here.

Checked on 2026-09-08 with `fixed angle inverse scattering potential 2025 2026 uniqueness` and `Fixed angle inverse scattering with non-constant velocity`. The newest paper's assumptions were inspected. No theorem covering the statement above was located.
