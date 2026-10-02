# 536. Optimal star-discrepancy lower bound for infinite sequences

**Area:** Uncertainty quantification and quasi-Monte Carlo integration

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix an integer $`d\ge2`$ and an infinite sequence $`x_1,x_2,\ldots`$ in $`[0,1)^d`$. For its first $`N`$ points, define the normalized star discrepancy

```math
D_N^*=\sup_{t\in[0,1]^d}\left|\frac1N\sum_{n=1}^N\mathbf1_{[0,t)}(x_n)-\prod_{j=1}^d t_j\right|,
```

where $`[0,t)=\prod_{j=1}^d[0,t_j)`$.

Must every such sequence satisfy

```math
\limsup_{N\to\infty}\frac{N D_N^*}{(\log N)^d}>0?
```

Equivalently, does every sequence have a positive constant $`c`$ for which $`D_N^*\ge c(\log N)^d/N`$ for infinitely many $`N`$? The constant may depend on the sequence and on $`d`$. Sequences attaining the corresponding upper order exist; the question is whether any sequence can improve that order at all sufficiently large prefixes.

## Application

Star discrepancy controls equal-weight integration error for functions of bounded Hardy–Krause variation through the Koksma–Hlawka inequality. The question concerns a fundamental limit on extensible quadrature rules used in uncertainty quantification.

## References

1. T. J. Sullivan, [Introduction to Uncertainty Quantification](https://doi.org/10.1007/978-3-319-23395-6), Springer (2015), p.190, following Theorem 9.23.
2. M. B. Levin, [On the lower bound of the discrepancy of Halton's sequence I](https://doi.org/10.1016/j.crma.2016.02.003), Comptes Rendus Mathématique **354** (2016), 445–448, introduction, equations (2)–(3).
3. R. Hofer, [Variants of the Littlewood conjecture, their connection to uniformly distributed sequences, and the exact order of the discrepancy of van der Corput–Kronecker-type sequences](https://doi.org/10.5802/jtnb.1369), Journal de Théorie des Nombres de Bordeaux **38** (2026), 489–514.
4. J. Dick, [A Proof of Novak–Woźniakowski Conjecture: Optimal Polynomial Tractability Exponents for Inverse Star Discrepancy](https://arxiv.org/abs/2607.23571v2), version 2 (2026), Theorems 1.1–1.2 and Remark 1.4.

## Status review

Reference [2] states the infinite-sequence conjecture and proves the order for Halton sequences, which leaves the universal assertion unresolved. Reference [3]'s publisher abstract still describes the general order as conjectural; that abstract was checked, rather than its full proof text.

Reference [4] announces optimal tractability exponents for inverse star discrepancy in a joint dimension–accuracy regime. It does not establish this fixed-dimensional lower bound along infinitely many prefixes of every sequence. The review found no matching solution announcement as of the check date.
