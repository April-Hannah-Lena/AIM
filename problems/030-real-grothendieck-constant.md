# 030. The exact real Grothendieck constant

**Area:** Operator norms and semidefinite optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Determine the smallest real number $K_G$ such that, for all positive integers $m,n,d$, every real matrix $A=(a_{ij})\in\mathbb R^{m\times n}$ and all unit vectors $u_i,v_j\in\mathbb R^d$,
$$\left|\sum_{i=1}^m\sum_{j=1}^n a_{ij}\langle u_i,v_j\rangle\right|
\le K_G\max_{\epsilon_i,\delta_j\in\{-1,1\}}
\left|\sum_{i=1}^m\sum_{j=1}^n a_{ij}\epsilon_i\delta_j\right|.$$
The target is the exact universal real constant, with matching sharp upper and lower bounds.

## Application

This constant measures the worst loss when a sign-constrained bilinear optimization is relaxed to vector inner products, the central step in several semidefinite approximation algorithms. It also bounds certain quantum correlation advantages.

## References

1. G. Pisier, [Grothendieck’s Theorem, Past and Present](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.UNCUT.pdf), survey (2012); section 4, The Grothendieck constants.
2. R. Saha et al., [New Lower and Upper Bounds for the Grothendieck Constant](https://arxiv.org/abs/2608.11158), 2026. August improvements to both bounds.
3. C. Jones and G. Malavolta, [The Grothendieck Constant is Strictly Larger than Davie–Reeds’ Bound](https://arxiv.org/abs/2603.30039), 2026. Earlier improvement to the lower bound.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The August 2026 preprint gives $6\pi/11\le K_G\le\pi/(2\log(1+\sqrt2))-10^{-4}$, leaving a nonzero gap. These recent improvements supersede older numerical intervals but do not determine the exact constant.

Searches included: `Grothendieck constant exact 2026`; `New Lower Upper Bounds Grothendieck Constant`; `Grothendieck constant solved`. This is a documented literature check, not a certification that no solution exists.
