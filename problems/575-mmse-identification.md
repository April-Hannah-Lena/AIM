# 575. Identifying a distribution from its Gaussian-channel MMSE curve

**Area:** Statistical estimation and information theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $X$ and $Y$ be real random variables with finite second moments. For any such variable $U$, let $Z\sim N(0,1)$ be independent of $U$ and define its Gaussian-channel minimum mean-square error by
$$\operatorname{mmse}_U(s)=\mathbb E\left[(U-\mathbb E[U\mid\sqrt{s}\,U+Z])^2\right],\qquad s>0.$$

Prove or disprove that
$$\operatorname{mmse}_X(s)=\operatorname{mmse}_Y(s)\quad\text{for every }s>0$$
implies
$$Y\stackrel{d}=a+\eta X\qquad\text{for some }a\in\mathbb R,\quad\eta\in\{-1,1\}.$$

Translations and reflection leave the curve unchanged, so these ambiguities are unavoidable. The assertion concerns the complete curve, rather than only a finite collection of derivatives or moments. This is the finite-second-moment formulation of the MMSE conjecture in [1, Section 2.2].

## Application

The curve records the optimal denoising error at every signal-to-noise ratio. Identifiability would show whether this collection of scalar performance measurements determines the source distribution, up to the symmetries invisible to Gaussian noise.

## References

1. P. Mansanarez, G. Poly and Y. Swan, [Derivatives of Entropy and the MMSE Conjecture](https://doi.org/10.1109/TIT.2024.3466566), *IEEE Transactions on Information Theory* **70**(11) (2024), 7647–7663. Sections 2.2–2.3; [author manuscript](https://arxiv.org/html/2311.04831v2).
2. M. Ledoux, [Differentials of entropy and Fisher information along heat flow: A brief review of some conjectures](https://perso.math.univ-toulouse.fr/ledoux/files/2019/10/IEEE.pdf), *IEEE Transactions on Information Theory* **62**(6) (2016), 3353–3361. Section VI, Corollary 8.

## Status review

**Known cases:** Cumulant methods prove identification under additional restrictions. In [1, Theorem 2.15], a symmetric moment-determinate $X$ with strictly positive even cumulants is identified among centered competitors with moments of every order. Theorem 2.17 covers alternating even-cumulant signs when the competitor has matching fourth-cumulant sign. These include the uniform and Rademacher examples under the stated competitor restriction.

**Remaining target:** Prove identification for arbitrary finite-variance laws, or construct two laws with identical curves that are not translations or reflections of each other.

The current arXiv revision retains the general conjecture. Knowing the recursive polynomial expressions for the derivatives does not automatically resolve the signs of all cumulants or justify moment determination without assumptions. Recent counterexamples to complete monotonicity of entropy derivatives concern a different assertion and do not by themselves resolve this identification problem.

Searches through 24 September 2026 found no matching solution announcement or repository duplicate. Palomar returned no MMSE record; GitHub searches returned a paper-announcement mirror and unrelated arXiv digest hits, and the source's public code repository provides polynomial computation. Zenodo's native API returned HTTP 403; indexed searches found no matching announcement.
