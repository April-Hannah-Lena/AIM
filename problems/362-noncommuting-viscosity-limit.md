# 362. Vanishing nonlinear viscosity without commuting transport and diffusion matrices

**Area:** Hyperbolic conservation laws; physical viscosity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $f\in C^4(U;\mathbb R^N)$, $N\ge2$, on an open set $U$, and suppose $Df$ is strictly hyperbolic, with each characteristic field genuinely nonlinear or linearly degenerate. Suppose there is a strictly convex entropy $\eta$, with entropy flux $q$ satisfying $Dq=D\eta\,Df$. Let $B\in C^3(U;\mathbb R^{N\times N})$ be symmetric and uniformly positive definite, and assume $\operatorname{sym}(D^2\eta\,B)$ is uniformly positive definite near a fixed state $u_*$. For all sufficiently small $\operatorname{TV}(u_0)$, with $u_0-u_*\in L^1(\mathbb R)$ and range near $u_*$, must solutions of
$$\partial_tu^\varepsilon+\partial_xf(u^\varepsilon)=\varepsilon\partial_x\bigl(B(u^\varepsilon)\partial_xu^\varepsilon\bigr),\qquad u^\varepsilon(0)=u_0$$
satisfy $\sup_{t\ge0}\operatorname{TV}(u^\varepsilon(t))\le C\operatorname{TV}(u_0)$ uniformly for $0<\varepsilon\le1$, and converge in $C([0,T];L^1)$ for every finite $T$ to the standard small-BV entropy semigroup solution? The matrices $B(u)$ and $Df(u)$ need not commute.

## Application

Real viscosity depends on the state and can mix characteristic wave families. This asks whether the well-established artificial-viscosity selection principle remains valid for a broad class of entropy-dissipating constitutive viscosities.

## References

1. A. Bressan, [*One Dimensional Hyperbolic Conservation Laws: Past and Future*](https://arxiv.org/abs/2310.16707), Journal of Hyperbolic Differential Equations 21 (2024), 523–561, §5, Open Problem 2.
2. S. Bianchini and A. Bressan, [*Vanishing viscosity solutions of nonlinear hyperbolic systems*](https://doi.org/10.4007/annals.2005.161.223), Annals of Mathematics 161 (2005), 223–342, main uniform-BV and convergence theorem for artificial viscosity.
3. B. Haspot and A. Jana, [*Vanishing viscosity limit for $n\times n$ hyperbolic system of conservation laws in 1-d with nonlinear viscosity: Part-I Uniform BV estimates*](https://arxiv.org/abs/2512.15620), preprint (2025), revised May 2026, main theorem and commuting-matrix hypothesis.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using nonlinear viscosity, uniform BV, noncommuting diffusion, and Haspot–Jana. The 2025 Temple-class theorem and its 2026 general-system extension assume $B(u)Df(u)=Df(u)B(u)$. That explicit restriction leaves the displayed noncommuting case untreated. The entropy compatibility imposed here rules out unstable arbitrary diffusion choices. No later theorem removing commutation in this setting was located.
