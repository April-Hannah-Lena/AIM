# 095. The planar Mumford–Shah regularity conjecture

**Area:** Image segmentation and fracture

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^2$ be bounded and smooth and $g\in L^\infty(\Omega)$. Minimize
$$
\mathcal F(u,K)=\int_{\Omega\setminus K}
\big(|\nabla u|^2+|u-g|^2\big)\,dx+\mathcal H^1(K)
$$
over relatively closed sets $K\subset\Omega$ of finite length and $u\in H^1(\Omega\setminus K)$. Use a reduced minimizer: remove irrelevant zero-length additions to $K$ and take $K$ to be the support in $\Omega$ of $\mathcal H^1\!\restriction K$.
Must $K$ locally consist of finitely many embedded $C^1$ arcs whose only interior singularities are isolated free endpoints and junctions of three arcs with pairwise tangent angles $120^\circ$? In particular, neither singularities nor distinct components may accumulate inside $\Omega$. The assertion concerns the interior, not boundary regularity.

## Application

The functional is a standard model for image edges and brittle cracks. The conjecture predicts a finite, interpretable local structure for optimal discontinuity sets.

## References

- [Camillo De Lellis and Matteo Focardi, *The Regularity Theory for the Mumford–Shah Functional on the Plane* (EMS Monographs in Mathematics 13, 2025), Chapter 1](https://doi.org/10.4171/EMM/13).
- [Camille Labourie and Antoine Lemenant, *Finite number of traces for Mumford–Shah minimizers in dimension 2* (Comptes Rendus Mathématique, 2026), introduction](https://doi.org/10.5802/crmath.826).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 monograph treats the conjecture and its equivalent global-minimizer classifications. The April 2026 paper bounds the number of limit values near the singular set; this does not give its complete arc/junction structure. The full planar regularity conjecture was not resolved in the later literature located.

Status-search topics (2026-09-08): `Mumford-Shah conjecture 2026`; `The Regularity Theory for the Mumford–Shah Functional on the Plane authors`. This is a literature search, not a proof that no solution exists.
