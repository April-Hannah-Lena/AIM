# 125. Subpolynomial compact-set peaks of Hecke–Maass waves

**Area:** Arithmetic quantum chaos

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $X=\operatorname{PSL}_2(\mathbb Z)\backslash\mathbb H$ have hyperbolic measure $dx\,dy/y^2$. Let $u$ be an $L^2$-normalized smooth real cusp form with

$$-y^2(\partial_x^2+\partial_y^2)u=(\tfrac14+t^2)u,\qquad t\ge0,$$

which is an eigenfunction of every Hecke operator

$$(T_nf)(z)=n^{-1/2}\sum_{ad=n,\ a,d>0}\ \sum_{b=0}^{d-1}f\!\left(\frac{az+b}{d}\right).$$

The cusp condition means $\int_0^1u(x+iy)\,dx=0$ for every $y>0$. Prove or disprove that for each compact $K\subset X$ and every $\varepsilon>0$ there is $C_{K,\varepsilon}$, independent of $u,t$, such that

$$\sup_K|u|\le C_{K,\varepsilon}(1+t)^\varepsilon.$$

The compact set is fixed as frequency grows.

## Application

These functions model quantized chaotic motion on an arithmetic surface. The estimate rules out polynomially large exceptional wave peaks in any fixed observable region, beyond what average equidistribution says.

## References

1. Y. N. Petridis and M. S. Risager, [Averaging over Heegner points in the hyperbolic circle problem](https://doi.org/10.1093/imrn/rnx026), International Mathematics Research Notices (2018), §1, conjectural assumption (C2): compact-set sup-norm conjecture.
2. P. Humphries and R. Khan, [$L^p$-norm bounds for automorphic forms via spectral reciprocity](https://doi.org/10.1112/plms.70061), Proceedings of the London Mathematical Society 130 (2025), introduction and main results: quantitative partial norm bounds.
3. H. Ki, [$L^4$-norms and sign changes of Maass forms](https://annals.math.princeton.edu/articles/22563), accepted by Annals of Mathematics (6 February 2026), abstract: a recent fourth-moment result.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 accepted paper resolves a fourth-moment conjecture, not the pointwise compact-set bound. Compactness is necessary: the noncompact cusp permits a different peak scale. Neither averaged equidistribution nor a fourth-moment bound controls every point of every eigenfunction as required here.

**Search audit:** “Sarnak sup norm conjecture compact Hecke Maass 2026”; “Maass forms sup norm proof counterexample 2025 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
