# 025. The complete Crouzeix conjecture

**Area:** Operator theory and numerical linear algebra

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

For every $`n,m\ge1`$, $`A\in\mathbb C^{n\times n}`$, and polynomial $`F(z)=\sum_{j=0}^d C_jz^j`$ with coefficients $`C_j\in\mathbb C^{m\times m}`$, is

```math
\left\|\sum_{j=0}^d C_j\otimes A^j\right\|_2
\le 2\max_{z\in W(A)}\|F(z)\|_2?
```

Here $`W(A)=\{x^*Ax:x\in\mathbb C^n,\ \|x\|_2=1\}`$, $`\otimes`$ is the Kronecker product, and $`\|\cdot\|_2`$ is the Euclidean operator norm. The unresolved range is arbitrary $`n\ge4`$ and arbitrary matrix level $`m`$.

## Application

Matrix-valued approximation bounds control coupled matrix functions and block computations. Complete spectral-set bounds also govern dilation and similarity methods used to analyze nonnormal operators.

## References

1. M. Crouzeix and C. Palencia, [The numerical range is a $`(1+\sqrt2)`$-spectral set](https://doi.org/10.1137/17M1116672), SIAM J. Matrix Anal. Appl. 38 (2017), 649–655. Universal complete bound.
2. P. Åhag, R. Czyż and J. Virtanen, [Square Functions and the Complete Crouzeix Conjecture in Dimension Three](https://arxiv.org/abs/2608.27346), 2026, v2; introduction and Theorem 1.1. Complete bound through order three.
3. A. Townsend and A. Greenbaum, [The Neurosurgery Resident Who Proved Crouzeix’s Conjecture](https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf), 15 August 2026. Expert verification of the distinct scalar result.

## Status review

**Known cases:** The complete matrix-valued bound is established through matrix order three, for arbitrary amplification level.

**Remaining target:** The complete bound for arbitrary matrix order, including orders at least four, and arbitrary amplification level.

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The September 2026 version of Åhag–Czyż–Virtanen distinguishes the complete conjecture from the now-resolved scalar conjecture and reports only the dimensions $`n\le3`$. The scalar theorem does not establish this matrix-amplified inequality. No general complete resolution was located.

Searches included: `complete Crouzeix conjecture 2026`; `Square Functions Complete Crouzeix dimension three`; `Crouzeix solution 2026`. This is a documented literature check, not a certification that no solution exists.
