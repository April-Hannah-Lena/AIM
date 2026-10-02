# 549. Separation of measures by Cartan–Hadamard sliced distances

**Area:** Statistical inference and optimal transport on manifolds

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`(M,g)`$ be a finite-dimensional, complete, simply connected Riemannian manifold with nonpositive sectional curvature. Fix $`o\in M`$, let $`S_o`$ be the unit sphere in $`T_oM`$, and let $`\lambda_o`$ be its uniform probability measure. For $`v\in S_o`$, set $`\gamma_v(t)=\exp_o(tv)`$ and define two real-valued projections:

```math
G_v(x)=\mathop{\rm argmin}_{t\in\mathbb R}d(x,\gamma_v(t))^2,
\qquad H_v(x)=\lim_{t\to\infty}\bigl(d(x,\gamma_v(t))-t\bigr).
```

The first is the signed coordinate of the nearest point on a geodesic; the second is its Busemann function. Both are well-defined and 1-Lipschitz in $`x`$.

For $`1\le p<\infty`$, let $`\mathcal P_p(M)`$ be the Borel probability measures with finite $`p`$th distance moment. For either choice $`F=G`$ or $`F=H`$, define

```math
D_{F,p}(\mu,\nu)^p=\int_{S_o}W_p^p\bigl((F_v)_\#\mu,(F_v)_\#\nu\bigr)\,d\lambda_o(v),
```

where $`W_p`$ on the right is the usual Wasserstein distance on $`\mathbb R`$ and $`\#`$ denotes pushforward.

Prove or disprove, for each of these two projection families, that

```math
D_{F,p}(\mu,\nu)=0\quad\Longrightarrow\quad\mu=\nu
```

for every such manifold, base point, exponent and pair $`\mu,\nu\in\mathcal P_p(M)`$. Equivalently, determine whether equality of the projected probability laws for $`\lambda_o`$-almost every direction determines the original measure. This is the distance-property conjecture in §5.1 of [1]. The two variants form one problem here; a result for one variant alone does not settle the other.

The integration uses the entire tangent unit sphere. Restricting the directions, fixing relative direction weights on a product manifold, or replacing the probability measures by a particular smooth density class changes the question.

## Application

Sliced optimal transport compares high-dimensional distributions through inexpensive one-dimensional transport problems. On manifolds, this supports statistical comparison of hyperbolic embeddings and matrix-valued data. Separation is needed to know that a zero population discrepancy identifies the distribution, rather than concealing a difference that every chosen projection misses.

## References

1. C. Bonet, L. Drumetz and N. Courty, [Sliced-Wasserstein Distances and Flows on Cartan-Hadamard Manifolds](https://www.jmlr.org/papers/v26/24-0359.html), *Journal of Machine Learning Research* **26**(32) (2025), 1–76. Definition 5, p.12; §5.1, pp.24–25; Lemma 25 and Proposition 26, p.27. [Published PDF](https://www.jmlr.org/papers/volume26/24-0359/24-0359.pdf).
2. The same authors, [arXiv:2403.06560](https://arxiv.org/abs/2403.06560), §5.1. The located arXiv version also states the conjecture; it is another version of [1].

## Status review

**Known cases:** Both constructions are finite pseudometrics. The source proves separation for pullback Euclidean metrics, including its log-Euclidean positive-definite-matrix example.

**Remaining target:** Establish or refute separation for both projection families on general Cartan–Hadamard manifolds, for all Borel probability measures with the stated finite moment.

The source relates separation to injectivity of an associated transform of measures. Existing results for geodesic X-ray transforms with specified function classes and curvature or decay assumptions do not establish the stated all-measure, all-manifold assertion. The later hierarchical hybrid sliced construction retains a conditional injectivity requirement; its discussion of fixed product weights concerns a different restriction of the directions. The 2026 Busemann-function work concerns projections in Wasserstein space and does not supply this separation theorem.

Searches through 24 September 2026 found no matching proof, counterexample or solution announcement. Repository searches found no equivalent existing target; the Cartan–Hadamard isoperimetric problem is distinct.
