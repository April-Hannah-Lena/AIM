# 297. Balanced Gaussian simplex noise stability for four or more classes

**Area:** Gaussian geometry and noise robustness

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $q\ge4$, $n\ge q-1$ and $0<\rho<1$. Let $X,Z$ be independent standard Gaussian vectors in $\mathbb R^n$ and put $Y=\rho X+\sqrt{1-\rho^2}Z$. For a measurable partition $\mathcal A=(A_1,\ldots,A_q)$ satisfying $\gamma_n(A_i)=1/q$, define

$$
\mathop{\mathrm{Stab}}\nolimits_{\rho}(\mathcal A)
=\sum_{i=1}^{q}\mathbb P\{X\in A_i,\ Y\in A_i\}.
$$

Choose unit vectors $u_1,\ldots,u_q\in\mathbb R^n$ with $\langle u_i,u_j\rangle=-1/(q-1)$ for $i\ne j$, and define the regular-simplex cone partition $\mathcal S=(S_1,\ldots,S_q)$ by

$$
S_i=\{x:\langle u_i,x\rangle\ge\langle u_j,x\rangle
\text{ for every }j\}.
$$

Ties may be assigned arbitrarily, since their Gaussian measure is zero. Does every such balanced partition satisfy

$$
\mathop{\mathrm{Stab}}\nolimits_{\rho}(\mathcal A)
\le\mathop{\mathrm{Stab}}\nolimits_{\rho}(\mathcal S)?
$$

The question covers all measurable partitions and every fixed positive correlation. No smoothness or hyperstability hypothesis is imposed. This is the $q\ge4$ part of the balanced, positive-correlation standard simplex conjecture.

## Application

Assigning label $i$ to points in $A_i$ gives a balanced classification rule for Gaussian data. The displayed objective is exactly the probability that the label survives Gaussian noise with correlation $\rho$. The conjecture would identify an optimal rule in this model. The literature also connects the Gaussian problem, through an invariance principle, to the robustness of voting rules with many voters, small individual influences and equal outcome probabilities.

## References

1. M. Isaksson and E. Mossel, [*Maximally Stable Gaussian Partitions with Discrete Applications*](https://arxiv.org/pdf/0903.3362v3), arXiv:0903.3362v3, August 3, 2009; Definition 1.3 and Conjecture 1.4, p. 2.
2. S. Heilman and A. Tarter, [*Three candidate plurality is stablest for small correlations*](https://doi.org/10.1017/fms.2021.56), Forum of Mathematics, Sigma **9** (2021), e65; §§1.1–1.4, especially Conjecture 1.6 and Theorems 1.9–1.10.
3. S. Heilman, [*Hyperstable Sets with Voting and Algorithmic Hardness Applications*](https://arxiv.org/html/2209.11216v1), arXiv:2209.11216v1, September 22, 2022; Definition 1.3 and Theorem 1.5.
4. S. Heilman, [*Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT*](https://arxiv.org/pdf/2608.00333v1), arXiv:2608.00333v1, submitted July 31, 2026; Appendix A, Theorem A.1, printed p. 38. The served manuscript bears August 24, 2026.
5. S. Heilman, E. Mossel and J. Neeman, [*Standard Simplices and Pluralities are Not the Most Noise Stable*](https://arxiv.org/pdf/1403.0885v3), arXiv:1403.0885v3, July 9, 2014; Theorem 2.6, printed p. 4.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 17, 2026 review searched standard-simplex and plurality-is-stablest aliases, balanced Gaussian partitions, four-class formulations, proof/disproof terms, 2025–2026 developments, unrestricted results, corrections and version histories. The Isaksson–Mossel conjecture and the independent Heilman–Tarter formulation include the statement above.

Heilman–Tarter reduce the positive-noise maximization problem to $q-1$ dimensions; the reduced partition's optimal shape remains to be established. Heilman's hyperstability theorem covers four classes only under an additional variational assumption. His 2026 Theorem A.1 concerns exactly three classes and $0<\rho\le2/5$, so it does not cover this entry.

Heilman–Mossel–Neeman's counterexamples require unequal Gaussian masses. Their theorem explicitly excludes the balanced vector used here. A 2026 manuscript by Mulgund claiming the weak simplex conjecture concerns maximum-likelihood decoding of a finite Gaussian-channel codebook. Its Corollary 2.6 does not optimize arbitrary equal-mass partitions of a correlated Gaussian pair.

The [evidence record](../research/expansion-2026-09/candidates/gaussian-simplex.json) gives the full scope comparisons, source-version date discrepancies, duplicate screening and separate adversarial self-review. Discrete plurality formulations and separate values of $q$ are not counted as additional problems. This finite-correlation Gaussian objective also differs from the catalogue's Euclidean perimeter and binary mutual-information questions.
