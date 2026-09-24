# 086. The three-dimensional lattice-periodic Kelvin problem

**Area:** Foams and geometric optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $L\subset\mathbb R^3$ range over full-rank lattices with covolume one. Let $E\subset\mathbb R^3$ range over bounded measurable sets of volume one and finite perimeter such that the translates $\{E+\ell:\ell\in L\}$ partition $\mathbb R^3$ up to sets of Lebesgue measure zero. Determine the exact value of
$$
\mathcal K_{\mathrm{lat},3}
=\inf_{(L,E)}\frac12\,\operatorname{Per}(E)
$$
and characterize the minimizing pairs, if the infimum is attained. Here $\operatorname{Per}(E)$ is the total variation of the distributional gradient of $1_E$; the factor $1/2$ counts each cell interface once. Curved interfaces and nonconvex cells are allowed.

## Application

This is a precise surface-energy minimization problem for periodic equal-volume foams and cellular materials.

## References

- [Annalisa Cesaroni and Matteo Novaga, *Minimal periodic foams with fixed inradius* (Mathematika, 2025), introduction and §5](https://doi.org/10.1112/mtk.70020).
- [Annalisa Cesaroni and Matteo Novaga, *Minimal periodic foams with equal cells* (2023 preprint; Springer INdAM Series, 2024), existence results and discussion of the isotropic case](https://arxiv.org/abs/2302.07112).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 paper explicitly leaves the lattice-periodic Kelvin problem open in dimensions at least three. Its existence theorem adds a fixed-inradius constraint. The earlier equal-cell paper proves existence results for the volume-constrained problem, but neither identifies the exact three-dimensional minimum and its optimizing shape. The Weaire–Phelan improvement of Kelvin's original proposal uses inequivalent cells and does not answer this single-cell lattice problem.

Status-search topics (2026-09-08): `Kelvin problem 2025 open`; `Minimal periodic foams with fixed inradius authors`. This is a literature search, not a proof that no solution exists.
