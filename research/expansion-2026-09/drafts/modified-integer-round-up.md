# The modified integer round-up conjecture for cutting stock

**Area:** Stochastic dynamics, reaction networks and applied optimization

**Status:** Open in cited literature; no later resolution located as of 2026-09-19.

**Last checked:** 2026-09-19

## Problem statement

Fix a positive integer stock length $W$ and $n\geq1$ item types. Type $i$ has integer length $1\leq\ell_i\leq W$ and positive integer demand $b_i$. A cutting pattern is a vector in

$$
\mathcal P=\left\{a\in\mathbb Z_{\geq0}^{n}:
\sum_{i=1}^{n}\ell_i a_i\leq W\right\}.
$$

Use every capacity-feasible pattern: there is no additional restriction $a_i\leq b_i$. Thus the relaxation below includes patterns containing more copies of an item than its demand, sometimes called *nonproper patterns*.

Let the minimum number of stock pieces needed to meet all demands be

$$
\begin{aligned}
z_{\mathrm{IP}}=\min\quad&\sum_{a\in\mathcal P}x_a\\
\text{subject to}\quad&\sum_{a\in\mathcal P}a_i x_a\geq b_i
\quad(1\leq i\leq n),\\
&x_a\in\mathbb Z_{\geq0}\quad(a\in\mathcal P).
\end{aligned}
$$

Define $z_{\mathrm{LP}}$ by replacing the integer constraint with $x\in\mathbb R_{\geq0}^{\mathcal P}$. Each use of a pattern counts as one stock piece, including repeated uses.

Does every such instance satisfy

$$
z_{\mathrm{IP}}\leq\left\lceil z_{\mathrm{LP}}\right\rceil+1?
$$

This is the modified integer round-up property (MIRUP) conjectured by Scheithauer and Terno. The ceiling is the least integer no smaller than its argument. The question requires the same additive one for arbitrary item types, lengths, capacity and demands. It compares the two optima and does not prescribe the time needed to find a packing.

## Applied significance

Cutting stock models production from standard rolls or bars, including paper and metal cutting. Fractional pattern optimization supplies lower bounds used to assess production plans. MIRUP would place the true stock requirement within one piece of that rounded lower bound, uniformly over the order sizes. A counterexample would expose a larger systematic gap in this planning estimate. The statement concerns the classical one-dimensional model with one stock length and the stock-count objective; setup costs and machine-specific cutting restrictions require different models.

## References

1. Guntram Scheithauer and Johannes Terno, *The modified integer round-up property of the one-dimensional cutting stock problem*, European Journal of Operational Research 84(3) (1995), 562–571. [DOI](https://doi.org/10.1016/0377-2217%2895%2900022-I). Original attribution; publisher abstract checked. The full formulation here is also given in reference 2.
2. Renan Fernando Franco da Silva, Vinícius Loti de Lima, Rafael C. S. Schouery, Jean-François Côté and Manuel Iori, *Polynomial and Pseudopolynomial Algorithms for Two Classes of Bin Packing Instances*, [arXiv:2604.05152v2](https://arxiv.org/html/2604.05152v2), June 4, 2026, preprint. §1; §2, equations (1)–(3) and Property 2; §§3–5 and §7. Explicit integer-input model, nonproper-pattern convention and current conjecture statement.
3. Rebecca Hoberg and Thomas Rothvoss, *A Logarithmic Additive Integrality Gap for Bin Packing*, SODA 2017, 2616–2625. [DOI](https://doi.org/10.1137/1.9781611974782.172); [arXiv:1503.08796v1](https://arxiv.org/pdf/1503.08796), March 30, 2015. The accessed preprint's §1, equation (1), and §1.1, Theorem 2, pp. 1–3, give the pattern relaxation, conjecture and logarithmic additive bound.
4. Friedrich Eisenbrand, Dömötör Pálvölgyi and Thomas Rothvoß, *Bin Packing via Discrepancy of Permutations*, [arXiv:1007.2170v2](https://arxiv.org/pdf/1007.2170), February 2, 2012, journal-version manuscript. §6, Definition 1 and Theorems 11–12, pp. 12–16. Lower bounds for a specified class of rounding procedures.
5. Constantine Goulimis, *Counterexamples in the CSP*, [arXiv:2004.01937v3](https://arxiv.org/pdf/2004.01937), July 7, 2020, preprint; PDF title *Counterexamples in the Cutting Stock Problem*. §1; §2, p. 2; §5.1, pp. 6–7. Distinguishes integer rounding, modified integer rounding and a different conjecture about the number of distinct patterns.
6. John Martinovic, *A note on the integrality gap of cutting and skiving stock instances*, 4OR 20 (2022), 85–104, published online December 23, 2020. [Published article](https://link.springer.com/article/10.1007/s10288-020-00469-4), §2, Definition 3, and §4, Theorem 4. An improved bound under divisibility assumptions.

## Status review

The June 2026 preprint states the exact ceiling-plus-one conjecture with nonproper patterns and reports no known violating instance. Its polynomial and pseudopolynomial algorithms exploit the specifically constructed AI and ANI benchmark families; their optimality guarantees do not extend to arbitrary input instances.

Hoberg–Rothvoss prove a general additive $O(\log(2+z_{\mathrm{LP}}))$ bound. This leaves the uniform one-piece target unresolved. Their randomized algorithm runs in expected time polynomial in the total number of individual items; this is not a claim about polynomial time in binary-encoded demands. The discrepancy-based lower bounds of Eisenbrand–Pálvölgyi–Rothvoß restrict the patterns available to the rounding procedure, as specified in their Definition 1. They do not give that lower bound for the unrestricted integer optimum.

The stronger ordinary integer round-up assertion $z_{\mathrm{IP}}=\lceil z_{\mathrm{LP}}\rceil$ is false. Goulimis records an instance with $W=132$, lengths $(44,33,12)$ and demands $(2,3,6)$, for which $z_{\mathrm{LP}}=259/132$ and $z_{\mathrm{IP}}=3$; it satisfies MIRUP. The same paper's distinct-pattern counterexample concerns the support of a waste-optimal production plan, a different objective from the total stock count here.

For the special case in which $W/\ell_i$ is an integer for every item type, Martinovic proves the stronger bound $z_{\mathrm{IP}}-z_{\mathrm{LP}}<4/3$. That divisibility hypothesis is absent from the general conjecture.

[Entry 326](../../../problems/326-online-bin-packing-optimal-ratio.md) asks for an online competitive ratio under unknown future arrivals. [Entry 336](../../../problems/336-strong-komlos-prefix-discrepancy.md) concerns signed vector prefixes, and [entry 285](../../../problems/285-metric-tsp-four-thirds.md) concerns a routing relaxation. Their full statements were compared; none is the displayed offline stock-count inequality.

Searches on September 18–19, 2026 covered MIRUP and rounding-up aliases, the mathematical bound, proofs and counterexamples, original and later authors, recent packing algorithms, corrections and version histories. The [evidence ledger](../candidates/modified-integer-round-up.json) records theorem-level scope comparisons and access limits. The original 1995 full text was unavailable; its accessible explicit restatements supply the formulation. The researching agent completed a separate adversarial self-review; no independent agent or human review is claimed.
