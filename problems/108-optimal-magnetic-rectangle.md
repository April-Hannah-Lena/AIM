# 108. Is the optimal magnetic rectangle always a square?

**Area:** Magnetic quantum wells

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $B\ge0$ put $A_B(x)=\frac B2(-x_2,x_1)$ and $q_{\Omega,B}[u]=\int_\Omega|(-i\nabla-A_B)u|^2\,dx$.

For $a>0$, set $R_a=(0,a)\times(0,a^{-1})$ and

$$\lambda_1(R_a,B)=\inf_{0\ne u\in H_0^1(R_a;\mathbb C)}\frac{q_{R_a,B}[u]}{\|u\|_2^2}.$$

Prove or disprove that $\lambda_1(R_a,B)\ge\lambda_1(R_1,B)$ for every $a>0$ and every $B>0$. Thus area and field are fixed while the aspect ratio varies.

## Application

Rectangular confinement is common in quantum-well models. The question asks whether magnetic coupling can make a non-square aspect ratio energetically preferable.

## References

1. D. Krejčiřík, [Is the optimal magnetic rectangle a square?](https://arxiv.org/abs/2508.16152), preprint (2025), main question: exact rectangle problem.
2. V. Lotoreichik and L. Morin, [On Shape Optimization with Large Magnetic Fields in Two Dimensions](https://doi.org/10.1007/s12220-026-02363-7), Journal of Geometric Analysis (2026), Theorem 2 and following discussion: asymptotic approach of optimizers to a square.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The nonmagnetic rectangle result follows from separation of variables, which the magnetic coupling prevents. The 2026 result establishes asymptotic symmetry at large field; it explicitly leaves optimality at each fixed field open.

**Search audit:** “Is the optimal magnetic rectangle a square 2026”; “magnetic rectangle square conjecture proof”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
