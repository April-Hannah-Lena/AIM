# 207. The entropy photon-number inequality

**Area:** Quantum optics; communication limits

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`\rho_A,\rho_B`$ be arbitrary states of $`n\ge1`$ bosonic modes, each with finite expected total photon number. The joint input is $`\rho_A\otimes\rho_B`$. For $`0\le\eta\le1`$, mix corresponding modes by a beam-splitter unitary, so that the output annihilation operators are

```math
c_j=\sqrt\eta\,a_j+\sqrt{1-\eta}\,b_j,\qquad d_j=-\sqrt{1-\eta}\,a_j+\sqrt\eta\,b_j.
```

Let $`\rho_C`$ be the reduced state of the $`c`$ modes after discarding the $`d`$ modes. With $`S(\rho)=-\mathop{\mathrm{Tr}}\nolimits(\rho\log\rho)`$ and $`g(t)=(t+1)\log(t+1)-t\log t`$ for $`t\ge0`$, is

```math
g^{-1}\!\left(\frac{S(\rho_C)}n\right)\ge\eta g^{-1}\!\left(\frac{S(\rho_A)}n\right)+(1-\eta)g^{-1}\!\left(\frac{S(\rho_B)}n\right)
```

always true? The inverse is on $`[0,\infty)`$; correlations among the $`n`$ modes within either input are allowed.

## Application

This gives a sharp lower bound on optical output noise at fixed input entropies, with consequences for information rates in bosonic broadcast and wiretap communication.

## References

1. Saikat Guha, Baris I. Erkmen, and Jeffrey H. Shapiro, [The Entropy Photon-Number Inequality and its Consequences](https://arxiv.org/abs/0710.5666), preprint (2007). Equation (13) states the original beam-splitter conjecture.
2. Giacomo De Palma, Dario Trevisan, Vittorio Giovannetti, and Luigi Ambrosio, [Gaussian optimizers for entropic inequalities in quantum information](https://arxiv.org/abs/1803.02360), *J. Math. Phys.* 59 (2018), 081101. Section V.B, Conjecture V.15, equation (70), gives the multimode form; Section VII.A distinguishes the proved quantum entropy-power inequality.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The quantum entropy-power inequality is weaker than this conjecture. Gaussian-input results and certain one-mode Gaussian-channel optimizer theorems do not cover two arbitrary independent multimode inputs. Current searches did not locate a proof or counterexample for that class.

**Search audit:** Queries: “entropy photon-number inequality 2026”, “entropy photon number inequality proof counterexample 2025 2026”, “Gaussian optimizers De Palma EPnI”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
