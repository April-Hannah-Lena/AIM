# 051 — Global conductivity uniqueness for the p-Laplacian in higher dimensions

**Area:** Nonlinear inverse problems / electrical materials

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Fix $n\geq3$, $1<p<\infty$, $p\ne2$, and a bounded connected smooth domain $\Omega\subset\mathbb R^n$. Let $\gamma_j\in C^\infty(\overline\Omega)$ be strictly positive. For boundary data $f$, solve
$$
\nabla\cdot(\gamma_j|\nabla u|^{p-2}\nabla u)=0,
\qquad u|_{\partial\Omega}=f,
$$
and define the nonlinear Dirichlet-to-Neumann map $\Lambda_{\gamma_j,p}f=\gamma_j|\nabla u|^{p-2}\partial_\nu u$, interpreted weakly on the trace space of $W^{1,p}(\Omega)$.

Prove or disprove that equality of these maps for all boundary data implies $\gamma_1=\gamma_2$. Do not assume an ordering, smallness, analyticity, or invariance in one direction.

## Application

The power-law constitutive relation models nonlinear conducting media. The question asks whether nonlinear boundary response identifies their spatial material coefficient.

## References

1. C.-Y. Guo, M. Kar and M. Salo, *Inverse problems for p-Laplace type equations under monotonicity assumptions* (2016). [Paper](https://arxiv.org/abs/1602.02591).
2. M. Kar, J. Railo and P. Zimmermann, *The fractional p-biharmonic systems: optimal Poincaré constants, unique continuation and inverse problems*, Calculus of Variations **62** (2023), 130, introduction. [Paper](https://doi.org/10.1007/s00526-023-02468-9).
3. C. I. Cârstea and A. Feizmohammadi, *Two uniqueness results in the inverse boundary value problem for the weighted p-Laplace equation*, Forum of Mathematics, Sigma **13** (2025), e147, Theorems 1.2–1.3 and Corollary 1.1. [Paper](https://doi.org/10.1017/fms.2025.10095).

## Status review

**Known cases:** The cited 2025 paper proves higher-dimensional uniqueness for certain analytic or direction-independent weights.

**Remaining target:** Uniqueness for arbitrary smooth positive weights in dimensions at least three, without those structural assumptions.

**Literature check:** Open in cited literature; no later resolution located

Reference 2 explicitly records unrestricted interior uniqueness as open. The 2025 paper resolves smooth planar weights and certain higher-dimensional analytic or direction-independent weights. It does not prove the general smooth $n\geq3$ statement above.

Checked on 2026-09-08 using `p-Laplace Calderón open problem`, `p Calderon 2026 uniqueness`, and the exact title of reference 3. The theorem hypotheses were inspected to exclude its solved cases. No full higher-dimensional resolution was located.
