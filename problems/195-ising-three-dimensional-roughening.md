# 195. A roughening transition in the three-dimensional Ising model

**Area:** Interfaces and equilibrium statistical mechanics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

For $\beta>0$, consider the nearest-neighbor ferromagnetic Ising model on $\mathbb Z^3$ at zero field. Its Gibbs laws have, in every finite $\Lambda$, conditional probabilities proportional to
$$\exp\!\left(\beta\!\!\sum_{\{x,y\}:\ |x-y|_1=1,\ \{x,y\}\cap\Lambda\ne\varnothing}\sigma_x\sigma_y\right),\qquad \sigma_x\in\{-1,1\},$$
with the spins outside $\Lambda$ fixed. Let $\beta_c(3)=\inf\{\beta:\mu_\beta^+(\sigma_0)>0\}$, where $\mu_\beta^+$ is the limit with all-plus boundary condition.

Does there exist $\beta_R>\beta_c(3)$ such that every Gibbs law is translation invariant for $\beta_c(3)<\beta<\beta_R$, while a Gibbs law that is not translation invariant exists for every $\beta>\beta_R$?

## Applied significance

Nontranslation-invariant Gibbs laws describe a rigid phase boundary. The conjecture predicts an ordered-temperature interval in which interfaces become rough before bulk magnetization disappears.

## References

- [Sacha Friedli and Yvan Velenik, *Statistical Mechanics of Lattice Systems: A Concrete Mathematical Introduction* (Cambridge, 2017), author chapter](https://www.unige.ch/math/folks/velenik/smbook/Ising_Model.pdf), §3.10, discussion following Theorem 3.60, manuscript p.151.
- [Atsushi Ueda, Lander Burgelman, Luca Tagliacozzo and Laurens Vanderstraeten, *Interface roughening in the 3-D Ising model with tensor networks* (2026 preprint)](https://arxiv.org/abs/2601.07829), computational investigation.

## Status review

The book poses this Gibbs-state formulation of roughening. Low-temperature interface rigidity is known. The January 2026 tensor-network study concerns numerical phase diagrams and does not establish the asserted interval or classify Gibbs laws there.

Search topics checked on 2026-09-08: three dimensional Ising roughening rigorous proof 2025 2026; Ising Gibbs translation invariance betaR conjecture.
