# 033. The maximum number of mutually unbiased bases in dimension six

**Area:** Quantum information and matrix design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Determine $`M(6)`$, the largest integer $`r`$ for which there exist orthonormal bases $`B_a=\{u_{a1},\ldots,u_{a6}\}`$ of $`\mathbb C^6`$, $`1\le a\le r`$, with

```math
|\langle u_{ai},u_{bj}\rangle|^2=\frac16\quad(a\ne b,\ 1\le i,j\le6).
```

In particular, decide whether four such bases exist. The known general bounds are $`3\le M(6)\le7`$; constructions in prime-power dimensions do not settle dimension six.

## Application

Mutually unbiased measurements distribute information evenly between incompatible observables. They are used in quantum tomography, uncertainty relations and communication protocols.

## References

1. P. Horodecki, Ł. Rudnicki and K. Życzkowski, [Five open problems in quantum information](https://arxiv.org/abs/2002.03233), 2020; published in PRX Quantum 3 (2022), 010101. MUB problem.
2. M. Cárdenes Wuttig and J. Tindall, [A Complete Classification of Complex Hadamard Matrices of Order Six](https://arxiv.org/abs/2608.18053), 2026, v2. Recent classification relevant to, but distinct from, simultaneous MUB construction.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The August 2026 classification concerns individual complex Hadamard matrices, and presents MUBs as a further application. It does not construct four MUBs or prove their nonexistence. Targeted searches located no determination of M(6).

Searches included: `mutually unbiased bases dimension six 2026`; `four MUB dimension 6 proof`; `complete classification Hadamard order six MUB`. This is a documented literature check, not a certification that no solution exists.
