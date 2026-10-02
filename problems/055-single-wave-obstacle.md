# 055 — Determine a smooth sound-soft obstacle from one far-field pattern

**Area:** Inverse obstacle scattering / acoustic detection

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix a wavenumber $`k>0`$ and direction $`\theta\in S^2`$. Let $`D\subset\mathbb R^3`$ be a bounded domain with smooth boundary and connected exterior. The total field satisfies

```math
(\Delta+k^2)u=0\text{ in }\mathbb R^3\setminus\overline D,
\quad u|_{\partial D}=0,
\quad u=e^{ikx\cdot\theta}+u^s,
```

where $`u^s`$ is outgoing. Let $`a_D(\omega;\theta,k)`$, $`\omega\in S^2`$, be its far-field amplitude, defined by $`u^s(r\omega)=r^{-1}e^{ikr}a_D(\omega;\theta,k)+O(r^{-2})`$.

Must $`a_{D_1}(\omega;\theta,k)=a_{D_2}(\omega;\theta,k)`$ for every observation direction $`\omega`$ imply $`D_1=D_2`$? Frequency and incident direction remain fixed, and no size bound relative to the wavelength is assumed.

## Application

This is the ideal identifiability limit for recovering the shape of an acoustically soft target from a single monochromatic illumination.

## References

1. D. Colton and R. Kress, *Looking Back on Inverse Scattering Theory*, SIAM Review **60** (2018), 779–807, §2 (author manuscript p. 4). [Survey](https://doi.org/10.1137/17M1144763), [author manuscript](https://num.math.uni-goettingen.de/kress/looking-back.pdf).
2. X. Cao, H. Diao and J. Li, *Some Recent Progress on Inverse Scattering Problems Within General Polyhedral Geometry*, Electronic Research Archive **29** (2021), 1753–1782. [Paper](https://doi.org/10.3934/era.2020090).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Colton–Kress explicitly identify uniqueness for one plane wave at one wavenumber as open in §2, directly after Theorem 2.2. The cited special uniqueness results require size or shape restrictions and do not cover arbitrary smooth obstacles. This scattering question is distinct from the overdetermined-eigenfunction conjecture also associated with Schiffer's name.

The review searched `inverse scattering single incident open 2026`, `Schiffer conjecture obstacle single`, and the exact title of reference 1 on 2026-09-08. Recent reconstruction algorithms and special geometries were located, but no unrestricted smooth-obstacle uniqueness theorem for one fixed plane wave was found.
