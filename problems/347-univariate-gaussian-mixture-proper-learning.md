# 347. Polynomial-time proper learning of univariate Gaussian mixtures

**Area:** Statistical density estimation and unsupervised learning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-19

## Problem statement

For an integer $`k\ge1`$, let $`\mathcal G_k`$ be the densities on $`\mathbb R`$ of the form

```math
f(x)=\sum_{i=1}^k w_i\frac{1}{\sqrt{2\pi}\,\sigma_i}
\exp\!\left(-\frac{(x-\mu_i)^2}{2\sigma_i^2}\right),
\qquad
w_i\ge0,\quad \sum_{i=1}^k w_i=1,\quad
\mu_i\in\mathbb R,\quad \sigma_i>0.
```

Zero weights allow mixtures with fewer than $`k`$ components. The component means, variances and weights are unknown and otherwise unrestricted.

Does there exist a randomized algorithm $`A`$ and a fixed polynomial $`p`$ with the following guarantee? For every $`k\ge1`$, every $`0<\varepsilon<1`$ and every $`f\in\mathcal G_k`$, the algorithm receives $`k,\varepsilon`$ and access to independent samples from $`f`$. Using at most $`p(k,\varepsilon^{-1})`$ samples and operations, it outputs an explicit list of at most $`k`$ Gaussian components defining a density $`\widehat f\in\mathcal G_k`$ such that

```math
\Pr_{\text{samples},A}\!\left[
d_{\mathrm{TV}}(f,\widehat f)
=\frac12\int_{\mathbb R}|f(x)-\widehat f(x)|\,dx
\le\varepsilon\right]\ge\frac23?
```

Use the infinite-precision real-arithmetic sampling model of Daskalakis–Kamath, §2, including exact Gaussian-density evaluation. The bound counts arithmetic operations and sample access; it is not a bit-complexity claim for arbitrary real inputs. The same polynomial must work for all $`k`$: an exponent depending on $`k`$ does not meet the target.

This is the realizable *proper-learning* question. No separation, bounded parameter range or minimum nonzero weight is assumed. The output must use at most $`k`$ components, but its parameters need not match the original components. Neither recovery of hidden labels nor maximizing an empirical likelihood is required. The question is explicitly retained even without noise in Li–Liu–Moitra's revised manuscript.

## Application

Gaussian mixtures describe heterogeneous scalar measurements through a small collection of normal distributions. Proper learning asks whether an accurate density estimate can always retain this compact model form within feasible computation. Total variation controls the error in every event probability, while the component limit controls the size of the fitted representation. Recovering that representation does not identify physical subpopulations: different component parameters can produce very similar densities. This distinction matters when a mixture is used as a statistical approximation rather than as a uniquely identifiable mechanism. The sources discuss both the value of compact mixture descriptions and the additional difficulties of parameter estimation.

## References

1. Ilias Diakonikolas, *Learning Structured Distributions*, contribution to *Handbook of Big Data* (2016), [author manuscript](http://www.iliasdiakonikolas.org/distribution-learning-survey.pdf). §§1.2–1.3 define the learning model; §1.6, pp. 13–14, discusses univariate Gaussian mixtures and poses Open Problem 1.6.2 on proper learning of parametric mixtures. The numbering refers to this manuscript.
2. Jerry Li and Ludwig Schmidt, *Robust and Proper Learning for Mixtures of Gaussians via Systems of Polynomial Inequalities*, COLT 2017, PMLR 65, 1302–1382, [published paper](https://proceedings.mlr.press/v65/li17a/li17a.pdf). §§1.1–1.2.1, Theorem 1, and §2.1; internal PDF pp. 2–5 and 13. Explicit Gaussian formulation and a fixed-$`k`$ algorithm.
3. Constantinos Daskalakis and Gautam Kamath, *Faster and Sample Near-Optimal Algorithms for Proper Learning Mixtures of Gaussians*, COLT 2014, PMLR 35, 1183–1213, [published paper](https://proceedings.mlr.press/v35/daskalakis14.pdf). §2, internal p. 5, specifies total variation and the real-arithmetic model; Theorem 1 concerns two components.
4. Allen Liu, Jerry Li and Ankur Moitra, *Robust Model Selection and Nearly-Proper Learning for GMMs*, NeurIPS 2022, 22830–22843, [proceedings paper](https://papers.nips.cc/paper/2022/file/8f75af4704feac629a560f4ad6b67cef-Paper-Conference.pdf); [expanded arXiv:2106.02774v2](https://arxiv.org/pdf/2106.02774v2), revised April 23, 2023. §1.1, Theorem 1.1, and the open-question paragraph following Theorem 1.3, p. 3.
5. Spencer Compton and Jerry Li, *Density estimation for Hellinger via minimum-distance estimators: mixtures of Gaussians, log-concave, and more*, COLT 2026, PMLR 336, 1436–1475, [published paper](https://raw.githubusercontent.com/mlresearch/v336/main/assets/compton26a/compton26a.pdf). §1.1, Theorem 2 and the following paragraph specify a piecewise-polynomial output.
6. Sitan Chen, Vasilis Kontonis and Kulin Shah, *Learning general Gaussian mixtures with efficient score matching*, COLT 2025, [published paper](https://raw.githubusercontent.com/mlresearch/v291/main/assets/chen25e/chen25e.pdf). §1.1, Definition 1 and Theorem 2; formal Theorem 11, internal p. 22. The result outputs a sampling procedure under additional parameter conditions.
7. Hengzhi He and Guang Cheng, *Sharp proper estimation of fixed-component Gaussian location mixtures in polynomial time*, [arXiv:2608.12701v1](https://arxiv.org/pdf/2608.12701v1), August 13, 2026, preprint. Theorem 1.1 and §8 retain fixed component count, unit covariance and bounded means; the runtime exponent depends on $`k`$.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of **2026-09-19**. The independently authored Diakonikolas survey and Li–Schmidt paper distinguish proper learning from unrestricted density estimation. Li–Liu–Moitra explicitly leave the all-$`k`$ proper-learning question open and conjecture computational hardness when extra components are forbidden; this is a conjecture, not a hardness theorem.

Li–Schmidt obtain nearly optimal sample complexity, with a runtime containing $`(k\log(1/\varepsilon))^{O(k^4)}`$. Their result is efficient for each fixed $`k`$ but not polynomial uniformly in $`k`$. Li–Liu–Moitra give polynomial dependence on $`k`$ and accuracy while allowing a polylogarithmic factor more than $`k`$ output components. Compton–Li's 2026 theorem achieves near-linear runtime and strong statistical guarantees by outputting a piecewise-polynomial density. Its Hellinger bound implies a total-variation bound, but does not supply a mixture with at most $`k`$ components.

The score-matching result retains conditioning and weight parameters and produces a sampler. Robust Gaussian-mixture algorithms with a fixed number of components retain $`k`$-dependent accuracy exponents. He–Cheng's August 2026 preprint obtains a sharp statistical rate for fixed-$`k`$ location mixtures; its explicit runtime bound still has a $`k`$-dependent exponent, and its means and variances are restricted. Certified nonparametric maximum-likelihood computation for location mixtures uses a common fixed variance and does not impose the target component limit. Known hardness results inspected here concern arbitrary-data likelihood optimization or a growing ambient dimension; neither establishes hardness of this one-dimensional sampling question.

Searches covered proper and nearly-proper learning, univariate Gaussian mixtures, recent algorithms, resolution claims, corrections and withdrawals. Exact theorem comparisons, source versions and access limits are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/univariate-gaussian-mixture-proper-learning.json). Nearby catalogue questions concern [sample compression](307-linear-sample-compression.md), [independence of Gaussian polynomial statistics](317-gaussian-polynomial-unlinking.md) and [Boolean rule learning](326-classical-uniform-dnf-learning.md). The [private-PAC problem](343-private-pac-vc-logstar.md) concerns the sample cost of private classification. None asks for this density-estimation algorithm. All component counts and equivalent total-variation conventions are one problem family.

A separate adversarial self-review checked the quantifiers, computation model, source versions and possible indirect resolutions. This was not an independent expert review or a certification of the cited proofs. The source ledger records full-text access alternatives and the limits of each comparison.
