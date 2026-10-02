# 517. Tail bounds for causal equivalence classes of uniform random DAGs

**Area:** Statistical inference and random graphical models

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`\mathcal D_n`$ be the finite set of simple directed acyclic graphs on the labeled vertex set $`[n]=\{1,\ldots,n\}`$, and sample $`G_n`$ uniformly from $`\mathcal D_n`$. Its skeleton is the undirected graph obtained by forgetting edge orientations. A $`v`$-structure is a triple $`i\to k\leftarrow j`$ with $`i,j`$ nonadjacent. Define

```math
M(G)=\{H\in\mathcal D_n:H\text{ has the same skeleton and }v\text{-structures as }G\}.
```

This is the Markov equivalence class of $`G`$: its members encode the same conditional independence relations.

For every $`\varepsilon\in(0,1)`$, do constants $`C_\varepsilon<\infty`$ and $`t_\varepsilon>1`$ exist such that, simultaneously for every $`n\ge1`$ and every real $`t\ge t_\varepsilon`$,

```math
\Pr\bigl(|M(G_n)|>t\bigr)\le C_\varepsilon\exp\!\left[-(\log t)^{2-\varepsilon}\right]?
```

Here $`\log`$ is the natural logarithm. Prove this bound or refute it for some fixed $`\varepsilon`$. The distribution is uniform over labeled DAGs; uniform sampling of equivalence classes, or choosing an order and then random forward edges, gives different distributions.

## Application

Even exact observational independence information can leave several causal graphs indistinguishable. A tail bound quantifies how frequently this ambiguity becomes large under a specified model prior. It sharpens an average-size guarantee by controlling rare cases with many possible causal explanations. The uniform-DAG model chiefly describes dense graphs; the question does not claim the same behavior for sparse causal networks.

## References

1. D. Schmid and A. Sly, [On the number and size of Markov equivalence classes of random directed acyclic graphs](https://arxiv.org/abs/2209.04395v2), revised 28 September 2024, Theorem 1.1 and the open question immediately following it, p.2. [PDF](https://arxiv.org/pdf/2209.04395v2).
2. C. Squires and C. Uhler, [Causal Structure Learning: A Combinatorial Perspective](https://doi.org/10.1007/s10208-022-09581-9), Foundations of Computational Mathematics **23**, 1781–1815 (2023), p.1796, for the preceding average-size questions.
3. E. L. Jahn, F. Eberhardt and L. J. Schulman, [Lower Bounds on the Size of Markov Equivalence Classes](https://proceedings.mlr.press/v286/jahn25a.html), PMLR **286**, 1819–1836 (2025).

## Status review

Reference [1] proves a uniform tail estimate with power $`1+1/20`$ on $`\log t`$ and explicitly asks whether the power can approach two from below. It also proves positive limiting ratios for counts of equivalence classes and essential DAGs, so those older existence questions are not included here. The target is a stronger tail bound, without asserting the endpoint power two.

Reference [3] gives large-class lower bounds under sparse DAG priors and in mixed or cyclic graph models. These changed assumptions do not resolve the stated uniform-DAG question. Searches on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar records, found no matching resolution or announced solution.
