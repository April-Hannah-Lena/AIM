# 167. The Euler vortex-filament limit for a general moving curve

**Area:** Vortex dynamics and fluid mechanics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\gamma:[0,T]\times(\mathbb R/L\mathbb Z)\to\mathbb R^3`$ be a smooth embedded closed curve, parametrized by arclength, solving binormal curvature flow

```math
\partial_t\gamma=\partial_s\gamma\times\partial_{ss}\gamma.
```

Can one construct, for every sufficiently small $`\epsilon>0`$, a smooth finite-energy Euler velocity $`u^\epsilon`$ on physical times $`0\le\tau\le4\pi T/|\log\epsilon|`$, whose initial vorticity $`\omega^\epsilon=\nabla\times u^\epsilon`$ is supported within distance $`C\epsilon`$ of $`\gamma(0)`$, with $`\int|\omega^\epsilon(0,x)|\,dx\to L`$, and such that for every compactly supported smooth vector field $`\phi`$,

```math
\sup_{0\le t\le T}\left|\int\omega^\epsilon\!\left(\frac{4\pi t}{|\log\epsilon|},x\right)\cdot\phi(x)\,dx-\int_0^L\partial_s\gamma(t,s)\cdot\phi(\gamma(t,s))\,ds\right|\to0?
```

Euler means $`\partial_\tau u^\epsilon+(u^\epsilon\cdot\nabla)u^\epsilon+\nabla p^\epsilon=0`$, $`\mathop{\mathrm{div}}\nolimits u^\epsilon=0`$; $`C`$ is independent of $`\epsilon`$.

## Application

This would justify the moving-filament model used to approximate slender vortex tubes without imposing axial or helical symmetry.

## References

1. Robert L. Jerrard and Christian Seis, *On the vortex filament conjecture for Euler flows*, Archive for Rational Mechanics and Analysis 224 (2017), 135–172. [Paper](https://arxiv.org/abs/1603.00227). Introduction and main theorem establish the geometric limit conditional on sustained vorticity concentration.

2. Dengjun Guo, In-Jee Jeong and Lifeng Zhao, *Global dynamics of a single vortex ring* (2026). [Paper](https://arxiv.org/abs/2602.20131). Main theorem proves global concentration and leading propagation speed for axisymmetric flow without swirl.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “vortex filament conjecture general curve 2026”, “Xiaoyu Huang vortex filament 2026”, and “Global dynamics of a single vortex ring” found the strong 2026 ring theorem and helical constructions. These impose symmetries absent from a general moving closed curve. Jerrard–Seis assume the persistence of concentration that this existence formulation must establish. No unrestricted construction was located.
