# 249. Existence of an optimal asymmetric Bloch wall of prescribed angle

**Area:** Micromagnetics and magnetic interfaces

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Let $\Omega=\mathbb R\times(-1,1)$, with coordinates $(x_1,x_3)$. For $\theta\in(0,\pi/2]$, let $\mathcal L_\theta$ consist of maps $m=(m_1,m_2,m_3)\in H^1_{\mathrm{loc}}(\Omega;S^2)$ satisfying
$$\int_\Omega|\nabla m|^2<\infty,\quad \partial_1m_1+\partial_3m_3=0,\quad m_3|_{\partial\Omega}=0,$$
and
$$\int_{\Omega\cap\{\pm x_1>0\}}|m-(\cos\theta,\pm\sin\theta,0)|^2\,dx<\infty$$
for both signs. Impose boundary winding number $+1$: under the conformal identification $z=x_1+ix_3\mapsto\tanh(\pi z/4)$ with the unit disk, the boundary trace $w=m_1+im_2$ lies in $H^{1/2}(S^1;S^1)$ and has degree one. Precisely, if $\widehat w_k=(2\pi)^{-1}\int_0^{2\pi}w(e^{it})e^{-ikt}\,dt$, this means $\sum_{k\in\mathbb Z}k|\widehat w_k|^2=1$.

Is $\inf_{m\in\mathcal L_\theta}\int_\Omega|\nabla m|^2\,dx$ attained for every $\theta\in(0,\pi/2]$?

## Applied significance

The divergence constraint removes the magnetic stray field, while the winding condition selects a Bloch-wall core. Attainment would justify an optimal magnetic transition layer within that topological class.

## References

- Lukas Döring, Radu Ignat and Felix Otto, [*A reduced model for domain walls in soft ferromagnetic films at the cross-over from symmetric to asymmetric wall types*](https://www.math.univ-toulouse.fr/~rignat/gammalim_full.pdf) (2013 manuscript; 2014 publication), §1.1 equations (1)–(2), §1.3, Open problem 1, and Appendix A: the boundary convention, the precise degree-one question, and nonemptiness.
- Lukas Döring and Radu Ignat, [*Asymmetric domain walls of small angle in soft ferromagnetic films*](https://arxiv.org/abs/1412.2382) (2014 preprint; 2016 publication), §1 and Theorem 1: asymptotic analysis for small-angle Néel walls, with a different topological class.

## Status review

Searched “asymmetric Bloch wall degree one infimum attained Doring Ignat Otto”, “asymmetric Bloch minimizer degree 2025 2026”, and later domain-wall existence results. No resolution of Open problem 1 was located. Existence of unrestricted asymmetric minimizers does not preserve the imposed boundary degree in a weak limit; small-angle Néel-wall results do not answer this Bloch-wall attainment question.
