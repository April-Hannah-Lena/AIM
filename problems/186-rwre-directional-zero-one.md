# 186. The directional zero–one law in three-dimensional random media

**Area:** Random transport and ergodicity

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

Let $(\omega_x)_{x\in\mathbb Z^3}$ be iid nearest-neighbor transition probability vectors, with $\omega_x(e)\ge\kappa>0$ almost surely for each of the six unit lattice directions. Conditional on $\omega$, let the walk start at $0$ and take step $e$ from $x$ with probability $\omega_x(e)$. Under the joint law $P$ of the environment and the walk, must
$$P(X_n\cdot\ell\longrightarrow+\infty)\in\{0,1\}$$
hold for every deterministic unit vector $\ell\in\mathbb R^3$?

## Applied significance

This tests whether transport in a fixed macroscopic direction is an all-or-nothing property of an independently disordered medium. It is a basic obstruction to an unconditional deterministic law of large numbers.

## References

- [Ofer Zeitouni, *Random Walks in Random Environments*, author survey (19 July 2006)](https://www.wisdom.weizmann.ac.il/~zeitouni/pdf/rwrereview.pdf), Conjecture 4.2 and Theorem 4.3.
- [Martin P. W. Zerner and Franz Merkl, *A zero-one law for planar random walks in random environment* (2001)](https://doi.org/10.1214/aop/1015345769), the planar result.

## Status review

The survey separates the solved one- and two-dimensional cases from higher dimensions. Counterexamples under stationary dependent environments do not satisfy the iid assumption here. This asks for a directional probability law, whereas entry 185 assumes directional transience and asks for positive speed.

Search topics checked on 2026-09-08: Kalikow directional zero one law iid random environment dimension three 2025 2026 solved.
