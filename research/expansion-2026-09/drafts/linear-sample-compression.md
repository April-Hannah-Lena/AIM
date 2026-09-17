# Linear-size sample compression for binary concept classes

**Area:** Statistical learning and combinatorial dimension

**Status:** Accepted; published as entry 318

**Last checked:** 2026-09-17

## Problem statement

Let $X$ be a finite set and let $\varnothing\ne\mathcal C\subseteq\{0,1\}^{X}$. A set $B\subseteq X$ is shattered if every binary labeling of $B$ is the restriction of a member of $\mathcal C$; write $d$ for the largest size of such a set. Assume $d\ge1$.

Let $\mathcal S_{\mathcal C}$ consist of labeled samples $S\subseteq X\times\{0,1\}$ consistent with some $c\in\mathcal C$. A compression scheme consists of maps

$$
\kappa:\mathcal S_{\mathcal C}\longrightarrow
\mathcal S_{\mathcal C}\times\{0,1\}^{*},\qquad
\rho:\mathcal S_{\mathcal C}\times\{0,1\}^{*}
\longrightarrow\{0,1\}^{X}.
$$

For every $S$, writing $\kappa(S)=(T,b)$, require $T\subseteq S$ and $\rho(T,b)(x)=y$ for all $(x,y)\in S$. Here $b$ is a finite bitstring. The size of the scheme is

$$
\max_{S\in\mathcal S_{\mathcal C}}|T(S)|
+\max_{S\in\mathcal S_{\mathcal C}}|b(S)|.
$$

Does a universal constant $K$ exist such that every such class admits a scheme of size at most $Kd$? The maps may depend on $X$ and $\mathcal C$, but the same maps must serve every realizable sample. No runtime bound is imposed. The reconstructor receives only $(T,b)$ and may output a function outside $\mathcal C$. The retained sample is an unordered set; additional ordering information must be encoded in $b$.

## Applied significance

Sample compression models learning from a small selection of observed examples. Such schemes yield generalization guarantees; a linear bound would tie the retained information directly to VC dimension, independently of the original sample size. This is an existence question, so efficient implementation would require further work.

## References

1. Romain Bourneuf, Jędrzej Hodor, Piotr Micek and Clément Rambaud, *Sample compression schemes for balls in structurally sparse graphs*, [arXiv:2604.02949v1](https://arxiv.org/html/2604.02949v1), April 3, 2026 preprint, §1 definitions and conjecture; §2.1 distinguishes array schemes.
2. Idan Attias, Steve Hanneke and Arvind Ramaswami, *Sample Compression Scheme Reductions*, PMLR 272 (2025), 134–162, [publication record](https://proceedings.mlr.press/v272/attias25a.html); [author manuscript v3](https://arxiv.org/pdf/2410.13012v3), §2 Definition 2.1 and conjecture.
3. Shay Moran and Amir Yehudayoff, *Sample compression schemes for VC classes*, JACM 63(3) (2016), [author manuscript](https://arxiv.org/pdf/1503.06960), §1.2 and Theorems 1.3–1.4.
4. Zachary Chase, Bogdan Chornomaz, Steve Hanneke, Shay Moran and Amir Yehudayoff, *Dual VC Dimension Obstructs Sample Compression by Embeddings*, [arXiv:2405.17120v1](https://arxiv.org/html/2405.17120v1), §1.2 Conjecture 1 and Theorem A.

## Status review

The April 2026 graph paper explicitly retains the linear-size conjecture with the set-and-bitstring convention used here. Attias–Hanneke–Ramaswami independently discuss the unresolved binary conjecture. Moran–Yehudayoff prove a general exponential bound in $d$, already independent of sample size; the remaining issue is linear dependence on dimension.

The embedding obstruction rules out one proposed route through extremal classes, rather than all compression maps. Results for graph balls and complexes of oriented matroids impose structural hypotheses. The Pálvölgyi–Tardos counterexample concerns unlabeled compression of size exactly $d$. A 2026 negative result additionally requires monotonicity under inserted examples. Neither is a counterexample to this formulation.

The apparent March 2026 compression claim, later retitled, is [withdrawn in arXiv v4](https://arxiv.org/abs/2603.23561), with the authors reporting an incorrect proof of Lemma 2. Its withdrawal is not an independent verification of the argument. Full scope comparisons and source limitations are in the [evidence ledger](../candidates/linear-sample-compression.json). This family is counted once, without separate entries for stronger or restricted compression variants.

A clearly separated adversarial self-pass passed on September 17. Integrated as [entry 318](../../../problems/318-linear-sample-compression.md) after the September 17, 2026 batch refresh.
