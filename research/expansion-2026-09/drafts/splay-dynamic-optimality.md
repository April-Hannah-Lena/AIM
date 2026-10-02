# Dynamic optimality of splay trees

**Area:** Adaptive data structures and online computation

**Status:** Accepted; published as entry 308

**Last checked:** 2026-09-17

## Problem statement

For $`n\ge1`$, store the ordered keys $`\{1,\ldots,n\}`$ in a binary search tree $`T`$. A request sequence is any finite word $`X=(x_1,\ldots,x_m)`$ of these keys. Use the root-access model: before serving a request, rotate its key to the root, paying one per rotation and one for the access. A rotation promotes a child above its parent while preserving the ordering of the keys. No keys are inserted or deleted.

The bottom-up splay rule moves the requested node $`x`$ to the root as follows. If its parent is the root, rotate $`x`$ once. Otherwise, write $`p`$ for its parent and $`g`$ for its grandparent. If $`x,p`$ are both left children or both right children, rotate $`p`$ above $`g`$, then $`x`$ above $`p`$. If their orientations differ, rotate $`x`$ twice. Repeat until $`x`$ is the root.

Let $`S(T,X)`$ be its total cost. Let $`\mathop{\mathrm{OPT}}\nolimits(T,X)`$ be the least cost of any rotation schedule serving $`X`$ from the same initial tree, allowed full knowledge of $`X`$. Is there an absolute constant $`C<\infty`$ and a finite function $`f:\mathbb N\to[0,\infty)`$ such that

```math
S(T,X)\le C\mathop{\mathrm{OPT}}\nolimits(T,X)+f(n)
```

for every $`n`$, every initial tree $`T`$, and every finite request sequence $`X`$? The additive term depends only on the number of keys; $`C`$ is independent of that number and of the requests. This is the splay-tree dynamic optimality conjecture with an allowed initialization cost. The root-access and usual search-depth cost models are equivalent up to absolute factors.

## Applied significance

An ordered dictionary must serve lookups whose frequencies and locality can change over time. This question asks whether one simple self-adjusting rule adapts as well, up to a universal factor, as a search tree designed with advance knowledge of the entire workload. It is a foundational performance question for comparison-based data structures.

## References

1. John Iacono, *In pursuit of the dynamic optimality conjecture*, [arXiv:1306.0207v1](https://arxiv.org/abs/1306.0207v1), 2013, §1, Conjecture 1 and the following definition of dynamic optimality.
2. Petr Chmel, Bernhard Haeupler, Richard Hladík, Michal Koucký, Antti Roeyskoe, Václav Rozhoň, Ondřej Sladký and Robert E. Tarjan, *Splay trees are almost dynamically optimal*, [arXiv:2607.18498v1](https://arxiv.org/html/2607.18498v1), July 20, 2026 preprint, §§1–2, §5 Theorem 1 and Appendix B Lemma 37.
3. Luís M. S. Russo, *A Study on Splay Trees*, Theoretical Computer Science 776 (2019), 1–18, [published article](https://doi.org/10.1016/j.tcs.2018.12.020); [author manuscript, v3](https://arxiv.org/pdf/1511.03148v3), revised April 7, 2020, Conjecture 3.1 and Theorem 4.6.
4. J. Ian Munro, Richard Peng, Sebastian Wild and Lingyi Zhang, *Dynamic Optimality Refuted – For Tournament Heaps*, [author manuscript](https://www.wild-inter.net/publications/unordered-dynamic-optimality.pdf), August 10, 2019, Definition 1.1 and Theorems 1.2–1.3.

## Status review

The July 2026 preprint reports a bound $`O((\mathop{\mathrm{OPT}}\nolimits+n)\log\log n\,\log^2\log\log n)`$. Its competitive factor still grows with $`n`$. Russo's constant-factor comparison assumes the unproved regular-access conjecture. The tournament-heap refutation changes the allowed operations and removes the ordered-search model; it is not a refutation for splay trees.

The September 17 review searched the conjecture and aliases, authors, constant competitiveness, proofs and counterexamples, recent and unrestricted dates, corrections and version histories. The [evidence ledger](../candidates/splay-dynamic-optimality.json) records the source comparisons, initialization convention and duplicate review. A constant factor for this particular algorithm remains the requested conclusion; existence of some dynamically optimal search tree is not counted as a second entry here.

A clearly separated adversarial self-pass passed on September 17. Integrated as [entry 306](../../../problems/305-splay-dynamic-optimality.md) after the September 17, 2026 batch refresh.
