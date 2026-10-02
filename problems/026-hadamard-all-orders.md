# 026. Hadamard matrices in every admissible order

**Area:** Matrix design, coding and experimental design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For every integer $`k\ge1`$, does there exist $`H\in\{-1,1\}^{4k\times4k}`$ satisfying

```math
HH^{\mathsf T}=4k\,I_{4k}?
```

Equivalently, can $`4k`$ pairwise orthogonal sign vectors of length $`4k`$ always be constructed? The conjecture is about all positive multiples of four, not the existence of any particular previously missing order.

## Application

These matrices provide orthogonal experimental designs, error-correcting codes and balanced transforms. The existence theorem would remove arithmetic restrictions on those exact designs.

## References

1. P. Browne, R. Egan, F. Hegarty and P. Ó Catháin, [A Survey of the Hadamard Maximal Determinant Problem](https://arxiv.org/abs/2104.06756), 2021, v4. Historical results and constructions.
2. P. Sin, [Hadamard Conjecture](https://people.clas.ufl.edu/sin/files/UMSHadamard.pdf), University of Florida lecture notes (2022). Explicit universal formulation.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The survey and lecture notes state the all-order conjecture. Searches found recent constructions and reports about formerly missing orders, including order 668, but no general existence theorem for every multiple of four. Consequently, this entry does not label order 668 or any other individual order as still open.

Searches included: `Hadamard conjecture 2026 all orders proof`; `Hadamard matrices all multiples four 2026`; `Hadamard order 668 August 2026`. This is a documented literature check, not a certification that no solution exists.
