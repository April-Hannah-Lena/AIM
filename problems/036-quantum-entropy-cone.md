# 036. Are the standard quantum entropy inequalities complete?

**Area:** Quantum information and convex optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For each $`N\ge4`$, let $`\Gamma_N^Q`$ be the closure of the conic hull of vectors $`(S(\rho_I))_{\varnothing\ne I\subseteq[N]}`$, over all finite-dimensional $`N`$-party density matrices and all local dimensions. Here $`\rho_I`$ is the reduced state and $`S(\rho)=-\mathop{\mathrm{tr}}\nolimits(\rho\log_2\rho)`$.

Let $`\Sigma_N`$ be the cone of vectors $`h`$ with $`h(\varnothing)=0`$, $`h(I)\ge0`$, and, for every pairwise disjoint $`I,J,K`$,

```math
\begin{aligned}
h(I)+h(J)&\ge h(IJ),\\
h(I)+h(IJ)&\ge h(J),\\
h(IJ)+h(JK)&\ge h(J)+h(IJK),\\
h(IJ)+h(JK)&\ge h(I)+h(K),
\end{aligned}
```

where juxtaposition denotes union. Determine whether $`\Gamma_N^Q=\Sigma_N`$ for every $`N\ge4`$, or exhibit a universal homogeneous linear inequality not implied by these constraints.

## Application

Entropy inequalities bound communication rates, entanglement conversion and distributed quantum information processing. Completeness would justify optimizing over a finite polyhedral set of standard constraints.

## References

1. T. He, J. Lee and H. Ooguri, [Exploring the holographic entropy cone via reinforcement learning](https://arxiv.org/abs/2601.19979), JHEP 06 (2026), 267; introduction and section 2. Explicitly distinguishes the unresolved quantum cone from the restricted holographic cone.
2. N. Pippenger, [The inequalities of quantum information theory](https://doi.org/10.1109/TIT.2003.809569), IEEE Transactions on Information Theory 49 (2003), 773–789. Basic quantum entropy cone framework.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The 2026 paper explicitly asks whether further inequalities hold for all quantum states beyond the three-party case. Its new findings concern holographic states, which form a restricted class and cannot settle this universal problem. No general completeness theorem or new universal independent inequality was located.

Searches included: `quantum entropy cone 2026 open inequalities`; `universal quantum entropy inequalities beyond strong subadditivity 2026`; `quantum entropy cone complete`. This is a documented literature check, not a certification that no solution exists.
