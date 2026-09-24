# 348. The sharp support–concentration bound for subset sums

**Area:** Combinatorial probability, information theory and packing algorithms

**Status:** 🔵 OPEN

**Last checked:** 2026-09-19

## Problem statement

Let $`n\geq1`$ be an integer and let $`w=(w_1,\ldots,w_n)\in\mathbb R^n`$. For independent random variables $`X_i`$ with $`\Pr(X_i=0)=\Pr(X_i=1)=1/2`$, define

```math
S_w=\sum_{i=1}^n w_iX_i,\qquad
R(w)=\left\{\sum_{i=1}^n w_ix_i:x\in\{0,1\}^n\right\}.
```

Write $`N(w)=|R(w)|`$ for the number of distinct subset sums and $`\rho(w)=\max_{t\in\mathbb R}\Pr(S_w=t)`$ for the largest probability of a single sum. Prove or disprove the conjecture that, for every $`n`$ and $`w`$,

```math
N(w)\,\rho(w)^2\leq1.
```

Repeated, negative and zero weights are allowed. The subsets are labelled by their indices, and all $`2^n`$ subsets are equally likely. The sums and equality of their values are exact. The bound has no additional constant or asymptotic error. If every weight is zero, $`N(w)=\rho(w)=1`$.

In counting terms, if $`M(w)`$ is the greatest number of subsets having the same sum, then $`M(w)=2^n\rho(w)`$ and the conjecture is $`N(w)M(w)^2\leq4^n`$. Equivalently, with natural logarithms, define the order-zero and order-infinity Rényi entropies by

```math
H_0(S_w)=\log N(w),\qquad H_\infty(S_w)=-\log\rho(w).
```

The conjecture is $`H_0(S_w)\leq2H_\infty(S_w)`$. Jain, Sah and Sawhney propose this tradeoff; Li states the entropy formulation explicitly. The exponent two is sharp: for $`w=(1,\ldots,1)`$, $`N(w)=n+1`$ and $`\rho(w)=2^{-n}\binom{n}{\lfloor n/2\rfloor}`$, so $`H_0/H_\infty\to2`$ as $`n\to\infty`$.

## Application

In bin packing, items with given weights must be partitioned among bins without exceeding their capacities. Exact algorithms can exploit the number of attainable item-weight totals: fewer totals can mean fewer states in a dynamic program. Nederlof and coauthors use a tradeoff between this number and the largest multiplicity of a total in their algorithm for a fixed number of bins. Jain, Sah and Sawhney show that improving the tradeoff improves that algorithm's dependence on the number of bins. The probability above measures collisions among subsets of a fixed input; it imposes no random-input assumption. The entropy formulation also asks how much uncertainty in the most likely outcome controls the entire range of a weighted sum of fair bits.

## References

- V. Jain, A. Sah and M. Sawhney, [*Anticoncentration versus the Number of Subset Sums*](https://arxiv.org/pdf/2101.07726v2), *Advances in Combinatorics* 2021:6, 10 pp., [DOI: 10.19086/aic.24872](https://doi.org/10.19086/aic.24872). Question 1.1 and the conjecture paragraph immediately before equation (1.2), p. 2; Theorem 1.2; §1.1, p. 3, for bin packing. The linked June 14 revision is the published text.
- J. Li, [*Multiplicative comparisons of Rényi entropies for weighted Bernoulli sums*](https://arxiv.org/html/2609.01529v1), arXiv:2609.01529v1, September 1, 2026, preprint. Conjecture 1.1, Remarks 1.2–1.3, Theorems 1.5–1.6 and §3. This independently authored work explicitly retains the exact conjecture.
- J. Nederlof, J. Pawlewicz, C. M. F. Swennenhuis and K. Węgrzycki, [*A Faster Exponential Time Algorithm for Bin Packing With a Constant Number of Bins via Additive Combinatorics*](https://arxiv.org/html/2007.08204v4), *SIAM Journal on Computing* **52**(6) (2023), 1369–1412, [DOI: 10.1137/22M1478112](https://doi.org/10.1137/22M1478112). Theorems 1.1–1.2, §1.1.1 and §3.2, Lemma 3.5; the linked author version is dated September 8, 2023.

## Status review

**Literature check:** Open in cited literature; no later resolution located as of 2026-09-19.

Checked on **2026-09-19** using the subset-sum, anticoncentration, maximum-atom and Rényi-entropy formulations, author names, and proof, counterexample, correction and recent-result searches. The published Jain–Sah–Sawhney paper and Li's September 2026 preprint explicitly state the conjecture. No later resolution of the full assertion was located.

Jain, Sah and Sawhney prove that $`\rho(w)\geq\exp(-\varepsilon n)`$ implies $`N(w)\leq\exp(C\sqrt\varepsilon\,n)`$, for an absolute constant $`C`$, provided $`\varepsilon>0`$ and $`n\geq\varepsilon^{-1/2}`$. Li reports the stronger entropy comparison

```math
H_0(S_w)\leq
\min\left\{\log_2(m+1),\ 2+\log_2\!\left(\frac{m\log2}{H_\infty(S_w)}\right)\right\}
H_\infty(S_w),
```

where $`m`$ is the number of nonzero weights and this displayed expression is used for $`w\ne0`$. Its coefficient still depends on the input. Li also proves bounds for positive Rényi orders; their constants grow as the order approaches zero, so those statements do not supply the missing factor two at order zero. These are reported preprint results; their full proofs have not been independently certified here. The SIAM publisher link restricted direct access; its primary author manuscript was accessible.

The audit also compares earlier high-multiplicity constructions, 2026 bounds for fixed-size random subsets of finite groups, and structural classifications of sets with few subset sums, including a September 14 revision. Their stated conclusions do not give the required bound for all real weight vectors with repetitions. The remaining question is the uniform, exact factor two for the full support, with fair independent bits. Biased bits are outside its scope.

This differs from [integer 3SUM hardness](343-integer-three-sum-hardness.md), which asks about running time; [cutting-stock rounding](344-modified-integer-round-up.md), which asks about an integrality gap; and [online bin packing](318-online-bin-packing-optimal-ratio.md), which asks for an online competitive ratio. The probability, counting and entropy formulations above are one problem. Source versions, theorem-scope comparisons, access limits and the separated adversarial self-review are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/subset-sum-support-concentration.json).
