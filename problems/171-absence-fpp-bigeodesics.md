# 171. Absence of doubly infinite minimizing paths in planar first-passage percolation

**Area:** Optimal transport through random media

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Assign independent mean-one exponential times to the nearest-neighbor edges of $`\mathbb Z^2`$, and let $`T(x,y)`$ be the minimum path time. A bigeodesic is an injective path $`(v_k)_{k\in\mathbb Z}`$ such that, for every pair of integers $`i<j`$,

```math
\sum_{k=i}^{j-1}\tau_{\{v_k,v_{k+1}\}}=T(v_i,v_j).
```

Is the probability that any bigeodesic exists equal to zero? There is no restriction on its direction, and both ends lie in the full plane.

## Application

A bigeodesic would be an indefinitely extending optimal transport channel in a disordered medium. Excluding such channels clarifies the geometry of optimal routes.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §4.5, Question 31.
- [Barbara Dembin, Dor Elboim and Ron Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation* (2024)](https://doi.org/10.1007/s00039-024-00672-z), introduction and bigeodesic discussion.
- [Michael Damron and Jack Hanson, *Bigeodesics in first-passage percolation* (2015 preprint)](https://arxiv.org/abs/1512.00804), directional and conditional results.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2024 paper still identifies the unrestricted conjecture as open. Results in fixed directions, half-planes, or under unproved shape assumptions do not rule out randomly directed full-plane bigeodesics. Directed last-passage nonexistence is a separate theorem.

Search topics checked on 2026-09-08: `bigeodesics first-passage 2025 2026; full plane exponential FPP bigeodesics nonexistence`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
