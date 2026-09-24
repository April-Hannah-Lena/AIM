# 015. Extended states in the three-dimensional Anderson model

**Area:** Disordered quantum transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $\ell^2(\mathbb Z^3)$ define

$$
(H_\eta\psi)(n)=\sum_{|m-n|_1=1}\psi(m)+\eta V_n\psi(n),
$$

where $(V_n)$ are independent uniform random variables on $[-1,1]$ and $\eta>0$. Prove or disprove that there exist $\eta_0>0$ and a nonempty open interval $I\subset(-6,6)$ such that, for every $0<\eta<\eta_0$, almost surely the restriction of $H_\eta$ to its spectral subspace for $I$ is purely absolutely continuous and $I\subset\sigma(H_\eta)$.

## Application

The assertion gives a rigorous conducting spectral phase for a standard model of an electron moving through a weakly disordered three-dimensional solid.

## References

1. B. Simon, [Schrödinger operators in the twenty-first century](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=00-78), in Mathematical Physics 2000 (2000), pp. 283–288, Problem 1.
2. F. Hernández, [Lecture notes on Quantum Diffusion and Random Matrix Theory](https://arxiv.org/abs/2511.04380), preprint (2025), §1.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Simon's Problem 1 asks for an absolutely continuous phase; the displayed formulation fixes a standard bounded single-site distribution. Hernández's November 2025 notes explicitly identify bulk extended states as beyond current results. Finite-time diffusion and proofs on trees or band-matrix models are not infinite-volume spectral proofs on Z³.

**Search audit:** “Anderson model three dimensions absolutely continuous weak disorder 2025 2026”; “extended states conjecture proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
