# 538. Minimax estimation of topic distributions with weak sparsity

**Area:** Statistical inference and topic models

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix an integer $`K\ge2`$, $`q\in(0,1)`$ and positive constants $`c,\kappa`$. Observe independent word-count vectors

```math
X_i\sim\mathop{\mathrm{Multinomial}}\nolimits(N,Aw_i),\qquad i=1,\ldots,n,
```

where $`N\ge2`$, $`A\in[0,1]^{p\times K}`$ and $`W=(w_1,\ldots,w_n)\in[0,1]^{K\times n}`$. Every column of $`A`$ and $`W`$ sums to one. Both matrices are unknown; $`K`$ is known and fixed.

Let $`\mathcal F_{n,N,p}(q,s;c,\kappa)`$ consist of these pairs $`(A,W)`$ satisfying the following conditions. With $`\sigma_K`$ denoting the smallest singular value of a matrix with $`K`$ columns or rows, require

```math
\sigma_K(A)\ge c\sqrt K,\qquad
\lambda_{\min}(WW^T/n)\ge c,\qquad
\min_{k,l}(A^TA)_{kl}\ge c.
```

For each topic $`k`$, there must be an anchor word $`j_k`$ with $`A_{j_k k}>0`$ and $`A_{j_k l}=0`$ for $`l\ne k`$, whose average corpus frequency obeys

```math
\mu_{j_k}:=\frac1n\sum_{i=1}^n(AW)_{j_k i}
>\kappa\sqrt{\frac{\log(p\vee n)}{nN}}.
```

Finally, writing the entries in each column in decreasing order as $`A_{(1)k}\ge\cdots\ge A_{(p)k}`$, impose weak sparsity:

```math
\max_{k\le K}\max_{j\le p}j\,A_{(j)k}^{\,q}\le s.
```

This permits arbitrarily many small positive entries. It is a bound on ordered decay, not a bound on the number of nonzero entries or on $`\sum_j A_{jk}^q`$.

Determine, up to multiplicative constants independent of $`n,N,p,s`$, the minimax risk

```math
R^*_{n,N,p}(q,s;c,\kappa)
=\inf_{\widehat A}\sup_{(A,W)\in\mathcal F_{n,N,p}(q,s;c,\kappa)}
\mathbb E_{A,W}\!\left[\min_{\pi\in S_K}
\sum_{k=1}^K\sum_{j=1}^p
|\widehat A_{jk}-A_{j,\pi(k)}|\right].
```

The infimum is over measurable estimators with probability-vector columns. Consider the parameter regimes where the class is nonempty, with $`K,q,c,\kappa`$ fixed and $`\kappa`$ sufficiently large as in the anchor-frequency condition of reference [1]. Establish matching upper and lower bounds, including the correct dependence on $`s`$ and any necessary logarithmic factors as the vocabulary size grows. The constants may depend on the fixed parameters.

## Application

Topic models infer word distributions from document collections. Weak sparsity models a vocabulary with a small number of common words and a long tail of rare ones. Sharp rates would quantify the data needed to recover these distributions and clarify the statistical cost of discarding rare words. Similar multinomial mixture models occur in microbiome and single-cell data analysis.

## References

1. H. Tran, Y. Liu and C. Donnat, [Sparse Topic Modeling via Spectral Decomposition and Thresholding](https://jmlr.org/beta/papers/v27/23-1344.html), *Journal of Machine Learning Research* 27(59) (2026), 1–76. Model §1.1; Assumptions 1–5; Theorem 19; open question in §5, p.33. [Preprint](https://arxiv.org/abs/2310.06730).
2. X. Bing, F. Bunea and M. Wegkamp, [Optimal Estimation of Sparse Topic Models](https://jmlr.org/papers/volume21/20-079/20-079.pdf), *JMLR* 21(177) (2020), 1–45, §2 and Theorem 1.
3. Y. Liu and C. Donnat, [Tensor Topic Modeling Via HOSVD](https://arxiv.org/abs/2501.00535), preprint (2025), §2.4, particularly the weak-sparsity bound in Lemma 2.2 of v1.

## Status review

Reference [1] explicitly leaves the sharp weak-sparsity rate open. Its Theorem 19 proves a high-probability upper bound of order

```math
\left(\frac{\log(p\vee n)}{nN}\right)^{1/4}
+s\left(\frac{\log(p\vee n)}{nN}\right)^{(1-q)/2}
```

in its stated consistency regime. This is not asserted to be minimax optimal, nor is its probability statement silently converted here into an expected-risk bound. The displayed minimax problem makes the statistical parameter class and permutation-invariant loss explicit; the paper's algorithmic vertex-hunting requirement is not a restriction on that parameter class.

The sparsity-dependent lower bounds in [2] concern the number of nonzero entries. They do not determine the rate over the ordered-decay class above. Reference [3] extends the upper-bound approach to tensor data; its weak-sparsity result supplies no matching lower bound for this target.

Checks on 24 September 2026 found no matching solution or announcement, and no equivalent repository entry.
