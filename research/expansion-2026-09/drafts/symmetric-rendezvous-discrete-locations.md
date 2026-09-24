# Optimal symmetric rendezvous among discrete locations

**Area:** Decentralized coordination and search theory

**Status:** Accepted; integrated as entry 323

**Last checked:** 2026-09-18

## Problem statement

Let $n\ge4$ and $[n]=\{1,\ldots,n\}$. Two agents can visit any one of $n$ locations at each synchronized integer time $t\in\mathbb N_0=\{0,1,2,\ldots\}$. They can recognize locations they have visited, but their private location labels have an unknown correspondence. They receive no observations of each other's movements and can communicate only when they meet. Both must follow the same randomized strategy, using independent private randomness.

Precisely, a strategy is a probability law $\mu$ on infinite sequences in $[n]^{\mathbb N_0}$, with its product sigma-algebra. Draw $X=(X_t)$ and $Y=(Y_t)$ independently with law $\mu$. Independently draw a uniformly random permutation $\pi$ of $[n]$, representing the correspondence between the agents' private labels. Define

$$
T_{\mu,\pi}=\inf\{t\in\mathbb N_0:\pi(X_t)=Y_t\},
\qquad
r_n=\inf_{\mu}\mathbb E[T_{\mu,\pi}],
$$

where $\inf\varnothing=+\infty$ and the expectation includes all three independent random choices. **Determine the exact optimal expected meeting time $r_n$ for every $n\ge4$.**

The strategy may depend on $n$ and may have arbitrary memory and temporal correlations. It need not repeat in fixed blocks or be a Markov chain. There are no markers, shared random bits, distinguishable assigned roles, or common location labels. Sampling an entire sequence is a representation of a randomized strategy: until meeting, the only external observation is that meeting has not occurred, so this does not impose an additional memory restriction.

The first visit occurs at time zero and may already be a meeting; the problem is not conditioned on distinct starting locations. Sources that count the first visit as step one have an expected value larger by one. All numbers of locations are one problem family here, rather than separate entries.

## Applied significance

The model measures the cost of coordination when two identical agents can use the same protocol but cannot assign complementary roles or agree on location names. Alpern's telephone interpretation has two rooms of terminals joined by an unknown matching: the agents must select connected terminals simultaneously before they can communicate. Rendezvous protocols also model repeated attempts to find a common communication channel. The optimum would quantify the delay inherent in this information constraint and provide a benchmark for decentralized search protocols. This idealized model assumes synchronized attempts and equal travel cost between locations; it is not a complete physical search-and-rescue model.

## References

1. Steve Alpern, *Ten Open Problems in Rendezvous Search*, in *Search Theory: A Game Theoretic Perspective* (2013), pp. 223–230, [publisher record](https://doi.org/10.1007/978-1-4614-6825-7_14), [author-hosted excerpt](https://diamhomes.ewi.tudelft.nl/~rfokkink/rendezvousproblems.pdf). §14.2, Problem 5, p. 226, explicitly poses the discrete-location problem.
2. Javier Cembrano, Felix Fischer and Max Klimm, *Faster Symmetric Rendezvous on Four or More Locations*, [arXiv:2604.02058v2](https://arxiv.org/html/2604.02058v2), revised August 2, 2026. Preprint. §2 defines the sequence/permutation model; §2.1 separates conditional starting positions; §4.2, Theorem 2, gives the improved strategy; §5 retains the optimal-strategy question.
3. Richard Weber, *Optimal Symmetric Rendezvous Search on Three Locations*, Mathematics of Operations Research 37(1) (2012), 111–122, [DOI](https://doi.org/10.1287/moor.1110.0528), [author manuscript](https://www.statslab.cam.ac.uk/~rrw1/research/K3%20revised.pdf). §1 and Theorem 2.1, including the initial-position convention.
4. Richard Weber, *The Anderson–Weber strategy is not optimal for symmetric rendezvous search on K4*, [arXiv:0912.0670v1](https://arxiv.org/pdf/0912.0670v1), December 3, 2009. Preprint. §§1–2 describe the four-location improvement.
5. Varsha Dani, Thomas P. Hayes, Cristopher Moore and Alexander Russell, *Codes, lower bounds, and phase transitions in the symmetric rendezvous problem*, Random Structures & Algorithms 49(4) (2016), 742–765, [DOI](https://doi.org/10.1002/rsa.20691), [author preprint](https://arxiv.org/pdf/1609.01582v1). §2, Definitions 1–3; §3, Theorems 1–3 and Proposition 9.

## Status review

The September 17, 2026 investigation covered symmetric rendezvous, discrete locations, complete graphs, the Mozart Café name, the original and later authors, recent proofs, counterexamples, corrections and version histories. Alpern's explicit problem and the independent Cembrano–Fischer–Klimm August 2026 revision support the formulation and remaining gap. Full access and scope comparisons are recorded in the [evidence ledger](../candidates/symmetric-rendezvous-discrete-locations.json).

Two and three locations are solved. Weber's value $5/2$ assumes distinct initial locations; it becomes $r_3=5/3$ with the time-zero convention here. His four-location result and Cembrano–Fischer–Klimm's Theorem 2 improve the Anderson–Weber strategy without determining the optimum. The latter gives an explicit improvement for every finite $n\ge4$ and explicitly leaves optimal strategies open in §5. It therefore refutes optimality of that particular strategy, not the present open optimization question.

Dani–Hayes–Moore–Russell give an asymptotic lower bound $(0.6389\ldots-o(1))n$, while the Anderson–Weber construction provides an upper bound $(0.8289\ldots+o(1))n$. Their sharp $4n$ threshold concerns meeting with probability tending to one as $n$ grows, rather than minimizing the unrestricted expected meeting time. Their short-horizon optimality theorem also does not optimize all tail probabilities with one strategy. These distinct objectives must not be identified.

Other apparently relevant solutions use detectable tokens, one-step success probabilities, shared location labels, an infinite line, or restricted memory. In particular, the September 12, 2026 integer-line result concerns oblivious self-distance strategies and does not solve the complete-graph problem. The ledger records the exact restrictions and source-reading limits. Mathematical proofs have not been independently certified.

Unlike [entry 294](../../../problems/294-cerny.md), this question concerns two agents with independent random choices and an unknown label matching, not one word resetting every state of a deterministic automaton. The online allocation objective in [entry 318](../../../problems/318-online-bin-packing-optimal-ratio.md) instead compares performance with an offline optimum under adversarial requests.

The separated A32 adversarial self-pass checked the time convention, unrestricted strategy class, source versions and related-result scopes. No independent agent or human review occurred.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../batch-04-review.md). No matching later resolution was located.

Integrated page: [331. Optimal symmetric rendezvous among discrete locations](../../../problems/323-symmetric-rendezvous-discrete-locations.md).
