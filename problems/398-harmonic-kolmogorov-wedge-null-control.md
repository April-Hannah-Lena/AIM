# 398. Exact null control of a harmonically confined kinetic equation from a wedge

**Area:** PDE control / kinetic transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For $0<\theta<\pi/4$ let $\omega_\theta=\{(x,v)\in\mathbb R^2:v=\alpha x\text{ for some }0<\alpha<\tan\theta\}$. Consider

$$
\partial_t f+v\partial_x f-x\partial_v f-\partial_v^2f=\mathbf1_{\omega_\theta}h,\qquad f(0)=f_0\in L^2(\mathbb R^2).
$$

Is it true that for every $T>\pi-\theta$ and every $f_0$ there is $h\in L^2((0,T)\times\omega_\theta)$ for which the mild solution satisfies $f(T)=0$? The assertion is exact null controllability; convergence to an arbitrarily small terminal error is insufficient.

## Application

This kinetic Fokker–Planck model couples velocity diffusion to rotation in phase space. It tests whether every trajectory spending sufficient time in an actuator region is enough for exact control despite degenerate diffusion.

## References

1. K. Beauchard, M. Egidi and K. Pravda-Starov, *Geometric conditions for the null-controllability of hypoelliptic quadratic parabolic equations with moving control supports*, Comptes Rendus Mathématique 358 (2020), 651–700, preprint §2.4, Proposition 2.4(iii). [DOI](https://doi.org/10.5802/crmath.79); [arXiv:1908.10603](https://arxiv.org/abs/1908.10603).
2. P. Alphonse and J. Martin, *Approximate Null Controllability with Uniform Cost for the Hypoelliptic Ornstein–Uhlenbeck Equations*, SIAM Journal on Control and Optimization 61 (2023), 1679–1711, §2.3, Example 2.7. [DOI](https://doi.org/10.1137/22M1487412); [arXiv:2201.01516](https://arxiv.org/abs/2201.01516).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2020 source explicitly leaves null controllability above the rotation threshold open. The SIAM paper proves approximate null control with uniform cost above that threshold and noncontrollability at the threshold; it explicitly distinguishes the remaining exact question. Searches through 22 September 2026 for harmonic Kolmogorov cone control, integral thickness and subsequent work by these authors located no exact positive result or counterexample.
