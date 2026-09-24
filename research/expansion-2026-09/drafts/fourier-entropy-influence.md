# The Fourier entropy–influence conjecture

**Integrated:** [504 — canonical entry](../../../problems/496-fourier-entropy-influence.md) on 2026-09-23. This file preserves the September 19 research draft; use the canonical page for current status and wording.

**Area:** Boolean models, statistical learning and Fourier analysis

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-19

## Problem statement

For an integer $n\ge1$, let $f:\{-1,1\}^n\to\{-1,1\}$ be any Boolean-valued function, and write $[n]=\{1,\ldots,n\}$. Use the uniform probability measure on the cube. For every subset $S\subseteq[n]$, define

$$
\chi_S(x)=\prod_{i\in S}x_i,\qquad
\widehat f(S)=2^{-n}\sum_{x\in\{-1,1\}^n}f(x)\chi_S(x),
$$

with $\chi_\varnothing=1$. Then $f=\sum_{S\subseteq[n]}\widehat f(S)\chi_S$ and $\sum_{S\subseteq[n]}\widehat f(S)^2=1$. Thus $p_f(S)=\widehat f(S)^2$ is a probability distribution on subsets of $[n]$. Its Shannon entropy in bits is

$$
H_{\mathrm F}(f)=
\sum_{S\subseteq[n]}\widehat f(S)^2
\log_2\frac{1}{\widehat f(S)^2},
$$

where a summand with $\widehat f(S)=0$ is zero. The empty subset is included.

For a uniform random input $X$, let $X^{(i)}$ be $X$ with its $i$th coordinate flipped. Define the individual and total influences by

$$
\begin{aligned}
\mathop{\mathrm{Inf}}\nolimits_i(f)
&=\Pr\{f(X)\ne f(X^{(i)})\}
=\sum_{S\ni i}\widehat f(S)^2,\\
I(f)&=\sum_{i=1}^n\mathop{\mathrm{Inf}}\nolimits_i(f)
=\sum_{S\subseteq[n]}|S|\widehat f(S)^2.
\end{aligned}
$$

Does there exist a finite universal constant $C>0$, independent of $n$ and $f$, such that

$$
H_{\mathrm F}(f)\le C I(f)
$$

for every such function? This is the Fourier entropy–influence conjecture of Friedgut and Kalai. No balance, monotonicity, symmetry or degree bound is imposed. Constant functions satisfy the inequality with both sides zero. The question asks for some universal constant, rather than prescribing its sharp numerical value. [1–3]

## Applied significance

Boolean functions model classification rules and decisions from binary features. Total influence measures the expected number of single-feature flips that change the decision at a random input. Fourier entropy measures how broadly the model's squared coefficients are distributed among parity interactions. The conjecture would connect stability under these local changes to the existence of a compact spectral approximation.

Specifically, for every $0<\varepsilon<1$, it would imply that some collection $\mathcal A$ of at most $2^{C I(f)/\varepsilon}$ subsets satisfies

$$
\mathbb E\left[
\left(f(X)-\sum_{S\in\mathcal A}\widehat f(S)\chi_S(X)\right)^2
\right]\le\varepsilon.
$$

This follows from the entropy concentration argument in [2, equation (1.2)] and Parseval's identity. It bounds representation size; locating the coefficients is an additional computational task. For DNF rules, the conjecture also implies a spectral-concentration form of Mansour's conjecture, with consequences for agnostic learning at fixed accuracy using membership queries—chosen inputs whose labels can be requested. This consequence does not provide the passive examples-only learner sought in entry 329. [1, §1.1; 5, §1.3.1]

## References

1. Ryan O'Donnell, John Wright and Yuan Zhou, *The Fourier Entropy–Influence Conjecture for Certain Classes of Boolean Functions*, ICALP 2011, LNCS **6755**, 330–341, DOI 10.1007/978-3-642-22006-7_28. [Author manuscript](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf), §§1–2, unnumbered conjecture and Theorems 1–3; definitions on author-PDF pp.4–5.
2. Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica **45** (2025), Article 4; published online December 20, 2024. [Full published text](https://link.springer.com/article/10.1007/s00493-024-00133-z), Conjecture 1.1, equation (1.2), Theorem 1 and §3. The [December 10, 2025 preprint revision](https://arxiv.org/html/2312.08271v2) adds a note acknowledging related prior work [4].
3. María José González, Paul MacManus and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, [arXiv:2606.00246v2](https://arxiv.org/html/2606.00246v2), June 9, 2026, preprint. §1; Proposition 5.1, Definition 5.2, Theorem 5.3, Definitions 6.2 and 6.7, and Theorems 6.3 and 6.8.
4. Nathan Keller, Elchanan Mossel and Tomer Schlank, *A Note on the Entropy/Influence Conjecture*, [arXiv:1105.2651v1](https://arxiv.org/pdf/1105.2651v1), submitted May 13, 2011; the retrieved PDF carries an internal date of October 22, 2018. Definitions 1.1–1.3, Conjecture 1.5, and Claim 4.1 with its proof, internal p.10.
5. Esty Kelman, Guy Kindler, Noam Lifshitz, Dor Minzer and Muli Safra, *Towards a Proof of the Fourier–Entropy Conjecture?*, [arXiv:1911.10579v2](https://arxiv.org/pdf/1911.10579v2), May 7, 2020, inspected preprint version. §§1.1–1.3, Theorems 1.1–1.3, internal pp.3–5.
6. Guy Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, [arXiv:1806.03646v2](https://arxiv.org/pdf/1806.03646v2), January 24, 2019. Conjecture 1, Theorems 2–6 and 9; §2.1 defines read-$k$ decision trees.
7. Joseph Slote, Alexander Volberg and Haonan Zhang, *Tightness of and counterexamples to several quantum estimates*, [arXiv:2608.04411v2](https://arxiv.org/html/2608.04411v2), August 6, 2026, preprint. §6, particularly §§6.3–6.6, Proposition 3 and equations (84)–(85).
8. Peijie Li and Guangyue Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof*, [arXiv:2512.03117](https://arxiv.org/abs/2512.03117), withdrawn. The December 9, 2025 version-3 notice attributes the result to the earlier Claim 4.1 in [4].
9. Joseph Slote, *Dense Hamiltonians at the Parseval Limit: The Noncommutative BH Constant is Exponential and the Quantum FEI Conjecture is False*, [arXiv:2608.01424v1](https://arxiv.org/html/2608.01424v1), August 2, 2026, preprint. Theorem 1 and §3, especially Conjecture 4 and Theorem 5.

## Status review

The June 2026 manuscript [3] retains the general classical conjecture, and the independently authored August paper [7, §6] explicitly describes it as open while addressing its quantum extension. The September 19 check covered names and aliases, the spectral-entropy/average-sensitivity formulation, recent and unrestricted-date searches, author-hosted texts, revisions, corrections and potential resolutions.

The symmetric-function and read-once decision-tree theorems in [1] restrict the input function. The improved read-$k$ bound in [6, Theorem 9] has a constant of order $\sqrt{k}$, where each variable may label at most $k$ nodes in the entire tree; it does not give a universal constant when $k$ grows. The extremal-regime theorems in [6] likewise retain their quantitative restrictions.

General estimates still leave extra terms: the coordinate-entropy bound [4, Claim 4.1] and Han's bound [2, Theorem 1] can exceed a constant multiple of total influence. The spectral result [5, Theorem 1.3] retains logarithmic degree weights; its concentration theorem retains logarithmic normalized-influence dependence. Neither proves the stated inequality for every function.

The new families in [3] have explicit splitting/separation hypotheses. Its Proposition 5.1 defeats a stronger auxiliary inequality for a particular splitting variable; Theorem 5.3 verifies FEI for the constructed family using another splitting strategy. This is not a counterexample to FEI. The counterexamples in [7, 9] use complex phases or Hermitian quantum operators. Those outputs are outside the scalar Boolean class here. The withdrawal in [8] records prior discovery, not a disproof of the classical conjecture.

The [evidence record](../candidates/fourier-entropy-influence.json) contains the detailed comparisons and access limits. The original 1996 publisher PDF was inaccessible; the complete explicit restatements in [1–4] were inspected. Research was followed by a separated adversarial self-review. No independent agent or human review, or certification of the cited proofs, is claimed.

[Entry 330](../../../problems/330-aaronson-ambainis-influence.md) seeks one influential coordinate of a bounded real low-degree polynomial. The [DNF-learning question](../../../problems/329-classical-uniform-dnf-learning.md) asks for an algorithm with a specified data-access model. These are distinct from the spectral-entropy inequality. Equivalent formulations and its restricted cases receive no additional entries.
