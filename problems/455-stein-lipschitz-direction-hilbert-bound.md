# 455. Stein’s Hilbert-transform bound along Lipschitz directions

**Area:** Directional singular integrals and variable-direction propagation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Do absolute constants $K\ge1$ and $C<\infty$ exist such that the following holds? For every $v:\mathbb R^2\to S^1$ satisfying $|v(x)-v(y)|\le|x-y|$, every Schwartz function $f$, and every $\lambda>0$, define

$$
H_vf(x)=\lim_{\varepsilon\downarrow0}\int_{\varepsilon<|t|<1/K}f(x-tv(x))\,\frac{dt}{t}.
$$

Then require

$$
\lambda^2\big|\{x\in\mathbb R^2:|H_vf(x)|>\lambda\}\big|\le C\|f\|_{L^2(\mathbb R^2)}^2.
$$

The constants must be uniform over all such direction fields, including fields depending on both spatial coordinates.

## Application

Directional singular integrals model filtering along a spatially varying preferred orientation. The estimate would give uniform control when the local direction changes at a bounded rate, a basic issue for anisotropic transport and directional image processing.

## References

1. M. Lacey and X. Li, [On a conjecture of E. M. Stein on the Hilbert transform on vector fields](https://doi.org/10.1090/S0065-9266-10-00572-7), *Memoirs of the American Mathematical Society* **205** (2010), no. 965, Conjecture 1.5 and equation (1.6); [preprint](https://arxiv.org/abs/0704.0808).
2. F. Di Plinio, S. Guo, C. Thiele and P. Zorin-Kranich, [Square functions for bi-Lipschitz maps and directional operators](https://doi.org/10.1016/j.jfa.2018.07.005), *Journal of Functional Analysis* **275** (2018), 2015–2058, introduction and Corollary 1.4; [preprint](https://arxiv.org/abs/1706.07111).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The first source states precisely this weak-L2 conjecture after scaling the Lipschitz constant. Conditional bounds and results for one-variable or restricted direction fields do not provide the uniform two-variable estimate. Searches through the review date located no resolution. The small fixed upper cutoff is essential; the problem does not claim an unrestricted large-scale bound.
