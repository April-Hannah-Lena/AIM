# 064 — Injectivity with attenuation of finite angular degree

**Area:** Attenuated tomography

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $M$ be a smooth compact oriented simple Riemannian surface, with strictly convex boundary and unique smoothly varying geodesics. Let $a\in C^\infty(SM;\mathbb C)$ have finite angular degree: there is a single integer $N\ge0$ such that its angular Fourier coefficients satisfy $a_k(x)=0$ for every $x\in M$ and $|k|>N$. For every maximal unit-speed boundary-to-boundary geodesic $\gamma:[0,\ell]\to M$, define

$$
I_af(\gamma)=\int_0^\ell
 \exp\!\left(\int_0^t a(\gamma(s),\dot\gamma(s))\,ds\right)f(\gamma(t))\,dt.
$$

For every such $a$, does $I_af=0$ imply $f=0$ for smooth scalar functions $f$ on $M$?

## Application

This asks when direction-dependent absorption permits unique recovery of an emitting or attenuating scalar field.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions* (2023), §15.1, problem 4. [Open problems chapter](https://doi.org/10.1017/9781009039901.018).
2. Mikko Salo and Gunther Uhlmann, *The Attenuated Ray Transform on Simple Surfaces*, Journal of Differential Geometry **88** (2011), 161–187. [Journal](http://projecteuclid.org/euclid.jdg/1317758872), [preprint](https://arxiv.org/abs/1004.2323).

## Status review

**Known cases:** Injectivity is established for position-dependent scalar attenuation, the angular-degree-zero case.

**Remaining target:** Injectivity for every smooth complex attenuation with arbitrary finite angular degree.

**Literature check:** Open in cited literature; no later resolution located

The book lists finite angular attenuation as an open injectivity question. Salo–Uhlmann settle position-dependent scalar attenuation; that does not allow arbitrary higher angular modes. Searches on 2026-09-08: "attenuation finite Fourier injectivity 2025 2026" and "attenuated ray transform finite degree attenuation injectivity solved". No resolution for unrestricted finite angular degree was located.
