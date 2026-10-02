# 185. Liouville invariance under changing local moves on a Cayley network

**Area:** Random walks and network potential theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Gamma`$ be an infinite finitely generated group with identity $`e`$, and let $`S,T\subset\Gamma\setminus\{e\}`$ be finite symmetric generating sets: $`S=S^{-1}`$ and $`T=T^{-1}`$. For $`A\in\{S,T\}`$, the $`A`$-walk moves from $`g`$ to $`ga`$ with probability $`1/|A|`$ for each $`a\in A`$.

Call this walk Liouville if every bounded function $`f:\Gamma\to\mathbb R`$ satisfying

```math
f(g)=\frac1{|A|}\sum_{a\in A}f(ga)\qquad\text{for all }g\in\Gamma
```

is constant. Must the $`S`$-walk be Liouville if and only if the $`T`$-walk is Liouville, for every choice of $`(\Gamma,S,T)`$?

Both walks use uniform probabilities on symmetric generating sets. Arbitrary changes to the graph, directed steps, or unbounded jump distributions are outside this statement.

## Application

Bounded harmonic functions describe bounded equilibrium potentials for discrete diffusion. The question tests whether the existence of nonconstant equilibria, and the long-term information retained by a homogeneous network walk, depends on its microscopic choice of allowed moves.

## References

- [Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (Cambridge, 2016; paperback 2021), online revision of 19 August 2026](https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf), §14.7, printed p.507, paragraph following Theorem 14.49. Explicit generating-set question, attributed to Kaimanovich and Vershik.
- [Tianyi Zheng, *Asymptotic behaviors of random walks on countable groups*, ICM 2022; author manuscript](https://mathweb.ucsd.edu/~tiz161/Zheng_RWsurvey.pdf), §2.1, final paragraph. Discusses the broader unresolved stability question for symmetric finitely supported walks.
- [Nicolás Matte Bon, Volodymyr Nekrashevych and Tianyi Zheng, *Liouville property for groups and conformal dimension* (2023 preprint, revised February 2025)](https://arxiv.org/abs/2305.14545), Theorem 1.1. Establishes the Liouville property throughout a restricted class of contracting self-similar groups and walk measures.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The updated book explicitly retains invariance under changing generators as a question. Counterexamples on nontransitive networks do not provide two Cayley graphs of one group as required here. The 2025 theorem covers groups satisfying contraction and conformal-dimension hypotheses; it does not settle arbitrary finitely generated groups.

Search topics checked on 2026-09-08: Liouville change of generators 2026; Liouville generating set counterexample; Liouville Kaimanovich Vershik 2025 open problem; Liouville property finite support counterexample generators. No later resolution of the exact statement was located; this is a literature review, not a proof of openness.
