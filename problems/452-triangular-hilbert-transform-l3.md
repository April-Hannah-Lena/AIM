# 452. A uniform L3 estimate for the triangular Hilbert transform

**Area:** Multilinear harmonic analysis and coupled signal interactions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For Schwartz functions $f,g:\mathbb R^2\to\mathbb C$ and $0<\varepsilon<R<\infty$, set
$$H_{\varepsilon,R}(f,g)(x,y)=\int_{\varepsilon<|t|<R}f(x+t,y)g(x,y+t)\,\frac{dt}{t}.$$
Does there exist an absolute constant $C$ such that
$$\|H_{\varepsilon,R}(f,g)\|_{L^{3/2}(\mathbb R^2)}\le C\|f\|_{L^3(\mathbb R^2)}\|g\|_{L^3(\mathbb R^2)}$$
for every $f,g,\varepsilon,R$? The constant must be independent of both truncation scales.

## Application

This operator couples two signals sampled along crossing coordinate directions with a singular interaction kernel. Uniform control would supply a basic bound for modulation-sensitive multilinear interactions and encompass important Fourier reconstruction estimates.

## References

1. F. Yu-Hsiang Lin and L. Slavíková, [Rough averages of triangular Hilbert transforms](https://arxiv.org/abs/2607.20206), preprint (2026), §1, definition of H and discussion before (1.1).
2. P. Durcik, V. Kovač and C. Thiele, [Power-type cancellation for the simplex Hilbert transform](https://arxiv.org/abs/1608.00156), *Journal d’Analyse Mathématique* **139** (2019), 67–82, introduction and main theorem; [published article](https://doi.org/10.1007/s11854-019-0052-4).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The July 2026 paper explicitly says that bounds for the unaveraged triangular operator remain open for any admissible exponent triple. Its averaging theorem and the power improvement in truncation-length growth from the second reference do not yield the uniform bound above. Searches through the review date located no subsequent resolution.
