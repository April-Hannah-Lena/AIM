# 106. Strict angle monotonicity of magnetic wedge ground energy

**Area:** Corner superconductivity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $0<\theta<\pi$, let $W_\theta=\{(r\cos\phi,r\sin\phi):r>0,\ 0<\phi<\theta\}$. Define the magnetic Neumann Laplacian $H_\theta$ by the closed form

$$
q_\theta[u]=\int_{W_\theta}|(-i\nabla-A)u|^2,\qquad A(x)=\tfrac12(-x_2,x_1),
$$

on $\{u\in L^2(W_\theta):(-i\nabla-A)u\in L^2(W_\theta)\}$, with distributional derivatives. Put $\mu(\theta)=\inf\sigma(H_\theta)$. Prove or disprove

$$
\mu(\theta_1)<\mu(\theta_2)\qquad\text{whenever }0<\theta_1<\theta_2<\pi.
$$

The field strength remains one while the opening angle varies.

## Application

In a superconducting sample with several corners, this predicts that the sharpest corner has the lowest local magnetic energy and is the preferred site for superconductivity to nucleate.

## References

1. V. Bonnaillie-Noël, [Schrödinger operator with magnetic field in domain with corners](https://proceedings.centre-mersenne.org/articles/10.5802/jedp.15/), Journées Équations aux Dérivées Partielles (2005), §2, p. II–5: explicit strict-angle-monotonicity conjecture.
2. A. Kachmar and M. Sundqvist, [Bound states for the magnetic Neumann Laplacian in planar sectors](https://arxiv.org/abs/2607.12600), preprint (14 July 2026), Theorem 1.1 and introduction: resolution claim for the weaker threshold comparison, with monotonicity discussed separately.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The July 2026 preprint proves that each convex sector has energy below the half-plane threshold. Its theorem compares each angle with the straight-angle endpoint, not two arbitrary convex angles. The older conjecture also concerns nonconvex sectors; the strict convex-angle ordering here is a substantive remaining part. No proof of that ordering was located.

**Search audit:** “magnetic sector angle monotonicity conjecture proof 2025 2026”; “Bonnaillie strictly increasing sector ground energy”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
