# 476. Barenblatt attraction for porous-medium diffusion with time memory

**Area:** PDEs with memory; nonlinear diffusion asymptotics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $`d\ge1`$, $`m>1`$ and $`0<\alpha<1`$. Let $`u`$ solve $`D_t^\alpha u=\Delta(u^m)`$ on $`\mathbb R^d`$ with nonnegative compactly supported $`u_0\in L^1\cap L^\infty`$, of mass $`M>0`$. Consider nonnegative weak solutions $`u\in C([0,\infty);L^1(\mathbb R^d))`$ with $`u(0)=u_0`$ in $`L^1`$, $`u^m\in L^1_{\rm loc}([0,\infty)\times\mathbb R^d)`$ and $`\int u(t)=M`$ for every $`t`$. The Caputo derivative is based at time zero, specified by the Volterra identity

```math
u(t)=u_0+\Gamma(\alpha)^{-1}\int_0^t(t-r)^{\alpha-1}\Delta(u(r)^m)\,dr
```

in spatial distributions. Set $`b=\alpha/[d(m-1)+2]`$ and $`a=db`$. Let $`U_{\alpha,m,M}`$ be the nonnegative radial self-similar profile of mass $`M`$ constructed in the cited paper, so $`t^{-a}U_{\alpha,m,M}(t^{-b}x)`$ is a point-source solution.

Does every such $`u`$ satisfy

```math
\lim_{t\to\infty}\|t^a u(t,t^b\,\cdot)-U_{\alpha,m,M}\|_{L^1(\mathbb R^d)}=0?
```

The rescaling changes the observation variables only; it does not replace the original Caputo memory by a derivative with a shifted lower limit.

## Application

The result would justify a universal spreading profile for nonlinear infiltration and anomalous diffusion, independent of the detailed initial source shape.

## References

1. D. Gómez-Castro, Ł. Płociniczak and J. L. Vázquez, *Self-similar solutions to the time-fractional Porous-Medium Equation* (2026 preprint), §1 and §8, “Uniqueness of weak solutions with Dirac initial data” and “Asymptotic behavior for general initial data.” [Full preprint](https://arxiv.org/html/2604.09281v1).
2. J. Caballero, H. Okrasińska-Płociniczak, Ł. Płociniczak and K. Sadarangani, *Barenblatt solutions for the time-fractional porous medium equation: approach via integral equations*, Fract. Calc. Appl. Anal. (2026), construction of the self-similar profiles. [Article](https://doi.org/10.1007/s13540-026-00514-9).
3. J. L. Vázquez, *The Porous Medium Equation: Mathematical Theory*, Oxford University Press (2007), classical fundamental solutions and large-time asymptotics. [Book](https://doi.org/10.1093/acprof:oso/9780198569039.001.0001).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Section 8 of the 2026 preprint explicitly asks whether its profiles attract general solutions. Searches on 2026-09-22 for nonlinear time-fractional Barenblatt attraction and long-time asymptotics found no matching convergence theorem. The classical case $`\alpha=1`$, linear case $`m=1`$, bounded-domain decay, and asymptotics of the profile itself are different results. The $`L^1`$ conclusion avoids imposing uniform convergence to a profile that can be spatially singular in higher dimensions.
