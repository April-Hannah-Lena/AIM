# 548. Monotonicity of connectivity in spherical Čech filtrations

**Area:** Applied and computational topology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For an integer $`n\ge2`$, equip the unit sphere $`S^n\subset\mathbb R^{n+1}`$ with the geodesic distance $`d(x,y)=\arccos\langle x,y\rangle`$. For $`r>0`$, define the intrinsic open Čech complex

```math
C_n(r)=\left\{\sigma\subset S^n:\sigma\text{ is finite and }\bigcap_{x\in\sigma}\{z\in S^n:d(x,z)<r\}\ne\varnothing\right\}.
```

Use its ordinary geometric realization with the CW topology, and write $`|C_n(r)|`$ for that space.

For a path-connected space $`Y`$, let

```math
\mathop{\mathrm{conn}}\nolimits(Y)=\sup\{k\in\mathbb Z_{\ge0}:\pi_i(Y,y_0)=0\text{ for all }1\le i\le k\},
```

allowing the value $`+\infty`$. The complexes above are path-connected at positive scales.

Prove or refute that for every $`n\ge2`$ and every $`0<r<s<\pi`$,

```math
\mathop{\mathrm{conn}}\nolimits(|C_n(r)|)\le\mathop{\mathrm{conn}}\nolimits(|C_n(s)|).
```

The intersection defining a simplex is taken inside the sphere, using open geodesic balls. This is Conjecture 8.1 of [1], restricted to the unresolved dimensions.

## Application

Čech filtrations describe the topology inferred from data as a neighborhood radius grows. Monotonicity would rule out the reappearance of low-dimensional homotopy after it has vanished in the filtration of an entire round sphere, constraining a basic model used to interpret spherical data.

## References

1. H. Adams, E. Jauhari and S. Mallick, [Homotopy Connectivity of Čech Complexes of Spheres](https://doi.org/10.1007/s00454-026-00847-5), Discrete & Computational Geometry (2026), Conjecture 8.1, PDF p.19; definitions, §§3.1–3.3. [Author version 2](https://arxiv.org/abs/2502.00122v2).
2. H. Adams, A. Karassev and Ž. Virk, [Vietoris thickenings and complexes of manifolds are homotopy equivalent](https://arxiv.org/abs/2512.23108v1), Corollaries 3.2 and 3.6 (2025).

## Status review

The circle case is known. Reference [1] establishes covering-number bounds and infinitely many homotopy-type changes, but leaves the stated monotonicity conjecture open. Reference [2] identifies complexes with their metric thickenings; it does not establish monotonicity across scales.

The source's April 2026 revision and published statement agree. Later-work, author-page and announcement checks found no matching resolution as of the check date. This concerns common intersections of balls, rather than the pairwise diameter condition in problem 521.
