# 239. Uniqueness of the homogeneous cooling state for inelastic hard spheres

**Area:** Granular-gas kinetic theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

For a coefficient of normal restitution $`\alpha\in(0,1)`$, define the three-dimensional hard-sphere collision operator weakly by

```math
\int Q_\alpha(F,F)\varphi\,dv=\frac12\iiint_{\mathbb R^3\times\mathbb R^3\times S^2}|(v-w)\cdot\omega|F(v)F(w)[\varphi(v')+\varphi(w')-\varphi(v)-\varphi(w)]\,d\omega\,dv\,dw,
```

where $`v'=v-\frac{1+\alpha}{2}((v-w)\cdot\omega)\omega`$ and $`w'=w+\frac{1+\alpha}{2}((v-w)\cdot\omega)\omega`$, and $`d\omega`$ is surface area.

For every $`\alpha\in(0,1)`$, is there exactly one nonnegative density $`F`$ satisfying

```math
Q_\alpha(F,F)=\nabla_v\cdot(vF),\qquad \int F\,dv=1,\qquad \int vF\,dv=0,
```

in distributions, with $`\int(1+|v|^3)F\,dv<\infty`$ and $`\int F|\log F|\,dv<\infty`$? The coefficient of the dilation term is fixed at one, which fixes the velocity scale. No rotational symmetry is imposed.

## Application

In a freely cooling granular gas, collisions dissipate energy. Uniqueness would identify a single velocity-distribution shape after the shrinking thermal velocity is rescaled.

## References

- Stéphane Mischler and Clément Mouhot, [*Cooling process for inelastic Boltzmann equations for hard spheres, Part II: Self-similar solutions and tail behavior*](https://arxiv.org/abs/math/0607536) (2006), Theorem 1.1: existence of smooth positive profiles for all restitution coefficients in the stated range.
- Stéphane Mischler and Clément Mouhot, [*Stability, convergence to self-similarity and elastic limit for the Boltzmann equation for inelastic hard spheres*](https://arxiv.org/abs/math/0701449) (2007 preprint; 2009 publication), §§1.2–1.4 and Theorem 1.1(i): rescaling, the Ernst–Brito question, and uniqueness for sufficiently small inelasticity.

## Status review

**Known cases:** Uniqueness of the cooling profile is established for restitution coefficients sufficiently close to one.

**Remaining target:** Uniqueness for every restitution coefficient strictly between zero and one in the stated hard-sphere model.

**Literature check:** Open in cited literature; no later resolution located.

Searched “inelastic hard spheres self similar profile uniqueness arbitrary restitution solved 2025 2026”, “homogeneous cooling state uniqueness”, and the 2025 one-dimensional moderately-hard-potential result. The near-elastic theorem covers only a neighborhood of $`\alpha=1`$. Results for Maxwell molecules, one-dimensional collision laws, particle-bath forcing, or diffusive heating do not settle this three-dimensional, freely cooling hard-sphere profile problem.
