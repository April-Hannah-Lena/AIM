# 178. A nonuniqueness phase on every nonamenable transitive graph

**Area:** Percolation and network resilience

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`G=(V,E)`$ be infinite, connected, locally finite and vertex-transitive. Assume it is nonamenable, meaning

```math
\inf_{\varnothing\ne K\subset V,\ |K|<\infty}\frac{|\partial_E K|}{|K|}>0,
```

where $`\partial_EK`$ consists of edges with exactly one endpoint in $`K`$. For independent bond percolation, set $`p_c=\inf\{p:\mathbb P_p(\text{an infinite open cluster exists})>0\}`$ and $`p_u=\inf\{p:\mathbb P_p(\text{exactly one infinite open cluster exists})=1\}`$. Must $`p_c<p_u`$?

## Application

A strict gap gives a regime with several macroscopic conducting regions before the network forms one global connected phase.

## References

- [Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (Cambridge, 2016; paperback 2021), online revision of 19 August 2026](https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf), §7.7, Conjecture 7.31; this entry uses its transitive case.
- [Tom Hutchcroft, *Percolation on Hyperbolic Graphs* (2019)](https://doi.org/10.1007/s00039-019-00498-0), a substantial class where the gap is known.
- [Tom Hutchcroft and Minghao Pan, *Percolation at the uniqueness threshold via subgroup relativization* (2024 preprint)](https://arxiv.org/abs/2409.12283), later results about particular group structures and behavior at the uniqueness threshold.

## Status review

**Known cases:** A strict nonuniqueness phase is established for the cited hyperbolic-graph class and other specified algebraic classes.

**Remaining target:** A strict gap between the percolation and uniqueness thresholds for every transitive nonamenable graph in the statement.

**Literature check:** Open in cited literature; no later resolution located.

The updated book retains the general conjecture. Results for hyperbolic graphs, specially chosen generating sets, and particular algebraic classes do not cover every transitive nonamenable graph. The properties of the model at $`p_u`$ are a distinct issue from proving a strict gap.

Search topics checked on 2026-09-08: `nonamenable transitive pc pu conjecture 2025 2026; Benjamini Schramm nonuniqueness phase resolution`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
