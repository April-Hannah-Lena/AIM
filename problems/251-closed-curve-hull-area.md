# 251 — A sharp surface-area bound for the convex hull of a closed curve

**Area:** Geometric inequalities / enclosure design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\gamma:[0,1]\to\mathbb R^3$ be any continuous rectifiable closed curve, of length $L$, and put $K=\mathop{\mathrm{conv}}\nolimits(\gamma([0,1]))$. Define $A(K)$ to be the surface area of $\partial K$ when $K$ is three-dimensional, twice its planar area when it is two-dimensional, and zero otherwise. Is

$$
A(K)\leq \frac{L^2}{2\pi}
$$

always true? A planar circle attains equality. The curve need not lie on the boundary of its convex hull.

## Application

This would give an optimal surface-enclosure limit for a closed wire. Its polygonal form bounds the length of a tour through the vertices of a three-dimensional convex component.

## References

1. M. Ghomi, *Open problems in geometry of curves and surfaces* (2019 revision), [author survey](https://ghomi.math.gatech.edu/Papers/op.pdf), Problem 5.3, p. 14. Explicit continuous-curve conjecture.
2. M. Ghomi, *Shortest loop through vertices of a convex polytope* (2024), [author's expert problem statement](https://mathoverflow.net/questions/480430/shortest-loop-through-vertices-of-a-convex-polytope), question and discussion. Restates the equivalent polygonal inequality and the known boundary-contained case.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Ghomi's later statement still presents the inequality as unresolved. The classical nonpositive-curvature argument handles a simple curve on its hull boundary; a shortest tour can instead cut through the hull interior. Searches included “convex hull closed curve surface area inequality”, “Ghomi shortest loop polytope 2025 2026”, and “Tilli convex hull surface area”. No proof in the unrestricted class or violating curve was located.
