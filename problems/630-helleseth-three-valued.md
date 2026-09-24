# 630. Excluding three correlation levels in quadratic field towers

**Area:** Coding theory and sequence design

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $p\ge5$ be prime, $r\ge0$ an integer, and $F=\mathbb F_{p^{2^r}}$. For a positive integer $d$ coprime to $|F|-1$, define

$$
W_{F,d}(a)=\sum_{x\in F}\exp\!\left(\frac{2\pi i}{p}\mathop{\mathrm{Tr}}\nolimits_{F/\mathbb F_p}(x^d-ax)\right).
$$

Must the set

$$
\{W_{F,d}(a):a\in F\setminus\{0\}\}
$$

have cardinality different from three?

This is the unresolved characteristic range of Helleseth's three-valued conjecture. No assumption $d\equiv1\pmod{p-1}$ is imposed. Exponents congruent to a power of $p$ modulo $|F|-1$ are allowed, but their two-valued spectra already satisfy the assertion.

## Application

These spectra describe cross-correlation of maximum-length sequences and weight distributions of related cyclic codes. Ruling out three levels constrains the sequence and code designs possible over fields obtained by repeated quadratic extension.

## References

1. L. Nguyen, [On Weil Sums, Conjectures of Helleseth, and Niho Exponents](https://arxiv.org/abs/2006.15726), *Journal of Number Theory* **234** (2022), 240–258, Section 1.2, Conjecture 1.5.
2. D. J. Katz, [Weil sums of binomials: properties, applications and open problems](https://par.nsf.gov/servlets/purl/10090054), Section 10, Conjecture 10.6 and Corollary 10.9.
3. D. J. Katz, [Divisibility of Weil Sums of Binomials](https://arxiv.org/abs/1407.7923), for the characteristic-three case.
4. G. Wu, K. Feng, N. Li, and T. Helleseth, [New Results on the −1 Conjecture on Cross-Correlation of m-Sequences Based on Complete Permutation Polynomials](https://doi.org/10.1109/TIT.2023.3238994), *IEEE Transactions on Information Theory* **69**(6) (2023), 4035–4044. Journal discovery route through the related vanishing conjecture.

## Status review

**Known cases:** The analogous statement is proved for characteristics two and three. In every characteristic, a possible counterexample in a quadratic tower cannot have its three values symmetric about zero.

**Remaining target:** Exclude nonsymmetric three-valued spectra in characteristics at least five. This differs from the vanishing conjecture, which asks whether zero occurs without prescribing the size of the spectrum.

Current web and arXiv searches found no general proof or announcement. Native Helleseth/conjecture searches in GitHub, Zenodo, and Palomar returned no matching announcement; repository comparison found no duplicate. No recent comprehensive status survey was found.
