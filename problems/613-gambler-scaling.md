# 613. Fourth-order diffusion approximation for three-player ruin

**Area:** Applied probability and diffusion approximation

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Three players start with positive integer capitals $`A,B,C`$. At each step, choose uniformly among pairs of surviving players, toss a fair coin, and transfer one unit from the loser to the winner. Remove a player when their capital reaches zero. Let $`P_{A,B,C}(\sigma)`$ be the probability of elimination order $`\sigma\in S_3`$, with the final winner listed last.

Write $`N=A+B+C`$ and let

```math
P^{\rm BM}_{A,B,C}(\sigma)=\lim_{m\to\infty}P_{mA,mB,mC}(\sigma),
```

whose existence follows from the Brownian diffusion limit. For every fixed $`A,B,C`$ and $`\sigma`$, is

```math
\left|P_{nA,nB,nC}(\sigma)-P^{\rm BM}_{A,B,C}(\sigma)\right|=O\!\left((nN)^{-4}\right)\qquad(n\to\infty)?
```

The implied constant may depend on the fixed capital proportions and elimination order. This is Conjecture 4.2(b) of Diaconis and Ethier.

## Application

Elimination probabilities enter fair allocation of tournament prizes. A quantitative diffusion approximation would certify the accuracy of replacing a large finite-state computation by a Brownian boundary-value problem.

## References

1. P. Diaconis and S. N. Ethier, [Gambler's Ruin and the ICM](https://doi.org/10.1214/21-STS826), *Statistical Science* **37**(3) (2022), 289–305. [Author manuscript](https://arxiv.org/abs/2011.07610), Section 4.1, Theorem 4.1 and Conjecture 4.2(b).
2. D. Denisov and V. Wachtel, [Harmonic measure in a multidimensional gambler's problem](https://doi.org/10.1214/24-AAP2069), *Annals of Applied Probability* **34**(5) (2024), 4387–4407. [Author manuscript](https://arxiv.org/html/2212.11526v1), Proposition 5 and the following paragraph.

## Status review

**Known cases:** Denisov and Wachtel establish a cubic-order error bound between the discrete and Brownian probabilities. They also prove exact asymptotics for a different regime, with two players' initial capitals fixed and the third growing.

**Remaining target:** The fourth-order bound above. Reference [2] explicitly distinguishes its cubic estimate from this conjecture and leaves the faster rate unresolved. Its abstract's statement about confirming a conjecture concerns the separate asymptotic regime.

Searches through 24 September 2026 found no matching resolution or duplicate. Exact-paper GitHub searches and Palomar returned no result; broader GitHub and Zenodo matches concerned other problems. No later comprehensive status survey was found.
