# 247 — The shortest space curve of prescribed minimum width

**Area:** Geometric optimization / search paths

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a continuous rectifiable curve $`\gamma:[0,1]\to\mathbb R^3`$, define

```math
w(\gamma)=\min_{u\in S^2}\left(\max_{t\in[0,1]}\gamma(t)\cdot u-\min_{t\in[0,1]}\gamma(t)\cdot u\right).
```

Determine the exact infimum of $`\mathop{\mathrm{Length}}\nolimits(\gamma)`$ subject to $`w(\gamma)=1`$, and identify all minimizing images up to rigid motion. The endpoints are free and the curve is not required to close.

## Application

This asks for the shortest wire that cannot pass through any gap of width less than one. Equivalently, it describes a three-dimensional search path guaranteed to span every direction by a prescribed distance.

## References

1. M. Ghomi, *The length, width, and inradius of space curves* (2018), [Geometriae Dedicata 196, 123–143; author manuscript](https://arxiv.org/abs/1605.01144), §1, Theorem 1.1. Gives rigorous lower bounds and discusses the unresolved sharp constant.
2. V. A. Zalgaller, *The shortest space curve of unit width* (1994), [English translation by S. Finch (2019)](https://arxiv.org/abs/1910.02729), the construction of $`L_3`$ and concluding conjectures. Supplies an explicit candidate and explains the distinction between open and closed curves.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The established lower estimate and Zalgaller's explicit upper construction leave a nonzero gap. The later sphere-inspection theorem of Ghomi and Wenk prescribes an inscribed sphere in the convex hull, a different constraint. Searches included “shortest space curve width 2025 2026”, “Zalgaller L3 optimal proof”, and “length width inradius space curves sharp”. No proof of the exact width-constrained optimum was located.
