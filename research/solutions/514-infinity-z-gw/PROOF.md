# A bounded, path-connected attribute space with disconnected infinity Z-GW space

**Target:** Problem 514 at repository revision `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete counterexample, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex, at the repository user's request. The proof and its audit are by the same AI agent; no independent or human review is claimed.

## Construction

Equip $`Z=\mathbb R`$ with the bounded metric

```math
d_Z(s,t)=\min\{1,|s-t|\}.
```

This is a metric because $`\min\{1,a+b\}\le\min\{1,a\}+\min\{1,b\}`$ for nonnegative $`a,b`$. It induces the usual topology of the line. Thus $`Z`$ is separable and path connected. It is also complete: a sequence Cauchy for $`d_Z`$ is Euclidean Cauchy, since for every $`0<\varepsilon<1`$ the inequality $`d_Z(s,t)<\varepsilon`$ is equivalent to $`|s-t|<\varepsilon`$. Its Euclidean limit is also its $`d_Z`$ limit.

Every measurable real-valued network kernel is essentially bounded as a $`Z`$-valued kernel, since $`d_Z(\omega,0)\le1`$ everywhere. In particular all the kernels below satisfy the target's infinity-integrability requirement.

Divide these networks into two classes:

- $`\mathcal B`$: kernels that are essentially bounded in the **ordinary absolute value** on $`\mathbb R`$;
- $`\mathcal U`$: kernels that are not essentially bounded in ordinary absolute value.

These definitions use an auxiliary property of real representatives, not an extra requirement in the definition of admissible networks.

## Uniform separation for every coupling

Let $`\mathcal X\in\mathcal B`$ and $`\mathcal Y\in\mathcal U`$. Choose $`K<\infty`$ with $`|\omega_X|\le K`$ for $`\mu_X\otimes\mu_X`$-almost every pair. For every coupling $`\pi\in\Pi(\mu_X,\mu_Y)`$, the $`X^2`$ and $`Y^2`$ marginals of $`\pi\otimes\pi`$ are $`\mu_X\otimes\mu_X`$ and $`\mu_Y\otimes\mu_Y`$ respectively. Consequently:

- $`|\omega_X(x,x')|\le K`$ holds almost surely under $`\pi\otimes\pi`$;
- the event $`|\omega_Y(y,y')|>K+1`$ has strictly positive $`\pi\otimes\pi`$ probability.

On that positive-probability event, outside the null exceptional set,

```math
|\omega_X(x,x')-\omega_Y(y,y')|>1,
\qquad d_Z(\omega_X(x,x'),\omega_Y(y,y'))=1.
```

The distance integrand is everywhere at most one. Thus its essential supremum is exactly one **for every coupling**, and the normalization in the target gives

```math
\mathrm{GW}_\infty^Z(\mathcal X,\mathcal Y)=\frac12.
```

In particular, no zero-distance equivalence class meets both $`\mathcal B`$ and $`\mathcal U`$. They therefore induce a partition of the quotient metric space $`\mathcal M_\infty(Z)`$. Each part is open, since every open metric ball of radius $`1/2`$ centered in one part lies entirely in that part. Each part is also closed, being the complement of the other open part.

## Both parts are nonempty

For $`\mathcal B`$, take the one-point probability space and its constant zero kernel.

For $`\mathcal U`$, take the discrete Polish space $`X=\mathbb N=\{1,2,\ldots\}`$, probability masses $`\mu(\{n\})=2^{-n}`$, and the measurable kernel

```math
\omega(n,m)=n.
```

The ordinary absolute value of this kernel is essentially unbounded: for every $`K`$, the set $`\{n>K\}\times\mathbb N`$ has positive product probability. Its $`Z`$-distance to zero is nevertheless always one, so this is an admissible infinity-measure network. Symmetry is not required in the target. If desired, the symmetric kernel $`\max\{n,m\}`$ gives the same conclusion.

We have exhibited a partition of $`\mathcal M_\infty(Z)`$ into two nonempty open sets. The space is disconnected and therefore not path connected. This refutes problem 514 in its full stated generality.

## Audit and relation to the source question

The proof covers every possible coupling and every possible intermediate network, not just a proposed interpolation on a fixed probability space. Allowing node spaces, measures, kernels or zero-distance representatives to change along a path does not avoid the separation.

The truncation of the attribute metric is essential: it admits kernels unbounded in ordinary real value while maintaining the required essential boundedness in the actual metric. The target does not require $`Z`$ to be proper, geodesic, or to have compact bounded sets. The construction satisfies every hypothesis that is present: nonemptiness, completeness, separability, path connectivity, Polish node spaces, probability measures, measurable kernels and essential boundedness in $`d_Z`$.

The continuous image of a connected interval cannot meet both parts of the exhibited separation, so a path from the zero network to the explicit countable network cannot exist. This is an elementary topological consequence; no regularity of a lift of a quotient path is assumed.

The source is M. Bauer, F. Mémoli, T. Needham and M. Nishino, [The Z-Gromov-Wasserstein Distance](https://www.jmlr.org/papers/v26/24-2189.html), the infinity-case path-connectivity question in §4.2.3; see also the [author manuscript](https://arxiv.org/html/2408.08233). The source's disconnected two-point example has a disconnected attribute space. The present attribute space is path connected and meets the stronger hypothesis in the repository target. Geodesic attribute-space results and finite-exponent interpolation results are not contradicted.

The same AI agent checked the metric, completeness, the two marginal identities, positivity of the tail event under every coupling, the factor of one half, quotient invariance, and nonemptiness. No numerical evidence or unproved construction lemma is required. Independent review remains outstanding.
