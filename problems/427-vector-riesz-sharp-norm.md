# 427. The sharp vector Riesz inequality for multidimensional potential fields

**Area:** Harmonic analysis and elliptic potential fields

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For an integer $`d\ge2`$ and a real-valued $`f\in C_c^\infty(\mathbb R^d)`$, define $`R_j f`$ by

```math
\widehat{R_j f}(\xi)=-i\frac{\xi_j}{|\xi|}\widehat f(\xi),\qquad j=1,\ldots,d,
```

where $`\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx`$. Put $`Rf=(R_1f,\ldots,R_df)`$, use the Euclidean norm on its vector values, and set $`p^*=\max\{p,p/(p-1)\}`$.

Is it true that for every $`1<p<\infty`$,

```math
\left\|\left(\sum_{j=1}^d|R_jf|^2\right)^{1/2}\right\|_{L^p(\mathbb R^d)}
\le \cot\!\left(\frac{\pi}{2p^*}\right)\|f\|_{L^p(\mathbb R^d)}?
```

The displayed constant is a necessary lower bound already from one component. Thus the assertion identifies the exact norm, uniformly in dimension; Plancherel proves its $`p=2`$ case.

## Application

The vector transform converts a scalar field to the negative gradient of its half-order potential. Sharp bounds quantify amplification in elliptic potential reconstruction and enter estimates for nonlinear geometric PDEs and Hodge decompositions.

## References

1. R. Bañuelos and A. Osękowski, [Sharp martingale inequalities and applications to Riesz transforms on manifolds, Lie groups and Gauss space](https://doi.org/10.1016/j.jfa.2015.06.015), *Journal of Functional Analysis* **269** (2015), 1652–1713, introduction after (1.7), explicitly stating the conjectured constant; [author preprint](https://arxiv.org/abs/1305.1492).
2. R. Bañuelos, [Cotlar martingale transforms and related singular integrals](https://arxiv.org/abs/2604.09365), preprint (2026), §§5.1–5.2, especially (5.1), (5.13) and the discussion following it.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 paper retains the exact vector norm as open and obtains asymptotic information rather than the conjectured constant at every p. Searches through September 22, 2026 for the sharp vector norm, the complex Riesz transform, proofs and counterexamples found no matching resolution. The August 2026 result arXiv:2608.18068 concerns a dimension-free weak-(1,1) bound and does not establish this sharp strong-Lp inequality. Bounds for one Riesz component are already known and are a different assertion.
