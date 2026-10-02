# 540. Finite homotopy models for spherical Čech complexes

**Area:** Applied and computational topology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`n\ge2`$, and equip $`S^n\subset\mathbb R^{n+1}`$ with its round geodesic metric $`d(x,y)=\arccos\langle x,y\rangle`$. For $`r>0`$, let $`C_n(r)`$ be the abstract simplicial complex with vertex set $`S^n`$ in which a finite set $`\sigma`$ is a simplex precisely when

```math
\bigcap_{x\in\sigma}B_{S^n}(x;r)\ne\varnothing,\qquad B_{S^n}(x;r)=\{z\in S^n:d(x,z)<r\}.
```

Give its geometric realization $`|C_n(r)|`$ the ordinary CW topology.

Is $`|C_n(r)|`$ homotopy equivalent to a finite CW complex for every $`n\ge2`$ and every $`r>0`$? The finite model may depend on $`n`$ and $`r`$; no uniform cell-count or dimension bound is required. Prove the assertion or give a counterexample.

This is the higher-dimensional part of Conjecture 8.4 of [1]. It asks for finite homotopy type, which is stronger than having finite-dimensional homology groups.

## Application

The Čech complex of an entire sphere has infinitely many vertices. A finite homotopy model would show that its topology at a fixed scale can nevertheless be represented by a finite object, clarifying what finite computations in topological data analysis aim to approximate.

## References

1. H. Adams, E. Jauhari and S. Mallick, [Homotopy Connectivity of Čech Complexes of Spheres](https://doi.org/10.1007/s00454-026-00847-5), Discrete & Computational Geometry (2026), Conjecture 8.4, PDF p.19; §§3.1–3.3 and 6. [Author version 2](https://arxiv.org/abs/2502.00122v2).
2. H. Adams, A. Karassev and Ž. Virk, [Vietoris thickenings and complexes of manifolds are homotopy equivalent](https://arxiv.org/abs/2512.23108v1), Corollary 3.2 and Lemma 3.4 (2025).
3. K. McCabe, [Lower Bounds for Approximating the Vietoris-Rips Filtration](https://arxiv.org/abs/2607.06524v1), §3.2 (2026).

## Status review

The circle case and small-scale sphere case are known. Reference [1] explicitly retains the general assertion. Open balls are essential: the analogous closed-ball assertion already fails for the circle.

Reference [2]'s homotopy equivalence with a metric thickening and absolute-neighborhood-retract result do not supply a finite model. Reference [3] concerns the size of approximating filtrations of finite metric spaces; it does not decide this fixed-scale assertion for an entire sphere. The target differs from the Rips-complex question in problem 520. No matching solution announcement was found as of the check date.
