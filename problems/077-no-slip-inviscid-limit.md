# 077. The no-slip inviscid limit in two dimensions

**Area:** Fluid dynamics and boundary layers

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^2$ be a bounded smooth simply connected domain and $u_0\in C_c^\infty(\Omega;\mathbb R^2)$ be divergence-free. Let $u^\nu$ solve incompressible Navier–Stokes with viscosity $\nu>0$, no forcing, initial value $u_0$ and boundary condition $u^\nu=0$. Let $u^E$ solve Euler with the same datum and $u^E\cdot n=0$ on $\partial\Omega$. Is
$$
\lim_{\nu\downarrow0}\sup_{0\le t\le T}
\|u^\nu(t)-u^E(t)\|_{L^2(\Omega)}=0
$$
for every $T<\infty$ and every such $(\Omega,u_0)$? A counterexample within these hypotheses also resolves the question. The datum is fixed independently of viscosity.

## Application

This tests whether inviscid simulation approximates viscous flow near a solid wall, where thin boundary layers may dissipate appreciable energy.

## References

- [Toan T. Nguyen, *The inviscid limit problem for Navier-Stokes equations* (2022), equations and discussion of the no-slip problem](https://sites.psu.edu/nguyen/2022/08/18/the-inviscid-limit-problem-for-navier-stokes-equations/).
- [Franck Sueur, *A Kato type Theorem for the inviscid limit of the Navier-Stokes equations with a moving rigid body* (2011 preprint), introduction and comparison with Kato's fixed-boundary criterion](https://arxiv.org/abs/1110.6065).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited exposition presents the general smooth-data boundary problem as open. Kato's criterion characterizes convergence through dissipation in a viscosity-scale layer; it does not establish its vanishing for all data. Recent searches returned analytic/Gevrey, special-flow and conditional results rather than the unrestricted statement.

Searches run on 2026-09-08: `site.arxiv.org inviscid limit no-slip open problem 2025`; `Inviscid limit and Prandtl system no slip open 2026`. This is a literature search, not a proof that no solution exists.
