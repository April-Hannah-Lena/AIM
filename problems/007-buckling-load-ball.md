# 007. Pólya–Szegő conjecture for the first buckling load

**Area:** Elastic stability

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For every bounded smooth planar domain $\Omega$, define its first clamped buckling eigenvalue by

$$\Lambda_1(\Omega)=\inf_{0\ne u\in H^2_0(\Omega)}\frac{\int_\Omega|\Delta u|^2\,dx}{\int_\Omega|\nabla u|^2\,dx}.$$

Thus $\Delta^2u=-\Lambda\Delta u$ with $u=\partial_\nu u=0$ on the boundary. If $B$ is a disk of the same area, prove or disprove $\Lambda_1(\Omega)\ge\Lambda_1(B)$. No sign condition is imposed on a first eigenfunction.

## Application

The eigenvalue is proportional to the compressive load at which a clamped plate buckles. The conjecture identifies the most easily buckled shape of prescribed area.

## References

1. P. R. S. Antunes, [On the buckling eigenvalue problem](https://doi.org/10.1088/1751-8113/44/21/215205), Journal of Physics A 44 (2011), 215205, §3.2.1.
2. A. Chakib, I. Khalil and A. Sadik, [On numerical resolution of shape optimization bi-Laplacian eigenvalue problems](https://doi.org/10.1016/j.matcom.2024.11.007), Mathematics and Computers in Simulation 230 (2025), 149–164, introduction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Antunes explicitly states the conjecture without a ground-state sign assumption. The 2025 numerical study says that only partial buckling results are established. The clamped-plate vibration theorem concerns a different denominator and cannot be substituted for this buckling statement.

**Search audit:** “buckling ball conjecture first eigenvalue 2025 2026”; “Pólya Szegő buckling conjecture solved”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
