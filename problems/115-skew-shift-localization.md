# 115. Anderson localization for the cosine skew-shift model at every coupling

**Area:** Deterministic quantum disorder

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\alpha\in\mathbb R`$ be Diophantine: there are $`c,\tau>0`$ such that $`\|q\alpha\|_{\mathbb R/\mathbb Z}\ge c|q|^{-\tau}`$ for every nonzero integer $`q`$. For $`\lambda>0`$ and $`(x,y)\in(\mathbb R/\mathbb Z)^2`$, define on $`\ell^2(\mathbb Z)`$

```math
(H_{x,y}\psi)_n=\psi_{n+1}+\psi_{n-1}+2\lambda\cos\!\left(2\pi\left[y+nx+\tfrac{n(n-1)}2\alpha\right]\right)\psi_n.
```

Prove or disprove that, for every such $`\alpha`$ and every $`\lambda>0`$, for Lebesgue-almost every $`(x,y)`$, $`H_{x,y}`$ has an orthonormal basis of eigenvectors, each satisfying $`|\psi_n|\le C_\psi e^{-c_\psi|n|}`$ for some $`C_\psi,c_\psi>0`$.

## Application

This deterministic lattice model is expected to emulate random disorder even at arbitrarily weak coupling. Localization would imply that its stationary electronic states remain spatially confined.

## References

1. D. Damanik, [Schrödinger operators with dynamically defined potentials](https://arxiv.org/abs/1410.2445), Ergodic Theory and Dynamical Systems (2017), §9.1, boxed “Skew-Shift-Problem”: explicit cosine-model question.
2. J. Bourgain, [Green’s Function Estimates for Lattice Schrödinger Operators and Applications](https://doi.org/10.1515/9781400837144), Annals of Mathematics Studies 158, Princeton University Press (2005), Chapter 15: large-coupling methods.
3. W. Liu, M. Powell and X. Wang, [Quantum dynamical bounds for long-range operators with skew-shift potentials](https://doi.org/10.1016/j.jfa.2026.111378), Journal of Functional Analysis 290 (2026), abstract and main bounds: subsequent dynamical results.
4. C. Wang, Y. Peng and D. Piao, [Positivity and log-Hölder Continuity of Lyapunov Exponents for Multi-Frequency Skew-Shift Schrödinger Operators](https://arxiv.org/abs/2606.23316), preprint (2026), abstract: large-coupling Lyapunov results.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cosine sampling function and Diophantine frequency are essential to this formulation: generic continuous sampling functions can behave differently. The 2026 results concern dynamical bounds or sufficiently large coupling, not exponential eigenfunction localization for every positive coupling in this model.

**Search audit:** “skew shift cosine localization small coupling conjecture 2025 2026”; “skew shift Schrödinger Anderson localization all coupling”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
