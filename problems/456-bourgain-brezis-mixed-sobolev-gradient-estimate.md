# 456. A mixed Sobolev estimate for reconstructing a scalar potential

**Area:** Elliptic potential reconstruction and critical function spaces

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For every integer $d\ge2$, is there $C_d<\infty$ such that every real $\psi\in C^\infty(\mathbb T^d)$ with $\int_{\mathbb T^d}\psi=0$ satisfies

$$
\|\psi\|_{H^{1/2}(\mathbb T^d)+W^{1,1}(\mathbb T^d)}\le C_d\|\nabla\psi\|_{H^{-1/2}(\mathbb T^d;\mathbb R^d)+L^1(\mathbb T^d;\mathbb R^d)}?
$$

Here $\mathbb T^d=\mathbb R^d/\mathbb Z^d$ has unit volume, $\|u\|_{H^s}^2=\sum_{k\in\mathbb Z^d}(1+4\pi^2|k|^2)^s|\widehat u(k)|^2$, $W^{1,1}$ has its usual norm, and $\|u\|_{X+Y}=\inf_{u=a+b}(\|a\|_X+\|b\|_Y)$. The vector-valued norms use Euclidean length and the sum of component Fourier energies.

## Application

The estimate would recover a potential from a gradient containing both rough integrable and fractional-Sobolev components. It is tied to phase lifting in circle-valued fields and to critical elliptic estimates used in superconductivity models.

## References

1. J. Bourgain and H. Brezis, [On the equation div Y = f and application to control of phases](https://sites.math.rutgers.edu/~brezis/PUBlications/171-J.pdf), *Journal of the American Mathematical Society* **16** (2003), 393–426, equation (1.16), p. 397.
2. H. Brezis, [Some of my favorite open problems](https://doi.org/10.4171/RLM/1008), *Rendiconti Lincei — Matematica e Applicazioni* **34** (2023), §7, Open Problem 7.1; [author PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/234.pdf).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2023 source retains this exact mixed-norm estimate as open. Searches through the review date for equation (1.16), Open Problem 7.1, and mixed H1/2 + W1,1 Bourgain–Brezis estimates found no resolution. The August 2026 paper [arXiv:2608.04237](https://arxiv.org/abs/2608.04237) addresses critical homogeneous Hodge estimates with dimension-dependent differentiability, not this fixed-half-derivative sum-norm inequality. Classical divergence solvability and one-dimensional fractional Bergman–Bourgain–Brezis inequalities also differ.
