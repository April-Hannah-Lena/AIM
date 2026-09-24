# 634. Permutation snarks with order congruent to six modulo eight

**Area:** Computational graph theory and edge colouring

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

A *cycle permutation graph* is a finite simple cubic graph with a spanning 2-factor consisting of two chordless cycles. Equivalently, for some integer $k\ge3$, it consists of two disjoint $k$-cycles and a perfect matching between their vertex sets. Such a graph is a *permutation snark* if its edges cannot be coloured with three colours so that incident edges have different colours.

Does there exist a permutation snark $G$ satisfying

$$
|V(G)|\equiv6\pmod8?
$$

Construct one, or prove that every cycle permutation graph with this order is 3-edge-colourable. Equivalently, with $k\equiv3\pmod4$, determine whether any matching between two $k$-cycles can produce a permutation snark. The existence of a single example is the target; no extra girth or connectivity condition is imposed.

## Application

The question identifies an unexplained arithmetic restriction on a structured family of edge-colouring obstructions. It also gives a precise target for exhaustive graph generation and independently checkable colouring certificates.

## References

1. J. Goedgebeur, J. Renders and S. Van Overberghe, [Generation of cycle permutation graphs and permutation snarks](https://doi.org/10.1090/mcom/4247), *Mathematics of Computation*, electronically published 13 August 2026. Section 3, Proposition 4; [arXiv:2411.12606v4](https://arxiv.org/abs/2411.12606v4).
2. E. Máčajová and M. Škoviera, [Permutation snarks of order 2 (mod 8)](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/1313), *Acta Mathematica Universitatis Comenianae* **88** (2019), 929–934. Corollary 2.2 and Section 4.
3. E. Máčajová and M. Škoviera, [Are there any permutation snarks on 6 (mod 8) vertices?](https://doi.org/10.1016/j.procs.2025.10.294), *Procedia Computer Science* **273** (2025), 163–168.

## Status review

**Known cases:** Permutation snarks exist at every order $n\equiv2\pmod8$ with $n\ge10$. Even cycle lengths admit an immediate 3-edge-colouring, so the only possible orders are $2$ and $6$ modulo $8$. The exhaustive computations in [1] exclude the latter residue below 54 vertices. Reference [2] also shows that a smallest example in the missing residue, if one exists, must be cyclically 5-edge-connected.

**Remaining target:** Settle existence in the residue class $6\pmod8$. Reference [3] obtains a conditional construction from a noncritical permutation snark but does not establish existence.

The August 2026 journal article and the current [House of Graphs catalogue](https://houseofgraphs.org/meta-directory/snarks) still describe the question as open. Current literature, arXiv, public GitHub, native Zenodo and Palomar searches found no resolution or matching announcement. No equivalent catalogue problem was found.
