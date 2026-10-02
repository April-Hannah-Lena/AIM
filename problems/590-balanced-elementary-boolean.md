# 590. Classifying balanced elementary symmetric Boolean functions

**Area:** Cryptography and Boolean functions

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For integers $`n\geq d\geq2`$, define

```math
\sigma_{n,d}(x_1,\ldots,x_n)=\bigoplus_{1\leq i_1<\cdots<i_d\leq n}x_{i_1}\cdots x_{i_d},\qquad x\in\mathbb F_2^n.
```

Here $`\oplus`$ is addition modulo two. A Boolean function is balanced if it takes each output value on exactly half its inputs.

Prove or disprove the Cusick–Li–Stănică conjecture:

```math
\sigma_{n,d}\text{ is balanced}\quad\Longleftrightarrow\quad d=2^t\ \text{and}\ n=2^{t+1}\ell-1\quad\text{for some integers }t,\ell\geq1.
```

The coefficient of every degree-$`d`$ squarefree monomial is one; arbitrary symmetric Boolean functions are outside this classification.

## Application

Balancedness prevents output bias in cryptographic Boolean functions. This explicit family offers a test of how symmetry and algebraic degree constrain that basic requirement.

## References

1. W. Su, X. Tang, and A. Pott, [A Note on a Conjecture for Balanced Elementary Symmetric Boolean Functions](https://doi.org/10.1109/TIT.2012.2215576), *IEEE Transactions on Information Theory* **59**(1) (2013), 665–671. [Author manuscript](https://arxiv.org/pdf/1203.1418), Section I, Conjectures 1–2.
2. T. W. Cusick, Y. Li, and P. Stănică, [Balanced Symmetric Functions over GF(p)](https://arxiv.org/abs/math/0608369), *IEEE Transactions on Information Theory* **54**(3) (2008), 1304–1307.

## Status review

**Known cases:** The displayed family is balanced. The classification holds when $`d`$ is a power of two; odd degrees $`d>1`$ are excluded. For each fixed degree not a power of two, sufficiently large $`n`$ are also excluded. Reference [1] gives further arithmetic cases and a reduction of the remaining question.

**Remaining target:** Rule out every other pair $`(n,d)`$. Fixed-degree asymptotics do not settle all degrees simultaneously.

Searches through 24 September 2026 located no full solution announcement or repository duplicate. Native GitHub and Palomar searches returned no matching announcement; the two native Zenodo results concerned biology and bioinformatics. The literature found in this pass supplies partial results rather than a recent comprehensive status survey.
