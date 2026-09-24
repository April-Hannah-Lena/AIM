# 158. Concentration of eikonal entropy production on jump curves

**Area:** Variational interfaces and nonlinear PDE

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^2$ be open and $m\in L^\infty(\Omega;\mathbb R^2)$ satisfy $|m|=1$ almost everywhere and $\operatorname{div}m=0$ in distributions. Call $\Phi\in C^{1,1}(S^1;\mathbb R^2)$ an entropy if

$$
\frac{d}{d\theta}\Phi(e^{i\theta})\cdot e^{i\theta}=0.
$$

Assume every $\mu_\Phi=\operatorname{div}\Phi(m)$ is a locally finite signed Radon measure. Must $|\mu_\Phi|(\Omega\setminus J_m)=0$ for every entropy? Here $J_m$ is the approximate jump set: at each of its points $m$ has two distinct constant limiting values in mean on the two half-balls determined by some line through that point. The assertion says all entropy production lies on these one-dimensional interfaces.

## Application

Entropy measures encode the limiting interfacial energy in the Aviles–Giga model for thin-film patterns. Concentration would justify locating all of this entropy production on jump interfaces, supporting descriptions of the patterns by curves instead of a diffuse distribution of interfacial energy.

## References

1. Xavier Lamy and Elio Marconi, *Rectifiability of entropy productions for weak solutions of the 2D eikonal equation with supercritical regularity*, Revista Matemática Iberoamericana (2026), introduction and main theorem. [Article](https://doi.org/10.4171/RMI/1614). Explicit conjecture and a new regularity-dependent result.

2. Camillo De Lellis and Felix Otto, *Structure of entropy solutions to the eikonal equation*, Journal of the European Mathematical Society 5 (2003), 107–145. [Article](https://ems.press/journals/jems/articles/141). Main structure theorem establishes rectifiability of the jump set; concentration of every entropy production there is the additional issue.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 article leaves the critical case open. Its Theorem 1.1 proves concentration with additional Besov regularity $B^{1/p}_{p,\infty}$, $p<3$, for odd entropies plus constants (class $\widetilde{\mathrm{ENT}}$ in equation (1.4)). Searches for “eikonal entropy production rectifiability conjecture 2026” and the exact Lamy–Marconi title located no unconditional result. This entry concerns concentration, not identification of the entire Aviles–Giga $\Gamma$-limit.
