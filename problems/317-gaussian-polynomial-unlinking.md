# 317. Orthogonal separation of independent Gaussian polynomial statistics

**Area:** Probability and mathematical statistics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $`n\ge2`$, let $`X\sim N(0,I_n)`$ be a standard real Gaussian vector, and let $`f,g\in\mathbb R[x_1,\ldots,x_n]`$ be nonconstant polynomials. Suppose that the random variables $`f(X)`$ and $`g(X)`$ are independent: for every pair of Borel sets $`A,B\subseteq\mathbb R`$,

```math
\mathbb P\{f(X)\in A,\ g(X)\in B\}
=\mathbb P\{f(X)\in A\}\mathbb P\{g(X)\in B\}.
```

Must there exist an orthogonal matrix $`O\in\mathbb R^{n\times n}`$, an integer $`1\le k<n`$, and polynomials $`F\in\mathbb R[y_1,\ldots,y_k]`$ and $`G\in\mathbb R[y_{k+1},\ldots,y_n]`$ such that, for every $`y\in\mathbb R^n`$,

```math
O^TO=I_n,\qquad
f(Oy)=F(y_1,\ldots,y_k),\qquad
g(Oy)=G(y_{k+1},\ldots,y_n)?
```

This is the **U-conjecture**, or Gaussian polynomial unlinking conjecture, attributed to Kagan, Linnik and Rao. The requested conclusion separates the two statistics into disjoint coordinate blocks after one orthogonal change of variables. Its converse follows from independence of the coordinates of $`O^TX`$. The general question permits arbitrary finite polynomial degrees; it imposes no convexity, symmetry or single-chaos assumption. Independence is essential: zero covariance alone is not the hypothesis. The two-dimensional case is known; the unresolved general assertion concerns higher dimensions.

## Application

Polynomial functions of Gaussian observations include linear contrasts, quadratic statistics and higher-order summaries. Independence lets statistical procedures separate sources of random variation, but a nonlinear statistic can depend on several original coordinates. The conjecture asks whether exact independence of two polynomial summaries always has an underlying explanation through orthogonal groups of Gaussian inputs. A positive answer would give a structural characterization of such independence beyond familiar linear and quadratic cases; a counterexample would identify a limit of that explanation. This is a foundational question in multivariate statistics, rather than a proposed procedure for inferring independence from finite samples.

## References

1. He-Jing Hong and Ze-Chun Hu, *Unlinking Theorem for Symmetric Quasi-Convex Polynomials*, Chinese Journal of Applied Probability and Statistics **38**(1) (2022), 151–158, [published PDF](https://aps.ecnu.edu.cn/cn/article/pdf/preview/10.3969/j.issn.1001-4268.2022.01.011.pdf), [DOI](https://doi.org/10.3969/j.issn.1001-4268.2022.01.011). §1, pp. 151–152, and Theorem 1. Explicit general formulation, known two-dimensional case, and a restricted unlinking theorem.
2. Gilles Hargé, *Characterization of equality in the correlation inequality for convex functions, the U-conjecture*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **41**(4) (2005), 753–765, [full text](https://www.numdam.org/article/AIHPB_2005__41_4_753_0.pdf), [DOI](https://doi.org/10.1016/j.anihpb.2004.05.005). §1 and Theorem 1.2, pp. 753–754. Independent formulation and a convex-function result.
3. Dominique Malicet, Ivan Nourdin, Giovanni Peccati and Guillaume Poly, *Squared chaotic random variables: new moment inequalities with applications*, Journal of Functional Analysis **270**(2) (2016), 649–670, [DOI](https://doi.org/10.1016/j.jfa.2015.10.013); [author manuscript, arXiv:1503.02154v1](https://arxiv.org/html/1503.02154v1), March 7, 2015. §1.5, Theorem 1.7, and its proof in §3.6. A result for specified sums of squares of Wiener-chaos polynomials.
4. Christian Genest, Frédéric Ouimet and Donald Richards, *On the Gaussian product inequality conjecture for disjoint principal minors of Wishart random matrices*, Electronic Journal of Probability **29** (2024), 26 pp., [DOI](https://doi.org/10.1214/24-EJP1222); [author manuscript, arXiv:2311.00202v3](https://arxiv.org/html/2311.00202v3), October 1, 2024. §1, discussion following Eq. (1). Further independent specialist restatement of the U-conjecture.
5. Guolie Lan, Frédéric Ouimet and Wei Sun, *Results related to the Gaussian product inequality conjecture for mixed-sign exponents in arbitrary dimension*, [arXiv:2505.09976v3](https://arxiv.org/pdf/2505.09976v3), preprint, August 27, 2026. §1, p. 1, paragraph following Eq. (1). Current restatement using a standard Gaussian vector.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Hong–Hu explicitly retain the general question while proving unlinking when both polynomials are even and quasi-convex. Here quasi-convexity means that every sublevel set is convex. Hargé's Theorem 1.2 assumes two convex functions, with one analytic and attaining its minimum at the origin. These hypotheses do not include arbitrary polynomials.

Malicet–Nourdin–Peccati–Poly prove unlinking for their class of finite sums $`\sum_{j=1}^m F_j^2`$, where $`F_j`$ belongs to the $`j`$th Wiener chaos. That is the eigenspace with eigenvalue $`-j`$ of the Gaussian Ornstein–Uhlenbeck operator $`\mathcal L=\Delta-x\cdot\nabla`$. Their proof uses nonnegative covariances of the squared chaos components. General polynomial expansions need not have this form. The 2024 Wishart paper independently restates the unrestricted question; multiple versions of a work are not counted as independent evidence.

The September 17, 2026 searches covered the name, unlinking and independence formulations, authors, unrestricted dates, 2025–2026, proofs, counterexamples, corrections and withdrawals. Two recent neighboring claims were checked at statement level. Ouimet–Greaves' [strong Gaussian product-inequality manuscript](https://www.researchgate.net/publication/410720385_A_proof_of_the_strong_Gaussian_product_inequality_conjecture), Theorem 2.1, concerns products of absolute powers of jointly Gaussian coordinates. Long's [Gaussian-moments counterexample](https://arxiv.org/html/2607.18186v1), Theorem 5.1, uses complex polynomials and vanishing moments, without an independent pair of real polynomial statistics. Neither statement supplies the conclusion or a counterexample required here. This scope comparison does not certify those proofs.

Lan–Ouimet–Sun's August 2026 revision also retains the U-conjecture. It shares an author with the Wishart paper, so these two works are not counted as separate independent teams. The historical monograph was accessed through explicit scholarly restatements. No matching general resolution was located; indexing and access limitations remain. The [evidence ledger](../research/expansion-2026-09/candidates/gaussian-polynomial-unlinking.json) records the searches and theorem comparisons. The [Gaussian simplex problem](294-gaussian-simplex.md) optimizes partition agreement rather than asking for structural separation of independent polynomial statistics. No separate entries are counted for special dimensions or polynomial classes.

The separated A29 adversarial self-pass passed on September 17, 2026.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
