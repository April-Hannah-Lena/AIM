# 282. Positive recurrence of every weakly reversible stochastic reaction network

**Area:** Stochastic chemical kinetics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Take a finite set of reactions $y\to y'$ with complexes $y,y'\in\mathbb N_0^d$ and constants $\kappa_{y\to y'}>0$. Assume every directed edge of the complex graph belongs to a directed cycle. At population $x\in\mathbb N_0^d$, reaction $y\to y'$ changes $x$ to $x+y'-y$ at rate $\kappa_{y\to y'}\prod_i(x_i)_{y_i}$, where $(m)_j=m!/(m-j)!$ for $m\ge j$ and zero otherwise. Must the minimal continuous-time chain be nonexplosive and every state in each closed communicating class be positive recurrent? For a nonsingleton class, positive recurrence means finite expected return time after leaving the starting state; absorbing singleton classes are included as stationary classes.

## Applied significance

This would guarantee equilibrium distributions for broad chemical and biochemical count models without imposing detailed or complex balance.

## References

- [David F. Anderson and Jinsu Kim, *Some network conditions for positive recurrence of stochastically modeled reaction networks*, SIAM Journal on Applied Mathematics (2018)](https://web.math.wisc.edu/~dfanderson/papers/AndersonKimSIAP2018.pdf), §6, positive recurrence conjecture.
- [Chuang Xu, *Exponential ergodicity of first order endotactic stochastic reaction systems* (2026)](https://arxiv.org/abs/2601.00176), introductory conjectures and Theorem C.

## Status review

First-order and several low-dimensional or structurally restricted families are established. These results do not cover arbitrary molecular order and dimension. The formulation explicitly includes nonexplosion so that a formal stationary solution of the master equation is not mistaken for an equilibrium of an explosive chain.

Search topics checked on 2026-09-13: `weakly reversible stochastic reaction network positive recurrence conjecture 2026 Xu two dimensional proof`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
