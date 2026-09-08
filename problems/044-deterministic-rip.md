# 044. Deterministic sensing matrices with optimal RIP measurement count

**Area:** Compressed sensing and matrix construction

**Status:** Open in cited literature; no later resolution located

**Last checked:** 2026-09-08

## Problem statement

Construct a deterministic algorithm polynomial in $N$ that, for every $1\le s\le N$, outputs an $m\times N$ rational matrix $A$ with polynomial-bit entries such that, for an absolute constant $C$,
$$m\le C s\log(eN/s),\qquad
\tfrac23\|x\|_2^2\le\|Ax\|_2^2\le\tfrac43\|x\|_2^2$$
for every $x\in\mathbb R^N$ with at most $s$ nonzero coordinates. Thus the restricted-isometry constant at order $s$ is at most $1/3$, with the same order of measurements as random constructions. Enumerating all supports is not polynomial time when $s$ varies.

## Applied significance

Such matrices would provide deterministic measurement designs with uniform stability guarantees for sparse recovery, including sensing and imaging applications, at the optimal order of sample count.

## References

1. A. S. Bandeira, M. Fickus, D. G. Mixon and P. Wong, [The road to deterministic matrices with the restricted isometry property](https://arxiv.org/abs/1202.1234), Journal of Fourier Analysis and Applications 19 (2013), 1123–1149. Construction problem and known obstacles.
2. K. Moonchaisook, P. Kumam and S. Sriwongsa, [Compressed sensing matrices from orthogonal spaces over finite fields of odd characteristic](https://arxiv.org/abs/2608.23062), 2026. Recent deterministic, coherence-based families.

## Status review

Checked on **2026-09-08**. The August 2026 construction derives guarantees from coherence for particular finite-field families; it does not claim optimal measurements for all N,s. Searches located no deterministic polynomial-time construction meeting the full random-optimal scaling above. A deterministic matrix with some RIP guarantee is not enough.

Searches included: `deterministic restricted isometry 2026 open`; `optimal deterministic RIP matrices s log N`; `compressed sensing orthogonal spaces finite fields 2026`. This is a documented literature check, not a certification that no solution exists.
