# 276. The four-thirds integrality gap for metric routing

**Area:** Operations research and routing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On the complete graph $`K_n`$, let $`c_e\ge0`$ satisfy the triangle inequality. Write $`\mathrm{OPT}(c)`$ for the cheapest Hamiltonian cycle, and let $`\mathrm{HK}(c)`$ minimize $`\sum_ec_ex_e`$ subject to $`x_e\ge0`$, $`\sum_{e\ni v}x_e=2`$ for each vertex, and $`\sum_{e\in\delta(S)}x_e\ge2`$ for every nonempty proper vertex set $`S`$; $`\delta(S)`$ denotes its crossing edges. Must $`\mathrm{OPT}(c)\le\tfrac43\mathrm{HK}(c)`$ hold for every $`n\ge3`$ and every such metric?

## Application

This would give the sharp worst-case accuracy of a principal lower bound used in exact vehicle-routing and tour optimization.

## References

- [William Cook, Stefan Hougardy and Moritz Petrich, *Extending Exact Integrality Gap Computations for the Metric TSP* (2026)](https://arxiv.org/abs/2603.12995), Introduction and computational verification scope.
- [Billy Jin, Nathan Klein and David P. Williamson, *Maximum Entropy is a 10/7-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances* (2026)](https://arxiv.org/abs/2607.01536), introductory four-thirds conjecture.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 papers verify bounded-size or restricted families. Neither establishes the inequality for arbitrary metrics. Lower-bound examples already approach four thirds, so the stated upper bound is the unresolved direction.

Search topics checked on 2026-09-13: `metric TSP four thirds integrality gap conjecture 2026 proof Cook Hougardy Petrich`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
