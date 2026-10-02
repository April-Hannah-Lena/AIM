# 580. Infinitely many obstacle resonances in a fixed strip under trapping

**Area:** Scattering theory and numerical wave propagation

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`K\subset\mathbb R^3`$ be the closure of a bounded open set with smooth boundary and connected exterior $`\Omega=\mathbb R^3\setminus K`$. Consider the Dirichlet Laplacian $`-\Delta_D`$ on $`\Omega`$. Let $`\mathop{\mathrm{Res}}\nolimits(K)`$ be its scattering resonances, the poles of the meromorphic continuation of the outgoing resolvent

```math
(-\Delta_D-z^2)^{-1}:L^2_{\mathrm{comp}}(\Omega)\longrightarrow H^2_{\mathrm{loc}}(\Omega),
```

continued from $`\mathop{\mathrm{Im}}\nolimits z>0`$ with the outgoing convention $`e^{izr}/r`$.

Suppose the exterior billiard dynamics is trapping: there is a geometric-optics ray which remains in a bounded region for all forward time, with specular reflection at regular boundary encounters (and the generalized-ray interpretation at tangencies).

Prove or disprove the modified Lax–Phillips conjecture in dimension three: there exists $`C=C(K)>0`$ such that

```math
\#\{z\in\mathop{\mathrm{Res}}\nolimits(K):-C\le\mathop{\mathrm{Im}}\nolimits z<0\}=\infty.
```

The strip width may depend on the obstacle. The claim does not require resonances whose imaginary parts approach zero.

## Application

A resonance records an oscillation frequency and decay rate of scattered waves. This conjecture asks whether geometric trapping always creates infinitely many high-frequency modes whose decay rates stay bounded. It provides a qualitative target for numerical resonance computations on complicated obstacle geometries.

## References

1. C. J. S. Alves and P. R. S. Antunes, [Wave scattering problems in exterior domains with the method of fundamental solutions](https://doi.org/10.1007/s00211-024-01395-x), *Numerische Mathematik* **156** (2024), 375–394. Section 5.2, Conjecture 1, page 386.
2. M. Ikawa, [On poles of scattering matrices for several convex bodies](https://www.numdam.org/item/10.5802/jedp.388.pdf), *Journées Équations aux dérivées partielles* (1990), exposition VI. Uses the opposite sign convention for resonances.
3. Y. Chaubet and V. Petkov, [Dynamical zeta functions for billiards](https://doi.org/10.5802/aif.3743), *Annales de l'Institut Fourier* **76** (2026), 1537–1592; [author manuscript](https://www.math.u-bordeaux.fr/~vpetkov/publications/AIF.zeta.pdf), introduction and Section 5.
4. V. Petkov, [Dirichlet dynamical zeta function for billiard flow](https://arxiv.org/abs/2501.03818), 2025.

## Status review

**Known cases:** Important obstacle classes are known, including two separated strictly convex obstacles and finite collections of strictly convex real-analytic obstacles satisfying the non-eclipse condition. Reference [3] establishes the latter result; [4] supplies further sufficient dynamical conditions.

**Remaining target:** Prove the fixed-strip assertion for arbitrary smooth trapping obstacles. The results above do not cover this class.

The original stronger expectation of resonances approaching the real axis fails for some hyperbolic trapping configurations. The fixed-strip statement above is the modified conjecture. It also differs from asking for a resonance-free strip under uniformly hyperbolic trapping: both a small empty strip and a wider strip containing infinitely many resonances can coexist.

No complete resolution or matching announcement was found in current literature, arXiv, author-hosted papers, public GitHub or native Palomar searches. Zenodo's native API returned HTTP 403; indexed hits concerned unrelated arithmetic scattering and Riemann-hypothesis claims. No equivalent catalogue entry was found.
