# 426. Existence of a nonaffine polynomial minimal graph

**Area:** Quasilinear elliptic PDEs / minimal interfaces

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Does there exist an integer $n\ge8$ and a real polynomial $P:\mathbb R^n\to\mathbb R$ of degree at least two satisfying the polynomial identity
$$\big(1+|\nabla P|^2\big)\Delta P-\sum_{i,j=1}^nP_{x_i}P_{x_j}P_{x_ix_j}=0?$$
Equivalently, the entire scalar graph $\{(x,P(x)):x\in\mathbb R^n\}$ must have zero mean curvature. The unknown is an exact polynomial solution, not a smooth solution bounded by a polynomial.

## Application

The minimal-surface equation governs isotropic interface equilibrium. An exact nonplanar polynomial graph would supply an explicit equilibrium and a concrete test case for geometric PDE analysis and interface approximation.

## References

1. Y. Guo, *On polynomial solutions to the minimal surface equation*, Calculus of Variations and Partial Differential Equations 65 (2026), 141, §1.1, Definition 1 and Theorems 1.1–1.3. [DOI](https://doi.org/10.1007/s00526-026-03316-2); [revised full text](https://arxiv.org/html/2404.00115v2).
2. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.1, polynomial-solution question. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
3. L. Simon, *The minimal surface equation*, in *Geometry V*, Encyclopaedia of Mathematical Sciences 90 (1997), 239–266, discussion of entire graphs and polynomial solutions. [Chapter DOI](https://doi.org/10.1007/978-3-662-03484-2_5).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The March 2026 revision explicitly reports that no nonaffine scalar polynomial example is known. It rules out degrees two and three, homogeneous polynomials, and several possible tangent cones without resolving existence. Searches through 22 September 2026 found no later construction or general nonexistence theorem. Polynomial growth of all smooth entire graphs is a separate open assertion.
