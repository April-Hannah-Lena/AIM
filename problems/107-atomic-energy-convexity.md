# 107. Convexity of atomic ground-state energy in electron number

**Area:** Quantum chemistry and density functional theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For $Z>0$ and $N\ge1$, let $E(N,Z)$ be the infimum of the spectrum of

$$H_{N,Z}=\sum_{j=1}^N\left(-\frac12\Delta_{x_j}-\frac Z{|x_j|}\right)+\sum_{1\le i<j\le N}\frac1{|x_i-x_j|}$$

on the antisymmetric space $\bigwedge^N L^2(\mathbb R^3;\mathbb C^2)$, with its standard quadratic-form realization. Set $E(0,Z)=0$.

For every integer nuclear charge $Z\ge1$ and every integer $N\ge1$, prove or disprove

$$E(N+1,Z)+E(N-1,Z)\ge2E(N,Z).$$

The external potential is the attractive Coulomb potential of one point nucleus. Arbitrary external potentials and multi-nucleus molecules are outside this statement.

## Application

Convexity says successive electron removals do not become cheaper as a fixed atom loses electrons. It underlies interpretations of chemical hardness and fractional electron-number interpolation.

## References

1. M. Lewin, [Some open mathematical problems concerning charged quantum particles](https://doi.org/10.5802/crphys.249), Comptes Rendus Physique 26 (2025), §2.1.3, equation (6), and discussion of Simon’s atomic Problem 10A: conjecture and limits of generalizations.
2. S. Di Marino, M. Lewin and L. Nenna, [Ground state energy is not always convex in the number of electrons](https://arxiv.org/abs/2409.08632), preprint (2024), counterexample discussion: general external-potential version.
3. M. Martínez González and P. W. Ayers, [Counterexamples to the Convexity of the Energy for Coulomb Particles](https://doi.org/10.1021/acs.jpclett.5c03648), Journal of Physical Chemistry Letters (2026), abstract: nonconvex model systems and proposed molecular structures.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Lewin separates Simon’s single-nucleus atomic question from stronger external-potential claims. The six-nucleus counterexample uses fractional nuclear charges. It and the 2026 paper on Coulomb particles invalidate broad generalizations; the latter discusses model systems and molecular structures, not a resolution for the displayed one-nucleus Hamiltonian. No atomic proof or counterexample was located.

**Search audit:** “atomic ground state energy convexity Simon Problem 10A”; “Counterexamples Convexity Energy Coulomb Particles 2026 atoms”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
