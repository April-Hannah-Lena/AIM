# 061 — Simultaneously recover sound speed and initial pressure

**Area:** Photoacoustic tomography / inverse wave problems

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix a ball $`B\subset\mathbb R^3`$. Let $`c_j\in C^\infty(\mathbb R^3)`$ be strictly positive, equal to one outside $`B`$, and nontrapping: every unit-speed geodesic of $`c_j^{-2}dx^2`$ eventually leaves each bounded set. Let $`0\ne f_j\in C_c^\infty(B)`$ be real. Define $`u_j`$ by

```math
\partial_t^2u_j-c_j^2\Delta u_j=0,
\quad u_j(0,x)=f_j(x),\quad\partial_tu_j(0,x)=0.
```

Does
$`u_1|_{(0,\infty)\times\partial B}=u_2|_{(0,\infty)\times\partial B}`$
imply $`c_1=c_2`$ and $`f_1=f_2`$? Each experiment has just one unknown initial pressure. No ordering between the speeds or finite-dimensional source model is assumed.

## Application

Photoacoustic reconstruction usually requires a known sound speed. Joint uniqueness would establish when the same pressure measurements can also calibrate the acoustic medium.

## References

1. Y. Kian and G. Uhlmann, *Determination of the sound speed and an initial source in photoacoustic tomography*, Transactions of the AMS **378** (2025), 5329–5353, introduction and main theorems. [Paper](https://doi.org/10.1090/tran/9467); [preprint](https://arxiv.org/abs/2302.03457).
2. P. Stefanov and G. Uhlmann, *Thermoacoustic tomography with variable sound speed*, Inverse Problems **25** (2009), 075011. [Preprint](https://arxiv.org/abs/0902.1973).

## Status review

**Literature check:** Open in cited literature; no later resolution located

The 2025 paper describes the general simultaneous recovery problem and obtains uniqueness under monotonicity assumptions, including suitable piecewise constant cases. The 2009 theorem reconstructs the source with known sound speed. Neither provides the unrestricted joint conclusion above.

Searches on 2026-09-08 included `photoacoustic simultaneous uniqueness 2026`, `sound speed photoacoustic uniqueness open problem`, and the exact title of reference 1. Numerical simultaneous-reconstruction and learning papers were screened as algorithms rather than global identifiability proofs. No resolution of this smooth nontrapping joint problem was located.
