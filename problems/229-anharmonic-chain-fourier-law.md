# 229. Fourier’s law for a boundary-thermostated anharmonic chain

**Area:** Nonequilibrium heat transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For $`N\geq2`$, take scalar positions and momenta $`(q_i,p_i)_{i=1}^N`$, fixed endpoints $`q_0=q_{N+1}=0`$, and

```math
H_N=\sum_{i=1}^N\left[\frac{p_i^2}{2}+U(q_i)\right]+\sum_{i=0}^NV(q_{i+1}-q_i),\qquad U(r)=V(r)=\frac{r^2}{2}+\frac{r^4}{4}.
```

In the interior use Hamilton’s equations. At sites $`1,N`$ add respectively $`-p_1dt+\sqrt{4}\,dW_L`$ and $`-p_Ndt+\sqrt{2}\,dW_R`$ to $`dp_i`$, with independent Brownian motions; thus the bath temperatures are $`2`$ and $`1`$. Let $`\mu_N`$ be the invariant probability measure.

For any interior bond put $`j_i=-\frac12(p_i+p_{i+1})V'(q_{i+1}-q_i)`$; stationarity makes $`J_N=\int j_i\,d\mu_N`$ independent of $`i`$. Prove or disprove

```math
\lim_{N\to\infty}N J_N\in(0,\infty).
```

There is no noise or extra forcing in the bulk.

## Application

A finite positive limit gives the inverse-length heat-current scaling expected for a pinned anharmonic solid. The explicit reservoirs and potentials make the macroscopic transport question reproducible.

## References

- Federico Bonetto, Joel L. Lebowitz and Luc Rey-Bellet, [*Fourier’s Law: A Challenge to Theorists*](https://doi.org/10.1142/9781848160224_0008) (2000), microscopic-chain discussion and concluding problems: the transport-law question.
- Luc Rey-Bellet, [*Statistical mechanics of anharmonic lattices*](https://arxiv.org/abs/math-ph/0303021) (2003), §§3–5: stationary measures, entropy production and Langevin reservoir models.
- Giovanni Canestrari, Carlangelo Liverani and Stefano Olla, [*Heat equation from a deterministic dynamics*](https://doi.org/10.1007/s00222-026-01429-1) (2026), abstract and model definition: a recent hydrodynamic limit with an additional chaotic force.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “pinned anharmonic Hamiltonian chain Fourier law rigorous 2025 2026”, “boundary Langevin quartic chain conductivity”, and the new deterministic heat-equation result. The explicit quartic potentials specify a standard instance of the published microscopic transport question. Finite-chain ergodicity does not give the thermodynamic limit. The 2026 theorem uses an external chaotic force, and bulk-noise or self-consistent-reservoir models alter the dynamics here.
