# 310. Equal-weight decomposition of quantum channels with bounded Kraus rank

**Area:** Quantum information and channel simulation

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-17

## Problem statement

Write $`M_d(\mathbb C)`$ for the complex $`d\times d`$ matrices. A quantum channel $`\Phi:M_m(\mathbb C)\to M_n(\mathbb C)`$ is a complex-linear map that preserves trace and is completely positive: $`\mathop{\mathrm{id}}\nolimits_k\otimes\Phi`$ preserves positive semidefiniteness for every integer $`k\ge1`$. Its Kraus rank is the least integer $`r`$ for which matrices $`A_1,\ldots,A_r\in\mathbb C^{n\times m}`$ satisfy

```math
\Phi(X)=\sum_{a=1}^r A_aXA_a^*,\qquad
\sum_{a=1}^r A_a^*A_a=I_m
\quad\text{for every }X\in M_m(\mathbb C).
```

For every pair of integers $`m,n\ge2`$ and every such channel $`\Phi`$, do there exist channels $`\Phi_1,\ldots,\Phi_n:M_m(\mathbb C)\to M_n(\mathbb C)`$ such that

```math
\Phi=\frac1n\sum_{j=1}^n\Phi_j,
\qquad \mathop{\mathrm{KrausRank}}\nolimits(\Phi_j)\le m\quad(1\le j\le n)?
```

Repeated channels are allowed. These rank-bounded channels are the generalized extreme points, meaning the closure of the extreme points of the convex set of channels; they need not themselves be extreme. The question requires exactly $`n`$ equal weights and exact equality of maps, with no unitality assumption. This is the strong Ruskai–Audenaert conjecture.

## Application

Quantum channels describe noisy quantum dynamics. Such a decomposition would implement any channel by choosing uniformly among $`n`$ simpler channels, each admitting an environment of dimension at most $`m`$ in a Stinespring implementation. This links classical randomness to the quantum resources needed for channel simulation. It is an existence question; an efficient procedure for finding the components is a further issue.

## References

1. Mary Beth Ruskai, *Some Open Problems in Quantum Information Theory*, [arXiv:0708.1902v1](https://arxiv.org/pdf/0708.1902v1), August 14, 2007. §1 Theorem 1 and §2 Conjectures 2–5. Conjecture 2 prints an inconsistent output-dimension rank bound; the input-dimension bound used here agrees with the adjacent dual/block formulations and the modern source below.
2. Raban Iten and Roger Colbeck, *Smooth manifold structure for extreme channels*, Journal of Mathematical Physics 59 (2018), 012202; [author manuscript v2](https://arxiv.org/html/1610.02513v2), September 25, 2019. §I, §IV Theorem 22 and Remark 3, and §V. Independent discussion of the conjectured term bound and implementation motivation.
3. Niranjan Kumar and Michael M. Wolf, *The Ruskai-Audenaert conjecture & equipartitions of positive operators*, [arXiv:2607.23066v1](https://arxiv.org/html/2607.23066v1), July 25, 2026. §2 Conjecture 1 and Corollary 2; §3 Theorems 3–5; §4 Theorems 6–7.

## Status review

**Known cases:** The stated equal-weight decomposition is known for qubit inputs, qubit outputs, and classical-to-quantum or quantum-to-classical channels.

**Remaining target:** Exactly the output dimension many equal-weight components of the stated Kraus-rank bound for every channel in arbitrary input and output dimensions.

**Literature check:** Open in cited literature; no later resolution located.

Kumar–Wolf retain the general assertion as Conjecture 1. They prove it for qubit inputs and classical-to-quantum or quantum-to-classical channels, and on a set with nonempty interior in every dimension. Qubit outputs were already covered by the older argument. Their qutrit-to-qutrit result permits unequal weights. Their general equal-weight existence theorem allows more than $`n`$ components. None establishes the displayed universal statement. Their counterexamples to equal-weight decompositions into actual extreme points do not concern the larger class allowed here.

Current-year, prior-year and unrestricted searches covered both name orders, generalized extreme channels, equal weights and possible proofs or counterexamples. No matching resolution was located. Source versions, the older dimensional typo, full theorem-scope comparisons and semantic duplicate checks are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/ruskai-audenaert-decomposition.json). A clearly separated adversarial self-pass passed on September 17, 2026; no independent agent or human review occurred. Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration.
