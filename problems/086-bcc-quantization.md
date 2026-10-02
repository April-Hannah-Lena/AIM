# 086. The optimal three-dimensional quadratic quantization constant

**Area:** Quantization and mesh generation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $`N\ge1`$, define

```math
q_N=\inf_{z_1,\ldots,z_N\in[0,1]^3}
\int_{[0,1]^3}\min_i|x-z_i|^2\,dx.
```

Let $`L_{\mathrm{BCC}}=2^{1/3}\big(\mathbb Z^3\cup(\mathbb Z^3+(1/2,1/2,1/2))\big)`$, which has one point per unit volume, and let $`V_{\mathrm{BCC}}`$ be the Voronoi cell of its origin. Prove or disprove

```math
\lim_{N\to\infty}N^{2/3}q_N
=\int_{V_{\mathrm{BCC}}}|x|^2\,dx.
```

The left side optimizes over arbitrary point sets. This is the energy-constant version of the three-dimensional Gersho/BCC conjecture, without additionally demanding congruence of every asymptotic cell.

## Application

The constant governs the best mean-square vector quantization error and informs three-dimensional centroidal Voronoi mesh design.

## References

- [Rustum Choksi and Xin Yang Lu, *Bounds on the Geometric Complexity of Optimal Centroidal Voronoi Tesselations in 3D* (2018 preprint; Communications in Mathematical Physics, 2020)](https://arxiv.org/abs/1806.07591).
- [David P. Bourne and Riccardo Cristoferi, *Asymptotic Optimality of the Triangular Lattice for a Class of Optimal Location Problems* (Communications in Mathematical Physics, 2021), discussion of three-dimensional Gersho's conjecture](https://doi.org/10.1007/s00220-021-04216-6).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Both references distinguish the still-open unrestricted three-dimensional problem from BCC optimality among lattices. The cited geometric-complexity bounds and computer-assisted proof proposal do not supply the claimed equality. Searches through 2026 located no completed resolution.

Status-search topics (2026-09-08): `Gersho conjecture three 2025 2026`; `Gersho three dimensions Choksi Lu`; `Bounds on the geometric complexity Choksi Lu`. This is a literature search, not a proof that no solution exists.
