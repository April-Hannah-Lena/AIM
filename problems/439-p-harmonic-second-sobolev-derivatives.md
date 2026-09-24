# 439. Second-order Sobolev regularity of p-harmonic functions beyond the Cordes range

**Area:** Degenerate elliptic PDE regularity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For every $p\ge5$, every open $\Omega\subset\mathbb R^3$, and every weak solution $u\in W^{1,p}_{\mathrm{loc}}(\Omega)$ of $\operatorname{div}(|\nabla u|^{p-2}\nabla u)=0$, must $u\in W^{2,2}_{\mathrm{loc}}(\Omega)$? Thus every distributional second derivative is required to belong locally to $L^2$, including neighborhoods of critical points where $\nabla u=0$.

## Application

Second derivatives control spatial changes of gradients in nonlinear conduction. Their square integrability supports sensitivity estimates and error analysis in regions where the constitutive law degenerates.

## References

1. P. Lindqvist, [Notes on the p-Laplace Equation](https://jyx.jyu.fi/bitstreams/2a8cbc94-58e9-4e75-94d6-0f1f5bc22ac1/download), second edition, University of Jyväskylä Report 161 (2017), §11, p. 93, “Second Derivatives,” and discussion preceding §4.
2. Q. H. Nguyen and L. X. Truong, [Higher Regularity of Homogeneous Gradient Compositions for p-Laplace-Type Equations](https://arxiv.org/abs/2608.11586), preprint (2026), Theorem 1.1 and comparison with unweighted derivative regularity.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The classical three-dimensional Cordes range is 1<p<5. The August 2026 paper regularizes sufficiently high homogeneous powers of the gradient, which is different from asserting an unweighted L2 Hessian. Searches for p-harmonic W2,2 beyond the Cordes range and recent Hessian estimates located no unrestricted theorem for the displayed range.
