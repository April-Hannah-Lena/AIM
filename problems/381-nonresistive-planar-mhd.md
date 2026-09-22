# 381. Global regularity of viscous planar MHD without magnetic diffusion

**Area:** Magnetohydrodynamics; conducting fluids

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

For every divergence-free $u_0,b_0\in\bigcap_{k\ge0}H^k(\mathbb R^2;\mathbb R^2)$, does
$$\partial_tu+u\cdot\nabla u-\Delta u+\nabla P=b\cdot\nabla b,\qquad\partial_tb+u\cdot\nabla b=b\cdot\nabla u,\qquad\nabla\cdot u=\nabla\cdot b=0,$$
with $(u,b)(0)=(u_0,b_0)$ have a unique solution $(u,b)\in C([0,\infty);H^k\times H^k)$ for every integer $k\ge0$? The magnetic field has no diffusion or damping. No smallness, symmetry or imposed constant background field is allowed.

## Applied significance

Viscosity dissipates fluid motion while magnetic structures can retain fine scales. The question isolates whether this indirect dissipation prevents singular currents in a planar conducting fluid.

## References

1. X. Suo and Q. Jiu, [*Global well-posedness of 2D incompressible Magnetohydrodynamic equations with horizontal dissipation*](https://doi.org/10.3934/dcds.2022063), Discrete and Continuous Dynamical Systems 42 (2022), 4523–4553, §1, explicit open full-viscosity nonresistive problem.
2. Z. Ye, [*A new regularity criterion for the 2D non-resistive incompressible MHD equations*](https://doi.org/10.1016/j.jde.2024.05.030), Journal of Differential Equations 402 (2024), 625–640, introduction and main conditional criterion.

## Status review

Checked on 22 September 2026 using planar nonresistive MHD arbitrary-data global regularity and singularity formation. Ye resolves a specific conditional regularity question, not unconditional smooth existence. The September 2026 strip-domain result [DOI:10.1016/j.jde.2026.114428](https://doi.org/10.1016/j.jde.2026.114428) requires a sufficiently strong imposed magnetic field; it does not cover the decaying arbitrary fields above. No matching unrestricted theorem was located. Unlike the existing ideal-MHD problem, this system has full viscous dissipation of velocity.
