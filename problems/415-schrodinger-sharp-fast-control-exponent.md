# 415. Sharp exponential cost of fast boundary quantum control

**Area:** PDE control / Schrödinger dynamics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Fix $L>0$ and consider complex-valued solutions of
$$iy_t+y_{xx}=0\quad\text{on }(0,T)\times(0,L),\qquad y(t,0)=h(t),\quad y(t,L)=0.$$
Define
$$C_S(T,L)=\sup_{\|y_0\|_{H^{-1}(0,L)}=1}\inf\{\|h\|_{L^2(0,T)}:y(0)=y_0,\ y(T)=0\},$$
where solutions and boundary values are understood by transposition. Is it true that
$$\lim_{T\downarrow0}T\log C_S(T,L)=L^2/4?$$

## Applied significance

This coefficient measures the energy penalty for steering a quantum wave in a very short time. Bounds with unspecified exponential constants cannot determine the limiting resource requirement.

## References

1. P. Lissy, *Effective multipliers for weights whose log are Hölder continuous. Application to the cost of fast boundary controls for the 1D Schrödinger equation*, preprint (2025), §§3.1–3.2, conjecture preceding Theorem 3.1. [Full text](https://arxiv.org/html/2502.04859v1).
2. P. Lissy, *On the cost of fast controls for some families of dispersive or parabolic equations in one space dimension*, SIAM Journal on Control and Optimization 52 (2014), 2651–2676, §1.2 and control-cost bounds. [Author manuscript](https://cermics.enpc.fr/~lissyp/Publi/KdV.pdf).
3. M. Tucsnak and G. Weiss, *Observation and Control for Operator Semigroups*, Birkhäuser (2009), §7.1 and Corollary 8.2.4, boundary Schrödinger control framework. [Book DOI](https://doi.org/10.1007/978-3-7643-8994-9).

## Status review

The 2025 source explicitly conjectures the displayed coefficient and improves the upper coefficient to 27^(1/4)/4. Nguyen’s January 2026 preprint arXiv:2601.12810 gives fractional-order cost bounds, not this sharp classical coefficient; its Theorem 1.1 assumes 1/2<s<1. Lissy’s August 2026 arXiv:2608.08041 concerns the heat equation. Searches through 22 September 2026 located no resolution for the Schrödinger assertion.
