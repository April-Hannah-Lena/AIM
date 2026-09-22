# 099. The dimension-free Kannan–Lovász–Simonovits inequality

**Area:** High-dimensional probability and sampling

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a universal constant $C<\infty$ such that, for every $n\ge1$, every probability density $e^{-V}$ on $\mathbb R^n$ with convex extended-real $V$, mean zero and covariance $I_n$, and every smooth compactly supported $f:\mathbb R^n\to\mathbb R$,
$$
\operatorname{Var}_\mu(f)
:=\int f^2\,d\mu-\left(\int f\,d\mu\right)^2
\le C\int|\nabla f|^2\,d\mu?
$$
Extended-real convex potentials include uniform measures on convex bodies. The same $C$ must work in all dimensions and for all such densities and functions. This is the Poincaré formulation of KLS.

## Application

A dimension-free spectral gap would strengthen guarantees for sampling log-concave distributions and for concentration in high-dimensional inference.

## References

- [Boaz Klartag and Joseph Lehec, *Isoperimetric inequalities in high-dimensional convex sets* (Bulletin of the AMS, 2025), KLS survey](https://doi.org/10.1090/bull/1869).
- [Brayden Letwin, *The KLS constant is O(log¹⁄⁴ n)* (July 2026), abstract and main result](https://arxiv.org/abs/2607.24164).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The July 2026 preprint establishes the conjectured variance bound for quadratic forms and improves a dimension-dependent KLS bound. It does not provide a dimension-free inequality for arbitrary smooth f. Bourgain's slicing problem is a separate, weaker problem and is not listed here as open.

Status-search topics (2026-09-08): `KLS conjecture 2026 solved`; `KLS 2026 site.arxiv.org`; `The KLS constant is Guan`. This is a literature search, not a proof that no solution exists.
