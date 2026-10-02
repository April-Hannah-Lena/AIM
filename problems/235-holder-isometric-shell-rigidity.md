# 235. Rigidity of positively curved shells above one-half Hölder regularity

**Area:** Thin-shell geometry and elasticity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

Let $`g`$ be any smooth Riemannian metric on $`S^2`$ with strictly positive Gaussian curvature. For every $`\alpha\in(1/2,1)`$ and every $`C^{1,\alpha}`$ embedding $`u:S^2\to\mathbb R^3`$ satisfying the isometry condition

```math
Du(x)^TDu(x)=g(x)
```

in local coordinates, must $`u(S^2)`$ be the boundary of a convex body?

Here $`C^{1,\alpha}`$ means that first derivatives are locally Hölder continuous with exponent $`\alpha`$, and an embedding is an injective immersion that is a homeomorphism onto its image. The unresolved assertion includes the interval $`1/2<\alpha\leq2/3`$.

## Application

An isometry models deformation of a thin shell without stretching its mid-surface. The conjecture identifies how much regularity prevents the highly folded configurations allowed by the Nash–Kuiper theorem.

## References

- Camillo De Lellis, [*Rigidity and flexibility of isometric embeddings*](https://math.ucsd.edu/seminar/rigidity-and-flexibility-isometric-embeddings) (2020 lecture), abstract: the positive-curvature formulation and expected exponent $`1/2`$.
- Wentao Cao and Dominik Inauen, [*Rigidity and flexibility of isometric extensions*](https://doi.org/10.4171/CMH/564) (2024), introduction and main theorems: a weaker connection-preservation threshold for extensions.
- Dominik Inauen, [*Flexibility of codimension one $`C^{1,\theta}`$ isometric immersions*](https://arxiv.org/abs/2603.08382) (2026 preprint), introduction: recent flexibility bounds and the still unknown optimal threshold.

## Status review

**Known cases:** Classical rigidity establishes convexity when the Hölder exponent is greater than two-thirds.

**Remaining target:** Convexity throughout the stated exponent range, including exponents greater than one-half and at most two-thirds.

**Literature check:** Open in cited literature; no later resolution located.

Searched “positive curvature isometric embedding rigidity alpha one half proof 2025 2026”, “Borisov threshold”, and the March 2026 flexibility paper. Classical rigidity above $`2/3`$ and results on connection preservation do not prove convexity throughout the displayed range. The 2026 preprint improves flexibility in higher dimensions; it does not close this two-dimensional rigidity gap.
