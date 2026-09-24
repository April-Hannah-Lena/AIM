# 250 — Maximum convex-hull volume for a closed curve of fixed length

**Area:** Geometric optimization / spatial enclosures

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\gamma:[0,1]\to\mathbb R^3$ range over continuous rectifiable curves with $\gamma(0)=\gamma(1)$ and $\operatorname{Length}(\gamma)=1$. Determine

$$
V_* =\sup_\gamma\operatorname{Vol}_3\bigl(\operatorname{conv}(\gamma([0,1]))\bigr),
$$

and characterize the maximizing curves up to rigid motion and reparametrization. Self-intersections are allowed; no symmetry or bound on the number of intersections with a plane is assumed.

## Application

The problem asks how much spatial volume a closed wire or cyclic sampling trajectory can enclose through its convex hull for a fixed total length.

## References

1. J. Bohr, S. Markvorsen and M. Raffaelli, *The convex hull of a convex space curve with four vertices* (2026), [Bulletin of the London Mathematical Society 58, e70311](https://doi.org/10.1112/blms.70311), §1, Problem 1.1 and Theorem 1.2. Restates the general problem and proves a bound under additional geometric assumptions.
2. Z. A. Melzak, *The isoperimetric problem of the convex hull of a closed space curve* (1960), [Proceedings of the AMS 11, 265–274](https://doi.org/10.1090/S0002-9939-1960-0116263-0), opening classification and the symmetry-constrained three-dimensional problem.
3. H. T. Croft, K. J. Falconer and R. K. Guy, *Unsolved Problems in Geometry* (1991), [Springer monograph](https://doi.org/10.1007/978-1-4612-0963-8), §A28. Classical book source; also identified by the 2026 paper.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Bohr–Markvorsen–Raffaelli explicitly retain the full question in 2026. Their estimate concerns simple curves on the hull boundary with precisely four torsion zeros. Older results for open arcs, special symmetry, or restricted hyperplane intersections do not cover the present class. Searches included “convex hull closed curves volume 2025 2026”, “Melzak convex hull maximum volume solution”, and the 2026 paper's title. No unrestricted sharp value was located.
