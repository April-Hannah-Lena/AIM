# 511. Monotonicity of connectivity in spherical Rips filtrations

**Area:** Applied and computational topology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Give the unit sphere $`S^n\subset\mathbb R^{n+1}`$ its geodesic metric $`d(x,y)=\arccos\langle x,y\rangle`$. For $`r>0`$, let $`K_n(r)`$ be the ordinary geometric realization, with the CW topology, of the abstract simplicial complex whose vertices are all points of $`S^n`$ and whose simplices are the finite subsets of diameter strictly less than $`r`$.

For a path-connected space $`Y`$, define

```math
\mathop{\mathrm{conn}}\nolimits(Y)=\sup\{k\in\mathbb Z_{\ge0}:\pi_i(Y,y_0)=0\text{ for every }1\le i\le k\},
```

with value $`+\infty`$ if all these homotopy groups vanish. The spaces $`K_n(r)`$ are path-connected for $`r>0`$.

Prove or refute the assertion that, for every integer $`n\ge2`$ and every $`0<r<s`$,

```math
\mathop{\mathrm{conn}}\nolimits(K_n(r))\le\mathop{\mathrm{conn}}\nolimits(K_n(s)).
```

This compares the first possible nonzero homotopy-group dimension at different scales. It does not assert that the inclusion $`K_n(r)\hookrightarrow K_n(s)`$ is a homotopy equivalence.

## Application

Increasing the scale in a Rips filtration fills in some holes while possibly creating others. The conjecture asks whether, on round spheres, new low-dimensional homotopy can appear after all homotopy in those dimensions has vanished. This would constrain the topology encountered when persistent-homology methods are applied to spherical data models.

## References

1. H. Adams, J. Bush and Ž. Virk, [The connectivity of Vietoris–Rips complexes of spheres](https://doi.org/10.1007/s41468-025-00214-y), Journal of Applied and Computational Topology **9**, article 15 (2025). Conjecture 7.1, p.21; §§1–2. [arXiv:2407.15818v2](https://arxiv.org/abs/2407.15818v2).
2. M. Adamaszek and H. Adams, [The Vietoris–Rips complexes of a circle](https://msp.org/pjm/2017/290-1/pjm-v290-n1-p01-s.pdf), Pacific Journal of Mathematics **290** (2017), 1–40.

## Status review

The circle case is known from [2]. Reference [1] explicitly restricts the surviving conjecture to round spheres: Hausmann's analogous question for arbitrary compact Riemannian manifolds has a counterexample. Its covering-radius bounds and proof of infinitely many homotopy-type changes do not establish monotonicity in scale.

Checks on 24 September 2026 compared the published and arXiv conjecture and searched for subsequent proofs, counterexamples and announcements, including indexed arXiv, Zenodo, GitHub and Palomar. No matching resolution was found. Monotonicity of equivariant coindex is a different property and does not settle this homotopy-connectivity question.
