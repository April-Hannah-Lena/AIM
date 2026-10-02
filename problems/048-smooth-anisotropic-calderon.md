# 048 — Smooth anisotropic Calderón uniqueness

**Area:** Inverse problems / anisotropic imaging

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`M`$ be a compact connected smooth manifold of dimension $`n\geq3`$ with nonempty smooth boundary. For a smooth Riemannian metric $`g`$, define $`\Lambda_g f=\partial_{\nu_g}u|_{\partial M}`$, where $`\Delta_g u=0`$ and $`u|_{\partial M}=f`$. Consider two metrics inducing the same boundary metric, so their boundary operators have the same interpretation.

Does $`\Lambda_{g_1}=\Lambda_{g_2}`$ imply the existence of a smooth diffeomorphism $`F:M\to M`$, with $`F|_{\partial M}=\mathrm{Id}`$, such that $`g_1=F^*g_2`$? The data consist of this single zero-frequency boundary operator for each metric.

## Application

Anisotropic electrical conductivity depends on direction as well as position. This question specifies the unavoidable coordinate ambiguity in recovering it from boundary electrical measurements.

## References

1. J. M. Lee and G. Uhlmann, *Determining anisotropic real-analytic conductivities by boundary measurements*, Communications on Pure and Applied Mathematics **42** (1989), 1097–1112. [Paper](https://doi.org/10.1002/cpa.3160420804).
2. Y. Yi, *Riemannian and Lorentzian Calderón Problem Under Magnetic Perturbation*, IMRN **2025**, rnaf366, §1.1. [Paper](https://doi.org/10.1093/imrn/rnaf366).

## Status review

**Known cases:** The cited Lee-Uhlmann theorem establishes uniqueness in its real-analytic setting.

**Remaining target:** Uniqueness up to a boundary-fixing diffeomorphism for arbitrary smooth metrics from the single stated boundary map.

**Literature check:** Open in cited literature; no later resolution located

Yi's December 2025 introduction explicitly identifies the smooth higher-dimensional Riemannian Calderón problem as open. The analytic theorem in reference 1 requires analyticity. Yi obtains metric recovery using a family of magnetic perturbations and their boundary maps, which supplies additional data absent here.

On 2026-09-08 the review searched `Riemannian Calderon smooth anisotropic uniqueness 2025 2026` and `Riemannian and Lorentzian Calderón Problem Under Magnetic Perturbation`. No full smooth single-map resolution was located. Singular cloaking coefficients and disjoint-data counterexamples do not satisfy this formulation.
