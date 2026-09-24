# 330. Aaronson–Ambainis influential-variable conjecture

**Area:** Boolean Fourier analysis and quantum query complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-18

## Problem statement

Let $n,d\ge1$ be integers and let $p:\{-1,1\}^n\to\mathbb R$ have the multilinear expansion
$$
p(x)=\sum_{S\subseteq[n]}\widehat p(S)\prod_{j\in S}x_j,
\qquad [n]=\{1,\ldots,n\},
$$
with $\widehat p(S)=0$ whenever $|S|>d$. Assume $|p(x)|\le1$ for every vertex of the cube. For a uniform random vertex $X$, write $X^{(i)}$ for $X$ with coordinate $i$ flipped, and define
$$
\operatorname{Var}(p)=\mathbb E\bigl[(p(X)-\mathbb E p(X))^2\bigr],
\qquad
\operatorname{Inf}_i(p)=\mathbb E\!\left[\left(\frac{p(X)-p(X^{(i)})}{2}\right)^2\right]
=\sum_{S\ni i}\widehat p(S)^2.
$$

Do there exist absolute constants $c,C>0$, independent of $n,d,p$, such that every such polynomial satisfies
$$
\max_{1\le i\le n}\operatorname{Inf}_i(p)
\ \ge\ c\left(\frac{\operatorname{Var}(p)}{d}\right)^C?
$$

This is a bound for all scalar-valued polynomials bounded on the cube, including nonhomogeneous ones. No matrix-input norm bound or special decomposition is assumed. Constant polynomials satisfy the inequality trivially. The statement asks for existence of an influential coordinate, without requiring an efficient procedure to find it. It is the normalization used in [2, Conjecture 1.2]; the $[0,1]$ formulation in [1] is equivalent by affine changes of input and output.

## Application

The acceptance probability of a quantum algorithm making $T$ queries to a binary input is a bounded polynomial of degree at most $2T$. The conjecture would let a classical decision tree repeatedly query influential coordinates and reduce the remaining uncertainty. As [1, Theorem 1.8] shows, it would imply that, for any positive errors $\varepsilon,\delta$, a deterministic classical algorithm can approximate that acceptance probability to additive error $\varepsilon$ on a $1-\delta$ fraction of uniformly distributed inputs using $\operatorname{poly}(T,1/\varepsilon,1/\delta)$ queries. This would constrain quantum advantage on typical inputs in the query model. It is a statement about access to input bits, not total runtime or simulation on every input. The reverse implication from the simulation conjecture to the influence conjecture is not asserted.

## References

1. Scott Aaronson and Andris Ambainis, *The Need for Structure in Quantum Speedups*, **Theory of Computing 10** (6), 133–166 (2014). [Published paper](https://theoryofcomputing.org/articles/v010a006/v010a006.pdf), §1.2, Conjecture 1.7 and Theorem 1.8, p. 139; §1.3 discusses influence conventions.
2. Francisco Escudero Gutiérrez, Miquel Saucedo and Carlos Palazuelos, *Optimal inequalities for completely bounded polynomials and the limitations of quantum query algorithms*, [arXiv:2609.05201v1](https://arxiv.org/html/2609.05201v1), September 4, 2026, preprint. Conjecture 1.2, Theorems 1.3–1.4, equation (6), and the comments following Corollary 1.5.
3. Guy Blanc, Jordan Docter, Carmen Strassle and Li-Yang Tan, *Quantum Speedups Require Structure or Depth*, [arXiv:2608.19158v1](https://arxiv.org/html/2608.19158v1), August 19, 2026, preprint version. §1 states the influence conjecture and its remaining exponential-degree bound; §2.2, Theorem 1, gives a simulation theorem with explicit round dependence.
4. Sreejata Kishor Bhattacharya, *Aaronson-Ambainis Conjecture Is True For Random Restrictions*, [arXiv:2402.13952v2](https://arxiv.org/abs/2402.13952v2), revised March 4, 2026; [ECCC revision 2 full text](https://eccc.weizmann.ac.il/report/2024/035/revision/2/download), Conjecture 1.3, Theorem 6.4 and §7. The conference version appeared as *Random Restrictions of Bounded Low Degree Polynomials Are Juntas*, [ITCS 2025, Article 17](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.17). These are versions of one work.
5. Francisco Escudero Gutiérrez, *Influences of Fourier Completely Bounded Polynomials and Classical Simulation of Quantum Algorithms*, [arXiv:2304.06713v2](https://arxiv.org/html/2304.06713), June 28, 2023, cited preprint version. Conjectures 1.2 and 1.5, Theorems 1.4, 1.6 and 1.8, and the norm comparison following Theorem 1.4.
6. Nathan Keller and Ohad Klein, *Quantum speedups need structure*, [arXiv:1911.03748](https://arxiv.org/abs/1911.03748). The November 2019 proof claim was withdrawn in version 2 on December 2, 2019; see the authors' correction notice.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-18. The review searched the name, influential-variable and bounded-polynomial formulations, authors, proof and counterexample claims, 2024–2026 work, unrestricted dates, and version/correction records. Independently authored [3, §1] and [4, Conjecture 1.3] corroborate the general problem, which [2] also explicitly retains in September 2026.

For unrestricted bounded polynomials, the general influence estimate recalled in [1, §1.2] and [3, §1] has inverse-exponential dependence on degree, rather than the desired inverse-polynomial dependence. The known Boolean-valued case does not cover arbitrary real values in $[-1,1]$. Theorems [2, 1.3] and [5, 1.6–1.8] impose completely bounded structure, with homogeneity in one case; scalar boundedness alone does not provide these stronger norm bounds. The general junta estimate [2, Theorem 1.4] depends on a sum of square roots of influences that can grow exponentially with degree.

In [4, Theorem 6.4], the influential coordinate belongs to a randomly restricted polynomial, with a variance hypothesis and a probability guarantee over restrictions. The coordinate can vary with the restriction; this is not a dimension-free bound for a fixed coordinate of the original polynomial. The algorithmic result [3, Theorem 1] is polynomial for a fixed number of query rounds, with constants and exponents depending on that number. It does not prove the unrestricted scalar-polynomial assertion. The authors of [6] explicitly withdrew their proof because a flaw in Lemma 5.3 invalidated the argument.

The [evidence record](../research/expansion-2026-09/candidates/aaronson-ambainis-influence.json) also compares the Liu–Mutreja parallel-query theorem, noncommutative counterexamples, unconditional randomness certification, and Agarwal–Ben-David's 2026 switching lemma. The latter still applies after a dimension-dependent random restriction. The others concern different models or consequences. Relevant full statements and scope discussions were read; complete proofs have not been independently certified. Historical bounds were checked through explicit scholarly restatements.

This differs from exact communication in [entry 293](293-log-rank.md), and efficient learning from examples in the [entry 329](329-classical-uniform-dnf-learning.md). Equivalent influence conventions and the simulation consequence receive no additional count. The separated A39 adversarial self-pass passed on September 18; no independent agent or human review is claimed.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../research/expansion-2026-09/batch-04-review.md). No matching later resolution was located.
