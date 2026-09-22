# 210. Néel order in the square-lattice spin-one-half antiferromagnet

**Area:** Quantum magnetism

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For even $L\ge4$, let $\Lambda_L=(\mathbb Z/L\mathbb Z)^2$. At every site put spin operators $S_x^a=\sigma_x^a/2$, where
$$\sigma^1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad\sigma^2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad\sigma^3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
Let $\psi_L$ be the normalized ground state of
$$H_L=\sum_{\{x,y\}\text{ nearest neighbors}}\sum_{a=1}^3S_x^aS_y^a$$
on $\bigotimes_{x\in\Lambda_L}\mathbb C^2$, with each bond counted once. Set $\eta_x=(-1)^{x_1+x_2}$. Prove or disprove
$$\liminf_{\substack{L\to\infty\\L\text{ even}}}\frac1{L^4}\sum_{x,y\in\Lambda_L}\eta_x\eta_y\langle\psi_L,\mathbf S_x\cdot\mathbf S_y\psi_L\rangle>0.$$

## Application

The predicted magnetic order underlies descriptions of insulating copper-oxide layers and provides a benchmark for quantum simulation of antiferromagnets.

## References

1. Elliott H. Lieb, [Long range order for the quantum Heisenberg model](https://web.math.princeton.edu/~aizenman/OpenProblems_MathPhys/9901.HeisenbergFerr.html), IAMP open-problem contribution (1999), Problem B: the exact two-dimensional spin-one-half ground-state question.
2. Tom Kennedy, Elliott H. Lieb, and B. Sriram Shastry, [Existence of Néel order in some spin-1/2 Heisenberg antiferromagnets](https://physics-legacy.pbsci.ucsc.edu/~sriram/papers/paper_37.pdf), *J. Stat. Phys.* 53 (1988), 1019–1030. Main results and concluding discussion explain the unresolved square-lattice case.
3. Ute Löw, [Néel order in the two-dimensional S=1/2 Heisenberg Model](https://arxiv.org/abs/0704.0713), *Phys. Rev. B* 76 (2007), 220409. The abstract explicitly identifies the use of Monte Carlo data together with rigorous inequalities.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Löw’s result uses high-precision Monte Carlo input; it is not a proof with fully certified bounds on that input. The unconditional inequality above remains the target. Positive-temperature nonordering in two dimensions does not address this ground-state limit.

**Search audit:** Queries: “two dimensional spin half Heisenberg long range order rigorous proof 2026”, “square lattice Neel order Kennedy Lieb Shastry Low proof”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
