# 103. Faber–Krahn inequality for graphene quantum dots

**Area:** Dirac spectral geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded connected $`C^2`$ domain, with outward unit normal $`n=(n_1,n_2)`$. On $`L^2(\Omega;\mathbb C^2)`$ consider the massless Dirac operator

```math
D_\Omega=\begin{pmatrix}0&-i\partial_1-\partial_2\\-i\partial_1+\partial_2&0\end{pmatrix},\qquad \mathop{\mathrm{dom}}\nolimits D_\Omega=\{u\in H^1(\Omega;\mathbb C^2):u_2=i(n_1+in_2)u_1\text{ on }\partial\Omega\}.
```

Write $`\lambda_+(\Omega)`$ for its smallest positive eigenvalue, and let $`B`$ be a disk with $`|B|=|\Omega|`$. Prove or disprove $`\lambda_+(\Omega)\ge\lambda_+(B)`$, with equality only for disks.

## Application

The operator models confined electronic excitations in a graphene quantum dot. The conjecture predicts the shape minimizing its lowest excitation energy at fixed area.

## References

1. J. Duran, A. Mas and T. Sanz-Perela, [A connection between quantum dot Dirac operators and $`\overline\partial`$-Robin Laplacians in the context of shape optimization problems](https://arxiv.org/abs/2507.18698), preprint (2025; revised February 2026), Conjecture 1.1 and the paragraph following it: the massless infinite-mass-boundary problem.
2. R. Benguria, S. Fournais, E. Stockmeyer and H. Van Den Bosch, [Spectral gaps of Dirac operators describing graphene quantum dots](https://arxiv.org/abs/1601.06607), Mathematical Physics, Analysis and Geometry 20 (2017), spectral-gap estimates: geometric partial bounds.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The February 2026 revision explicitly calls this case open. Its main results identify an equivalent family of $`\overline\partial`$-Robin inequalities and establish asymptotic regimes near zigzag boundary conditions, which do not prove the stated infinite-mass case.

**Search audit:** “quantum dot Dirac Faber Krahn infinite mass conjecture 2026”; “Duran Mas Sanz Perela 2507.18698”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
