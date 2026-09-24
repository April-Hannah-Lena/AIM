# 179. A deterministic nontrivial growth exponent for planar DLA

**Area:** Aggregation and fractal growth

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Start with $`A_1=\{0\}\subset\mathbb Z^2`$. Given $`A_n`$, attach one site of its exterior vertex boundary according to harmonic measure from infinity: the limiting first-hit distribution on that boundary for simple random walk started arbitrarily far away. Let $`R_n=\max\{|x|:x\in A_n\}`$. Does there exist a deterministic $`\beta\in(1/2,2/3]`$ such that

```math
\lim_{n\to\infty}\frac{\log R_n}{\log n}=\beta\qquad\text{almost surely}?
```

This is external diffusion-limited aggregation with one lattice site added at each step.

## Application

DLA models diffusion-controlled deposition. A growth exponent would quantify the relation between deposited mass and aggregate radius, including its departure from compact growth.

## References

- [Ilya Losev and Stanislav Smirnov, *How Long Are the Arms in DBM?* (2025)](https://doi.org/10.1007/s00220-025-05276-8), §1, growth-exponent prediction and Theorem 1.
- [Harry Kesten, *How long are the arms in DLA?* (1987), institutional copy](https://www.math.stonybrook.edu/~bishop/classes/math627.S22/papers/Kesten3.pdf), the planar upper bound.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 paper retains the prediction of a deterministic nontrivial exponent and matches the existing DLA growth bound. Neither the existence of the exponent nor its strict separation from compact growth is established by that bound.

Search topics checked on 2026-09-08: DLA growth exponent existence 2025 2026; diffusion limited aggregation deterministic exponent proof.
