# 282. A constant approximation for general max-min fair allocation

**Area:** Fair allocation of indivisible resources

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Given $m$ agents, $n$ indivisible items and nonnegative rational values $v_{ij}$, partition the items into sets $A_1,\ldots,A_m$. Define $V(A)=\min_i\sum_{j\in A_i}v_{ij}$ and $V^*=\max_A V(A)$. Does an absolute $C<\infty$ and a polynomial-time algorithm exist that always produces $V(A)\ge V^*/C$? Polynomial time is measured in the binary encoding length; a randomized algorithm with success probability at least $2/3$ is allowed. Values are arbitrary, not restricted to a common item value or zero.

## Application

This asks for a uniform efficiency guarantee when protecting the least-satisfied recipient of indivisible resources.

## References

- [Étienne Bamas et al., *Santa Claus meets Makespan and Matroids: Algorithms and Reductions* (2023; SODA 2024)](https://arxiv.org/abs/2307.08453), Introduction and reductions.
- [Trung Thanh Nguyen and Jörg Rothe, *Mathematical programming approaches for social welfare maximization*, 4OR (2026)](https://link.springer.com/article/10.1007/s10288-026-00628-z), §5.1.3, Open problem 5.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 survey still poses constant approximation of general egalitarian social welfare. Constant approximations for the restricted Santa Claus model do not apply to arbitrary values. The two scheduling/allocation entries ask different objectives; a known reduction between them is explicitly acknowledged.

Search topics checked on 2026-09-13: `general Santa Claus max min fair allocation constant approximation 2026 solved`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
