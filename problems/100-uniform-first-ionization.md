# 100. Uniform boundedness of the first atomic ionization energy

**Area:** Atomic spectroscopy

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $`Z>0`$ and $`N\ge1`$, let $`E(N,Z)`$ be the infimum of the spectrum of

```math
H_{N,Z}=\sum_{j=1}^N\left(-\frac12\Delta_{x_j}-\frac Z{|x_j|}\right)+\sum_{1\le i<j\le N}\frac1{|x_i-x_j|}
```

on the antisymmetric space $`\bigwedge^N L^2(\mathbb R^3;\mathbb C^2)`$, with its standard quadratic-form realization. Set $`E(0,Z)=0`$.

For neutral atoms with integer $`Z\ge1`$, the first ionization energy is

```math
I_1(Z)=E(Z-1,Z)-E(Z,Z).
```

Prove or disprove that $`\sup_{Z\in\mathbb N}I_1(Z)<\infty`$. The nuclear mass is infinite and electron spin has exactly two states.

## Application

This is a precise question about the energy needed to remove the outermost electron. It concerns a spectral energy difference, distinct from the maximum number of bound electrons.

## References

1. J. P. Solovej, [A new look at Thomas–Fermi Theory](https://arxiv.org/abs/1601.00497), Molecular Physics 114 (2016), discussion of the ionization conjecture and equation defining $`I_m(Z)`$: explicit bounded-ionization-energy problem.
2. J. P. Solovej, [The ionization conjecture in Hartree–Fock theory](https://doi.org/10.4007/annals.2003.158.509), Annals of Mathematics 158 (2003), introduction and main results: approximate-model comparison.
3. J. P. Solovej, [Mathematics of complex atoms and the periodic table](https://www.math.uci.edu/node/38671), research colloquium abstract (15 May 2026): current explicit open-status statement.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2016 paper explains that bounded first ionization energy remains beyond known large-$`Z`$ total-energy expansions. Solovej’s 2026 abstract again identifies bounded ionization energies as open for the full many-body Schrödinger model. The Hartree–Fock result uses a different admissible class of electronic states.

**Search audit:** “first ionization energy bounded Z Solovej conjecture”; “ionization energies full many body Schrödinger 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
