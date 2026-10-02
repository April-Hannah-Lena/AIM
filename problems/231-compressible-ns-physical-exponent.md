# 231. Global finite-energy compressible flow at the diatomic exponent

**Area:** Viscous compressible gas dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On $`\mathbb T^3`$, consider constant-viscosity barotropic flow

```math
\rho_t+\mathop{\mathrm{div}}\nolimits(\rho u)=0,\qquad(\rho u)_t+\mathop{\mathrm{div}}\nolimits(\rho u\otimes u)+\nabla\rho^{7/5}=\Delta u+\nabla\mathop{\mathrm{div}}\nolimits u.
```

Does every initial density $`\rho_0\geq0`$ and momentum $`m_0`$ with

```math
E_0=\int_{\mathbb T^3}\left(\frac{|m_0|^2}{2\rho_0}+\frac52\rho_0^{7/5}\right)dx<\infty
```

admit a global finite-energy weak solution? The kinetic term is $`0`$ at $`(\rho_0,m_0)=(0,0)`$ and infinite if $`\rho_0=0`$, $`m_0\ne0`$.

Require the displayed distributional equations and initial traces, $`\rho\in L^\infty_{\mathrm{loc}}([0,\infty);L^{7/5})`$, $`u\in L^2_{\mathrm{loc}}([0,\infty);H^1)`$, the renormalized continuity equation

```math
\partial_tb(\rho)+\mathop{\mathrm{div}}\nolimits(b(\rho)u)+(\rho b'(\rho)-b(\rho))\mathop{\mathrm{div}}\nolimits u=0
```

for $`b\in C^1`$ with compactly supported derivative, and, for almost every $`t`$,

```math
E(t)+\int_0^t\int(|\nabla u|^2+|\mathop{\mathrm{div}}\nolimits u|^2)\,dx\,ds\leq E_0.
```

Here $`E(t)`$ is the corresponding density-and-momentum energy.

## Application

The pressure exponent $`7/5`$ is the classical diatomic-gas value. General finite-energy existence would put a physically used compressible model within a complete large-data weak-solution theory.

## References

- Eduard Feireisl, Antonín Novotný and Hana Petzeltová, [*On the existence of globally defined weak solutions to the Navier–Stokes equations*](https://www.math.cmu.edu/~gautam/research/201208-fluids-working-group/Feireisl_2001.pdf) (2001), main theorem: the three-dimensional range $`\gamma>3/2`$.
- Mária Lukáčová-Medvid’ová and Andreas Schömer, [*Existence of dissipative solutions to the compressible Navier–Stokes system with potential temperature transport*](https://doi.org/10.1007/s00021-022-00713-3) (2022), §1, paragraph beginning with the simpler barotropic model: explicit unresolved range $`\gamma\leq3/2`$ for standard weak solutions.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “barotropic compressible Navier Stokes weak existence gamma 7/5”, “adiabatic exponent below 3/2 global weak solutions 2025 2026”, and density-dependent-viscosity results. Located all-exponent theorems for modified viscosities, stationary problems and measure-valued or dissipative solution concepts. These do not supply the standard distributional solution with constant viscosities specified above.
