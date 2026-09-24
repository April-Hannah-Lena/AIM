# 293. The log-rank conjecture for deterministic communication

**Area:** Communication complexity and distributed computation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $`M\in\{0,1\}^{m\times n}`$ be a finite Boolean matrix known to both participants. Alice receives $`i\in\{1,\ldots,m\}`$, Bob receives $`j\in\{1,\ldots,n\}`$, and they exchange bits to determine $`M_{ij}`$ exactly. Let $`D(M)`$ be the least worst-case number of bits in a deterministic interactive protocol, with unrestricted local computation and with both participants learning the answer.

Do there exist absolute constants $`C,c>0`$ such that every such matrix satisfies

```math
D(M)\le C\bigl[\log_2(2+\mathop{\mathrm{rank}}\nolimits_{\mathbb R}M)\bigr]^c?
```

All pairs $`(i,j)`$ are possible: there is no promise on the inputs. The real rank is exact, not an approximate rank. The additive constant inside the logarithm handles constant matrices. Requiring both participants to learn the output changes conventional one-output-party communication complexity by at most one bit and therefore does not change this conjecture.

## Application

This asks whether a linear-algebraic measure of a distributed decision table controls the communication needed to evaluate it. A positive answer would give a universal relation between real rank and exact interaction cost for processors with separate inputs. The relevance is to communication resources; the conjecture does not require efficient local computation or an efficient procedure for constructing the protocol.

## References

1. L. Hambardzumyan, S. Lovett and M. Shirley, [*The Log-Rank Conjecture: New Equivalent Formulations*](https://arxiv.org/html/2510.02583v3), arXiv:2510.02583v3, revised August 14, 2026; §1, Conjecture 1.1 and the following communication formulation. Preprint.
2. B. Sudakov and I. Tomon, [*Matrix discrepancy and the log-rank conjecture*](https://people.math.ethz.ch/~sudakovb/discrepancy-logrank-conjecture.pdf), Mathematical Programming **212** (2025), 567–579, DOI 10.1007/s10107-024-02117-9; §1, Theorem 1.1. Published online July 5, 2024.
3. H. Hatami, K. Hosseini, S. Lovett and A. Ostuni, [*Refuting approaches to the log-rank conjecture for XOR functions*](https://arxiv.org/html/2312.09400v2), arXiv:2312.09400v2, May 3, 2024; Theorems 3.1 and 4.1 and §5. Cited preprint version.
4. A. Chattopadhyay, N. S. Mande and S. Sherif, [*The Log-Approximate-Rank Conjecture is False*](https://eccc.weizmann.ac.il/report/2018/176/download), ECCC TR18-176 (2018); Theorems 1.9–1.10.
5. Z. Song, [*Alphabet-Preserving Lifting for the Log-Rank Conjecture*](https://arxiv.org/html/2608.01812v1), arXiv:2608.01812v1, August 3, 2026; Theorems 1.1 and 3.5. Preprint.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 17, 2026 review searched the name and Lovász–Saks alias, mathematical wording, proof/disproof terms, recent authors, and 2025–2026 results, together with unrestricted-date searches and version checks. Hambardzumyan–Lovett–Shirley explicitly retain the conjecture in their August 2026 version. Independent work of Sudakov–Tomon proves an $`O(\sqrt r)`$ communication upper bound, leaving the polylogarithmic target unresolved.

The apparent refutations above have different scopes. Chattopadhyay–Mande–Sherif separate randomized bounded-error communication from approximate rank. Hatami and coauthors disprove auxiliary Fourier-support claims and explain in §5 why their examples do not refute log-rank itself. Song's displayed polylogarithmic lower bound remains compatible with an upper bound having a sufficiently large fixed exponent; this review does not claim it is the strongest lower bound in every formulation.

The baseline matrix-rigidity, Grothendieck-constant and channel-capacity entries ask different questions. Equivalent rectangle formulations are counted only here. The [evidence record](../research/expansion-2026-09/candidates/log-rank.json) documents source access, searches and a separate adversarial self-review; no independent expert review is claimed.
