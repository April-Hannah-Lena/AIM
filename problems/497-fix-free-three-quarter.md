# 497. The three-quarter conjecture for binary fix-free codes

**Area:** Information theory and lossless compression

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

For every $`N\ge1`$ and every list of positive integers $`\ell_1,\ldots,\ell_N`$ satisfying

```math
\sum_{i=1}^N 2^{-\ell_i}\le\frac34,
```

must there exist distinct binary words $`c_1,\ldots,c_N`$ with $`|c_i|=\ell_i`$ such that no word is a prefix or a suffix of another?

Such a set is called **fix-free** (or **bifix**). Repeated lengths are allowed; the number of distinct lengths is unrestricted. The question concerns existence for every prescribed length list, rather than just a small average length for a given source distribution.

## Application

Fix-free codes allow a concatenated message to be parsed from either end. This supports bidirectional decoding and error recovery. A positive answer would give a general sufficient condition for imposing both parsing directions while controlling compression lengths.

## References

1. Y. Polyanskiy and Y. Wu, *Information Theory: From Coding to Learning*, Cambridge University Press (2025), Remark 10.5, p.208. [Author manuscript](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf), 16 August 2024; [published book](https://doi.org/10.1017/9781108966351).
2. S. Yekhanin, [Improved Upper Bound for the Redundancy of Fix-Free Codes](https://doi.org/10.1109/TIT.2004.836703), IEEE Transactions on Information Theory **50**(11) (2004), 2815–2818; [author preprint](https://arxiv.org/abs/cs/0408017), Theorem 1.
3. W. Gao and Z. Shan, [The 3/4 Conjecture for q-Ary Fix-Free Codes With at Most Three Distinct Codeword Lengths](https://arxiv.org/abs/2609.18237v1), preprint submitted 16 September 2026, Theorem 1.

## Status review

**Known cases:** Yekhanin's Theorem 1 proves existence for every prescribed binary length list with Kraft sum at most $`5/8`$. These instances lie inside the displayed target.

**Remaining target:** Establish the $`3/4`$ guarantee for arbitrary length lists, including Kraft sums above $`5/8`$, or produce a counterexample. This is one conjecture, not separate entries for different numbers of lengths.

The September 2026 preprint [3] announces the $`3/4`$ guarantee when at most three distinct lengths occur. Its theorem was checked for scope; its proof was not independently audited. It does not claim the unrestricted target. Searches through 23 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar, found no matching general resolution.
