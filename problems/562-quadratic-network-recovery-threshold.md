# 562. Perfect recovery threshold for unregularized quadratic-network training

**Area:** High-dimensional statistics and nonconvex learning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix $0<\kappa^*<\kappa<1$ and $\alpha>0$. As $d\to\infty$, take integers $m^*/d\to\kappa^*$, $m/d\to\kappa$, and $n/d^2\to\alpha$. Draw independent teacher vectors $w_i^*\sim N(0,I_d)$ and set
$$Z^*=\frac1{m^*}\sum_{i=1}^{m^*}w_i^*w_i^{*\top}.$$
Independently draw $n$ symmetric Gaussian sensing matrices $X_k$ with independent upper-triangular entries
$$ (X_k)_{ij}\sim N\!\left(0,\frac{1+\delta_{ij}}d\right),\qquad i\le j,$$
and observe the noiseless labels $z_k=\operatorname{Tr}(X_kZ^*)$.

For $W\in\mathbb R^{d\times m}$, define
$$\mathcal L_d(W)=\frac1{4n}\sum_{k=1}^n\bigl[\operatorname{Tr}(X_kWW^\top)-z_k\bigr]^2.$$
Run unregularized gradient flow $\dot W=-d\nabla\mathcal L_d(W)$, initialized independently with entries $W_{ij}(0)\sim N(0,1/m)$. Write
$$R(\alpha;\kappa,\kappa^*)=\lim_{t\to\infty}\lim_{d\to\infty}
\frac1d\mathbb E\|W(t)W(t)^\top-Z^*\|_F^2,$$
where expectation includes the teacher, measurements and initialization. Establishing the limits is part of the question.

Let $\sigma$ be the semicircle probability measure with density $\sqrt{4-x^2}/(2\pi)$ on $[-2,2]$, and choose $\omega\in(-2,2)$ by
$$\sigma([\omega,2])=\frac{\kappa-\kappa^*}{1-\kappa^*}.$$
Define
$$a_{\rm inter}=\kappa^*-\frac{(\kappa^*)^2}{2}
+\frac{(1-\kappa^*)^2}{2}\int_{\max(0,\omega)}^2 x^2\,d\sigma(x),
\qquad a_{\rm PR}=\min\!\left\{\kappa-\frac{\kappa^2}{2},a_{\rm inter}\right\}.$$

Prove or disprove that $R(\alpha;\kappa,\kappa^*)=0$ for every $\alpha>a_{\rm PR}$ and $R(\alpha;\kappa,\kappa^*)>0$ for every $0<\alpha<a_{\rm PR}$. No assertion at the critical value is requested.

This is the Gaussian-teacher, Gaussian-initialization instance of [1, Conjecture 15], restricted to strictly rank-deficient student and teacher matrices. The order of limits is fixed, and the regularization coefficient is identically zero.

## Application

The threshold predicts how many measurements gradient training needs to identify a low-rank positive semidefinite signal. It would quantify how increasing network width changes exact recovery and how the dynamics select among interpolating solutions.

## References

1. S. Martin, G. Biroli and F. Bach, [High-Dimensional Analysis of Gradient Flow for Extensive-Width Quadratic Neural Networks](https://www.jmlr.org/papers/v27/26-0672.html), *Journal of Machine Learning Research* **27**(136) (2026), 1–182. Sections 2 and 3.4.2, Conjecture 15 and equations (74)–(76). [Published PDF](https://www.jmlr.org/papers/volume27/26-0672/26-0672.pdf). The corresponding statement is Conjecture 11 in [arXiv:2601.10483v2](https://arxiv.org/html/2601.10483v2).
2. V. Erba, E. Troiani, L. Zdeborová and F. Krzakala, [The Nuclear Route: Sharp Asymptotics of ERM in Overparameterized Quadratic Networks](https://arxiv.org/abs/2505.17958), *Journal of Statistical Mechanics: Theory and Experiment* (2026), 074004. [DOI](https://doi.org/10.1088/1742-5468/ae8248).

## Status review

The published source supports the conjecture numerically, and its July 2026 arXiv revision retains it. The conjecture concerns selection by unregularized dynamics. The small-positive-regularization limit analyzed elsewhere in [1] has a different predicted threshold; the regularized empirical-risk analysis in [2] does not settle this question. The dynamical mean-field calculations in [1] should not be read as an unconditional rigorous proof of the stated recovery transition.

The central difficulty is controlling the long-time behavior of the nonconvex flow at the sharp proportional sampling scale, including which interpolating matrix it selects. Counting the parameters in the rank-constrained matrix manifold does not determine that selection.

Checks through 24 September 2026 found no matching solution announcement or repository duplicate.
