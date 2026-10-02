# 208. Sharp Fourier extension from the sphere in three dimensions

**Area:** Harmonic analysis; monochromatic wave concentration

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

Let $`\sigma`$ be surface area measure on $`S^2=\{\omega\in\mathbb R^3:|\omega|=1\}`$ and define

```math
Eg(x)=\int_{S^2}e^{2\pi i x\cdot\omega}g(\omega)\,d\sigma(\omega).
```

Is it true that for every $`p>3`$ there exists $`C_p<\infty`$ such that

```math
\|Eg\|_{L^p(\mathbb R^3)}\le C_p\|g\|_{L^\infty(S^2,\sigma)}
```

for every bounded measurable $`g:S^2\to\mathbb C`$? The constant must be independent of the angular amplitude $`g`$.

## Application

The extension operator superposes plane waves at a fixed frequency. The estimate limits how strongly such waves can concentrate throughout three-dimensional space.

## References

1. Shaoming Guo, Changkeun Oh, Hong Wang, Shukun Wu, and Ruixiang Zhang, [The Bochner–Riesz problem: an old approach revisited](https://arxiv.org/abs/2104.11188), *Peking Math. J.* 8 (2025), 201–270. Section 1, Conjecture 1.2, equations (1.4)–(1.5), states this dual restriction formulation.
2. Hong Wang and Shukun Wu, [Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities](https://arxiv.org/abs/2411.08871), preprint (2024). Abstract and principal restriction estimate establish the partial range $`p>22/7`$.
3. Eric T. Sawyer, [A comparison of trilinear testing conditions for the paraboloid Fourier extension and Kakeya conjectures in three dimensions](https://arxiv.org/abs/2411.18457v8), revised 8 February 2026. Current abstract and version history clarify a search result that still displays an earlier full-proof title.

## Status review

**Known cases:** The displayed Fourier extension estimate is established for every exponent p greater than 22/7.

**Remaining target:** The estimate for every p greater than three, including the remaining exponents up to 22/7.

**Literature check:** Open in cited literature; no later resolution located.

The proved range $`p>22/7`$ leaves exponents immediately above three. A search hit for Sawyer’s original 2024 title claimed a proof; the version history records a withdrawal on 2 January 2025, and the checked February 2026 version presents testing-condition comparisons. It is not used as a resolution. The three-dimensional Kakeya set theorem alone does not imply this restriction estimate.

**Search audit:** Queries: “sphere Fourier restriction conjecture three dimensions 2026 proof”, “Wang Wu restriction 22/7”, “Fourier Extension Conjecture three dimensions Sawyer”; checked the latest arXiv version of the apparent proof claim. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
