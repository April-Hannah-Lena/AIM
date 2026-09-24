# 009. The spectral honeycomb conjecture

**Area:** Spectral partitions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^2$ be a bounded connected Lipschitz domain of area $A$. For $k\ge1$, set

$$
\mathcal L_k(\Omega)=\inf_{(D_1,\ldots,D_k)}\max_{1\le i\le k}\lambda_1(D_i),
$$

where the infimum runs over pairwise disjoint nonempty connected open subsets of $\Omega$, and $\lambda_1$ is the first Dirichlet eigenvalue. Let $H$ be a regular hexagon of area one. Prove or disprove

$$
\lim_{k\to\infty}\frac{A\mathcal L_k(\Omega)}{k}=\lambda_1(H).
$$

In particular, the competitors are not required to be convex.

## Application

Spectral partitions model optimal division into cells with balanced lowest vibration or diffusion frequencies. The conjecture predicts a universal large-cell-count design.

## References

1. V. Bonnaillie-Noël and B. Helffer, [Nodal and spectral minimal partitions — The state of the art in 2016](https://arxiv.org/abs/1506.07249), in Shape Optimization and Spectral Theory (2017), §9.1, hexagonal conjecture.
2. D. Bucur, I. Fragalà, B. Velichkov and G. Verzini, [On the honeycomb conjecture for a class of minimal convex partitions](https://arxiv.org/abs/1703.05383), Transactions of the AMS 370 (2018), introduction and spectral application.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book chapter states the asymptotic conjecture. Bucur and coauthors prove results for convex partitions and specified functionals; their spectral case still requires additional polygonal inequalities. Their title does not represent a solution of the unrestricted Laplacian conjecture. The update search found no such resolution.

**Search audit:** “spectral honeycomb hexagonal conjecture 2025 2026”; “spectral partitions honeycomb proof Laplacian”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
