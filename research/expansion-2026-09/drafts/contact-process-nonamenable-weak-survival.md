# Weak survival of the contact process on nonamenable Cayley graphs

**Area:** Spatial epidemics and nonequilibrium phase transitions

**Status:** Open in cited literature; no later resolution located as of 2026-09-17.

**Last checked:** 2026-09-17

## Problem statement

Let $\Gamma$ be an infinite finitely generated group, and let $S\subset\Gamma\setminus\{e\}$ be any finite symmetric generating set, where $e$ is the identity and symmetric means $S^{-1}=S$. Its undirected Cayley graph $G=(\Gamma,E)$ has an edge $\{x,xs\}$ for each $x\in\Gamma$ and $s\in S$. Assume $G$ is nonamenable:
$$
h_E(G):=\inf_{\substack{\varnothing\ne K\subset\Gamma\\ |K|<\infty}}
\frac{|\partial_E K|}{|K|}>0,
$$
where $\partial_EK$ is the set of edges with exactly one endpoint in $K$.

Consider the ordinary contact process $(\xi_t)_{t\ge0}$, whose state is the set of infected vertices. Each infected vertex becomes healthy at rate $1$; each healthy vertex becomes infected at rate $\lambda$ times its number of infected neighbors. Initially $\xi_0=\{e\}$. Write $\mathbb P_\lambda$ for its law and define
$$
\lambda_{\mathrm{g}}(G)
=\inf\{\lambda>0:\mathbb P_\lambda(\xi_t\ne\varnothing\text{ for all }t\ge0)>0\},
$$
$$
\lambda_{\mathrm{l}}(G)
=\inf\{\lambda>0:\mathbb P_\lambda(e\in\xi_t\text{ for arbitrarily large }t)>0\}.
$$

**Must $\lambda_{\mathrm{g}}(G)<\lambda_{\mathrm{l}}(G)$ for every such Cayley graph?**

This is the isotropic Cayley-graph form of the weak-survival conjecture discussed by Lyons, Lalley and Swart. A strict gap gives an interval of infection rates with positive probability of survival forever, while each fixed finite set is eventually infection-free almost surely. The generating set is arbitrary but fixed when defining the process; finding a favorable generating set for each group would not answer the question. No behavior at either endpoint is asserted.

## Applied significance

The contact process is a basic susceptible–infected–susceptible epidemic model: recovery restores susceptibility, and transmission follows a contact network. A weak-survival phase separates persistence somewhere in a growing network from recurrent infection in a fixed neighborhood. The question asks whether uniform geometric expansion alone forces that distinction in homogeneous networks. This is an infinite-network foundation for interpreting persistence and local surveillance, rather than a quantitative prediction for any finite epidemic.

## References

- [Russell Lyons, *Phase Transitions on Nonamenable Graphs*, Journal of Mathematical Physics 41 (2000), 1099–1126; author revision of 11 July 2000](https://rdlyons.pages.iu.edu/pdf/review.pdf), §8, pp. 31–34: definitions, Theorem 8.1, the explicit question following Theorem 8.5, and Theorem 8.7.
- [Steven P. Lalley, *The weak/strong survival transition on trees and nonamenable graphs*, lecture slides dated 4 September 2006](https://galton.uchicago.edu/~lalley/Talks/kyoto.pdf), slides 22–31: rates, isotropy and the explicit nonamenable-group conjecture on slide 31.
- [Jan M. Swart, *Sharpness of the phase transition for local survival*, “Jan’s open problems,” undated author note](https://staff.utia.cas.cz/swart/problems/locsharp.pdf), pp. 1–3, especially “What is conjectured” on p. 3. This independently states the amenability/threshold-equality conjecture; its principal sharpness conjecture is a different question.
- [Jan M. Swart, *The contact process seen from a typical infected site*, Journal of Theoretical Probability 22 (2009), 711–740; arXiv manuscript v5, 28 August 2008](https://arxiv.org/abs/math/0507578), §§1.2–1.3, Theorem 1.2 and Corollary 1.3.
- [Xiangying Huang, *Exponential growth and continuous phase transitions for the contact process on trees*, arXiv:1911.03330v2, 11 December 2019](https://arxiv.org/abs/1911.03330), §1, periodic-tree definition and Theorem 7 (manuscript pp. 4–5).

## Status review

The literature check on 2026-09-17 covered weak/intermediate survival, distinct local and global critical values, Cayley/transitive nonamenable graphs, proof and counterexample searches, and author corrections. The [evidence record](../candidates/contact-process-nonamenable-weak-survival.json) gives exact queries, hypotheses and access limits.

The gap is established for regular trees and for transitive degree-$d$ graphs satisfying $h_E(G)/d\ge1/\sqrt2$; see Lyons’s Theorems 8.1 and 8.7. Huang’s Theorem 7 extends tree results to general periodic trees. These restrictions leave nonamenable Cayley graphs with cycles and without the stated quantitative expansion bound untreated. Swart’s critical-extinction theorem applies to this model, but extinction at $\lambda_{\mathrm{g}}$ does not itself separate $\lambda_{\mathrm{g}}$ from $\lambda_{\mathrm{l}}$.

Pemantle–Stacey counterexamples show that nonamenability alone is insufficient on arbitrary bounded-degree trees. Their primary manuscript was inaccessible, so this fact was checked through Lyons’s explicit restatement on p. 34. Such a counterexample cannot be a Cayley tree: Cayley graphs are regular, and the regular-tree theorem gives a strict gap. This scope conclusion is an inference from the two statements, not a claim to have read the inaccessible construction. The separate adversarial review is recorded in the ledger.

The closest catalogue question, [183](../../../problems/183-nonamenable-nonuniqueness-phase.md), concerns the uniqueness of static, independent bond-percolation clusters. Contact-process infection paths are directed in space-time and do not identify these two questions. Entries 179 and 190 concern competition between two populations, rather than one population's local versus global survival. Independent expert corroboration was obtained, but the source statements are historical or undated; no later resolution matching the formulation was located.
