# 639. A limiting law for maximal persistence in random clique complexes

**Area:** Applied topology / stochastic topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-09-24

## Problem statement

Assign independent uniform random variables $`U_e\in[0,1]`$ to the edges of the complete graph on $`n`$ vertices. Let $`X_n(p)`$ be the clique complex of the graph with edges $`U_e\le p`$. Fix $`k\ge1`$ and compute persistent homology over $`\mathbb Q`$. For its positive-length barcode intervals $`[b,d)`$, put

```math
M_k(n)=\max d/b,
```

with $`M_k(n)=0`$ if that barcode is empty. Define

```math
f_k(n)=n^{1/[k(k+1)]}(\log n)^{1/(k+1)}.
```

Does there exist a probability distribution $`\mu_k`$ on $`\mathbb R`$ and a constant $`\lambda_k>0`$ such that

```math
\frac{M_k(n)}{f_k(n)}\xrightarrow{\mathrm d}\mu_k,
\qquad \mu_k([\lambda_k,\infty))=1?
```

Prove this assertion or give a counterexample. The dimension $`k`$ stays fixed as $`n\to\infty`$; no particular named distribution is prescribed.

## Application

The law would calibrate the longest-lived topological features produced by an independent-edge null model, helping distinguish random network structure from signal.

## References

1. A. Ababneh and M. Kahle, [Maximal persistence in random clique complexes](https://doi.org/10.1007/s41468-023-00131-y), Journal of Applied and Computational Topology **8** (2024), 1449–1463, Conjecture 5.2; §4 definitions and Theorem 4.1. [Author preprint](https://arxiv.org/abs/2209.05713).

## Status review

**Known cases:** For every fixed $`\varepsilon>0`$, $`n^{1/[k(k+1)]-\varepsilon}\le M_k(n)\le n^{1/[k(k+1)]+\varepsilon}`$ with probability tending to one. More precisely, the source proves an upper bound $`f_k(n)\omega(n)`$ and a lower bound $`n^{1/[k(k+1)]}/\omega(n)`$ for every positive $`\omega(n)\to\infty`$.

**Remaining target:** Distributional convergence under the displayed logarithmic normalization, with a limiting law bounded away from zero.

Current primary-source and announcement searches found no matching resolution. Random geometric filtrations and deterministic torus-grid filtrations have different probability models and do not settle this conjecture. The weaker logarithmic lower bound in Conjecture 5.1 is kept within this problem's context rather than counted separately.
