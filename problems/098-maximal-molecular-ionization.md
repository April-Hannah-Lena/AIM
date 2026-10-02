# 098. A universal bound on excess molecular charge

**Area:** Many-electron quantum mechanics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For distinct nuclei $`R_1,\ldots,R_M\in\mathbb R^3`$ with charges $`Z_a\in\mathbb N`$, put $`Z=\sum_aZ_a`$ and let

```math
H_N=\sum_{j=1}^N\left(-\frac12\Delta_{x_j}-\sum_{a=1}^M\frac{Z_a}{|x_j-R_a|}\right)+\sum_{i<j}\frac1{|x_i-x_j|}
```

act on $`\bigwedge^N L^2(\mathbb R^3;\mathbb C^2)`$. Let $`N_{\max}`$ be the largest $`N`$ for which $`\inf\sigma(H_N)`$ is an eigenvalue, including a possible threshold eigenvalue. Prove or disprove that a universal finite constant $`C`$ satisfies

```math
N_{\max}\le Z+CM
```

for all choices of charges and nuclear positions.

## Application

The inequality would give a mathematically uniform limit on how many additional electrons a molecule can bind.

## References

1. M. Lewin, [Some open mathematical problems concerning charged quantum particles](https://doi.org/10.5802/crphys.249), Comptes Rendus Physique 26 (2025), Open Problem 1 and §2.1.2: exact target and known bounds.
2. E. H. Lieb, [Bound on the maximum negative ionization of atoms and molecules](https://doi.org/10.1103/PhysRevA.29.3018), Physical Review A 29 (1984), main bound: a general estimate proportional to total nuclear charge.
3. J. P. Solovej, [Mathematics of complex atoms and the periodic table](https://www.math.uci.edu/node/38671), research colloquium abstract (15 May 2026): explicitly distinguishes the open full many-body problem from Hartree–Fock theory.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Lewin’s 2025 Open Problem 1 asks for this universal bound. Lieb’s general estimate $`N_{\max}<2Z+M`$ leaves a charge-dependent excess. Hartree–Fock bounds and large-$`Z`$ asymptotics do not prove a uniform bound for the full fermionic Hamiltonian; the May 2026 Solovej abstract reiterates that distinction.

**Search audit:** “maximal ionization atoms molecules universal constant conjecture 2025 2026”; “ionization conjecture 2026 proof”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
