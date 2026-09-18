# Polynomial-time DNF learning from uniform random examples

**Area:** Statistical learning, Boolean rules and computational complexity

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-18

## Problem statement

For positive integers $n,s$, let $\mathcal D_{n,s}$ be the Boolean functions on $\{0,1\}^n$ representable as a disjunction of at most $s$ terms. Each term is a conjunction of literals, and a literal is either a coordinate $x_j$ or its negation $1-x_j$. Term lengths, overlaps and signs are unrestricted.

Does there exist a classical randomized algorithm $A$ and a polynomial $p$ with the following property? For every $n,s$, every unknown $f\in\mathcal D_{n,s}$, and every $\varepsilon,\delta\in(0,1/2)$, the algorithm is given $n,s,\varepsilon,\delta$ and access only to independent labeled examples
$$
(X,f(X)),\qquad X\sim\operatorname{Unif}(\{0,1\}^n).
$$
Within time at most
$$
p\!\left(n,s,\varepsilon^{-1},\log(1/\delta)\right),
$$
it outputs a description of a Boolean function $h:\{0,1\}^n\to\{0,1\}$ satisfying
$$
\Pr_{\text{training examples and algorithm}}\!
\left[
\Pr_{X\sim\operatorname{Unif}(\{0,1\}^n)}
\{h(X)\ne f(X)\}\le\varepsilon
\right]\ge1-\delta?
$$

The inner probability uses a fresh input. Reading examples and all preprocessing count toward the runtime; evaluating the resulting hypothesis on any input must also take polynomial time in the same parameters. The algorithm receives a size bound, not a formula for $f$. It may output a hypothesis outside the DNF class. Neither chosen label queries nor quantum examples are available. This is the noiseless, examples-only uniform-distribution PAC-learning question. [1–3]

## Applied significance

DNFs express rules in which any of several combinations of binary features can trigger a classification. The problem tests whether a compact rule model can always be converted into an efficiently learned predictor from passive observations. Its difficulty is computational: an elementary count of the possible formulas gives a polynomial sample bound for exhaustive search, but that search need not be efficient. The uniform-input assumption is an idealized benchmark; a solution would not automatically handle arbitrary feature distributions or recover an interpretable DNF representation. The role of DNFs as a model for knowledge representation is discussed in [3, §1.1].

## References

1. Liu Yang, Avrim Blum and Jaime Carbonell, *Learnability of DNF with Representation-Specific Queries*, ITCS 2013. [Author manuscript](https://www.cs.cmu.edu/~liuy/dnf_queries.pdf), §§1.1–1.2 and Theorem 3.3; publication identity checked on the [author's publication page](https://www.cs.cmu.edu/~liuy/).
2. Vitaly Feldman, *Learning DNF Expressions from Fourier Spectrum*, COLT 2012; [author manuscript, arXiv:1203.0594v3](https://arxiv.org/pdf/1203.0594v3), revised April 3, 2013. §2, p. 5, defines the learning and size conventions; §5, Corollary 5.1, Definition 5.2 and Theorems 5.4–5.5 distinguish query access, smoothed distributions and monotone formulas.
3. Josh Alman, Shivam Nadimpalli, Shyamal Patel and Rocco A. Servedio, *DNF Learning via Locally Mixing Random Walks*, [arXiv:2505.18839v1](https://arxiv.org/html/2505.18839v1), May 24, 2025, preprint. §§1.1–1.2, Theorems 1 and 3.
4. Mohsen Heidari and Roni Khardon, *Learning DNF through Generalized Fourier Representations*, [COLT 2025, PMLR 291, 2788–2804](https://proceedings.mlr.press/v291/heidari25a.html). The checked extended manuscript is [arXiv:2506.01075v2](https://arxiv.org/pdf/2506.01075v2), revised June 2, 2026: §2 Definition 1, §9.2 Corollary 47, and Appendix A.2 Lemma 71.
5. Varun Kanade, Andrea Rocchetto and Simone Severini, *Learning DNFs under product distributions via μ-biased quantum Fourier sampling*, [arXiv:1802.05690v3](https://arxiv.org/html/1802.05690), revised November 25, 2019, preprint version. §§1 and 2.5, Theorem 6 and Corollary 7.
6. Gautam Chandrasekaran, Georgios Gkrinias, Adam R. Klivans, Konstantinos Stavropoulos and Arsen Vasilyan, *Iterative Chow Filtering for Learning with Distribution Shift*, [arXiv:2605.17251v1](https://arxiv.org/html/2605.17251v1), May 17, 2026, preprint. §1, Definition 1.1, Table 1 and Theorem 4.1.
7. Sagnik Chatterjee, *The Quantum Learning Menagerie (A survey on Quantum learning for Classical concepts)*, [arXiv:2602.01054v1](https://arxiv.org/html/2602.01054v1), February 1, 2026, preprint survey, §5.5.

## Status review

Open in cited literature; no later resolution located as of 2026-09-18. Source [1, §1.2] explicitly poses the uniform examples-only gap. Independent sources [5, §1] and [7, §5.5] distinguish it from efficient learning with additional access. The September 18 review searched names, mathematical and oracle wording, recent work, author pages, versions, corrections and proof/counterexample claims.

The general examples-only bound recalled in [3, §1.1] has runtime $n^{O(\log(s/\varepsilon))}$, with confidence amplification. The 2026 distribution-shift result [6] also retains quasipolynomial dependence for DNFs. Setting its training and test distributions equal and treating abstentions as errors does not turn its displayed runtime into a polynomial.

The polynomial algorithms in [2, 4] use membership queries; [5] uses coherent quantum examples. The numerical similarity queries in [1] supply information beyond ordinary labels. Smoothed-distribution learning in [2] succeeds with high probability over a random perturbation of the input law; that guarantee does not include every fixed law, such as the uniform one. The new local-mixing algorithms in [3] use queries and remain quasipolynomial; their full learning theorem also assumes equal term lengths.

The [evidence record](../candidates/classical-uniform-dnf-learning.json) additionally compares random-target algorithms, local queries, positive-only lower bounds and conditional distribution-free hardness. None supplies a matching result for the stated model. Historical results are sometimes checked through explicit scholarly restatements; complete proofs have not been independently certified.

This differs from noisy-parity recovery in [entry 317](../../../problems/317-learning-parity-noise.md) and runtime-unrestricted sample compression in [entry 318](../../../problems/318-linear-sample-compression.md). All DNF sizes are one problem family; monotone, bounded-width and quantum variants receive no additional count. The separated A38 adversarial self-pass passed on September 18. A fresh status and upstream-duplicate check remains required before batch integration.
