# 175. Monotonicity of transport speed on Galton–Watson trees

**Area:** Transport on random branching networks

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $T$ be a Galton–Watson tree whose offspring distribution $(p_k)_{k\ge1}$ has finite support and mean $m>1$. There are no leaves. For $0<\lambda<m$, run the nearest-neighbor walk which, at a nonroot vertex with $k$ children, steps to its parent with probability $\lambda/(\lambda+k)$ and to each child with probability $1/(\lambda+k)$; at the root choose a child uniformly. Let

$$
v(\lambda)=\lim_{n\to\infty}\frac{d_T(X_n,\mathrm{root})}{n},
$$

the almost-sure deterministic speed. Must $v(\lambda_1)\ge v(\lambda_2)$ whenever $0<\lambda_1<\lambda_2<m$?

## Application

The question tests whether a stronger bias against outward motion necessarily reduces macroscopic transport through a random branching medium.

## References

- [Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (Cambridge, 2016; paperback 2021), online revision of 19 August 2026](https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf), Chapter 17, Question 17.33.
- [He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias* (2025)](https://www.cambridge.org/core/product/identifier/S002190022400113X/type/journal_article), restricted-bias progress.

## Status review

**Known cases:** The cited 2025 theorem proves speed monotonicity on a restricted interval of low bias values.

**Remaining target:** Monotonicity throughout the whole positive-speed interval for every finite-support offspring law in the statement.

**Literature check:** Open in cited literature; no later resolution located.

The updated book retains the monotonicity question. The 2025 paper proves it on a restricted bias interval; that does not cover the whole positive-speed interval. This entry uses bounded offspring to give a concrete subclass and avoids the separately studied regularity of the speed function.

Search topics checked on 2026-09-08: `Galton-Watson biased speed monotonicity 2026; Lyons Pemantle Peres monotonicity low bias 2025`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
