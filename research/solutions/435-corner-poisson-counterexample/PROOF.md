# A reentrant corner rules out the proposed Poisson bound

**Target:** Problem 435 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete counterexample, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Construction, domain checks, estimates and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Domain and an explicit harmonic extension

Take $`d=2`$, $`C=I`$, and the bounded sector

```math
\Omega=\{(r\cos\theta,r\sin\theta):0<r<1,\ 0<\theta<3\pi/2\}.
```

This is a bounded connected Lipschitz domain. Its corner at the origin has interior angle $`3\pi/2`$; the two corners at the ends of the circular arc also admit Lipschitz graph charts. The coefficient matrix is real, symmetric, uniformly elliptic and smooth on all of the plane.

Set $`\kappa=2/3`$ and define

```math
u(r,\theta)=r^\kappa\sin(\kappa\theta).
```

The polar-coordinate Laplacian shows $`\Delta u=0`$ in $`\Omega`$. Also

```math
|\nabla u|^2=\kappa^2r^{2\kappa-2},\qquad
\int_\Omega|\nabla u|^2<\infty,
```

and $`u\in H^1(\Omega)`$. Its trace $`f`$ is zero on both straight edges, and on the unit circular arc it is

```math
f(1,\theta)=\sin(\kappa\theta)\ge0.
```

In particular $`f\in H^{1/2}(\partial\Omega)\cap L^\infty(\partial\Omega)`$ and

```math
\|f\|_{L^1(\partial\Omega)}
=\int_0^{3\pi/2}\sin(2\theta/3)\,d\theta=3.                  \tag{1}
```

## The weak conormal derivative belongs to L2

On each straight edge the outward normal derivative of $`u`$ is

```math
\partial_\nu u=-\kappa r^{\kappa-1}=-\frac23r^{-1/3},
```

whereas on the circular arc it is $`\kappa\sin(\kappa\theta)`$. Denote this piecewise function by $`h`$. It is in $`L^2(\partial\Omega)`$, since $`\int_0^1r^{-2/3}\,dr<\infty`$.

We check the weak definition, including the corner. Integrate Green's formula over $`\Omega\cap\{r>\delta\}`$ against a function smooth on a neighborhood of $`\overline\Omega`$. The absolute value of the omitted small-circle flux term is bounded by

```math
\kappa\delta^{\kappa-1}\,\delta\int_0^{3\pi/2}|v(\delta,\theta)|\,d\theta
\le C_v\delta^\kappa\longrightarrow0.
```

The volume integral converges because $`\nabla u\in L^2`$, and the other boundary integrals converge to those involving $`h`$. Hence

```math
\int_\Omega\nabla u\cdot\overline{\nabla v}
=\int_{\partial\Omega}h\,\overline{\mathop{\mathrm{Tr}}\nolimits v}\,dS.
```

Density of restrictions of smooth functions in $`H^1(\Omega)`$, and continuity of the trace into $`L^2(\partial\Omega)`$, extend this identity to every $`H^1`$ test function. Thus, with exactly the operator definition in the target,

```math
f\in D(N),\qquad Nf=h.                                      \tag{2}
```

## Consequence of the conjectured bound on separated supports

Let $`T_t=e^{-tN}`$. Suppose the proposed bound held with finite constants $`M`$ and $`\omega`$. In dimension two it can be written as

```math
|K_t(z,w)|\le\frac{Mte^{\omega t}}{(t+|z-w|)^2}.              \tag{3}
```

For $`0<\varepsilon<1/4`$, let $`g_\varepsilon`$ be the characteristic function of the segment $`\theta=0`$, $`\varepsilon<r<2\varepsilon`$, and zero on the rest of the boundary. It belongs to $`L^2(\partial\Omega)`$, has $`L^1`$ norm $`\varepsilon`$, and its support is disjoint from that of $`f`$. Points on this segment have distance at least $`1-2\varepsilon>1/2`$ from the unit circular arc. Consequently (1), (3), and the kernel representation imply

```math
\frac{|\langle T_tf,g_\varepsilon\rangle_{L^2(\partial\Omega)}|}{t}
\le4Me^{\omega t}\|f\|_1\|g_\varepsilon\|_1
=12Me^{\omega t}\varepsilon.                               \tag{4}
```

By (2), the generator identity gives $`(T_tf-f)/t\to-Nf`$ in $`L^2`$ as $`t\downarrow0`$. Since $`\langle f,g_\varepsilon\rangle=0`$, the limit on the left of (4) is

```math
\left|\langle-Nf,g_\varepsilon\rangle\right|
=\kappa\int_\varepsilon^{2\varepsilon}r^{\kappa-1}\,dr
=(2^\kappa-1)\varepsilon^\kappa.
```

Thus (4) would require

```math
(2^{2/3}-1)\varepsilon^{2/3}\le12M\varepsilon
\qquad(0<\varepsilon<1/4).
```

Dividing by $`\varepsilon`$ and letting it tend to zero is a contradiction. No finite pair of constants in the proposed Poisson bound exists for this domain and coefficient matrix.

## Target comparison and audit

The counterexample uses the ordinary Laplacian, not rough coefficients or a different boundary operator. The harmonic trace is in the stated trace space, and its conormal derivative is square-integrable, so differentiating the semigroup at zero uses an actual vector in its generator domain. The second test function only needs to belong to $`L^2`$; no generator-domain assertion about it is used. The boundary sets remain a fixed positive distance apart, and the argument integrates the asserted almost-everywhere estimate, avoiding any exceptional-point issue at the corner itself.

The obstruction is the integrable but unbounded flux near a reentrant corner from boundary data supported on a distant arc. The proposed estimate would bound this separated-support flux by the product of the two boundary $`L^1`$ norms, which the explicit harmonic function violates.

The target is the real-coefficient Lipschitz-domain alternative in problem 5 of ter Elst and Ouhabaz, [Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients](https://link.springer.com/article/10.1007/s00020-025-02796-9). The argument does not address the separate smooth-domain complex-coefficient alternative. It is entirely analytic and supplies all geometric and operator-domain checks. Independent mathematical review remains outstanding.
