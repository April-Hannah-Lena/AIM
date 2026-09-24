# 616. The symmetry point of a unimodular lattice's secrecy function

**Area:** Lattice coding and information theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $L\subset\mathbb R^n$ be a full-rank integral unimodular lattice: $\langle x,z\rangle\in\mathbb Z$ for $x,z\in L$, and its covolume is one. For $y>0$, define

$$
\theta_L(y)=\sum_{x\in L}e^{-\pi y\|x\|_2^2},\qquad \Xi_L(y)=\frac{\theta_{\mathbb Z^n}(y)}{\theta_L(y)}.
$$

Prove or disprove the Belfiore–Solé conjecture:

$$
\Xi_L(y)\leq\Xi_L(1)\qquad\text{for every }n,L\text{ and }y>0.
$$

The point $y=1$ is already a symmetry point under $y\mapsto1/y$. The question is whether it always gives a global maximum. Uniqueness is not required; for $L=\mathbb Z^n$ the function is constant.

## Application

The secrecy function compares lattice theta sums in Gaussian wiretap coding. Locating its maximum would simplify evaluating the secrecy gain used to compare lattice code designs.

## References

1. A.-M. Ernvall-Hytönen, [On a Conjecture by Belfiore and Solé on Some Lattices](https://doi.org/10.1109/TIT.2012.2201915), *IEEE Transactions on Information Theory* **58**(9) (2012). [Author manuscript](https://arxiv.org/pdf/1104.3739), Section 1 and Theorem 1.
2. M. F. Bollauf and H.-Y. Lin, [On the Maximum Theta Series over Unimodular Lattices](https://arxiv.org/html/2403.16932v2), Section 3.2, Conjecture 2, and Section 4.

## Status review

**Known cases:** Reference [1] verifies the conjecture for the extremal even unimodular lattices known there. Reference [2] gives further sufficient criteria and reviews verified lattice families.

**Remaining target:** Prove the maximum assertion for every integral unimodular lattice, or give a counterexample. The disproof of the generalized conjecture for certain $\ell$-modular lattices with $\ell>1$ does not resolve this question.

The 2026 paper [A Sharp Reverse Minkowski Inequality for the Gaussian Mass of Integral Unimodular Lattices Through Rank 32](https://arxiv.org/html/2606.01347v1), Section 1, explicitly distinguishes its bound $\Xi_L(y)\geq1$ from the unresolved maximum-location conjecture. Searches through 24 September 2026 found no matching general resolution or repository duplicate. Native GitHub, Zenodo, and Palomar searches returned no matching record.
