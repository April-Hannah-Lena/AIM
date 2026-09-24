# 376. Quantization of radial finite-time collapse in fully parabolic Keller–Segel

**Area:** Chemotaxis; concentration of cell density

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega=B_R(0)\subset\mathbb R^2$. Consider radially symmetric nonnegative smooth compatible initial data for

$$
u_t=\Delta u-\nabla\cdot(u\nabla v),\qquad v_t=\Delta v-v+u,
$$

with $\partial_nu=\partial_nv=0$ on $\partial\Omega$. Suppose its maximal classical solution blows up at a finite time $T$ and has the measure limit

$$
u(\cdot,t)\,dx\stackrel{*}{\rightharpoonup}m\delta_0+f(x)\,dx\qquad(t\uparrow T),
$$

where $f\in L^1(\Omega)$ is nonnegative and $m\ge8\pi$. Must $m=8\pi$? The signal equation retains its time derivative; the question concerns finite-time collapse in this fully parabolic system.

## Application

The atom measures the number of cells concentrating into a singular cluster. Quantization would show that the local collapse mass is fixed by the model rather than by the total population.

## References

1. Y. Soga, [*A sufficient condition for absence of mass quantization in a chemotaxis system with local sensing*](https://arxiv.org/abs/2505.10912), preprint, version 2 (2025), §1, pp. 3–4: explicit open question for the fully parabolic Keller–Segel system.
2. T. Nagai, T. Senba and T. Suzuki, [*Chemotactic collapse in a parabolic system of mathematical biology*](https://doi.org/10.32917/hmj/1206124609), Hiroshima Mathematical Journal 30 (2000), 463–497, collapse measure and lower bound for its atom.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using fully parabolic Keller–Segel finite-time mass quantization and subsequent collapse results. Soga explicitly distinguishes this open question from proved quantization in the parabolic–elliptic model. His own possible failure of quantization concerns a different equation, $u_t=\Delta(e^{-v}u)$, at infinite time. Results on existence at critical total mass, including [arXiv:2602.03768](https://arxiv.org/abs/2602.03768), do not determine the mass of a finite-time atom for the displayed system. No matching resolution was located.
