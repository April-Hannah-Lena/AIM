# 081. Global regularity of two-dimensional ideal incompressible MHD

**Area:** Magnetohydrodynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For every pair of divergence-free Schwartz fields $u_0,b_0:\mathbb R^2\to\mathbb R^2$, do the ideal magnetohydrodynamic equations
$$
u_t+(u\cdot\nabla)u+\nabla p=(b\cdot\nabla)b,\qquad
b_t+(u\cdot\nabla)b=(b\cdot\nabla)u,\qquad
\nabla\cdot u=\nabla\cdot b=0
$$
admit a global smooth finite-energy solution with $(u,b)(0)=(u_0,b_0)$? Both viscosity and magnetic resistivity are exactly zero. A finite-time singularity from data in this class would answer the question negatively.

## Application

The model describes the ideal coupling of conducting fluids and magnetic fields; current concentration is central to interpreting plasma computations.

## References

- [Shu-Guang Shao, Shu Wang, Wen-Qing Xu and Yu-Li Ge, *On the local C¹,α solution of ideal magneto-hydrodynamical equations* (DCDS, 2017), introduction's open-problem list](https://doi.org/10.3934/dcds.2017090).
- [D. Hirata, *A regularity criterion for the 2D inviscid MHD equations* (ZAMP, 2025)](https://doi.org/10.1007/s00033-024-02411-8).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2017 paper explicitly identifies two-dimensional ideal MHD as unresolved. The 2025 result is a continuation criterion controlled by the magnetic field. Searches through 2026 located dissipative/damped and stability theorems with extra assumptions, not unrestricted ideal evolution.

Searches run on 2026-09-08: `ideal MHD two-dimensional global regularity open 2026`; `Global regularity 2D MHD 2025 inviscid`. This is a literature search, not a proof that no solution exists.
