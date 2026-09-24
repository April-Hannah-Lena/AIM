# 260 — A complete boundary-control criterion for coupled heat systems in higher dimensions

**Area:** Parabolic control / coupled diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Given a bounded connected smooth domain $`\Omega\subset\mathbb R^d`$, $`d\geq2`$, a nonempty relatively open $`\Gamma\subset\partial\Omega`$, $`T>0`$, and constant real matrices $`A\in\mathbb R^{n\times n}`$ and $`B\in\mathbb R^{n\times m}`$ with $`m<n`$, consider

```math
y_t-\Delta y-Ay=0,\qquad y|_{\partial\Omega}=Bf\,\mathbf1_\Gamma,\qquad y(0)=y_0\in L^2(\Omega)^n.
```

Find a necessary and sufficient spectral/algebraic condition for null controllability by $`f\in L^\infty(\Gamma\times(0,T))^m`$: every $`y_0`$ must admit such a control with $`y(T)=0`$, interpreted by transposition. The criterion should identify the interaction of $`A,B`$ with the Dirichlet Laplacian spectral data of $`\Omega`$ and the active boundary. Merely restating controllability as an adjoint observability inequality is not the requested characterization.

## Application

A criterion would determine when a few boundary actuators can independently regulate many coupled diffusing quantities, such as concentrations or temperatures.

## References

1. E. Fernández-Cara, *Remarks on control and inverse problems for PDEs* (2025), [SeMA Journal 82, 267–288](https://doi.org/10.1007/s40324-024-00363-7), §2, equation (4), Theorem 2 and Problem 1. Explicitly asks for a necessary and sufficient condition in spatial dimension at least two.
2. F. Ammar-Khodja, A. Benabdallah, M. González-Burgos and L. de Teresa, *The Kalman condition for the boundary controllability of coupled parabolic systems. Bounds on biorthogonal families to complex matrix exponentials* (2011), [author repository](https://idus.us.es/items/d74e864a-7e8d-4046-aaed-77a66fda2a02), JMPA 96, 555–590, main theorem. Gives the one-dimensional criterion.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The distributed-control Kalman rank test and the one-dimensional boundary test are established. They do not give the requested general multidimensional boundary characterization. Searches included “coupled parabolic boundary Kalman multidimensional 2026”, “higher dimensional boundary controllability necessary sufficient”, and the 2011 paper title. Recent time-discrete, cascade and stabilization results have different scopes; no full criterion was located.
