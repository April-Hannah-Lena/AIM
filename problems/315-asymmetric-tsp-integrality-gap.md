# 315. The factor-two integrality gap for asymmetric metric routing

**Area:** Operations research and directed routing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $V=\{1,\ldots,n\}$, where $n\ge3$, and assign a finite cost $c_{ij}\ge0$ to each ordered pair of distinct vertices. Set $c_{ii}=0$ and assume the directed triangle inequality

$$
c_{ik}\le c_{ij}+c_{jk}\qquad(i,j,k\in V).
$$

The two directions may have different costs. Let $\mathrm{OPT}(c)$ be the minimum cost of a directed Hamiltonian cycle, which visits every vertex exactly once and returns to its starting vertex. Define the subtour linear-programming bound

$$
\begin{aligned}
\mathrm{HK}(c)=\min\quad&\sum_{i\ne j}c_{ij}x_{ij}\\
\text{subject to}\quad
&\sum_{j\ne i}x_{ij}=\sum_{j\ne i}x_{ji}=1 &&(i\in V),\\
&\sum_{i\in S,\,j\notin S}x_{ij}\ge1 &&(\varnothing\ne S\subsetneq V),\\
&x_{ij}\ge0 &&(i\ne j).
\end{aligned}
$$

Must every such instance satisfy

$$
\mathrm{OPT}(c)\le2\,\mathrm{HK}(c)?
$$

This is the asymmetric traveling-salesman subtour integrality-gap conjecture. Known families have ratios approaching two, so the unresolved direction is this uniform upper bound. The inequality also covers zero-cost instances without division by zero. It asks for the existence of a tour with the stated cost; no efficient construction is required.

## Application

Directed routing models allow travel costs to depend on direction, as with one-way roads and direction-dependent journey times. Shortest-path costs in a strongly connected nonnegative road network satisfy the directed triangle inequality. The subtour LP provides a lower bound on the optimal tour cost. Determining its worst-case gap would identify the accuracy of this certificate and a target for rounding fractional routing solutions. The directed model differs from the symmetric metric model in [entry 278](278-metric-tsp-four-thirds.md).

## References

1. Vera Traub and Jens Vygen, *Approximation Algorithms for Traveling Salesman Problems*, Cambridge University Press, 2025, [author companion and errata](https://www.or.uni-bonn.de/tspbook/tsp_book.html), [electronic text](https://www.or.uni-bonn.de/tspbook/book.pdf). Equations (3.1)–(3.2), Theorem 3.4, Proposition 3.14, Theorem 3.18 and Open Problem 3.19, also listed in §18.2, p. 403. The companion dates publication to 2025; the electronic text carries copyright 2024.
2. Jens Vygen, *Better approximation guarantee for Asymmetric TSP*, [arXiv:2603.14334v1](https://arxiv.org/html/2603.14334v1), March 15, 2026, §1, equation (1) and Theorem 1. Preprint with an improved general upper bound.
3. Alessandro Sosso, Ambrogio Maria Bernardelli and Stefano Gualandi, *The cloven traveling salesman: cycle covers and the integrality gap of small ATSP instances*, Optimization Letters, published online June 14, 2026, [DOI 10.1007/s11590-026-02312-x](https://link.springer.com/article/10.1007/s11590-026-02312-x), §§1–2.1 and 5–6. Independent status discussion and finite computational results.
4. Tolson Bell and Alan M. Frieze, *Solving a Random Asymmetric TSP Exactly in Quasi-Polynomial Time w.h.p.*, [arXiv:2308.02946v15](https://arxiv.org/html/2308.02946v15), revised July 28, 2026, §1, Theorem 1 and §2.1. The exact algorithm has a random-instance scope.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-17. Vygen's Theorem 1 gives a tour costing at most $(12+2\sqrt2+\varepsilon)$ times the LP value for every fixed $\varepsilon>0$. Consequently the integrality gap is at most $12+2\sqrt2\approx14.828$. This improves the older bound of 17 reported in the book and in the June 2026 computational paper. The book establishes equivalence between the degree-constrained metric LP here and its balanced-circulation formulation for closed walks.

Sosso–Bernardelli–Gualandi examine half-integer extreme points with at most twelve vertices, leaving arbitrary sizes and fractional solutions unresolved. Bell–Frieze's exact algorithm applies with high probability to independent random arc costs satisfying distributional hypotheses; it supplies no worst-case factor-two bound for all directed metrics. A symmetric four-thirds bound would likewise leave the asymmetric assertion open.

The [evidence ledger](../research/expansion-2026-09/candidates/asymmetric-tsp-integrality-gap.json) records source versions, scope comparisons and duplicate checks. The separate A24 adversarial self-pass passed on September 17, 2026; no independent agent or human review is claimed.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
