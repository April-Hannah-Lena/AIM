# 213. Composing two PPT channels destroys all entanglement

**Area:** Quantum information; repeater channels

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

Let $d\ge2$ and let $\Phi,\Psi:M_d(\mathbb C)\to M_d(\mathbb C)$ be completely positive trace-preserving maps. Assume that $T\circ\Phi$ and $T\circ\Psi$ are also completely positive, where $T$ is matrix transposition in a fixed basis. Complete positivity means that $\operatorname{id}_r\otimes\Phi$ preserves positive semidefiniteness for every $r\ge1$, and similarly for the other maps.

Must $\Psi\circ\Phi$ be entanglement breaking? Explicitly, for every density operator $\rho$ on $\mathbb C^d\otimes\mathbb C^d$, must
$$(\operatorname{id}_d\otimes(\Psi\circ\Phi))(\rho)=\sum_{j=1}^k p_j\alpha_j\otimes\beta_j$$
for some finite $k$, probabilities $p_j$, and density operators $\alpha_j,\beta_j$?

## Application

This determines whether a pair of noisy quantum links with positive partial transpose can retain terminal entanglement, a basic limitation for quantum repeater designs.

## References

1. Matthias Christandl, Alexander Müller-Hermes, and Michael M. Wolf, [When Do Composed Maps Become Entanglement Breaking?](https://arxiv.org/abs/1807.01266), *Ann. Henri Poincaré* 20 (2019). Introduction and the discussion of the PPT-squared conjecture establish the formulation and dimension-three result.
2. Junhyeong An and Soojoon Lee, [Beyond the Positive Partial Transpose Squared Conjecture: The Qutrit Case](https://arxiv.org/abs/2607.15947), preprint, 17 July 2026. Introduction and Section II, Conjecture 2, explicitly leave higher dimensions open.

## Status review

**Known cases:** The PPT-composition conclusion is established in complex dimension three, the qutrit case.

**Remaining target:** The entanglement-breaking conclusion for compositions of all such channels in arbitrary complex dimension.

**Literature check:** Open in cited literature; no later resolution located.

The July 2026 paper confirms the higher-dimensional conjecture remains open. Its new composition theorems concern qutrits and additional map classes. The question here is over complex Hilbert spaces; counterexamples to real-Hilbert-space analogues do not settle it.

**Search audit:** Queries: “PPT squared conjecture proof counterexample 2026”, “Christandl Muller Hermes Wolf PPT composition”, with the July 2026 qutrit paper checked. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
