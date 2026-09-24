# 588. Uniform covariance bounds for constrained Ising replicas

**Area:** Probability, statistical mechanics and sampling

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Fix $n\geq1$, a real symmetric interaction matrix $J\in\mathbb R^{n\times n}$, and a partition $\mathcal A$ of $[n]$. For $N\geq2$, write a spin configuration as $\sigma=(\sigma(1),\ldots,\sigma(N))\in(\{-1,1\}^n)^N$. Choose integers $M_A$, one for each $A\in\mathcal A$, such that

$$
\Omega_{N,M}=\left\{\sigma:\sum_{i=1}^N\sum_{j\in A}\sigma_j(i)=M_A\text{ for every }A\in\mathcal A\right\}
$$

is nonempty. For an arbitrary external field $v\in\mathbb R^{Nn}$, define the probability measure

$$
\nu_{N,M,v}(\sigma)=\frac{\mathbf1_{\Omega_{N,M}}(\sigma)}{Z_{N,M,v}}
\exp\left\{\frac12\sum_{i=1}^N\sigma(i)^TJ\sigma(i)+\sum_{i=1}^N\sum_{j=1}^n v_{ij}\sigma_j(i)\right\}.
$$

Does there exist a finite constant $C(J,\mathcal A)$ such that

$$
\bigl\|\mathop{\mathrm{Cov}}\nolimits_{\nu_{N,M,v}}(\sigma)\bigr\|_{\mathrm{op}}\leq C(J,\mathcal A)
$$

for every $N$, every feasible $M$, and every $v$? The covariance is that of all $Nn$ spins, with the ordinary Euclidean operator norm. The constant may grow with the fixed interaction and dimension, but must be independent of the replica count, conserved magnetizations and external fields. Since there are finitely many partitions for fixed $n$, allowing dependence on $\mathcal A$ is equivalent to taking a maximum over partitions.

This is the tilted canonical-Ising covariance conjecture in [1, Section 4.5], with the constrained state space and measure expanded from equations (1.23)–(1.24).

## Application

The estimate would control fluctuations in particle systems that exchange spins while preserving specified magnetizations. The authors identify it as a route to entropy decay estimates uniform in the number of replicas, and consequently to quantitative convergence of nonlinear spin-exchange sampling at arbitrary interaction strengths.

## References

1. P. Caputo and M. Morellini, [Kac's Program and Relative Entropy Decay for Nonlinear Spin-Exchange Dynamics](https://arxiv.org/html/2511.05223v1), arXiv:2511.05223 (2025). Section 4.5; equations (1.23)–(1.24); Sections 3.3–3.4.
2. P. Caputo and A. Sinclair, [Entropy production in nonlinear recombination models](https://doi.org/10.3150/17-BEJ959), *Bernoulli* **24**(4B) (2018), 3246–3282. This journal article introduced the related reversible quadratic-system framework; the present conjecture is explicitly formulated in its later follow-up [1].

## Status review

**Known cases:** Stochastic-localization estimates give covariance control under a high-temperature spectral assumption on $J$. For a single total-magnetization constraint, [1, Proposition 3.6] gives the bound $2/(1-2\lambda_{max}(J))$ when $J$ is positive definite and $\lambda_{max}(J)<1/2$, uniformly over fields and system size. Section 3.4 handles the multicomponent setting needed for entropy decay. Section 4.5 also discusses bounds obtained through equivalence of ensembles with the tilt fixed; these do not give the required uniformity over arbitrary tilts.

**Remaining target:** Obtain a finite bound for every fixed interaction matrix, with the simultaneous uniformity stated above, or disprove it. A bound proportional to $Nn$ from the diagonal variances does not suffice.

The latest arXiv record remains version 1 of 7 November 2025 and retains the conjecture. The authors' July 2026 paper on nonlinear exchange for independent sets concerns a different state space and does not announce this result. Searches through 24 September 2026 found no matching solution announcement or repository duplicate. Native Palomar, GitHub repository/issue searches, and Zenodo returned no matching records under the source identifier or corresponding topic query.
