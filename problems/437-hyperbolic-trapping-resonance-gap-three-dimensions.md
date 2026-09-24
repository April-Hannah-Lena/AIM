# 437. A resonance gap for arbitrary uniformly hyperbolic trapping in three dimensions

**Area:** Scattering PDEs and wave decay

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $V\in C_c^\infty(\mathbb R^3;\mathbb R)$, $P_h=-h^2\Delta+V$, and let $E>0$ be a regular value of $p(x,\xi)=|\xi|^2+V(x)$. Let $\Phi^t$ be its Hamiltonian flow and
$$K_E=\{\rho\in p^{-1}(E):\{\Phi^t(\rho):t\in\mathbb R\}\text{ is bounded}\}.$$
Assume $K_E$ is compact and uniformly hyperbolic: its tangent energy bundle splits continuously and invariantly into the flow direction and stable/unstable subbundles on which $d\Phi^{\pm t}$ contracts at most $Ce^{-ct}$ for $t\ge0$.
Must there exist $\delta,\gamma,h_0>0$ such that $P_h$ has no scattering resonance in
$$\{z:|\operatorname{Re}z-E|<\delta,\ -\gamma h<\operatorname{Im}z\le0\}$$
for $0<h<h_0$? Resonances are poles of the meromorphic continuation of the compactly localized outgoing resolvent from $\operatorname{Im}z>0$ across the positive real axis.

## Application

A resonance gap gives a uniform lower bound on the damping of metastable high-frequency wave packets. The question asks whether chaotic trapping alone prevents arbitrarily long-lived modes.

## References

1. M. Zworski, [Mathematical study of scattering resonances](https://doi.org/10.1007/s13373-017-0099-4), *Bulletin of Mathematical Sciences* **7** (2017), 1–85, Conjecture 3 and the semiclassical resonance-free regions.
2. L. Vacossin, [Spectral gap for obstacle scattering in dimension 2](https://msp.org/apde/2024/17-3/apde-v17-n3-p06-s.pdf), *Analysis & PDE* **17** (2024), main theorem and introduction.
3. S. Dyatlov and M. Zworski, [Mathematical Theory of Scattering Resonances](https://math.mit.edu/~dyatlov/res/res_final.pdf), AMS, 2019, Chapter 6 and its notes.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The conjecture was compared with the two-dimensional gap theorem and the pressure-based and normally hyperbolic results. Searches through the review date for higher-dimensional fractal trapping and unconditional resonance gaps located no theorem covering every three-dimensional uniformly hyperbolic trapped set. No topological-pressure sign assumption is imposed here.
