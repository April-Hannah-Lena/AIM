# 473. Multidimensional weak uniqueness for porous-medium flow with fractional pressure

**Area:** Nonlocal PDEs; porous-medium transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $N\ge2$, $0<s<1$, and $m=2$.

On $\mathbb R^N$ use the model
$$u_t=\nabla\cdot(u^{m-1}\nabla p),\qquad p=(-\Delta)^{-s}u,$$
where the inverse fractional Laplacian has Fourier multiplier $|\xi|^{-2s}$. Take nonzero, nonnegative $u_0\in L^1\cap L^\infty$ with compact support. By a bounded energy weak solution mean a nonnegative distributional solution with the initial trace $u_0$, continuous into $L^1$ with its weak topology, conserving $\int u_0$, and satisfying $\|u(t)\|_\infty\le\|u_0\|_\infty$, locally integrable flux, and
$$\frac12\|(-\Delta)^{-s/2}u(t)\|_2^2+
\int_0^t\!\int u^{m-1}|\nabla(-\Delta)^{-s}u|^2
\le\frac12\|(-\Delta)^{-s/2}u_0\|_2^2.$$
Use also the dissipative $L^q$ inequalities, for every $q>1$,
$$\|u(t)\|_q^q+\frac{4q(q-1)}{(m+q-1)^2}\int_0^t\|(-\Delta)^{(1-s)/2}u^{(m+q-1)/2}\|_2^2\,dr\le\|u_0\|_q^q.$$

Is there at most one bounded energy weak solution for each such initial density, without strict positivity or additional smoothness assumptions?

## Application

Uniqueness would reconcile the different approximation and gradient-flow constructions of this macroscopic nonlocal transport model.

## References

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

4. G. Foghem, D. Padilla-Garza and M. Schmidtchen, *Gradient flow solutions for porous medium equations with nonlocal Lévy-type pressure*, Calc. Var. PDE **64**, 88 (2025). [Article](https://doi.org/10.1007/s00526-025-02942-6).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey explicitly distinguishes multidimensional weak uniqueness from the one-dimensional theorem and local smooth theory. Searches on 2026-09-22 checked subsequent uniqueness and gradient-flow results. The 2025 paper constructs gradient-flow solutions and proves uniqueness of discrete minimizers, which is not uniqueness of the continuous PDE. The 2026 paper's uniqueness theorem is one-dimensional. No matching theorem for the above multidimensional energy class was located.
