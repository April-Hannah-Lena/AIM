# 004. Pólya–Szegő polygonal Faber–Krahn conjecture

**Area:** Spectral shape optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix an integer $n\ge5$ and an area $A>0$. For every simple planar polygon $P$ with exactly $n$ sides and area $A$, let $\lambda_1(P)$ be the least eigenvalue of $-\Delta$ with zero Dirichlet boundary values. If $R_n$ is the regular $n$-gon of area $A$, prove or disprove

$$\lambda_1(P)\ge\lambda_1(R_n),$$

with equality only for polygons congruent to $R_n$. The polygon need not be convex.

## Application

This is a design question for membranes and waveguides manufactured with a prescribed number of straight edges: which shape gives the lowest fundamental frequency?

## References

1. B. Bogosel and D. Bucur, [On the polygonal Faber–Krahn inequality](https://numdam.org/articles/10.5802/jep.250/), Journal de l’École polytechnique — Mathématiques 11 (2024), 19–105, §1. It states the conjecture and traces it to G. Pólya and G. Szegő, Isoperimetric Inequalities in Mathematical Physics (1951), p. 158.
2. M. Levitin, D. Mangoubi and I. Polterovich, [Topics in Spectral Geometry](https://michaellevitin.net/Book/TSG230529.pdf), AMS (2023), Conjecture 5.1.19.
3. B. Bogosel and D. Bucur, [Polygonal Faber–Krahn inequality: local minimality via validated computing](https://github.com/beniamin-bogosel/PolyaSzego), accompanying author code and paper description (2024).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book and 2024 paper distinguish the open n≥5 problem from the solved triangular and quadrilateral cases. Validated computations establish local minimality for specified regular polygons; local minimality does not establish the global inequality. A July 2026 tangential-polygon paper found in the update search gives a sufficient criterion, rather than arbitrary polygons.

**Search audit:** “Pólya Szegő polygon eigenvalue conjecture 2025 2026”; “polygonal Faber Krahn global proof”; “Pólya Szegő tangential polygons”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
