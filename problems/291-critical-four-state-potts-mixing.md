# 291. Polynomial equilibration at the four-state planar Potts critical point

**Area:** Critical dynamics and statistical simulation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

On the nearest-neighbor torus $V_n=(\mathbb Z/n\mathbb Z)^2$, $n\ge3$, let $\pi_n(\sigma)\propto\exp((\log3)\sum_{xy\in E_n}\mathbf1_{\sigma_x=\sigma_y})$ for $\sigma\in\{1,2,3,4\}^{V_n}$. At each vertex, independently at rate one, resample its color from the conditional law under $\pi_n$. Let $t_{\rm mix}(n)=\inf\{t:\max_\sigma\|\mathcal L_\sigma(\sigma_t)-\pi_n\|_{\rm TV}\le1/4\}$. Do finite constants $C,a>0$ exist with $t_{\rm mix}(n)\le Cn^a$ for every $n$?

## Application

This would justify polynomial-time local Monte Carlo sampling at a marginal two-dimensional critical point.

## References

- [Reza Gheissari and Eyal Lubetzky, *Mixing times of critical 2D Potts models* (2016)](https://arxiv.org/abs/1607.02182), Introduction and the three-state polynomial versus four-state quasi-polynomial bounds.
- [Reza Gheissari and Eyal Lubetzky, *Quasi-polynomial mixing of critical two-dimensional random cluster models*](https://cims.nyu.edu/~eyal/papers/FK_mixing.pdf), Introduction and critical mixing conjecture.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited work gives a quasi-polynomial upper bound for four colors; polynomial mixing for three colors does not include the four-color endpoint. Recent mean-field Potts mixing theorems concern complete graphs, not the planar torus. Static critical exponents and numerical dynamic exponents are not a proved upper bound of the stated form.

Search topics checked on 2026-09-13: `critical four state planar Potts Glauber polynomial mixing time proof 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
