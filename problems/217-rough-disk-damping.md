# 217. The sharp decay rate for waves damped on a disk

**Area:** Wave propagation / damping

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On the flat torus $\mathbb T^2=\mathbb R^2/(2\pi\mathbb Z)^2$, let $D=\{(x,y):x^2+y^2<1\}$ in the fundamental square $[-\pi,\pi)^2$, and let $W=\mathbf1_D$. For real $\lambda\ne0$, set
$$
P_\lambda=-\Delta+i\lambda W-\lambda^2,
\qquad D(P_\lambda)=H^2(\mathbb T^2).
$$
Is the sharp high-frequency resolvent growth $|\lambda|^{2/5}$? Precisely, establish or refute the conjunction
$$
\exists C,\lambda_0>0\ \ \forall |\lambda|\ge\lambda_0:
\quad\|P_\lambda^{-1}\|_{L^2\to L^2}\le C|\lambda|^{2/5},
\qquad
\limsup_{\lambda\to+\infty}\lambda^{-2/5}\|P_\lambda^{-1}\|_{L^2\to L^2}>0.
$$
The inverse is for the periodic problem; the circle is an interface in the damping coefficient, not a boundary condition.

## Application

This is a model of a vibrating periodic medium with an abruptly bounded damping patch. The conjectured resolvent scale corresponds to the sharp uniform rate $E(t)^{1/2}\lesssim t^{-5/7}$ for the damped wave equation with one additional derivative of initial regularity.

## References

1. Perry Kleinhenz, [*Geometry of rough damping*](https://nsa.fjfi.cvut.cz/problems/07_CIRM_2026/2026-01/2026-01_CIRM_Kleinhenz.pdf), CIRM open-problem contribution (2026), Question 1, p. 1. Explicit indicator-disk resolvent question and predicted exponent.
2. B. Achammer and Perry Kleinhenz, [*Optimal decay for waves damped by superellipses*](https://arxiv.org/abs/2606.06166), preprint, 4 June 2026, Theorem 1.1, Assumption 1, and equations (1.18)–(1.19). Later sharp results for damping that vanishes smoothly at the interface.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The CIRM question explicitly concerns the discontinuous disk indicator. The June 2026 theorem assumes polynomial vanishing with exponent at least four for its lower bounds and at least nine for matching upper bounds. Thus it does not apply to $W=\mathbf1_D$, whose boundary growth exponent is zero. The lower-bound assertion here is expressed directly in resolvent norm to avoid relying on a quasimode notational ambiguity in the problem sheet.

**Search audit:** Searched “rough damping disk indicator sharp decay 2026”, “Kleinhenz disk two fifths resolvent”, and later superellipse and singular-damping papers; checked the June 2026 theorem’s regularity hypotheses. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
