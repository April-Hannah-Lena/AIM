# 199. The logarithmic correction to dilute Bose-gas energy

**Area:** Quantum equations of state

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a nonzero, nonnegative, radial $V\in C_c^\infty(\mathbb R^3)$, let $a>0$ be its scattering length: the solution of $(-\Delta+V/2)f=0$ with $f(x)\to1$ satisfies $f(x)=1-a/|x|$ outside the support. Let $E(N,L)$ be the ground energy of $N$ bosons in a periodic cube of side $L$, with kinetic energy $\sum_j-\Delta_j$ and pair potential given by the periodic extension of $V$. Define

$$e(\rho)=\lim_{N,L\to\infty,\ N/L^3\to\rho}\frac{E(N,L)}{L^3}.$$

Prove or disprove the asymptotic formula, as $\rho\downarrow0$ with $V$ fixed,

$$e(\rho)=4\pi a\rho^2\left[1+\frac{128}{15\sqrt\pi}(\rho a^3)^{1/2}+8\left(\frac{4\pi}{3}-\sqrt3\right)\rho a^3\log(\rho a^3)+o\big(\rho a^3|\log(\rho a^3)|\big)\right].$$

## Application

The coefficient is a universal next correction to the dilute-gas equation of state, beyond the Lee–Huang–Yang term used to model quantum fluctuations in ultracold atoms.

## References

1. M. Brooks, J. Oldenburg, D. Saint Aubin and B. Schlein, [Third Order Upper Bound for the Ground State Energy of the Dilute Bose Gas](https://arxiv.org/abs/2506.04153), preprint (2025), Theorem 1, equation (3), and the paragraph following the review of lower bounds: proves the upper estimate and explicitly leaves a matching lower estimate open.
2. C. Caraci, [A note on the Wu’s term in the ground state energy of a Bose gas in the Gross–Pitaevskii regime](https://doi.org/10.1063/5.0310157), Journal of Mathematical Physics 67, 031902 (2026), abstract and §I: explains the already resolved correction in another scaling.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 upper bound has an error smaller than the logarithmic term. Its authors explicitly identify the matching thermodynamic lower bound as missing. The 2026 Gross–Pitaevskii result concerns an interaction range and scattering length shrinking with particle number in a fixed box; that result does not establish this order of limits. No matching thermodynamic lower bound was found.

**Search audit:** “Wu logarithmic correction dilute Bose gas matching lower bound 2026”; “2506.04153 third order energy thermodynamic proof”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
