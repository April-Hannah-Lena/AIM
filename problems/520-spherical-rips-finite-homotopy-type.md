# 520. Finite homotopy models for spherical Rips complexes

**Area:** Applied and computational topology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For an integer $n\ge2$, equip the unit sphere $S^n\subset\mathbb R^{n+1}$ with its round geodesic distance $d(x,y)=\arccos\langle x,y\rangle$, so its diameter is $\pi$. For $r>0$, let

$$
\mathop{\mathrm{VR}}\nolimits_{<}(S^n;r)=\{\sigma\subset S^n:\sigma\text{ is finite and }\mathop{\mathrm{diam}}\nolimits(\sigma)<r\}.
$$

Use the ordinary geometric realization of this abstract simplicial complex, with its CW topology.

Is $|\mathop{\mathrm{VR}}\nolimits_{<}(S^n;r)|$ homotopy equivalent to a finite CW complex for every $n\ge2$ and every $r>0$? The finite model may depend on both $n$ and $r$, and no uniform bound on its dimension or number of cells is requested. Prove the assertion or give a counterexample.

This is the higher-dimensional, positive-scale part of Conjecture 7.3 in [1]. Finiteness of Betti numbers alone does not supply the required homotopy equivalence.

## Application

Vietoris–Rips complexes are used to compute persistent homology from sampled data. A round sphere is a basic model for the underlying shape, but the complex on all of its points has infinitely many vertices and unbounded dimension. The question asks whether its topology at each scale nevertheless admits a finite model, supporting a precise understanding of what finite computations approximate.

## References

1. H. Adams, J. Bush and Ž. Virk, [The connectivity of Vietoris–Rips complexes of spheres](https://doi.org/10.1007/s41468-025-00214-y), Journal of Applied and Computational Topology **9**, article 15 (2025). Conjecture 7.3, p.21; conventions and background, pp.2–9. [arXiv:2407.15818v2](https://arxiv.org/abs/2407.15818v2).
2. M. Adamaszek and H. Adams, [The Vietoris–Rips complexes of a circle](https://msp.org/pjm/2017/290-1/pjm-v290-n1-p01-s.pdf), Pacific Journal of Mathematics **290** (2017), 1–40.

## Status review

The circle case is known by [2], and [1] retains the higher-dimensional conjecture. Small scales recover the sphere; the unresolved assertion includes all larger positive scales. The strict diameter inequality is essential: with the non-strict convention, critical circle scales already produce infinite wedges of spheres. The metric is geodesic, and the topology here is the simplicial CW topology.

The published conjecture, its arXiv version and later literature were checked on 24 September 2026. Searches including indexed arXiv, Zenodo, GitHub and Palomar found no matching resolution or announced solution. Recent coindex bounds and results for ellipses, discrete grids or different metric thickenings do not establish the displayed assertion.
