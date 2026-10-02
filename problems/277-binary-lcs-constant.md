# 277. The exact asymptotic match fraction for independent binary sequences

**Area:** Sequence comparison and computational biology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`(X_i)`$ and $`(Y_i)`$ be independent sequences of independent fair bits. Define $`L_n=\max\{k:\exists i_1<\cdots<i_k\le n,\ j_1<\cdots<j_k\le n,\ X_{i_r}=Y_{j_r}\ (1\le r\le k)\}`$. Determine the exact value of the Chvátal–Sankoff constant $`\gamma_2=\lim_{n\to\infty}\mathbb E[L_n]/n`$. Its existence is known. An exact evaluation or characterization that determines the constant explicitly is sought, beyond successively improved numerical bounds or a restatement of this limit.

## Application

The constant is a baseline for deciding how much sequence similarity can arise by chance in a simple alignment model.

## References

- [John D. Dixon, *Longest common subsequences in binary sequences* (2013)](https://arxiv.org/abs/1307.2796), the outstanding constant-evaluation problem.
- [Ray Li, William Ren and Yiran Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings* (2025; published 2026)](https://arxiv.org/abs/2504.10425), Introduction and bounds for multiple strings.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Recent multiple-string asymptotics and alignment bounds do not determine the two-string binary constant. This is a question about the exact law-of-large-numbers coefficient, separate from fluctuation order.

Search topics checked on 2026-09-13: `binary Chvatal Sankoff constant exact value solved 2026 longest common subsequence`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
