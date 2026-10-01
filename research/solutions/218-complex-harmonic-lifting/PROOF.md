# Bounded complex harmonic lifting from Agmon's maximum estimate

**Target:** Problem 218 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete reduction to a classical theorem, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Source comparison, deduction and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Result and established ingredient

The bound in problem 218 holds. This report applies a classical maximum estimate for complex elliptic equations and then passes from smooth boundary values to the exact Sobolev trace class in the question. It does not claim a new maximum theorem.

The external ingredient is S. Agmon, [Maximum theorems for solutions of higher order elliptic equations](https://doi.org/10.1090/S0002-9904-1960-10402-8), Bulletin of the American Mathematical Society 66 (1960), 77–80, Theorem I, equation (7) on p.78; a [readable copy of the published paper](https://scispace.com/pdf/maximum-theorems-for-solutions-of-higher-order-elliptic-2ie7i0rbxm.pdf) was inspected. For a complex scalar elliptic operator of order two on a sufficiently smooth bounded domain, its specialization $`m=1`$, $`l=0`$ gives

```math
\|u\|_{L^\infty(\Omega)}
\le K_0\|u|_{\partial\Omega}\|_{L^\infty(\partial\Omega)}
+K_1\|u\|_{L^1(\Omega)}                                    \tag{1}
```

for smooth solutions of the homogeneous equation. The constants depend on the operator and domain, not on the solution. In dimension two the source additionally requires the proper-ellipticity roots condition; it is checked below. We retain the lower-order $`L^1`$ term, so no interpretation of the source's extra uniqueness clause for removing it is needed.

## 1. Checking ellipticity and the roots condition

Write

```math
Lu=-\sum_{j,k}C_{jk}\partial_j\partial_k u
=-\mathop{\mathrm{div}}\nolimits(C\nabla u).
```

Because the matrix is constant, these are the same differential operator in distributions. Its coefficients are smooth, the domain is smooth, and the accretivity assumption of the target gives a nonvanishing elliptic principal symbol on every nonzero real covector.

For completeness, let $`\nu`$ be a real unit normal and $`\xi\ne0`$ a real tangent covector with $`\xi\cdot\nu=0`$. Join $`C`$ to the identity by

```math
C_s=(1-s)I+sC,\qquad 0\le s\le1.
```

Each matrix is strictly accretive, with constant at least $`\min\{1,\mu\}`$. The quadratic polynomial

```math
p_s(\tau)=(\xi+\tau\nu)^T C_s(\xi+\tau\nu)
```

has no real roots, since its real part on the real axis is at least $`\min\{1,\mu\}(|\xi|^2+\tau^2)`$. Its leading coefficient $`\nu^TC_s\nu`$ is uniformly bounded away from zero. Thus no root escapes to infinity or crosses the real axis along the homotopy. At $`s=0`$ the two roots are $`\pm i|\xi|`$. There is consequently one root in each half-plane at $`s=1`$. This is precisely the required roots condition, including in dimension two, and is also the scalar Dirichlet complementing condition.

All assumptions needed to apply Agmon's estimate (1) to smooth solutions are satisfied. The antisymmetric part of the coefficient matrix does not affect the second-order differential expression; no Hermitian or real symmetry of $`C`$ has been added.

## 2. A boundary L2 estimate controls the lower-order term

Let $`\varphi\in C^\infty(\partial\Omega)`$ and let $`u`$ be its weak harmonic lifting. Coercivity, a bounded Sobolev trace extension and Lax–Milgram give existence and uniqueness in $`H^1`$. Standard smooth-domain Dirichlet elliptic regularity, with the complementing condition checked above, gives $`u\in C^\infty(\overline\Omega)`$.

We record a direct duality estimate for its $`L^2`$ norm. For any $`F\in L^2(\Omega)`$, solve the adjoint Dirichlet problem

```math
L^*v=F,\qquad v\in H_0^1(\Omega),\qquad
L^*=-\mathop{\mathrm{div}}\nolimits(C^*\nabla).
```

The adjoint matrix has the same accretivity. Coercivity and the usual $`H^2`$ Dirichlet regularity estimate on a smooth domain imply

```math
v\in H^2(\Omega),\qquad \|v\|_{H^2(\Omega)}\le K_2\|F\|_2.
```

The conormal trace therefore satisfies $`\|\nu\cdot C^*\nabla v\|_{L^2(\partial\Omega)}\le K_3\|F\|_2`$. Green's formula, together with harmonicity of $`u`$ and the zero trace of $`v`$, gives

```math
\int_\Omega u\overline F
=-\int_{\partial\Omega}\varphi\,
\overline{\nu\cdot C^*\nabla v}\,dS.
```

Taking the supremum over $`\|F\|_2\le1`$ proves

```math
\|u\|_{L^2(\Omega)}\le K_3\|\varphi\|_{L^2(\partial\Omega)}.
```

In particular

```math
\|u\|_{L^1(\Omega)}
\le |\Omega|^{1/2}K_3|\partial\Omega|^{1/2}\|\varphi\|_\infty.
```

Substituting into (1), we obtain a constant $`K=K(\Omega,C)<\infty`$ such that

```math
\|u\|_\infty\le K\|\varphi\|_\infty
\qquad\bigl(\varphi\in C^\infty(\partial\Omega)\bigr).        \tag{2}
```

This does not take an uncontrolled limit of finite-$`p`$ estimates. It uses one fixed $`L^2`$ estimate inside the endpoint maximum estimate (1).

## 3. Passing to bounded H1/2 boundary data

Let now $`\varphi\in H^{1/2}(\partial\Omega)\cap L^\infty(\partial\Omega)`$, with arbitrary complex values. Smooth it by the heat semigroup of the Laplace–Beltrami operator on the compact smooth boundary:

```math
\varphi_j=e^{t_j\Delta_{\partial\Omega}}\varphi,
\qquad t_j\downarrow0.
```

Its positive probability kernels give $`|\varphi_j|\le e^{t_j\Delta_{\partial\Omega}}|\varphi|`$, so $`\|\varphi_j\|_\infty\le\|\varphi\|_\infty`$ also for complex data. These functions are smooth, and strong continuity in $`H^{1/2}`$ gives $`\varphi_j\to\varphi`$ in that norm. These facts hold componentwise if the boundary is disconnected.

The harmonic lifting is bounded from $`H^{1/2}(\partial\Omega)`$ to $`H^1(\Omega)`$: subtract a bounded trace extension and use coercivity on $`H_0^1`$. Hence their liftings satisfy

```math
u_{\varphi_j}\longrightarrow u_\varphi\quad\text{in }H^1(\Omega).
```

A subsequence converges almost everywhere in $`\Omega`$. Estimate (2) is uniform along this subsequence, and passage to its almost-everywhere limit gives

```math
\|u_\varphi\|_{L^\infty(\Omega)}
\le K(\Omega,C)\|\varphi\|_{L^\infty(\partial\Omega)}.
```

This is the entire target of problem 218.

## Dependency and scope audit

The main published dependency is Agmon's complex-coefficient Theorem I, specifically its second-order case with the $`L^1`$ remainder retained. The remaining standard tools are the Sobolev trace extension theorem, Lax–Milgram, smooth-domain $`H^2`$ Dirichlet regularity, Green's identity, and heat smoothing on a compact manifold. The proof explicitly checks proper ellipticity in dimension two and explains how the estimate reaches bounded boundary data that need not be continuous.

The source of the target is ter Elst and Ouhabaz, [Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients](https://link.springer.com/article/10.1007/s00020-025-02796-9), the final paragraph of problem 1. This report settles the constant-coefficient, smooth-domain subquestion recorded as problem 218. It does not assert the corresponding conclusion for arbitrary measurable complex coefficients or merely Lipschitz domains. It is a deduction from an existing maximum theorem, not a claim to have newly proved that theorem. Independent review of the theorem application and all functional-space identifications remains outstanding.
