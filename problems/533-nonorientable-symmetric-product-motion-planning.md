# 533. Motion-planning complexity of symmetric products of non-orientable surfaces

**Area:** Applied topology and motion planning

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`N_g=\#^g\mathbb{RP}^2`$ be the closed non-orientable surface of genus $`g\ge2`$. For an integer $`n\ge2`$, let

```math
X_{n,g}=\mathop{\mathrm{SP}}\nolimits^n(N_g)=N_g^n/\mathfrak S_n,
```

where the symmetric group permutes coordinates; coincident points are allowed. Give this space the quotient topology.

Use normalized topological complexity: $`\mathop{\mathrm{TC}}\nolimits(X)`$ is the least integer $`r`$ such that $`X\times X`$ has an open cover $`U_0,\ldots,U_r`$ with continuous maps $`s_i:U_i\to C([0,1],X)`$ satisfying

```math
s_i(x,y)(0)=x,\qquad s_i(x,y)(1)=y.
```

The path space has the compact-open topology.

Determine $`\mathop{\mathrm{TC}}\nolimits(X_{n,g})`$ for all $`n,g\ge2`$. In particular, close the remaining gap between the known lower and upper bounds when $`n`$ is not a power of two.

## Application

The space describes unordered collections of points on a non-orientable surface, with collisions permitted. Its topological complexity measures the minimum number of continuous local rules needed to move between two such collections.

## References

1. E. Jauhari, [LS-category and sequential topological complexity of symmetric products](https://doi.org/10.1007/s41468-025-00223-x), Journal of Applied and Computational Topology **9**, 25 (2025), §6, especially pp.28–29.
2. J. González and E. Jauhari, [On the sequential topological complexity and the LS-category of the cofiber of higher diagonals for symmetric products of non-orientable surfaces](https://arxiv.org/abs/2603.14788), arXiv:2603.14788v1 (2026), Theorem 1.1, Corollary 1.6(ii) and §4.

## Status review

**Known cases:** Write $`2^e\le n<2^{e+1}`$. The 2026 work [2] proves

```math
L(n,g)\le\mathop{\mathrm{TC}}\nolimits(X_{n,g})\le4n-1,
```

where

```math
L(n,g)=\begin{cases}
2^{e+2}+g-2,&g\le2n-2^{e+1}+1,\\
2^{e+1}+2n-1,&g\ge2n-2^{e+1}+1.
\end{cases}
```

The two expressions agree at the boundary. Consequently $`\mathop{\mathrm{TC}}\nolimits(X_{2^e,g})=2^{e+2}-1`$ for $`e\ge1`$.

**Remaining target:** Exact values for the other symmetric powers. The lower bound computes a mod-2 zero-divisor cup length; it is not an exact computation of topological complexity in all cases. Higher sequential-complexity results in [2] also do not settle this ordinary two-endpoint invariant.

The genus-one case is excluded because it gives even-dimensional real projective spaces, already covered by [527](526-projective-motion-planning.md). Checks on 24 September 2026 found the partial announcement [2] but no full resolution of the stated family.
