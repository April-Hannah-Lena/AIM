# 199. Polynomial mixing of planar Ising dynamics with plus boundary

**Area:** Statistical mechanics and stochastic relaxation

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

Fix $\beta>\beta_c^{(2)}=\frac12\log(1+\sqrt2)$. On $\Lambda_n=\{1,\ldots,n\}^2$ take Ising spins with all exterior spins fixed to $+1$ and Gibbs weight proportional to $\exp(\beta\sum_{x\sim y}\sigma_x\sigma_y)$, summing over edges meeting $\Lambda_n$. Run continuous-time heat-bath Glauber dynamics: each interior site, at rate one, resamples its spin from the Gibbs conditional law.

Let
$$t_{\rm mix}(n,\beta)=\inf\{t:\max_\eta\|P_t(\eta,\cdot)-\mu_{n,\beta}^+\|_{\rm TV}\le1/4\}.$$
For every fixed $\beta>\beta_c^{(2)}$, do finite constants $C_\beta,a_\beta$ exist with $t_{\rm mix}(n,\beta)\le C_\beta n^{a_\beta}$ for all $n\ge1$?

## Applied significance

This asks whether relaxation to a boundary-selected equilibrium phase is efficient even at low temperatures and from the worst initial state.

## References

- [David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition (AMS, 2017), author manuscript](https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf), Chapter 26, §26.1, Question 1.
- [Eyal Lubetzky, Fabio Martinelli, Allan Sly and Fabio Lucio Toninelli, *Quasi-polynomial mixing of the 2D stochastic Ising model with plus boundary up to criticality* (2013)](https://arxiv.org/abs/1012.1271), the known upper bound.
- [Reza Gheissari and Allan Sly, *Rapid phase ordering of Ising dynamics on Z2* (May 2026 preprint)](https://arxiv.org/abs/2605.08052), later progress for specified initial laws.

## Status review

The book's polynomial-mixing question remains stronger than the quasi-polynomial bound. The May 2026 phase-ordering result uses biased random initial conditions in infinite volume; it does not give the finite-box worst-case polynomial bound asked here.

Search topics checked on 2026-09-08: 2D Ising plus boundary polynomial mixing open 2026; rapid phase ordering Gheissari Sly plus boundary quasipolynomial.
