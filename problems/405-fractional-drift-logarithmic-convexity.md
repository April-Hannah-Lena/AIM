# 405. Logarithmic convexity for subdiffusion with non-gradient drift

**Area:** Fractional PDEs / inverse initial-state recovery

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^n$, $n\ge2$, be a bounded smooth domain, $0<\alpha<1$ and $T>0$. Let $A(x)$ be a smooth symmetric uniformly positive-definite matrix field, $B(x)$ a smooth real vector field and $p(x)$ a smooth real scalar field. Define $Lu=\nabla\cdot(A\nabla u)+B\cdot\nabla u+pu$ with homogeneous Dirichlet boundary conditions. Does there exist $C=C(\Omega,A,B,p,\alpha,T)$ such that every solution of

$$
\partial_t^\alpha u=Lu,\qquad u(0)=u_0\in L^2(\Omega),
$$

satisfies

$$
\|u(t)\|_{L^2}\le C\|u_0\|_{L^2}^{1-t/T}\|u(T)\|_{L^2}^{t/T}\qquad(0<t<T)?
$$

Here $\partial_t^\alpha u=\Gamma(1-\alpha)^{-1}\int_0^t(t-s)^{-\alpha}u'(s)\,ds$ is the Caputo derivative, extended to mild solutions. No representation $B=A\nabla b$ is assumed.

## Application

The estimate would quantify recovery of earlier concentration fields from a final observation in anomalous diffusion with circulation or drift. The gradient-drift restriction excludes many transport fields encountered in applications.

## References

1. S.-E. Chorfi, *Logarithmic convexity of evolution equations and application to inverse problems*, preprint (2025), §4, Theorem 6 and §5, open problem 2. [Full text](https://arxiv.org/html/2506.19954v1).
2. S.-E. Chorfi, L. Maniar and M. Yamamoto, *Logarithmic convexity of non-symmetric time-fractional diffusion equations*, Mathematical Methods in the Applied Sciences 48 (2025), 2011–2021, gradient-drift assumption and main logarithmic convexity theorem. [DOI](https://doi.org/10.1002/mma.10421).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 primary sources explicitly leave removal of the gradient-drift assumption open. Classical time derivatives and operators conjugate to self-adjoint ones are covered by other results, but those do not include general fractional drift diffusion. Searches through 22 September 2026 for non-gradient fractional logarithmic convexity and later papers by the authors found no matching proof or counterexample.
