# 248 — The full three-dimensional Newton minimum-resistance problem

**Area:** Calculus of variations / aerodynamic shape optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Write $D=\{x\in\mathbb R^2:|x|<1\}$. For each height $M>0$, let $\mathcal U_M$ consist of concave functions $u:D\to[0,M]$. Determine the exact minimum

$$
\inf_{u\in\mathcal U_M} J(u),\qquad J(u)=\int_D\frac{1}{1+|\nabla u(x)|^2}\,dx,
$$

and characterize all minimizing functions, up to rotations of $D$. The gradient is the almost-everywhere gradient of a concave function. No axial or other symmetry is assumed.

This is the convex-body formulation of Newton's resistance functional for a body with circular base and bounded height in a dilute, parallel particle stream.

## Application

The functional models momentum transfer to a moving convex body. Determining its true optimizers would give a benchmark for global shape optimization beyond prescribed symmetry classes.

## References

1. G. Wachsmuth, *New numerical solutions to Newton's problem of least resistance via a convex hull approach* (2025), [arXiv:2511.09177](https://arxiv.org/abs/2511.09177), §1. Gives the full variational model and identifies its unresolved optimizer structure.
2. L. Lokutsievskiy, G. Wachsmuth and M. Zelikin, *Non-optimality of conical parts for Newton's problem of minimal resistance in the class of convex bodies and the limiting case of infinite height* (2022), [Calculus of Variations 61, article 31](https://doi.org/10.1007/s00526-021-02118-y), §§5–6; [author manuscript](https://arxiv.org/abs/2009.12128). Rules out earlier proposed structures.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 numerical study treats the unrestricted problem as open. Classical rotationally symmetric solutions and later numerical candidates do not establish this global optimum. The 2022 paper also excludes conical pieces occurring in earlier candidate descriptions. Searches included “Newton minimal resistance open problem 2025 2026”, “Newton problem resistance solved convex bodies”, and the two cited titles. A 2026 Lorentz–Minkowski variant concerns a different ambient model. No exact all-height solution of the stated Euclidean problem was located.
