# 486. Global classical Maxwell–Stefan diffusion with arbitrary pair friction

**Area:** Cross-diffusion PDEs; gas mixtures

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^3$ be bounded with smooth boundary, and let $N\ge4$. Fix arbitrary constants $f_{ij}=f_{ji}>0$ for $i\ne j$. The mole fractions $x_i$ and fluxes $J_i$ satisfy

$$
\partial_t x_i+\nabla\cdot J_i=0,\qquad
\nabla x_i=\sum_{j\ne i}f_{ij}(x_iJ_j-x_jJ_i),\qquad
\sum_{i=1}^N x_i=1,\quad \sum_{i=1}^N J_i=0.
$$

Impose $J_i\cdot\nu=0$ on $\partial\Omega$. For every smooth initial composition with $x_{i,0}\ge\delta>0$, $\sum_i x_{i,0}=1$, and the no-flux compatibility condition, does the unique local classical solution continue to every finite time, remaining classical and strictly positive on $\overline\Omega\times[0,T]$ for each $T<\infty$?

There are no chemical reactions or bulk advection. In particular, do not impose the special representation $f_{ij}=g_i+g_j$ or closeness of the initial data to a constant composition.

## Application

Maxwell–Stefan equations describe coupled diffusion in multicomponent mixtures, including diffusion of a species against its own concentration gradient. Global smoothness would justify the continuum constitutive law for large concentration variations.

## References

1. E. S. Daus, A. Jüngel and B. Q. Tang, *Exponential time decay of solutions to reaction-cross-diffusion systems of Maxwell–Stefan type*, Arch. Ration. Mech. Anal. **235** (2020), Remark 2. [Full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7021190/).
2. D. Bothe, *Global strong solutions for Maxwell–Stefan diffusion with additive friction coefficients* (2026 preprint), §1 and its main theorem. [arXiv:2609.06732](https://arxiv.org/abs/2609.06732).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The older existence theory gives weak solutions and local classical solutions, with a general classical continuation problem remaining. The search on 2026-09-22 located Bothe’s September 2026 preprint and checked its coefficient assumptions: its global theorem requires additive pair friction. The statement above retains arbitrary positive symmetric pair friction and $N\ge4$, where additivity is a genuine restriction. Neither that theorem nor near-equilibrium global results settle this formulation. The recent result is cited as a preprint, rather than silently treating its special case as still open.
