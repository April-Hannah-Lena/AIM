# 482. Uniqueness for a point source in time-fractional porous-medium flow

**Area:** PDEs with memory; porous-medium diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $d\ge2$, $m>1$, $0<\alpha<1$ and $M>0$. For the Caputo equation $D_t^\alpha u=\Delta(u^m)$ on $\mathbb R^d$, is there at most one nonnegative mass-$M$ weak solution with initial measure $M\delta_0$?

Here the weak class is $u\in C((0,\infty);L^1(\mathbb R^d))$, $u^m\in L^1_{\rm loc}([0,\infty)\times\mathbb R^d)$, $\int u(t)=M$, and, for each $\phi\in C_c^\infty(\mathbb R^d)$ and almost every $t>0$,
$$
\int u(t,x)\phi(x)\,dx=M\phi(0)+\frac1{\Gamma(\alpha)}\int_0^t(t-r)^{\alpha-1}\int u(r,x)^m\Delta\phi(x)\,dx\,dr.
$$
Require narrow convergence $u(t,x)dx\rightharpoonup M\delta_0$ as $t\downarrow0$. This Volterra identity specifies the Caputo convention for measure data. Do not impose self-similarity or radial symmetry; the known fundamental profile need not be bounded at the origin.

## Application

Uniqueness would make an instantaneous concentrated release well-defined in a porous-medium model with long temporal memory.

## References

1. D. Gómez-Castro, Ł. Płociniczak and J. L. Vázquez, *Self-similar solutions to the time-fractional Porous-Medium Equation* (2026 preprint), §1 and §8, “Uniqueness of weak solutions with Dirac initial data” and “Asymptotic behavior for general initial data.” [Full preprint](https://arxiv.org/html/2604.09281v1).
2. J. Caballero, H. Okrasińska-Płociniczak, Ł. Płociniczak and K. Sadarangani, *Barenblatt solutions for the time-fractional porous medium equation: approach via integral equations*, Fract. Calc. Appl. Anal. (2026), construction of the self-similar profiles. [Article](https://doi.org/10.1007/s13540-026-00514-9).
3. J. L. Vázquez, *The Porous Medium Equation: Mathematical Theory*, Oxford University Press (2007), classical fundamental solutions and large-time asymptotics. [Book](https://doi.org/10.1093/acprof:oso/9780198569039.001.0001).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The April 2026 preprint constructs and characterizes self-similar solutions but lists general weak uniqueness for Dirac data separately in §8. Searches on 2026-09-22 checked measure-data uniqueness, the paper title and subsequent citations. Uniqueness of the profile equation and results for regular one-dimensional initial-boundary data do not imply the assertion here. The weak formulation retains the initial measure inside the memory equation rather than restarting the equation at positive time.
