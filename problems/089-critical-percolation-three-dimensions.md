# 089. Absence of an infinite cluster at criticality in three-dimensional percolation

**Area:** Random media

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Independently retain each nearest-neighbor edge of $`\mathbb Z^3`$ with probability $`p`$. Let $`\theta(p)=\mathbb P_p(0\leftrightarrow\infty)`$ and $`p_c=\inf\{p\in[0,1]:\theta(p)>0\}`$, where $`0\leftrightarrow\infty`$ means that the open connected component containing the origin has infinitely many vertices. Prove or disprove

```math
\theta(p_c)=0.
```

The graph is the ordinary cubic lattice with only edges of Euclidean length one. This excludes long-range, hierarchical, slab and dependent percolation models.

## Application

The question asks whether the onset of macroscopic connectivity in a simple model of a porous medium is continuous.

## References

- [Tom Hutchcroft, *Power-law bounds for critical long-range percolation below the upper-critical dimension* (Probability Theory and Related Fields, 2021), introduction and discussion of nearest-neighbor percolation on Z³](https://doi.org/10.1007/s00440-021-01043-7).
- [Hugo Duminil-Copin, Vladas Sidoravicius and Vincent Tassion, *Absence of infinite cluster for critical Bernoulli percolation on slabs* (2014 preprint), introduction](https://www.ihes.fr/~duminil/publi/2014criticalslab.pdf).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The first source explicitly contrasts long-range continuity with the open nearest-neighbor problem, including Z³. Slab results and recent hierarchical or Gaussian-free-field percolation results have different graphs or laws. Targeted searches through 2026 found no resolution of nearest-neighbor Bernoulli percolation at p_c in Z³.

Status-search topics (2026-09-08): `Critical percolation Z^3 open problem`; `critical percolation three dimensions open 2025 2026`; `critical percolation Z3 2026 open`. This is a literature search, not a proof that no solution exists.
