# 578. Improving the exponential lower bound for peeling sequences

**Area:** Discrete geometry and geometric counting

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix an integer $d\ge2$. A finite set $P\subset\mathbb R^d$ is in general position if every subset of at most $d+1$ points is affinely independent. A peeling sequence is an ordering $(p_1,\ldots,p_n)$ of $P$ such that $p_i$ is a vertex of

$$
\mathop{\mathrm{conv}}\nolimits\{p_i,p_{i+1},\ldots,p_n\}
$$

for every $i$. Let $g_d(P)$ be the number of such orderings and let

$$
g_d(n)=\min_{|P|=n}g_d(P),
$$

where the minimum is over sets in general position.

Prove or disprove that for every fixed $d\ge2$ there are constants $\varepsilon_d>0$ and $c_d>0$, independent of $n$, such that

$$
g_d(n)\ge c_d(d+1+\varepsilon_d)^n\qquad(n\ge1).
$$

The question is a strict improvement of the exponential base, not just a larger multiplicative constant.

## Application

Peeling sequences count the legal ways to successively remove extreme data points. Their minimum measures the unavoidable branching in convex-hull elimination and provides a combinatorial measure of point-set structure.

## References

1. D. G. Simon, [The minimum number of peeling sequences of a point set](https://doi.org/10.1007/s00454-024-00713-2), *Discrete & Computational Geometry* **75** (2026), 1122–1133, Section 5, Conjecture 1. [arXiv:2312.00244](https://arxiv.org/abs/2312.00244).
2. D. G. Simon, [Peeling sequences: a directional method for the three-block construction](https://arxiv.org/abs/2609.19540), arXiv:2609.19540 (17 September 2026), introduction and Theorem 1.
3. A. Hisatsuga, G. Johnston and R. Miyazaki, [A base-8 upper bound for planar peeling sequences](https://arxiv.org/abs/2609.13122), arXiv:2609.13122 (11 September 2026).

## Status review

As long as more than $d$ points remain, general position guarantees at least $d+1$ convex-hull vertices. This gives $g_d(n)=\Omega((d+1)^n)$; the conjecture requires an exponential improvement over that argument. Dimension one is excluded: there only the two endpoints can be removed and $g_1(n)=2^{n-1}$.

The September 2026 planar paper [2] explicitly says the base-3 lower bound remains best known up to a constant. Its bound $g_2(n)=O(6.57^n)$ and the earlier improvement [3] are upper bounds from constructions. They do not prove the requested lower bound. Current searches found no matching solution announcement or repository duplicate.
