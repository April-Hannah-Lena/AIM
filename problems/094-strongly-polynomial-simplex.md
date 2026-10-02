# 094. A strongly polynomial pivot rule for the simplex method

**Area:** Numerical optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Given rational $`A\in\mathbb Q^{m\times n}`$ of full row rank, $`b\in\mathbb Q^m`$, $`c\in\mathbb Q^n`$, and an initial feasible basis for

```math
\min\{c^Tx:Ax=b,\ x\ge0\},
```

assume the optimal value is finite. Is there a deterministic simplex pivot rule that reaches an optimal basis using a number of rational arithmetic operations and comparisons bounded by a polynomial in $`m+n`$ alone, with every intermediate rational having bit length polynomial in the total input bit length? Successive bases must be connected by ordinary feasible simplex pivots along nonincreasing objective values; degenerate pivots are permitted. Rule selection and auxiliary computations count toward the bound, so a pivot oracle of unbounded computational cost is not allowed.

## Application

The simplex method is central to practical linear optimization. Such a rule would give a worst-case guarantee independent of numerical coefficient sizes.

## References

- [Alexander E. Black, *Exponential Lower Bounds for Many Pivot Rules for the Simplex Method* (2024), abstract and introduction](https://arxiv.org/abs/2403.04886).
- [Yann Disser, Georg Loho, Matthew Maat and Nils Mosis, *Lower Bounds for Ranking-Based Pivot Rules* (STACS, 2026), abstract and problem context](https://doi.org/10.4230/LIPIcs.STACS.2026.31).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The February 2026 paper explicitly lists polynomial simplex pivot rules as an open problem and proves lower bounds for a family of rules. Lower bounds for named rules do not rule out every possible rule. Strongly polynomial algorithms for restricted LP classes, and a recent substitution-method preprint, do not supply a general strongly polynomial simplex pivot rule.

Status-search topics (2026-09-08): `linear programming strongly polynomial open problem site.arxiv.org`; `strongly polynomial pivot rule 2026 simplex`. This is a literature search, not a proof that no solution exists.
