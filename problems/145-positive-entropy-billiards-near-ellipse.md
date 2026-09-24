# 145 — Positive metric entropy for billiards arbitrarily close to an ellipse

**Area:** Hamiltonian billiards / chaotic ray transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Can a smooth elliptical billiard be approximated by smooth strictly convex billiards with positive metric entropy?

Precisely, find a noncircular ellipse with boundary embedding $\gamma_E:S^1\to\mathbb R^2$ and smooth embeddings $\gamma_j$ bounding strictly convex domains $D_j$, such that $\gamma_j\to\gamma_E$ in $C^\infty$ and

$$
h_{\mu_j}(B_j)>0\qquad\text{for every }j.
$$

Here $B_j$ is the specular billiard collision map, with phase coordinates $(s,\varphi)$: boundary arclength $s$ and outgoing angle $\varphi\in(0,\pi)$ measured from the positive tangent. Its invariant probability measure is $d\mu_j=\sin\varphi\,ds\,d\varphi/(2|\partial D_j|)$, and $h_{\mu_j}$ is Kolmogorov–Sinai entropy.

The perturbation must come from changing the billiard table itself.

## Application

Elliptical optical cavities are integrable. The question asks whether arbitrarily small smooth changes of their shape can create chaotic transport on a set of positive physical phase-space measure.

## References

1. P. Berger, *Wild Dynamics on Manifolds* (ICM 2026), [Proceedings, volume 5, pp. 24–41](https://doi.org/10.1137/25M1810787), §2.3, Problem 2.17. Explicitly asks for a perturbation of an ellipse with positive metric entropy.
2. P. Berger and D. Turaev, *On Herman's positive entropy conjecture* (2019), [Advances in Mathematics 349, 1234–1288](https://doi.org/10.1016/j.aim.2019.04.002), main theorem. Gives positive-entropy perturbations among general area-preserving surface diffeomorphisms.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Berger's 2026 problem separates billiard-table perturbations from the established unrestricted symplectic-map perturbation theorem. A horseshoe or positive topological entropy can occur on a set of Liouville measure zero and does not answer this metric-entropy question. Searches included “ellipse billiard perturbation positive metric entropy 2026” and “Berger Problem 2.17 billiards solution”. No construction satisfying the stated approximation and measure requirements was located.
