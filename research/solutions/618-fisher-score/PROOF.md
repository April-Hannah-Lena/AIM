# Smooth-gradient approximation of Fisher scores by extension to a closed manifold

**Target:** Problem 618 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete proof using an established entropy theorem, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Proof construction, source comparison and self-review were performed by the same AI agent; no independent or human audit is claimed.

## Theorem

The assertion in problem 618 holds. In fact the approximating functions may be chosen smooth up to the boundary. The extension concerns the square root of the density, not its logarithm. Neither positivity nor boundedness of the original density is needed.

## Established ingredient on a manifold without boundary

We use M. Erbar's Proposition 4.3 in [The heat equation on manifolds as a gradient flow in the Wasserstein space](https://numdam.org/item/10.1214/08-AIHP306.pdf), Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 46 (2010), 1–23. Together with the definition of the tangent space in §2, its relevant consequence is:

> On a complete Riemannian manifold without boundary with Ricci curvature bounded below, a probability density with finite entropy and an integrable weak gradient of the form $`\nabla q=q w`$, $`w\in L^2(q)`$, has $`w`$ in the $`L^2(q)`$ closure of gradients of smooth compactly supported functions.

This is a paraphrase of the precise source implication, not a new density theorem assumed without justification. Compact closed manifolds satisfy the geometric hypotheses and all probability measures on them have finite second moment. The finite-entropy hypothesis will be verified below.

## 1. Extension and metric choice

First suppose $`M`$ is connected and has positive dimension. If its boundary is nonempty, let $`N`$ be a smooth compact double of $`M`$. If its boundary is empty, let $`N=M`$. Give $`N`$ any smooth Riemannian metric $`h`$. It is not necessary for its restriction to equal the given metric $`g`$: on the compact submanifold $`M`$, the two smooth positive-definite metrics, their cotangent norms and their volume densities are uniformly equivalent.

Write $`u=\sqrt\rho\in H^1(M)`$. There exists a nonnegative extension $`\widetilde u\in H^1(N)`$ with $`\widetilde u|_M=u`$. For completeness, the usual Sobolev extension is obtained in boundary charts by reflection across the flattened boundary and a smooth partition of unity. Equivalently, use a collar of the smooth double, reflect $`u`$ onto a collar in the second copy, multiply there by a cutoff equal to one near the common boundary, and set it to zero farther into that copy. The traces agree on the seam, so the glued function is $`H^1`$. Taking its absolute value preserves $`H^1`$, gives nonnegativity and keeps its restriction to $`M`$ equal to $`u`$. On a boundaryless $`M`$ no extension is necessary.

All Sobolev assertions are unchanged by the uniformly equivalent smooth metrics. Set

```math
Z=\int_N\widetilde u^2\,dV_h>0,\qquad
q=\frac{\widetilde u^2}{Z},\qquad
w=\begin{cases}2\nabla_h\widetilde u/\widetilde u,&\widetilde u>0,\\0,&\widetilde u=0.\end{cases}
```

## 2. Checking the entropy theorem's analytic assumptions

The Sobolev product and chain rules give $`q\in W^{1,1}(N)`$ and

```math
\nabla_h q=\frac{2\widetilde u\nabla_h\widetilde u}{Z}=q w.
```

The identity also holds on the zero set. Sobolev locality gives $`\nabla_h\widetilde u=0`$ almost everywhere on that set. Consequently

```math
\int_N|w|_h^2q\,dV_h
=\frac4Z\int_N|\nabla_h\widetilde u|_h^2\,dV_h<\infty.
```

The entropy is finite as well. Compact-manifold Sobolev embedding gives $`\widetilde u\in L^{2+\varepsilon}(N)`$ for some $`\varepsilon>0`$: in dimensions at least three use the exponent $`2d/(d-2)`$, in dimension two any finite exponent above two, and in dimension one boundedness. Hence $`q\in L^{1+\varepsilon/2}`$. The positive part of $`q\log q`$ is integrable by $`r\log r\le C(1+r^{1+\varepsilon/2})`$, and the negative part is bounded by $`1/e`$ pointwise on a finite-volume manifold.

The smooth compact manifold $`(N,h)`$ is complete and has a finite Ricci lower bound. Every assumption of Erbar's proposition is therefore satisfied.

## 3. Restriction of smooth potentials

By the cited tangent-space conclusion there exist $`\Phi_j\in C^\infty(N)`$ such that

```math
\int_N|\nabla_h\Phi_j-w|_h^2q\,dV_h\longrightarrow0.
```

Put $`\varphi_j=\Phi_j|_M`$, which is smooth up to the boundary. On $`\{u>0\}\subset M`$ define the cotangent field $`\eta=2\,du/u`$, and set it to zero elsewhere. Its $`g`$-dual is exactly the target score $`s_\rho`$. Its $`h`$-dual on $`M`$ is $`w`$, and $`q=\rho/Z`$ there. Uniform equivalence of the two metrics and volume elements gives a finite constant $`C`$, independent of $`j`$, such that

```math
\begin{aligned}
\int_M|\nabla_g\varphi_j-s_\rho|_g^2\rho\,dV_g
&=\int_M|d\varphi_j-\eta|_{g^{-1}}^2\rho\,dV_g\\
&\le C Z\int_M|\nabla_h\Phi_j-w|_h^2q\,dV_h\\
&\le C Z\int_N|\nabla_h\Phi_j-w|_h^2q\,dV_h\longrightarrow0.
\end{aligned}
```

This is the requested conclusion.

## Remaining geometric cases

A compact manifold has only finitely many connected components, since its components are open and compactness supplies a finite subcover. Apply the construction separately on each positive-mass component and choose the approximation error below $`1/j`$ divided by the number of such components. On a zero-mass component $`\rho=0`$ almost everywhere and it contributes nothing, so take the potential zero. Combining these componentwise functions is smooth. In dimension zero every gradient and the score vanish, making the statement immediate.

## Audit and scope

The proof checks the full target, including densities that vanish or are unbounded, nonconvex smooth boundary, arbitrary finite dimension, and the absence of a boundary condition on the approximating potentials. Restriction of ambient smooth potentials is legitimate precisely because no Neumann or Dirichlet condition is imposed on them.

The ambient metric need not be a reflected copy of $`g`$; using an arbitrary smooth metric avoids imposing a false smoothness assertion on a reflected metric at a non-totally-geodesic boundary. Covectors and uniform norm equivalence explicitly transfer the conclusion back to the required metric and volume.

This is an application of an established boundaryless theorem plus Sobolev extension and restriction. It does not assume weighted smooth-gradient density on the original manifold, does not mollify $`\log\rho`$ across its zeros, and does not assert that smoothing the density alone proves convergence in the original weighted norm. No computational certificate is needed. Independent checking of the source implication and the extension argument remains outstanding.

## References

- M. Erbar, [The heat equation on manifolds as a gradient flow in the Wasserstein space](https://numdam.org/item/10.1214/08-AIHP306.pdf), Proposition 4.3 and §2. These give the exact external theorem and the smooth-gradient definition of its tangent-space conclusion.
- J.-B. Casteras, M. Flaim and L. Monsaingeon, [Entropy and Fisher information in non-convex domains: one chain to rule them all](https://arxiv.org/html/2512.05826), the conjecture following Theorem 4 and Lemma A.3. These identify the target and its previously stated bounded-density case.
