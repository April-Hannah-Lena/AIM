# 121 — Local scalar geodesic tomography on smooth surfaces

**Area:** Geometric inverse problems / local tomography

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $(M,g)$ be a smooth Riemannian surface with boundary, strictly convex at $p\in\partial M$. Is there a sufficiently small neighborhood $U$ of $p$ with the following property? For every $f\in C^\infty(\overline U\cap M)$, if

$$
\int_\gamma f\,ds_g=0
$$

for every geodesic segment $\gamma$ lying in $U\cap M$ whose two endpoints lie on $U\cap\partial M$, then $f$ vanishes in some neighborhood of $p$ in $M$.

Only rays remaining in the small boundary neighborhood are available. The metric is smooth, without an analyticity assumption.

## Application

This asks whether measurements confined to a shallow part of a two-dimensional medium determine a scalar density there. It is the local uniqueness question behind reconstruction from grazing rays.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions* (Cambridge University Press, 2023), [Chapter 15, §15.1, Open problem 1](https://doi.org/10.1017/9781009039901.018). Source of the local surface question.
2. G. Uhlmann and A. Vasy, *The inverse problem for the local geodesic ray transform* (2016), [author preprint, arXiv:1210.2084](https://arxiv.org/abs/1210.2084), Theorem 1.1. Establishes the higher-dimensional local result.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book explicitly separates this surface problem from the local theorem in dimensions at least three. Euclidean and analytic special cases do not establish the statement for arbitrary smooth surface metrics. Searches included “local geodesic ray transform two dimensions open 2025 2026” and “local injectivity smooth surface Uhlmann Vasy solution”; no later general resolution was located.
