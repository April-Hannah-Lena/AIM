# 366. Global smooth Schrödinger maps below the degree-zero energy threshold

**Area:** Ferromagnetism; geometric dispersive PDEs

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $q\in\mathbb S^2$ and let $\phi_0:\mathbb R^2\to\mathbb S^2$ be smooth with $\phi_0-q\in\bigcap_{k\ge1}H^k(\mathbb R^2)$. Assume
$$E(\phi_0)=\frac12\int_{\mathbb R^2}|\nabla\phi_0|^2\,dx<8\pi,\qquad \deg\phi_0=\frac1{4\pi}\int_{\mathbb R^2}\phi_0\cdot(\partial_1\phi_0\times\partial_2\phi_0)\,dx=0.$$
Must the solution of the isotropic Landau–Lifshitz equation without damping,
$$\partial_t\phi=\phi\times\Delta\phi,\qquad\phi(0)=\phi_0,$$
extend uniquely to all $t\in\mathbb R$, with $\phi-q\in C(\mathbb R;H^k)$ for every integer $k\ge1$? No rotational symmetry or a priori spacetime bound is assumed. This is the global-regularity part of the strong threshold conjecture; the energy of a degree-one harmonic map in this normalization is $4\pi$.

## Application

The equation models conservative spin motion in an isotropic ferromagnetic film. The threshold tests whether a topologically trivial configuration can concentrate into singular magnetic textures without enough energy to create and unwind a harmonic-map bubble.

## References

1. D. Tataru, [*Schrödinger maps*](https://doi.org/10.5802/jedp.92), Journées Équations aux dérivées partielles (2012), Exposé IX, §5, Conjecture 3; [full text](https://www.numdam.org/item/10.5802/jedp.92.pdf).
2. I. Bejenaru, A. D. Ionescu, C. E. Kenig and D. Tataru, [*Global Schrödinger maps in dimensions $d\ge2$: Small data in the critical Sobolev spaces*](https://arxiv.org/abs/0807.0265), Annals of Mathematics 173 (2011), 1443–1506, main small-data theorem.
3. I. Bejenaru, A. D. Ionescu, C. E. Kenig and D. Tataru, [*Equivariant Schrödinger maps in two spatial dimensions*](https://doi.org/10.1215/00127094-2293611), Duke Mathematical Journal 162 (2013), introduction and main equivariant theorems.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 with Schrödinger-map strong threshold, non-equivariant energy below $8\pi$, and 2025–2026 global-regularity searches. The cited global theorem requires small critical norm; the equivariant theory imposes rotational symmetry. Theorem 1.1 of the 2026 Ishimori-system paper [arXiv:2601.03576](https://arxiv.org/abs/2601.03576) also imposes small critical norm and concerns a different coupled system, so its broad global-well-posedness title does not resolve this threshold problem. No theorem covering all the displayed data was located.
