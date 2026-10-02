# Simes error control for two-sided Gaussian tests

**Area:** Multiple testing and statistical inference

**Status:** Accepted; integrated as entry 332

**Last checked:** 2026-09-18

## Problem statement

Let $`n\ge1`$ and let $`\Sigma`$ be any real symmetric positive semidefinite $`n\times n`$ matrix with $`\Sigma_{ii}=1`$. Let

```math
X=(X_1,\ldots,X_n)\sim N_n(0,\Sigma),
\qquad
P_i=2\Phi(-|X_i|),
```

where $`\Phi`$ is the standard normal cumulative distribution function. Thus each $`P_i`$ is the two-sided Gaussian $`p`$-value for a zero mean, and every null hypothesis is true. Write $`P_{(1)}\le\cdots\le P_{(n)}`$ for their increasing order and define the Simes statistic

```math
S_n=\min_{1\le k\le n}\frac{nP_{(k)}}{k}.
```

**Does the inequality**

```math
\Pr\{S_n\le\alpha\}\le\alpha
```

**hold for every $`n`$, every such $`\Sigma`$, and every $`\alpha\in(0,1)`$?**

Equivalently, can the global test that rejects when some $`P_{(k)}\le k\alpha/n`$ have probability greater than $`\alpha`$ of rejecting a completely true null? The question asks for exact finite-dimensional control with arbitrary correlations. Marginal variances are known; no estimated covariance or Student $`t`$ statistic is involved. It is enough to settle positive definite $`\Sigma`$: approximation by $`(1-\varepsilon)\Sigma+\varepsilon I_n`$ extends the bound to singular matrices, because the rejection boundary has probability zero under the continuous marginal $`p`$-value laws.

## Applied significance

Large studies often combine correlated measurements to ask whether an entire group has any signal—for example, whether a prespecified group of gene-expression measurements departs from a null model. Under an exactly Gaussian model with known marginal variances, the proposed inequality would justify the usual Simes threshold without adjusting it for the unknown pattern of correlations. It would control the probability of declaring a signal when the whole group is null. This is a group-level guarantee; identifying which individual coordinates carry signals requires additional error-control arguments.

## References

1. Ziyu Chi, Aaditya Ramdas and Ruodu Wang, *Multiple testing under negative dependence*, Bernoulli 31(2) (2025), 1230–1255, [DOI](https://doi.org/10.3150/24-BEJ1768); [author manuscript](https://www.math.uwaterloo.ca/~wang/papers/2024Chi-Ramdas-Wang-BJ.pdf), 8 May 2024. Section 3.1, Eq. (13), defines the inequality; Section 3.3, Remark 11, manuscript p. 11, explicitly states this two-sided Gaussian conjecture.
2. Sanat K. Sarkar, *On Controlling the False Discovery Rate in Multiple Testing of the Means of Correlated Normals Against Two-Sided Alternatives*, [arXiv:2304.05261v1](https://arxiv.org/html/2304.05261v1), 11 April 2023. Section 1, immediately before the outline, distinguishes the unweighted Simes conjecture from the weighted test proved in Section 3.1, Theorem 1.
3. Sanat K. Sarkar, *Some probability inequalities for ordered MTP2 random variables: A proof of the Simes conjecture*, Annals of Statistics 26(2) (1998), 494–504, [DOI](https://doi.org/10.1214/aos/1028144846); [author-uploaded full text](https://www.researchgate.net/publication/38348568_Some_probability_inequalities_for_ordered_rm_MTPsb_2_random_variables_a_proof_of_the_Simes_conjecture). Theorem 3.1, pp. 499–500, proves a dependence-restricted inequality.
4. Sanat K. Sarkar, *On the Simes inequality and its generalization*, IMS Collections 1 (2008), 231–242, [DOI](https://doi.org/10.1214/193940307000000167); [author-uploaded full text](https://www.researchgate.net/publication/1923874_On_the_Simes_inequality_and_its_generalization). Section 3, Theorem 3.1 and the following discussion, give the relevant covariance restriction and clarify a previous scale-mixture proof gap.
5. Edgar Dobriban, *The Benjamini–Hochberg Procedure Can Fail to Control the FDR for Correlated Two-Sided Gaussian Tests*, [arXiv:2607.12208v1](https://arxiv.org/html/2607.12208v1), submitted 13 July 2026. Theorem 1 and Section 4 specify a counterexample with both zero and nonzero means.
6. Lihua Lei, *How Much Can Gaussian Dependence Inflate the Benjamini–Hochberg Procedure's FDR?*, [arXiv:2607.14812v3](https://arxiv.org/html/2607.14812v3), 22 July 2026. Theorem 2.1 and Section 2.5, Table 3, give further mixed-mean counterexamples; Remark 4.3 treats the dependence within their null block.
7. Deepra Ghosh and Sanat K. Sarkar, *Further Results on Controlling the False Discovery Rate in Two-Sided Gaussian Mean Testing*, [arXiv:2608.21267v2](https://arxiv.org/html/2608.21267v2), 24 August 2026. Theorems 3.1 and 4.2 concern covariance-dependent bounds and modified procedures.

## Status review

Open in cited literature; no later resolution located as of 2026-09-18.

Chi–Ramdas–Wang gives the exact conjecture, and Sarkar's 2023 introduction supplies an independently authored specialist discussion. Searches covered Simes and Gaussian global-null terminology, the cited authors, proofs and counterexamples, 2025–2026 results, unrestricted dates, corrections and version histories. The [evidence record](../candidates/two-sided-gaussian-simes.json) gives the source-access limits and theorem comparisons. Finner–Roters–Strassburger's 2017 paper was accessible only in preview; its Section 7 was not read, so admission relies on the accessible explicit restatement and independent discussion.

The bound is an equality for independent coordinates. Known sufficient dependence conditions also cover positive definite $`\Sigma`$ for which some diagonal matrix $`D`$ with entries in $`\{-1,1\}`$ makes every off-diagonal entry of $`D\Sigma^{-1}D`$ nonpositive. This restriction does not cover every correlation matrix. Sarkar's 1998 title therefore does not announce a solution of the unrestricted Gaussian problem. Chi–Ramdas–Wang's Theorem 8 concerns a different, monotone Gaussian-copula construction; Remark 11 explicitly separates the absolute-value case.

The 2026 Benjamini–Hochberg counterexamples concern false-discovery rate when some means are nonzero. Their constructions fail the all-zero hypothesis here. When all nulls are true, every rejection is false and false-discovery rate equals the probability of any rejection, giving exactly the displayed Simes question. The broader mixed-mean conjecture is not included. Weighted, shifted and covariance-calibrated procedures also change the statistic or thresholds, so their guarantees do not establish this inequality. An older all-null counterexample under weak dependence uses non-Gaussian uniform variables; its full construction was compared in the evidence record.

This is one problem across dimensions and correlation patterns. It differs from [Gaussian polynomial unlinking](../../../problems/317-gaussian-polynomial-unlinking.md), which concerns independence of polynomial statistics, and [Gaussian simplex noise stability](../../../problems/294-gaussian-simplex.md), which optimizes partitions.

The separated A41 adversarial self-pass passed on September 18. No independent agent or human review is claimed. The final batch refresh is recorded in the evidence ledger.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../batch-04-review.md). No matching later resolution was located.

Integrated page: [340. Simes error control for two-sided Gaussian tests](../../../problems/329-two-sided-gaussian-simes.md).
