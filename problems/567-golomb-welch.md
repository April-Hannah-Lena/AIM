# 567. Perfect Lee codes beyond dimension two

**Area:** Coding theory and discrete geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For integers $`n\geq3`$ and $`r\geq2`$, define the discrete Lee ball

```math
B_1(n,r)=\left\{z\in\mathbb Z^n:\sum_{j=1}^n|z_j|\leq r\right\}.
```

Prove or disprove that there is no set $`C\subseteq\mathbb Z^n`$ for which

```math
\mathbb Z^n=\bigsqcup_{c\in C}\bigl(c+B_1(n,r)\bigr).
```

Equivalently, no code in the integer lattice should correct every Lee-metric error of radius $`r`$ perfectly: every lattice point would have to lie within distance $`r`$ of exactly one codeword. This is the strong Golomb–Welch conjecture, stated as Conjecture 3 in [1, Section II]. The centers are arbitrary; no linearity, lattice, or periodicity assumption is imposed.

## Application

Lee distance measures the total magnitude of coordinate errors. Perfect Lee codes would meet the corresponding packing bound exactly, making their existence relevant to the limits of error correction for integer-valued signals and related finite-alphabet storage models.

## References

1. P. Horak and D. Kim, [50 Years of the Golomb–Welch Conjecture](https://doi.org/10.1109/TIT.2017.2786675), *IEEE Transactions on Information Theory* **64**(4) (2018), 3048–3061. Section II, Conjecture 3, and Sections III–IV; [author manuscript](https://arxiv.org/html/1706.03589v3).
2. K. H. Leung and Y. Zhou, [No lattice tiling of $`\mathbb Z^n`$ by Lee sphere of radius 2](https://doi.org/10.1016/j.jcta.2019.105157), *Journal of Combinatorial Theory, Series A* **171** (2020), 105157. [Preprint](https://arxiv.org/abs/1808.08520).

## Status review

**Known cases:** The conjecture holds for $`3\leq n\leq5`$ and every $`r\geq2`$, and for sufficiently large radius at each fixed dimension; [1] supplies explicit ranges. For radius two, [2] excludes lattice tilings in every dimension $`n\geq3`$. It also excludes arbitrary tilings when $`2n^2+2n+1`$ is prime, using the prime-cardinality tiling theorem.

**Remaining target:** Exclude arbitrary perfect Lee codes for every remaining pair $`(n,r)`$, or construct a counterexample. The all-dimensional lattice result at radius two does not dispose of general nonlinear codes. Quasi-perfect codes have different packing and covering radii and do not settle this question.

The 2026 primary paper [2-quasi-perfect Lee codes and abelian Ramanujan graphs](https://arxiv.org/html/2601.12393v1), Section 1, explicitly retains the conjecture as open. Searches through 24 September 2026 found no supported general solution announcement or repository duplicate. GitHub results include formalizations expressly limited to the known dimension-three, radius-two lattice case, and an unsupported statement in a conjecture-scoring discussion that the problem was proved in 2023; that discussion provides neither a proof nor a corresponding citation. Palomar returned no matching record. Zenodo's native API returned HTTP 403; indexed searches found no matching announcement.
