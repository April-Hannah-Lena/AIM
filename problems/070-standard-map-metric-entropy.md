# 070 — Positive metric entropy for a standard map

**Area:** Hamiltonian chaos and transport

**Status:** Open in cited literature; no later resolution located

**Last checked:** 2026-09-08

## Problem statement

On $\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2$, equipped with normalized Lebesgue measure $m$, consider the area-preserving standard map
$$
T_K(x,y)=(x+y+K\sin x,\ y+K\sin x)\pmod {2\pi}.
$$
Prove that there exists a real $K\ne0$ with positive Kolmogorov–Sinai entropy $h_m(T_K)>0$. Here
$$
h_m(T)=\sup_{\mathcal P}\lim_{n\to\infty}\frac1n
 H_m\!\left(\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\right),
\quad H_m(\mathcal P)=-\sum_{P\in\mathcal P}m(P)\log m(P),
$$
and the supremum runs over finite measurable partitions.

## Applied significance

The standard map models a periodically kicked rotor. Positive entropy for physical area measure would rigorously establish sustained chaos on a set of positive phase-space area.

## References

1. Alex Blumenthal, *Statistical Properties for Compositions of Standard Maps with Increasing Coefficient* Ergodic Theory and Dynamical Systems **41** (2021), 981–1024; online 2020, introduction. [DOI](https://doi.org/10.1017/etds.2019.115), [preprint](https://arxiv.org/abs/1710.09058).
2. Pierre Berger, *Wild Dynamics on Manifolds* (2025 preprint, ICM 2026 survey), §§1.4 and 2.3. [Author's survey](https://arxiv.org/abs/2510.12929).

## Status review

Blumenthal explicitly notes that positive metric entropy is not known for any single standard-map parameter. Time-dependent compositions, randomly perturbed maps, topological horseshoes, and positive entropy for nearby symplectic maps do not answer this fixed-family question. Berger surveys the continuing difficulties around Chirikov's family. Searches on 2026-09-08: "standard map positive metric entropy 2025 arxiv" and "standard map entropy 2026 arxiv". No qualifying parameter with a proof was located.
