# 024. Lieb’s permanental dominance conjecture

**Area:** Matrix analysis and quantum information

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`n\ge1`$, let $`A=(a_{ij})\in\mathbb C^{n\times n}`$ be Hermitian positive semidefinite, and let $`\chi`$ be any irreducible character of the permutation group $`S_n`$. Define

```math
d_\chi(A)=\sum_{\sigma\in S_n}\chi(\sigma)\prod_{i=1}^n a_{i,\sigma(i)},\qquad
\mathop{\mathrm{per}}\nolimits A=\sum_{\sigma\in S_n}\prod_{i=1}^n a_{i,\sigma(i)}.
```

Prove or disprove

```math
\frac{d_\chi(A)}{\chi(e)}\le\mathop{\mathrm{per}}\nolimits A
```

for every such $`n,A,\chi`$, where $`e`$ denotes the identity permutation. On this matrix class these quantities are real.

## Application

Immanants describe interference associated with particle exchange symmetries. Comparing their normalized values constrains multiparticle bunching and indistinguishability tests.

## References

1. I. M. Wanless, [Lieb’s permanental dominance conjecture](https://doi.org/10.4171/90-2/48), in The Physics and Mathematics of Elliott Lieb, vol. 2 (2022), chapter 48, pp. 501–516. Dedicated survey.
2. F. Zhang, [An update on a few permanent conjectures](https://arxiv.org/abs/1608.02844), 2016; section on Lieb’s conjecture. Separates it from stronger false conjectures.
3. K. Rodtes, [Some remarks on permanental dominance conjecture](https://doi.org/10.1016/j.aam.2024.102758), Advances in Applied Mathematics 160 (2024), 102758. Partial results.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The dedicated survey states the conjecture is unresolved; the 2024 work treats partial cases. Searches through the check date located further applications and immanant inequalities, but no proof or counterexample for this universal statement. Permanent-on-top and Bapat–Sunder counterexamples do not themselves refute Lieb’s inequality.

Searches included: `Lieb permanental dominance conjecture 2025 2026`; `Lieb permanent dominance proof counterexample`; `Some remarks permanental dominance`. This is a documented literature check, not a certification that no solution exists.
