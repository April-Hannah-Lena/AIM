# 097. Cardy's crossing formula for square-lattice bond percolation

**Area:** Random media and conformal invariance

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $D\subset\mathbb C$ be a bounded simply connected smooth domain with four distinct boundary points $a,b,c,d$ in counterclockwise cyclic order. On the induced nearest-neighbor graph $D\cap\delta\mathbb Z^2$, declare each edge open independently with probability $1/2$. Let $P_\delta$ be the probability of an open path connecting the lattice approximations of boundary arcs $ab$ and $cd$; use vertices within $2\delta$ of those arcs. Choose a conformal map to the upper half-plane sending $(a,b,c,d)$ to $(0,\eta,1,\infty)$, with $0<\eta<1$. Prove or disprove
$$
\lim_{\delta\downarrow0}P_\delta
=\frac{\Gamma(2/3)}{\Gamma(1/3)\Gamma(4/3)}
\eta^{1/3}\,{}_2F_1(1/3,2/3;4/3;\eta).
$$
Here $\Gamma$ is the gamma function and $\,{}_2F_1$ the Gauss hypergeometric function.

## Application

In a planar random network, the crossing probability measures the chance that two boundary regions remain connected through open bonds. The formula would predict that probability from the large-scale shape alone in the fine-mesh limit, giving an explicit benchmark for connectivity simulations.

## References

- [Vincent Tassion, *Rotation invariance of critical planar percolation* (Séminaire Bourbaki, June 2023, exposé 1210), Conjecture 3.1](https://www.bourbaki.fr/TEXTES/Exp1210-Tassion.pdf).
- [Mikhail Khristoforov, Mikhail Skopenkov and Stanislav Smirnov, *A Generalization of Cardy's and Schramm's Formulae* (Communications in Mathematical Physics, 2025), triangular-lattice setting and references](https://doi.org/10.1007/s00220-025-05255-z).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The Bourbaki account formulates square-lattice conformal crossing convergence as a conjecture. The 2025 paper works with triangular-lattice site percolation. Rotation invariance, knowledge of p_c=1/2, and triangular-lattice results do not establish the square-lattice formula. Later searches found no resolution.

Status-search topics (2026-09-08): `Cardy square lattice conjecture site.arxiv.org`; `Cardy formula square lattice 2026 proof`; `square lattice Cardy 2025 open`. This is a literature search, not a proof that no solution exists.
