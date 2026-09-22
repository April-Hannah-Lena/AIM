# 427. Uniform control of Neumann advection–diffusion for non-gradient flows

**Area:** PDE control / transport with weak diffusion

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^d$, $d\ge2$, be a bounded connected smooth domain, $\omega\Subset\Omega$ nonempty open, and $B\in W^{2,\infty}(\mathbb R^d;\mathbb R^d)$. Assume $B\cdot\nu\ge c_0>0$ on $\partial\Omega$. Write $X'(s)=-B(X(s))$, $X(0)=x$. Assume that some $T_0,r_0>0$ satisfy: for each $x\in\overline\Omega$ there is $s_x\in(0,T_0)$ with $X(s_x;B(x,r_0))\subset\omega$.
For $\varepsilon>0$, consider
$$y_t-\varepsilon\Delta y+B\cdot\nabla y=1_\omega h,\quad \partial_\nu y=0,\quad y(0)=y_0\in L^2(\Omega).$$
Must there exist $T_*<\infty$ such that, for every $T>T_*$, some $C_T,\varepsilon_T>0$ satisfy: every $0<\varepsilon<\varepsilon_T$ and every $y_0$ admit $h\in L^2((0,T)\times\omega)$ with $y(T)=0$ and
$$\|h\|_2\le C_T\|y_0\|_2?$$
No scalar potential representation $B=\nabla f$ is imposed.

## Applied significance

This asks whether a sensor-actuator region reached by all backward flow paths can uniformly control a weakly diffusive concentration in a bounded vessel. Rotational drift is allowed, which is important for realistic transport fields.

## References

1. F. Et-Tahri, J. A. Bárcena-Petisco, I. Boutaayamou and L. Maniar, *On uniform null controllability of transport-diffusion equations with vanishing viscosity limit*, Mathematical Methods in the Applied Sciences 48 (2025), 6531–6552, equation (1), Definition 1.3, Theorem 1.5 and Remark 1.6. [DOI](https://doi.org/10.1002/mma.10693); [full text](https://arxiv.org/html/2412.16660v1).
2. J. A. Bárcena-Petisco, *Cost of null controllability for parabolic equations with vanishing diffusivity and a transport term*, ESAIM: Control, Optimisation and Calculus of Variations 27 (2021), 106, introduction and main control-cost results. [DOI](https://doi.org/10.1051/cocv/2021103).

## Status review

Remark 1.6 explicitly identifies removal of the gradient-field assumption as open. The statement specializes to autonomous smooth drift while retaining strict outward flux and the uniform neighborhood version of the flushing condition. The available Neumann theorem requires gradient drift; Dirichlet and tangential-boundary results do not provide this conclusion. Searches through 22 September 2026 located no resolution.
