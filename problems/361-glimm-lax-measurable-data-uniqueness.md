# 361. Uniqueness of Glimm–Lax solutions for arbitrarily rough bounded data

**Area:** Gas dynamics; one-dimensional conservation laws

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`f\in C^4(B_r(d);\mathbb R^2)`$, with $`Df`$ strictly hyperbolic and both characteristic fields genuinely nonlinear. Is there $`\delta>0`$ such that, for every measurable $`u_0:\mathbb R\to B_r(d)`$ with $`a=\|u_0-d\|_\infty\le\delta`$, the equation

```math
u_t+f(u)_x=0,\qquad u(0)=u_0
```

has at most one solution in the Glimm–Lax class? Here this class consists of bounded distributional solutions attaining $`u_0`$ in $`L^1_{\rm loc}`$ as $`t\downarrow0`$, satisfying all convex entropy inequalities $`\partial_t\eta(u)+\partial_xq(u)\le0`$ with $`Dq=D\eta Df`$, and the bounds

```math
\|u(t)-d\|_\infty\le C_0\sqrt a,\qquad \sup_{b\in\mathbb R}\mathop{\mathrm{TV}}\nolimits_{[b,b+L]}u(t)\le C_0(\sqrt a+L/t)
```

for $`t,L>0`$, where $`C_0`$ is the fixed Glimm–Lax bound associated with $`f,d`$. No positive fractional Sobolev regularity of $`u_0`$ is assumed.

## Application

The Glimm–Lax construction provides weak gas-dynamic wave fields starting from bounded oscillatory data. Uniqueness is needed to predict a definite macroscopic evolution when the initial density or velocity has structure at arbitrarily small scales.

## References

1. J. Cheng, C. Faile and S. G. Krupa, [*The Unique Limit of the Glimm–Lax Construction for Sobolev Data and Obstructions to 1-d Convex Integration*](https://doi.org/10.1007/s00205-026-02232-1), Archive for Rational Mechanics and Analysis 250 (2026), §1.1, Theorem 1.1 and §1.6, Open Problem 1.
2. A. Bressan, [*One Dimensional Hyperbolic Conservation Laws: Past and Future*](https://arxiv.org/abs/2310.16707), Journal of Hyperbolic Differential Equations 21 (2024), 523–561, §8, discussion of the Glimm–Lax construction and uniqueness beyond BV.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using Glimm–Lax uniqueness, bounded data without fractional Sobolev regularity, and recent entropy-solution uniqueness. The August 2026 paper proves uniqueness when $`u_0\in W^{s,p}_{\rm loc}`$ for some $`s>0`$, and explicitly asks about data outside every such space. Small-BV uniqueness and the new fractional-Sobolev theorem therefore do not cover the stated measurable-data class. No subsequent full resolution was located.
