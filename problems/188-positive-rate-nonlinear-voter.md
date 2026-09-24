# 188. Two stationary phases in a positive-rate nonlinear voter perturbation

**Area:** Spatial population dynamics and phase coexistence

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $`L\ge1`$, put $`N_L=([-L,L]^3\cap\mathbb Z^3)\setminus\{0\}`$. Consider spins $`\eta(x)\in\{0,1\}`$ on $`\mathbb Z^3`$. At rate $`\varepsilon^{-2}`$ each site copies a uniformly chosen nearest neighbor. Independently, its additional flip rate is

```math
c_L(x,\eta)=\mathbb E\!\left[a_{K(x,\eta,Y)}+\frac1{100}\right],\quad
(a_0,a_1,a_2,a_3,a_4)=(0,2,3,11/2,7),
```

where $`Y=(Y_1,\ldots,Y_4)`$ is sampled uniformly without replacement from $`N_L`$ and $`K(x,\eta,Y)=\#\{j:\eta(x+Y_j)\ne\eta(x)\}`$.

Do there exist finite $`L_0`$ and, for every $`L\ge L_0`$, a number $`\varepsilon_0(L)>0`$ such that, for $`0<\varepsilon<\varepsilon_0(L)`$, there are two distinct translation-invariant stationary laws $`\nu^-,\nu^+`$ with

```math
\nu^-(\eta(0)=1)<1/2<\nu^+(\eta(0)=1)?
```

## Application

Positive flip rates model spontaneous changes, eliminating absorbing consensus states. The question asks whether spatial population dynamics can still retain two stable macroscopic compositions.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, book manuscript of 2 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf), §§7.5 and 7.8, concrete example and Open Problem 7.8.1.
- [J. Theodore Cox, Rick Durrett and Edwin A. Perkins, *Voter model perturbations and reaction diffusion equations* (Astérisque 349, 2013)](https://arxiv.org/abs/1103.1676), the scaling framework.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This is an explicit rate realization of the book's proposed example, with a fixed small spontaneous-flip rate. The tuple uses a_3=11/2, as required by the book's displayed calculation 6a_2−4a_3=−4. Finite-time convergence to a bistable reaction equation does not establish two stationary laws at fixed positive epsilon.

Search topics checked on 2026-09-08: Durrett Huang nonlinear voter positive rates two stationary distributions; nonlinear voter mean curvature stationary phases 2026.
