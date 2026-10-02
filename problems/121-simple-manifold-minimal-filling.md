# 121 — Minimal filling volume of a simple manifold

**Area:** Geometric analysis / travel-time bounds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

A compact Riemannian manifold $`(M^n,g)`$ is simple if its boundary is strictly convex and any two points are joined by a unique minimizing geodesic depending smoothly on its endpoints. Is every such manifold, for $`n\ge2`$, a minimal filling in the following sense?

For every compact oriented Riemannian $`n`$-manifold $`(N,h)`$ with an identified boundary $`\partial N=\partial M`$, assume its intrinsic distance satisfies

```math
d_h(x,y)\ge d_g(x,y)\qquad(x,y\in\partial M).
```

Must $`\mathop{\mathrm{Vol}}\nolimits_h(N)\ge\mathop{\mathrm{Vol}}\nolimits_g(M)`$? The topology of $`N`$ is unrestricted; no equality-case rigidity is requested.

## Application

The conjecture would turn boundary travel times into a sharp lower bound on the amount of material or geometric volume inside an inaccessible region.

## References

1. S. Ivanov, *Volume Comparison via Boundary Distances* (ICM 2010), [Proceedings, volume II](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2010.2/ICM2010.2.pdf), Conjecture 1.6 of Ivanov's chapter. States the minimal-filling conjecture.
2. S. Ivanov, *Filling minimality of Finslerian 2-discs* (2011), [arXiv:0910.2257](https://arxiv.org/abs/0910.2257), main theorem. Proves the two-dimensional comparison when the competing filling is also a disc.
3. J. Briggs and C. Wells, *A discrete view of Gromov's filling area conjecture* (2026), [arXiv:2602.17859](https://arxiv.org/abs/2602.17859), introduction and main lower bound. Gives new progress on the related unrestricted-topology filling-area problem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Ivanov explicitly states the conjecture. Two-dimensional disc-filling results must not be read as results for fillings of arbitrary topology. Searches included “simple manifold minimal filling conjecture solved 2025 2026” and “Gromov filling area Briggs Wells 2026”. The February 2026 improvement remains a lower bound rather than the conjectured sharp filling-area theorem. That closely related question is not counted as a second entry here.
