# 013. Quantum unique ergodicity in negative curvature

**Area:** Quantum chaos

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $(M,g)$ be any closed connected smooth Riemannian manifold of dimension at least two with strictly negative sectional curvature. For every sequence of $L^2$-normalized eigenfunctions $u_j$ with $-\Delta_g u_j=\lambda_j u_j$ and $\lambda_j\to\infty$, put $h_j=\lambda_j^{-1/2}$. Prove or disprove that, for every smooth compactly supported symbol $a$ on $T^*M$,

$$
\langle\mathop{\mathrm{Op}}\nolimits_{h_j}(a)u_j,u_j\rangle\longrightarrow\int_{S^*M}a\,dL,
$$

where $S^*M=\{(x,\xi):|\xi|_g=1\}$, $L$ is normalized Liouville measure, and $\mathop{\mathrm{Op}}\nolimits_h$ is any standard semiclassical quantization. The limit is required for every sequence, without discarding exceptional eigenfunctions.

## Application

QUE predicts uniform phase-space energy distribution in high-frequency chaotic modes and rules out persistent concentration on a small family of classical rays.

## References

1. S. Dyatlov, [Quantum Ergodicity in Theorems and Pictures](https://www.ams.org/journals/notices/202310/noti2801/noti2801.html), Notices of the AMS (2023), discussion of QUE.
2. H. Cao and S. Xiang, [Quantum ergodicity for Dirichlet-truncated operators on Z^d](https://arxiv.org/abs/2505.02339), preprint (2025), §1, discussion of the Rudnick–Sarnak conjecture.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2023 exposition describes the general conjecture as open. The 2025 paper likewise distinguishes it from density-one quantum ergodicity and from special arithmetic results. The displayed phase-space formulation is stronger than equidistribution against position-only observables; graph and arithmetic theorems do not settle arbitrary negatively curved manifolds.

**Search audit:** “quantum unique ergodicity negative curvature 2025 2026 proof”; “Rudnick Sarnak conjecture general manifolds”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
