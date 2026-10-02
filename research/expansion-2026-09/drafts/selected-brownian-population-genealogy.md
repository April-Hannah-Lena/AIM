# Bolthausen–Sznitman ancestry for a fixed-size selected population

**Area:** Population genetics and stochastic selection

**Status:** Accepted; integrated as entry 321

**Last checked:** 2026-09-17

## Problem statement

Consider $`N`$ particles on $`\mathbb R`$. Each moves as an independent standard Brownian motion (variance $`t`$ over time $`t`$) and, independently, splits into two particles at its current position at rate $`1`$. Immediately after each split, remove a leftmost particle, keeping exactly $`N`$ particles. Record the parent of each surviving child. This is the $`N`$-branching Brownian motion with selection, or $`N`$-BBM.

Write $`X_i(t)`$ for the positions and $`Y_i(t)=X_i(t)-\min_jX_j(t)`$ for their offsets from the leftmost particle. The offset process has a unique stationary probability law $`\psi_N`$. Use this law to specify the population's equilibrium regime; it is a law on configurations of $`N`$ particles, not a product of limiting one-particle densities.

Here is a finite-window formulation of the Brunet–Derrida genealogy conjecture. **Does there exist a constant $`c>0`$ such that the following holds?** Set $`a_N=c(\log N)^3`$. For every fixed integer $`k\ge2`$ and $`T>0`$, start the offset configuration with law $`\psi_N`$, run the population until time $`a_NT`$, and choose $`k`$ distinct surviving particles uniformly without replacement. For $`0\le s\le T`$, let $`\Pi_{N,k,T}(s)`$ partition $`\{1,\ldots,k\}`$ by declaring two sampled particles equivalent precisely when they have the same ancestor at time $`a_N(T-s)`$. As $`N\to\infty`$, is it true that

```math
\bigl(\Pi_{N,k,T}(s)\bigr)_{0\le s\le T}
\ \Longrightarrow\
\bigl(\Pi_k(s)\bigr)_{0\le s\le T}
```

in finite-dimensional distributions, where $`\Pi_k`$ is the standard Bolthausen–Sznitman coalescent?

For completeness, $`\Pi_k(0)`$ consists of $`k`$ singleton blocks. Whenever there are $`b`$ blocks, each specified collection of $`r`$ blocks, $`2\le r\le b`$, merges into one at rate

```math
\lambda_{b,r}=\int_0^1 x^{r-2}(1-x)^{b-r}\,dx
=\frac{(r-2)!(b-r)!}{(b-1)!}.
```

These are the only transitions. The same constant $`c`$ must work for all fixed sample sizes and time windows. It absorbs the time normalization of the population model. The question is convergence of the sampled partition process, not merely the order of a pair's expected coalescence time.

## Applied significance

Particle position represents inherited fitness, Brownian motion models changes in fitness, branching models reproduction, and removal of the least-fit individual imposes a fixed population size. The limiting genealogy would give a rigorous description of ancestry under this strong-selection rule. Multiple ancestral lines can merge on the rescaled clock even though reproduction is binary. This is a foundational population-genetics model; its conclusion is not asserted for every biological reproduction or selection mechanism.

## References

- [Julien Berestycki, *Topics on Branching Brownian motion*, EBP XVIII lecture notes, 7 August 2014](https://www.stats.ox.ac.uk/~berestyc/Articles/EBP18_v2.pdf), §9.1.1, Model 2, and §9.1.3, Conjecture 86, printed pp. 71–74.
- [Nathanaël Berestycki, *Recent progress in coalescent theory*, Ensaios Matemáticos 16 (2009), 1–193](https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/berestycki.pdf), §6.1 Eq. (6.1) and §6.3.3 Conjecture 6.1, for the coalescent rates and finite-dimensional formulation in the related discrete model.
- [Pascal Maillard, *Speed and fluctuations of N-particle branching Brownian motion with spatial selection*, Probability Theory and Related Fields 166 (2016), 1061–1173; journal-version manuscript v4, 19 June 2018](https://arxiv.org/abs/1304.0562), Theorem 1.1 and §§1.3–1.4.
- [Sarah Penington, Matthew I. Roberts and Zsófia Talyigás, *Genealogy and spatial distribution of the N-particle branching random walk with polynomial tails*, Electronic Journal of Probability 27 (2022), article 93](https://doi.org/10.1214/22-EJP806), §1.6; [author manuscript](https://arxiv.org/abs/2102.12424), p. 6, explicitly distinguishes the unproved light-tail and $`N`$-BBM conjectures from its polynomial-tail theorem.
- [Julien Berestycki and Oliver Tough, *Selection principle for the N-BBM*, arXiv:2407.05792v1, 8 July 2024](https://arxiv.org/abs/2407.05792), Theorems 1.1–1.4, for the stationary law and spatial-profile limit.
- [Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg, *The genealogy of branching Brownian motion with absorption*, Annals of Probability 41 (2013), 527–618](https://arxiv.org/abs/1001.2337), §1.4, Proposition 1 and Theorem 3.
- [Aser Cortines and Bastien Mallein, *A N-branching random walk with random selection*, ALEA 14 (2017), 117–137](https://alea.impa.br/articles/v14/14-07.pdf), §1 and Theorem 1.2.
- [Emmanuel Schertzer and Alejandro H. Wences, *Genealogical transition in the noisy N-Branching Random Walk. How stronger selection may promote genetic diversity*, Stochastic Processes and their Applications 199 (September 2026), 104975](https://doi.org/10.1016/j.spa.2026.104975), [author manuscript v2](https://arxiv.org/abs/2301.07762), §1.1, Theorem 2.5 and §5.
- [Alexandre Legrand and Pascal Maillard, *Time-inhomogeneous N-particle Branching Brownian Motion and the continuous random energy model*, arXiv:2402.04917v4, 9 April 2026](https://arxiv.org/abs/2402.04917), §2.6, “Genealogy of the N-BBM.”

## Status review

The 2026-09-17 check covered the Brunet–Derrida and Bolthausen–Sznitman aliases, fixed-size branching selection, recent proofs and counterexamples, author listings, and manuscript histories. The [evidence record](../candidates/selected-brownian-population-genealogy.json) documents the scope comparisons and separate self-review.

The April 2026 Legrand–Maillard manuscript still presents the genealogy limit as an expected extension of displacement results. Its current title and version supersede the older author-hosted PDF found during searching.

The displayed question makes the equilibrium regime and time normalization explicit using the stationary law from Berestycki–Tough. This is an equilibrium formulation of the genealogy conjecture, rather than a claim of uniform convergence over arbitrary starting configurations. Their spatial-profile theorem does not identify parent–child relationships. Maillard proves a limit for particle-position fluctuations and explicitly explains that his comparison couplings alter genealogies.

Berestycki–Berestycki–Schweinsberg prove the coalescent limit for absorption at a deterministic boundary with a tuned drift and a fluctuating population, not the exact-size selection rule above. Cortines–Mallein and Schertzer–Wences use exponential Poisson offspring clouds in discrete generations. The latter's 2026 result has a logarithmic clock in its Bolthausen–Sznitman regime. Penington–Roberts–Talyigás prove star-shaped ancestry for polynomial-tail jumps. Those model changes leave the stated Brownian binary-branching question unresolved in the checked literature.

This is one genealogy problem. The discrete branching-random-walk analogue, other mutation laws, pairwise moments and alternative normalizations are not counted as separate additions. Existing entries on spatial competition and exclusion concern different observables and mechanisms.

Integrated as [entry 319](../../../problems/318-selected-brownian-population-genealogy.md) after the September 17, 2026 batch refresh.
