# 547. Uniqueness of 277-point two-distance sets in dimension 23

**Area:** Computational geometry and Euclidean distance matrices

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For a finite set $`X\subset\mathbb R^{23}`$, put

```math
D(X)=\{\|x-y\|_2:x,y\in X,\ x\ne y\}.
```

Is every pair of sets $`X,Y\subset\mathbb R^{23}`$ satisfying

```math
|X|=|Y|=277,\qquad |D(X)|=|D(Y)|=2
```

related by a Euclidean similarity? Explicitly, must there exist $`\lambda>0`$, an orthogonal matrix $`Q\in\mathbb R^{23\times23}`$ and $`t\in\mathbb R^{23}`$ such that

```math
Y=\{t+\lambda Qx:x\in X\}?
```

Existence of such sets is known. The question is whether they form a single similarity class. No prescribed distance ratio, spherical constraint or containment of a particular smaller configuration is assumed. This is the uniqueness question posed in §3 of [1].

## Application

A uniqueness theorem would classify an exceptional finite Euclidean geometry from the restriction to two pairwise distances and its cardinality. It would provide a rigidity result and a reference configuration for exact reconstruction from structured distance data. A second similarity class would show that these constraints leave distinct geometric realizations.

## References

1. H.-J. Ge, J. Koolen and A. Munemasa, [A 2-Distance set with 277 Points in the Euclidean Space of Dimension 23](https://doi.org/10.1007/s00454-026-00843-9), Discrete & Computational Geometry (2026), Theorem 1 and §3; [corrected preprint, version 4](https://arxiv.org/abs/2504.18110v4), 3 August 2026.

## Status review

Reference [1] constructs a $`277`$-point set with squared distances $`4`$ and $`6`$. Its Proposition 3 concerns adding points to that particular configuration. Nonextendibility does not classify all configurations of the same cardinality, and it does not prove that $`277`$ is the largest possible cardinality in dimension $`23`$.

The August 2026 correction changes the description of extensions in dimension $`24`$ but retains the uniqueness question in dimension $`23`$. The corrected extension statement is therefore not an announced solution of this problem. The separate existence question for $`325`$ points in dimension $`24`$ is [problem 546](546-two-distance-325-points-dimension24.md).

No matching proof, counterexample or announced resolution was located through the check date.
