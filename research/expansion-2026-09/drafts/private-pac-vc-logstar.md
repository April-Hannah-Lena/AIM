# Private PAC learning with polynomial VC and iterated-logarithm sample cost

**Area:** Statistical learning, data privacy and sample complexity

**Status:** Accepted; integrated as entry 346

**Last checked:** 2026-09-19

## Problem statement

Let $`X`$ be a finite nonempty set and $`\varnothing\ne\mathcal C\subseteq\{0,1\}^{X}`$. Its VC dimension $`v`$ is the largest size of a subset of $`X`$ on which $`\mathcal C`$ realizes every binary labeling. Its Littlestone dimension $`d`$ is the largest depth of a complete binary tree with internal nodes labeled by points of $`X`$ and outgoing edges labeled $`0,1`$, such that every root-to-leaf path agrees with some $`c\in\mathcal C`$ at all its node-edge pairs. Assume $`v\ge1`$.

For an integer $`n\ge1`$, consider a randomized learner

```math
A:(X\times\{0,1\})^n\longrightarrow\{0,1\}^{X}.
```

The class is known to the learner. For every probability distribution $`D`$ on $`X`$ and target $`c\in\mathcal C`$, the learner receives only

```math
S=((x_1,c(x_1)),\ldots,(x_n,c(x_n))),\qquad x_i\ \text{independently drawn from }D.
```

It must output $`h=A(S)`$ with

```math
\Pr_{S,A}\!\left[\Pr_{x\sim D}\{h(x)\ne c(x)\}\le\frac1{16}\right]\ge\frac{15}{16}.
```

The inner probability uses a fresh input. In addition, for every pair of datasets $`S,S'`$ differing in one labeled record, and every set $`E\subseteq\{0,1\}^{X}`$, require

```math
\Pr[A(S)\in E]\le e^{0.1}\Pr[A(S')\in E]+\frac{1}{100n^3}.
```

This privacy condition applies to all datasets, including those inconsistent with $`\mathcal C`$. The output may lie outside $`\mathcal C`$, and there is no running-time bound.

Let $`m_{\mathrm{priv}}(\mathcal C)`$ be the smallest such sample size. Write $`\log_2^* t`$ for the number of iterated base-two logarithms needed to reduce $`t`$ to at most one. **Do universal constants $`K>0`$ and $`q\in\mathbb N`$, $`q\ge1`$, exist such that**

```math
m_{\mathrm{priv}}(\mathcal C)
\le K\left(1+v+\log_2^*(\max\{2,d\})\right)^q
```

**for every finite $`X`$ and every such class $`\mathcal C`$?**

This is a finite-domain, fixed-accuracy formulation of the quantitative question in [1, §6] and [2, §2]. Those sources suppress privacy and accuracy dependence. Here the accuracy, confidence and multiplicative privacy constant are fixed, and the privacy slack is explicitly inverse cubic in sample size, within the small-slack regime of [1, Theorem 2]. This formulation does not assert equivalence with every privacy-parameter regime or with arbitrary infinite domains.

## Applied significance

The question asks how many sensitive labeled records are fundamentally needed to release an accurate classifier while limiting the effect of any one record on its output distribution. Ordinary classification can have small sample cost even when the class has large Littlestone dimension. A positive answer would limit the additional data required for privacy to a polynomial in VC dimension and a very slowly growing function of that larger dimension. This is a statistical existence question; it would not itself supply a fast training algorithm. [1, §§1–2; 2, §§1–2]

## References

1. Noga Alon, Mark Bun, Roi Livni, Maryanthe Malliaris and Shay Moran, *Private and Online Learnability Are Equivalent*, Journal of the ACM 69(4) (2022), article 28. [Author manuscript dated January 28, 2022](https://web.math.princeton.edu/~nalon/PDFS/JACMjoint1.pdf), §6 first question, p. 33; §3.1, §3.2 and Definition 12; Theorems 2–3. Locators refer to the 41-page author manuscript.
2. Kobbi Nissim, Uri Stemmer and Eliad Tsfadia, *Invited Open Problem: Does Differential Privacy Make PAC Learning Much Harder?*, [COLT 2026, PMLR 336, 7129–7135](https://proceedings.mlr.press/v336/nissim26a.html); [full paper](https://raw.githubusercontent.com/mlresearch/v336/main/assets/nissim26a/nissim26a.pdf). §1 footnotes 1–2 and Theorems 2–3; §2 discussion following Open Question 1, PDF p. 3.
3. Chao Yan, *An Õptimal Differentially Private Learner for Concept Classes with VC Dimension 1*, [arXiv:2505.06581v2](https://arxiv.org/html/2505.06581v2), revised July 29, 2025. §1 and §1.1 Theorems 1–2; §3 definitions.
4. Xin Lyu, *Private Learning of Littlestone Classes, Revisited*, [arXiv:2510.00076v1](https://arxiv.org/html/2510.00076v1), September 30, 2025 manuscript. §1.1 Theorem 2 and §5 Corollary 5.1.
5. Dechen Zhang, Xuan Tang, Xinxiang Yin, Xingwu Chen, Jian Qian and Difan Zou, *VALG: An Agentic System for ML Theory Research and Demonstrations on COLT 2026 Open Problems*, [arXiv:2608.13060v2](https://arxiv.org/html/2608.13060v2), revised September 10, 2026, preprint. §4.4, Assumptions 4.43–4.50 and Theorems 4.10–4.11.

## Status review

Open in cited literature; no later resolution located as of 2026-09-19. Sources [1] and the independently authored [2] pose the polynomial VC/iterated-logarithm question. The review searched its mathematical wording, later bounds, purported resolutions, versions and corrections.

The known general upper bound has polynomial dependence on $`d`$, with Lyu's bound involving $`d^5`$ and logarithmic privacy factors. The lower bound is of order $`v+\log^*d`$ in the stated small-slack regime. Substituting the specified privacy slack into the upper bounds leaves a polynomial-in-$`d`$ guarantee, not the requested polynomial-in-$`v+\log^*d`$ guarantee. Yan proves nearly matching dependence on $`\log^*d`$ when $`v=1`$; the question here is uniform over all VC dimensions.

The September 2026 VALG manuscript reports results for Cartesian products of VC-one classes and a threshold-minor lower bound. Its complete assumptions retain the product structure, and its lower bound does not give a superpolynomial separation from the target here. These reported results are not independently certified proofs.

The [evidence record](../candidates/private-pac-vc-logstar.json) also compares distribution-restricted learning, density-estimation impossibility, cryptographic computational separations, pure-private proper-learning lower bounds and private decision-list algorithms. The smoothness and feature-count bounds retain extra parameters even when applied to a finite class. None supplies a matching resolution for arbitrary finite binary classes with unrestricted training time. The record states access limits and the explicit parameter normalization.

This differs from retaining a small reconstructing subsample in [entry 310](../../../problems/310-linear-sample-compression.md), efficient noisy-parity recovery in [entry 309](../../../problems/309-learning-parity-noise.md), and efficient uniform-DNF learning in [entry 329](../../../problems/329-classical-uniform-dnf-learning.md). Privacy restricts the distribution of the complete released classifier. One quantitative private-classification family is counted; no additional counts are assigned to its dimensions or parameter variants.

The separated A56 adversarial self-pass passed on September 19, 2026. This review is not an independent mathematical proof audit.
