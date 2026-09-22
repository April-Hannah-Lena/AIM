# 061 — Solenoidal injectivity of the geodesic ray transform on 2-tensors

**Area:** Tensor tomography / linearized travel-time imaging

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $(M,g)$ be any smooth compact simple Riemannian manifold of dimension $n\geq3$; simplicity means strictly convex boundary and unique geodesics depending smoothly on their endpoints. For a smooth symmetric covariant 2-tensor $f$, define
$$
I_2f(\gamma)=\int_0^{\ell_\gamma}
f_{\gamma(t)}(\dot\gamma(t),\dot\gamma(t))\,dt
$$
on every maximal unit-speed geodesic joining boundary points.

Is $I_2f=0$ equivalent to $f=d^sv$ for a smooth 1-form $v$ vanishing on $\partial M$, where
$(d^sv)_{ij}=(\nabla_i v_j+\nabla_j v_i)/2$? The reverse implication follows from integration along a geodesic; the requested result is that this describes the entire kernel.

## Application

The transform is the linearization of anisotropic travel-time measurements. Its potential-tensor kernel represents infinitesimal changes of coordinates that preserve the boundary.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Tensor tomography on surfaces*, Inventiones Mathematicae **193** (2013), 229–247; introduction following Theorem 1.1. [Author manuscript](https://users.jyu.fi/~salomi/pub/tensor_inv2.pdf).
2. G. P. Paternain, M. Salo and G. Uhlmann, *Tensor tomography: progress and challenges* (2014), §11, Problem 2. [Author manuscript](https://users.jyu.fi/~salomi/pub/surveychina16.pdf).
3. P. Stefanov, G. Uhlmann and A. Vasy, *Local and global boundary rigidity and the geodesic X-ray transform in the normal gauge* (2021). [Paper](https://doi.org/10.4007/annals.2021.194.1.1).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Reference 2 explicitly identifies $I_2$ on a general simple higher-dimensional manifold as unresolved. Surface tensor tomography is solved; the higher-dimensional results in reference 3 use extra geometry. Generic injectivity does not imply injectivity for every simple metric.

Searches on 2026-09-08 included `tensor tomography open simple 2024 2025 2026` and `rigidity simple tensor tomography 2026`. No all-simple-metrics theorem for the stated 2-tensor kernel was located.
