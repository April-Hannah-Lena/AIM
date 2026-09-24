# 204. Does a bound bipolaron ever break rotational symmetry?

**Area:** Polarons; nonlinear quantum energy minimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

For $\psi\in H^1(\mathbb R^6)$ with $\|\psi\|_2=1$, set
$$\rho_\psi(x)=\int(|\psi(x,y)|^2+|\psi(y,x)|^2)\,dy,$$
$$\mathcal P_U(\psi)=\iint\left(|\nabla_x\psi|^2+|\nabla_y\psi|^2+\frac{U|\psi|^2}{|x-y|}\right)dx\,dy-\iint\frac{\rho_\psi(x)\rho_\psi(y)}{|x-y|}\,dx\,dy.$$
Write $E_2(U)=\inf\mathcal P_U$ and
$$E_1=\inf_{\substack{\phi\in H^1(\mathbb R^3)\\\|\phi\|_2=1}}\left\{\int|\nabla\phi|^2-\iint\frac{|\phi(x)|^2|\phi(y)|^2}{|x-y|}\,dx\,dy\right\}.$$
For every $U\ge0$ with $E_2(U)<2E_1$, must every minimizer, after a common translation of its coordinates, obey
$$\psi(Rx,Ry)=\psi(x,y)\quad\text{for every }R\in O(3)?$$
Equivalently, determine whether rotational symmetry breaking occurs anywhere in the binding regime.

## Application

A bipolaron consists of two electrons coupled through a polarizable medium. The question distinguishes a symmetric charge cloud from an equilibrium with preferred spatial directions.

## References

1. Rupert L. Frank, Elliott H. Lieb, and Robert Seiringer, [Symmetry of bipolaron bound states for small Coulomb repulsion](https://arxiv.org/abs/1201.3954), *Commun. Math. Phys.* 319 (2013), 557–573. Equations (1.1)–(1.3), Theorem 1, and its following paragraph state the functional and the unresolved symmetry question near unbinding.
2. Rupert L. Frank, Elliott H. Lieb, Robert Seiringer, and Lawrence E. Thomas, [Ground state properties of multi-polaron systems](https://arxiv.org/abs/1209.3717), XVIIth International Congress on Mathematical Physics (2013). The discussion of the Pekar–Tomasevich approximation and ground-state symmetry provides the many-polaron context.

## Status review

**Known cases:** Rotational symmetry of bipolaron minimizers is established for sufficiently small repulsion.

**Remaining target:** Rotational symmetry throughout the full binding regime, including repulsion near the binding threshold.

**Literature check:** Open in cited literature; no later resolution located.

The theorem covers sufficiently small repulsion only. The primary paper explicitly asks what occurs near the binding threshold. Its choice $\alpha=1/2$ is rescaled here to $\alpha=1$; the question concerns all binding values and is unchanged by that normalization.

**Search audit:** Queries: “bipolaron rotational symmetry breaking Pekar Tomasevich proof 2025 2026”, “Frank Lieb Seiringer symmetry bipolaron critical repulsion”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
