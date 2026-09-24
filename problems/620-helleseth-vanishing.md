# 620. A zero in the nontrivial spectrum of a power permutation

**Area:** Information theory, sequence design and finite fields

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`F=\mathbb F_q`$, where $`q=p^n>2`$ and $`p`$ is prime. Let $`d`$ be a positive integer satisfying

```math
\gcd(d,q-1)=1,\qquad d\equiv1\pmod{p-1}.
```

Write $`\mathop{\mathrm{Tr}}\nolimits:F\to\mathbb F_p`$ for the absolute trace and define

```math
W_{F,d}(a)=\sum_{x\in F}\exp\!\left(\frac{2\pi i}{p}\mathop{\mathrm{Tr}}\nolimits(x^d-ax)\right).
```

Does there always exist $`a\in F\setminus\{0\}`$ for which $`W_{F,d}(a)=0`$?

This is Helleseth's vanishing conjecture, also called the $`-1`$ conjecture for cross-correlation of maximum-length sequences. Excluding $`a=0`$ is essential: the permutation condition already gives $`W_{F,d}(0)=0`$.

## Application

The sums determine cross-correlation values of decimated maximum-length shift-register sequences. Such sequences are used in communications and remote sensing. Their spectra also determine weight information for associated cyclic codes; a zero sum corresponds to a cross-correlation value of $`-1`$.

## References

1. G. Wu, K. Feng, N. Li, and T. Helleseth, [New Results on the −1 Conjecture on Cross-Correlation of m-Sequences Based on Complete Permutation Polynomials](https://doi.org/10.1109/TIT.2023.3238994), *IEEE Transactions on Information Theory* **69**(6) (2023), 4035–4044.
2. L. Nguyen, [On Weil Sums, Conjectures of Helleseth, and Niho Exponents](https://arxiv.org/abs/2006.15726), *Journal of Number Theory* **234** (2022), 240–258. Author manuscript v3, Section 1.2, Conjecture 1.2 and Theorem 1.6.
3. D. J. Katz, [Weil sums of binomials: properties, applications and open problems](https://par.nsf.gov/servlets/purl/10090054), Section 11, Conjectures 11.1–11.2.

## Status review

**Known cases:** Niho exponents satisfy the conjecture. This includes invertible exponents over $`\mathbb F_{p^{2m}}`$ congruent to a power of $`p`$ modulo $`p^m-1`$. Further families related to complete permutation polynomials are addressed in reference [1]. Exponents congruent to a power of $`p`$ modulo $`q-1`$ are elementary cases.

**Remaining target:** All invertible exponents obeying the congruence modulo $`p-1`$. The established binary and ternary cases of Helleseth's separate three-valued conjecture do not settle this target.

Current searches found no matching resolution or repository duplicate. Exact Helleseth/conjecture searches in GitHub issues and repositories, Zenodo, and Palomar returned no announcement. The precise formulation was checked in the complete author manuscript [2]; the IEEE article was traced through its registry record and indexed abstract, without obtaining its complete text. No recent comprehensive status survey was located.
