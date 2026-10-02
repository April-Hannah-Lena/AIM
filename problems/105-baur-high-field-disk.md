# 105. Baur’s high-field disk conjecture for all higher eigenvalues

**Area:** Magnetic confinement and shape design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $`B\ge0`$ put $`A_B(x)=\frac B2(-x_2,x_1)`$ and $`q_{\Omega,B}[u]=\int_\Omega|(-i\nabla-A_B)u|^2\,dx`$.

Let $`\lambda_k(\Omega,B)`$ be the $`k`$th eigenvalue, counted with multiplicity, of this form on $`H_0^1(\Omega;\mathbb C)`$. For every bounded simply connected planar domain $`\Omega`$, every integer $`k\ge2`$, and every $`B`$ satisfying $`B|\Omega|\ge2\pi k`$, prove or disprove

```math
\lambda_k(\Omega,B)\ge\lambda_k(D,B),\qquad |D|=|\Omega|,
```

where $`D`$ is a disk. The operator here is unshifted; subtracting the same $`B`$ from both spectra gives the equivalent shifted convention used in the 2026 reference.

## Application

This predicts an explicit magnetic-flux threshold beyond which the disk minimizes each confined energy level, including excited states.

## References

1. M. Baur, [Numerical optimization of eigenvalues of the planar magnetic Dirichlet Laplacian with constant magnetic field](https://doi.org/10.1063/5.0253311), Journal of Mathematical Physics 66 (2025), Conjecture 4.2: source of the threshold.
2. V. Lotoreichik and L. Morin, [On Shape Optimization with Large Magnetic Fields in Two Dimensions](https://doi.org/10.1007/s12220-026-02363-7), Journal of Geometric Analysis (2026), Conjecture 1 and Theorem 1: restatement and asymptotic partial theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 paper proves that minimizing domains approach disks as $`B\to\infty`$, and explicitly says its theorem does not imply the conjecture even for large fields. Baur’s calculations motivate a shape theorem, not a numerical-linear-algebra task.

**Search audit:** “Baur high magnetic field disk Conjecture 4.2 2026”; “magnetic Dirichlet eigenvalues flux 2 pi n proof”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
