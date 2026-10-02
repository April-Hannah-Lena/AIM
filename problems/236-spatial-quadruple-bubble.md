# 236. The quadruple-bubble conjecture in three-dimensional space

**Area:** Soap films and interfacial energy

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For four prescribed volumes $`v_1,\ldots,v_4>0`$, minimize

```math
P(E_1,E_2,E_3,E_4)=\frac12\sum_{i=1}^5\mathop{\mathrm{Per}}\nolimits(E_i),\qquad E_5=\mathbb R^3\setminus\bigcup_{i=1}^4E_i,
```

over pairwise disjoint measurable cells of finite perimeter with $`|E_i|=v_i`$ for $`i\leq4`$. Perimeter is the total variation of the distributional derivative of the indicator; interfaces are thus counted once.

Prove or disprove that every minimizing cluster, up to null sets and Euclidean isometries, is a standard quadruple bubble. Define this family as follows: choose five unit vectors $`c_i\in\mathbb R^4`$ with $`c_i\cdot c_j=-1/4`$ for $`i\ne j`$, partition $`S^3`$ into cells $`C_i=\{x:x\cdot c_i\geq x\cdot c_j\ \forall j\}`$, stereographically project from a point strictly inside $`C_5`$ to $`\mathbb R^3`$, and apply a Euclidean similarity. Select members having the prescribed four finite volumes. The cells need not be connected in the competing class.

## Application

This is the minimum amount of soap film needed to separate four trapped gas volumes from the surrounding air. It gives a benchmark for multiphase interfacial-energy models.

## References

- Emanuel Milman, [*Multi-Bubble Isoperimetric Problems*](https://arxiv.org/html/2510.07078v1) (2025 survey), Definition 3.1 and §9, open problem (1): specifically identifies the quadruple bubble in $`\mathbb R^3`$ as unresolved.
- Emanuel Milman and Joe Neeman, [*The Structure of Isoperimetric Bubbles on $`\mathbb R^n`$ and $`\mathbb S^n`$*](https://arxiv.org/abs/2205.09102) (2022 preprint; 2025 publication), main theorem and the standard-partition definition: proofs for a range that includes three bubbles in $`\mathbb R^3`$ and four in $`\mathbb R^4`$.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “quadruple bubble R3 conjecture proof 2025 2026”, “Milman Neeman maximal case k=n+1”, and later multi-bubble results. The survey’s explicit open problem matches four finite cells in dimension three. The proved three-dimensional triple-bubble theorem, and the quadruple theorem in dimension at least four, do not settle it. Here the exterior is the fifth cell, not a fifth prescribed-volume bubble.
