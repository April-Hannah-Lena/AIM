# 449. Hexagonal optimality for Gaussian time-frequency sampling

**Area:** Applied harmonic analysis and communication channels

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-22
## Problem statement

Put $`g(t)=2^{1/4}e^{-\pi t^2}`$. For each $`\delta>1`$ and full-rank lattice $`\Lambda\subset\mathbb R^2`$ of covolume $`1/\delta`$, let $`A_\Lambda,B_\Lambda`$ be the largest lower and smallest upper constants in

```math
A_\Lambda\|f\|_2^2\le\sum_{(x,\omega)\in\Lambda}\left|\int_{\mathbb R}f(t)\overline{e^{2\pi i\omega t}g(t-x)}\,dt\right|^2\le B_\Lambda\|f\|_2^2\qquad(f\in L^2(\mathbb R)).
```

These frame bounds are positive and finite. Let

```math
\Lambda_{\rm hex}=\delta^{-1/2}(2/\sqrt3)^{1/2}\begin{pmatrix}1&1/2\\0&\sqrt3/2\end{pmatrix}\mathbb Z^2.
```

Is $`B_\Lambda/A_\Lambda\ge B_{\Lambda_{\rm hex}}/A_{\Lambda_{\rm hex}}`$ for every such lattice and every $`\delta>1`$?

## Application

The ratio measures how unevenly Gaussian time-frequency measurements respond to signal directions. Minimizing it improves the stability of reconstruction and the robustness of pulse-shaped communication schemes in dispersive channels.

## References

1. T. Strohmer and S. Beaver, [Optimal OFDM design for time-frequency dispersive channels](https://doi.org/10.1109/TCOMM.2003.814200), *IEEE Transactions on Communications* **51** (2003), 1111–1122, discussion of Gaussian lattice design.
2. M. Faulhuber, [The Strohmer and Beaver Conjecture for Gaussian Gabor Systems — A Deep Mathematical Problem(?)](https://arxiv.org/abs/1905.05051), *SampTA* (2019), §III, Conjectures III.1–III.2; [published article](https://doi.org/10.1109/SampTA45681.2019.9030963).
3. M. Faulhuber, A. Gumber and I. Shafkulovska, [The AGM of Gauss, Ramanujan’s corresponding theory, and spectral bounds of self-adjoint operators](https://doi.org/10.1007/s00605-024-02051-0), *Monatshefte für Mathematik* (2025), §§6–7.

## Status review

**Known cases:** The hexagonal-lattice bound is established in special sampling-density regimes, including even integer densities.

**Remaining target:** Optimality among all lattices at every real sampling density greater than one.

**Literature check:** Open in cited literature; no later resolution located.

The third reference still treats the general Strohmer–Beaver assertion as conjectural. Theta-function methods settle special density regimes, including even integer densities, without settling all real densities above one. Searches through the review date for arbitrary-density Gaussian Gabor optimality located no general proof or counterexample. The determinant in the displayed lattice is exactly 1/δ.
