# 245 — Minimum volume of a three-dimensional body of constant width

**Area:** Convex geometry / geometric design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a compact convex body $K\subset\mathbb R^3$ with nonempty interior, define its support function by $h_K(u)=\max_{x\in K}x\cdot u$ for $u\in S^2$. Determine the exact value of

$$
v_3=\inf\left\{\operatorname{Vol}_3(K):h_K(u)+h_K(-u)=1\text{ for every }u\in S^2\right\},
$$

and characterize all bodies attaining this value, up to rigid motion. The condition prescribes width one in every direction. The infimum is over all such convex bodies; no rotational or polyhedral symmetry is imposed.

## Application

Constant-width bodies can rotate between parallel supports at a fixed separation. The problem identifies the least material needed for a three-dimensional component with this contact geometry.

## References

1. A. Nishioka, *An Improved Lower Bound for the Three-Dimensional Blaschke–Lebesgue Problem from Spectral and Dual Perspectives* (2026), [arXiv:2606.01754](https://arxiv.org/abs/2606.01754), §1 and Theorem 1. Explicit open-problem statement and a new general lower bound.
2. R. Hynd, *The density of Meissner polyhedra* (2024), [Geometriae Dedicata](https://doi.org/10.1007/s10711-024-00933-z), main approximation theorem. Gives Hausdorff approximation within the class of constant-width bodies.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 preprint still identifies the three-dimensional Blaschke–Lebesgue problem as open. Its lower bound does not coincide with the volume of the proposed Meissner minimizers. Hynd's density theorem supplies an approximation class, without establishing which body minimizes volume. Searches included “Blaschke Lebesgue conjecture 2026”, “Meissner minimum volume proof”, and “Hynd constant width 2025 2026”. No exact minimum or complete minimizing-shape theorem was located.
