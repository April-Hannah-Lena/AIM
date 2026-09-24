# 048 — Calderón uniqueness for bounded measurable conductivities

**Area:** Inverse problems / electrical impedance tomography

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected domain with smooth boundary. For a real scalar conductivity $`\gamma\in L^\infty(\Omega)`$ satisfying $`0<c\leq\gamma\leq C<\infty`$ almost everywhere, let $`u_f\in H^1(\Omega)`$ solve

```math
\nabla\cdot(\gamma\nabla u_f)=0,\qquad u_f|_{\partial\Omega}=f.
```

For $`f,h\in H^{1/2}(\partial\Omega)`$, define the weak Dirichlet-to-Neumann map by
$`\langle\Lambda_\gamma f,h\rangle=\int_\Omega\gamma\nabla u_f\cdot\nabla v_h\,dx`$, where $`v_h`$ is any $`H^1`$ extension of the boundary trace $`h`$. Prove or disprove that

```math
\Lambda_{\gamma_1}=\Lambda_{\gamma_2}\quad\Longrightarrow\quad
\gamma_1=\gamma_2\ \text{almost everywhere in }\Omega
```

for every pair of such conductivities. No continuity, derivative, or known partition assumption is imposed.

## Application

This asks whether ideal boundary voltage/current measurements can distinguish arbitrary bounded heterogeneous conductors, including discontinuous tissue or material coefficients.

## References

1. G. Uhlmann, *30 Years of Calderón's Problem* (2013), discussion of low regularity after the uniqueness theorems. [Authoritative lecture proceedings](https://www.numdam.org/article/SLSEDP_2012-2013____A13_0.pdf).
2. P. Caro, M. Á. García-Ferrero and K. M. Rogers, *Reconstruction for the Calderón problem with Lipschitz conductivities*, Analysis & PDE **18** (2025), 2033–2060, introduction and main theorem. [Paper](https://doi.org/10.2140/apde.2025.18.2033); [preprint](https://arxiv.org/abs/2401.06120).

## Status review

**Known cases:** Uniqueness and reconstruction are established for Lipschitz conductivities, which belong to the displayed bounded measurable class.

**Remaining target:** Uniqueness for arbitrary uniformly positive bounded measurable conductivities in three dimensions.

**Literature check:** Open in cited literature; no later resolution located

Uhlmann identifies rough-conductivity uniqueness as open; the older discussion also includes Lipschitz coefficients, which have since been resolved. The 2025 paper explicitly explains that higher-dimensional uniqueness still requires regularity and proves reconstruction for Lipschitz conductivities. That theorem does not cover arbitrary $`L^\infty`$ coefficients. The two-dimensional bounded-conductivity theorem is also outside this three-dimensional statement.

Searches on 2026-09-08 included `Calderon problem L infinity conductivities dimension three remains open 2025 2026`, `Calderón bounded open 2025 conductivity uniqueness`, and the exact 2025 paper title. No resolution of the stated measurable three-dimensional case was located. This is a literature status, not a certificate of nonexistence of a proof.
