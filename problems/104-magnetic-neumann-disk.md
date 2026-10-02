# 104. The disk maximizes the first magnetic Neumann eigenvalue

**Area:** Magnetic spectral optimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

For $`B\ge0`$ put $`A_B(x)=\frac B2(-x_2,x_1)`$ and $`q_{\Omega,B}[u]=\int_\Omega|(-i\nabla-A_B)u|^2\,dx`$.

For a bounded simply connected $`C^\infty`$ domain $`\Omega\subset\mathbb R^2`$, define

```math
\mu_1(\Omega,B)=\inf_{0\ne u\in H^1(\Omega;\mathbb C)}\frac{q_{\Omega,B}[u]}{\|u\|_2^2}.
```

If $`D`$ is a disk with $`|D|=|\Omega|`$, prove or disprove that $`\mu_1(\Omega,B)\le\mu_1(D,B)`$ for every $`B>0`$.

## Application

The lowest magnetic Neumann level determines the onset of superconductivity in a planar sample. This predicts an optimal sample shape under an area constraint.

## References

1. B. Colbois, C. Léna, L. Provenzano and A. Savo, [A reverse Faber–Krahn inequality for the magnetic Laplacian](https://arxiv.org/abs/2403.11336), Journal de Mathématiques Pures et Appliquées 192 (2024), Conjecture 1.5 and main theorem: Fournais–Helffer conjecture and moderate-field case.
2. V. Lotoreichik and L. Morin, [On Shape Optimization with Large Magnetic Fields in Two Dimensions](https://doi.org/10.1007/s12220-026-02363-7), Journal of Geometric Analysis (2026), §1.1: current discussion of magnetic Neumann partial results.

## Status review

**Known cases:** The disk comparison holds for magnetic-field strengths at which the disk ground eigenfunction is radial.

**Remaining target:** The same comparison for all positive field strengths and every bounded simply connected smooth planar domain.

**Literature check:** Open in cited literature; no later resolution located.

The 2024 theorem proves the inequality while the disk’s ground eigenfunction is radial, not for all field strengths. The 2026 paper continues to describe the Neumann results as partial. The displayed statement keeps simple connectivity, an important geometric restriction.

**Search audit:** “Fournais Helffer reverse Faber Krahn magnetic Neumann conjecture 2025 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
