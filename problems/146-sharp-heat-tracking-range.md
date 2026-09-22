# 146 — Sharp characterization of exactly trackable boundary heat fluxes

**Area:** PDE control / thermal flux tracking

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^d$, $d\ge2$, be bounded and connected with smooth boundary. Fix $T>0$ and nonempty relatively open boundary patches $\Gamma,\Sigma$ with disjoint closures. For $u\in L^2((0,T)\times\Gamma)$ let $y_u$ be the transposition solution of

$$
\partial_ty_u-\Delta y_u=0,\qquad y_u(0,\cdot)=0,\qquad
y_u|_{\partial\Omega}=\mathbf1_\Gamma u.
$$

Define the exactly trackable flux space

$$
\mathcal R_T=\{\partial_\nu y_u|_{(0,T)\times\Sigma}:
u\in L^2((0,T)\times\Gamma)\},
$$

where $\nu$ is the outward normal. Characterize $\mathcal R_T$ by necessary and sufficient regularity and compatibility conditions on the target flux itself, including the sharp quantitative restrictions near $t=0$. Merely restating membership as existence of a control or an abstract dual inequality is not the requested function-space characterization.

## Application

The problem identifies precisely which temperature-flux histories can be imposed on an inaccessible boundary by heating a separate accessible boundary.

## References

1. J. A. Bárcena-Petisco and E. Zuazua, *Tracking Controllability for the Heat Equation* (2025), [IEEE Transactions on Automatic Control 70, 1935–1940](https://doi.org/10.1109/TAC.2024.3476174) ([author manuscript](https://arxiv.org/abs/2310.00314)), §II, paragraph after equation (16), and Lemma IV.2. Explicitly leaves the sharp trackable space open; gives sufficient Gevrey conditions in one dimension.
2. J. Apraiz, J. A. Bárcena-Petisco and J. Muñoz-Matute, *Tracking controllability on moving targets for parabolic equations* (2026), [arXiv:2603.28449](https://arxiv.org/abs/2603.28449), abstract and introduction. Extends approximate tracking to moving observation targets.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Smoothing supplies necessary regularity, while one-dimensional flatness constructions supply sufficient Gevrey classes. These do not identify the sharp multidimensional range. The 2026 moving-target result concerns approximate tracking, which is weaker than exact range membership. Searches included “heat tracking controllability sharp space Gevrey 2026” and “boundary flux heat exact tracking range characterization 2025 2026”. No sharp general characterization was located.
