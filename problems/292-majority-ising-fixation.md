# 292. Does every strict initial majority win zero-temperature Ising dynamics?

**Area:** Coarsening and phase selection

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Fix an integer $d\ge2$ and $p\in(1/2,1]$. Start with independent spins on $\mathbb Z^d$, equal to $+1$ with probability $p$. Every site has a rate-one Poisson clock; when it rings, set its spin to the strict majority among its $2d$ nearest neighbors, breaking a tie by an independent fair coin. Is it almost surely true that for every site $x$ there is a finite random time $T_x$ such that $\sigma_t(x)=+1$ for all $t\ge T_x$? The conclusion concerns eventual fixation at each site, without a uniform fixation time over the infinite lattice.

## Application

This asks whether an arbitrarily small initial magnetization determines the final phase during idealized zero-temperature coarsening.

## References

- [Robert Morris, *Zero-temperature Glauber dynamics on the lattice* (2008)](https://arxiv.org/abs/0809.0353), Introduction, the critical initial-density conjecture and high-dimensional limit.
- [*Bootstrap Percolation and its Applications*, BIRS workshop report 24w5300 (2024)](https://www.birs.ca/workshops/2024/24w5300/report24w5300.pdf), zero-temperature Glauber dynamics open questions.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Fixation from sufficiently high initial density and convergence of the critical density to one half as dimension grows leave the fixed-dimension assertion open. One-dimensional or quasi-one-dimensional graph results and finite-box absorption do not settle the infinite-lattice statement.

Search topics checked on 2026-09-13: `zero temperature Glauber dynamics initial density p greater one half all plus fixation conjecture 2026 Morris`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
