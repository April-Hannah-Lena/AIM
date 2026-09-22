# 053 — Calderón uniqueness from an arbitrary local boundary patch

**Area:** Inverse problems / partial boundary data

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^n$, $n\geq3$, be a bounded connected smooth domain, and let $\Gamma$ be any nonempty relatively open subset of $\partial\Omega$. For a positive $\gamma\in C^\infty(\overline\Omega)$, impose smooth boundary voltages supported in $\Gamma$ and measure the flux on $\Gamma$:
$$
\Lambda^\Gamma_\gamma f
=\gamma\partial_\nu u_f|_\Gamma,\quad
\nabla\cdot(\gamma\nabla u_f)=0,\quad
u_f|_{\partial\Omega}=f\in C_c^\infty(\Gamma).
$$
Is $\Lambda^\Gamma_{\gamma_1}=\Lambda^\Gamma_{\gamma_2}$ sufficient to conclude $\gamma_1=\gamma_2$ throughout $\Omega$? No condition is imposed on the shape of the inaccessible boundary, and the conductivities need not be known near it.

## Application

In electrical imaging, electrodes may cover only one accessible part of an object. This isolates whether complete local experiments nevertheless determine its entire conductivity.

## References

1. C. Kenig and M. Salo, *Recent progress in the Calderón problem with partial data* (2014), §8, open problems. [Author manuscript](https://users.jyu.fi/~salomi/pub/calderon_partial_survey3.pdf).
2. C. Kenig and M. Salo, *The Calderón problem with partial data on manifolds and applications*, Analysis & PDE **6** (2013), 2003–2048. [Paper](https://msp.org/apde/2013/6-8/apde-v6-n8-p07-p.pdf).
3. Giovanni Covi, Antti Kujanpää and Jesse Railo, *Partial data stability for the inverse fractional conductivity problem* (2025), introduction comparing the classical problem. [Preprint](https://arxiv.org/abs/2505.18567).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Reference 1 explicitly lists the unrestricted partial-data problem. The 2025 comparison still describes classical partial-data uniqueness as unresolved in general. Existing reflection and Carleman-weight results impose geometric or measurement-set hypotheses; uniqueness for a linearization does not establish this nonlinear statement.

Searches on 2026-09-08 included `partial data Calderon arbitrary open boundary subset disjoint open problem 2025 2026`, `Calderón partial data open problem 2024`, and `Calderón arbitrary local 2026`. No proof for arbitrary $\Omega$ and $\Gamma$ was located. Fractional conductivity results concern a different forward operator.
