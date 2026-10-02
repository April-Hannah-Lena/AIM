# 228. Uniqueness of entropy-admissible renormalized Boltzmann solutions

**Area:** Rarefied-gas kinetics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On $`\mathbb T^3_x\times\mathbb R^3_v`$, consider $`\partial_tf+v\cdot\nabla_x f=Q(f,f)`$, with hard-sphere collisions

```math
Q(f,f)(v)=\int_{\mathbb R^3}\int_{\mathbb S^2}|(v-v_*)\cdot\omega|\,[f(v')f(v_*')-f(v)f(v_*)]\,d\omega\,dv_*,
```

where $`v'=v-[(v-v_*)\cdot\omega]\omega`$ and $`v_*'=v_*+[(v-v_*)\cdot\omega]\omega`$; all factors have the same $`(t,x)`$.

Are two nonnegative renormalized solutions with the same initial datum necessarily equal almost everywhere? Use the DiPerna–Lions finite-mass, finite-energy, finite-entropy class: on every finite time interval, $`\int f(1+|v|^2+|\log f|)\,dx\,dv`$ is bounded, $`Q(f,f)/(1+f)\in L^1_{\mathrm{loc}}`$, and

```math
(\partial_t+v\cdot\nabla_x)\beta(f)=\beta'(f)Q(f,f)
```

holds distributionally for every $`C^1`$ renormalization with $`|\beta'(z)|\leq C/(1+z)`$. Require the initial trace in $`L^1`$, conservation of mass and momentum, the energy inequality, and the entropy inequality $`H(f_t)+\int_0^tD(f_s)ds\leq H(f_0)`$, where $`H(f)=\int f\log f`$ and $`D(f)=-\int Q(f,f)\log f\geq0`$ is interpreted by its nonnegative collision integral.

## Application

This asks whether the natural large-data kinetic theory determines one gas evolution from its initial distribution, without assuming the regularity needed for classical solutions.

## References

- Ronald J. DiPerna and Pierre-Louis Lions, [*On the Cauchy problem for Boltzmann equations: Global existence and weak stability*](https://annals.math.princeton.edu/1989/130-2/p03) (1989), main existence and weak-stability results: the renormalized solution framework.
- Gayoung An and Donghyun Lee, [*Optimal $`C^{1/2}`$ regularity of the Boltzmann equation in non-convex domains*](https://doi.org/10.1007/s40818-026-00243-5) (2026), introduction: explicitly retains general renormalized uniqueness as open.
- Rafael Galeano Andrades and Mario Almanza Caro, [*Uniqueness of solutions to Boltzmann equations*](https://arxiv.org/abs/2006.08011) (2020 preprint), §2, Theorem 2.1 and subsequent contraction assumptions: a claim screened during the status check.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “DiPerna Lions renormalized Boltzmann uniqueness proof 2025 2026” and the title of the 2020 uniqueness preprint. That preprint introduces additional contraction hypotheses, including an explicit constant smaller than one; these are not consequences of finite mass, energy and entropy. The 2026 primary article continues to identify the unrestricted uniqueness problem as open. Boundary regularity and perturbative mild-solution uniqueness address narrower classes.
