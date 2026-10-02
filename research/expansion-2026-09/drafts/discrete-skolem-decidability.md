# Decidability of zeros in integer linear recurrences

**Area:** Discrete dynamics and formal verification

**Status:** Accepted; integrated as entry 319

**Last checked:** 2026-09-17

## Problem statement

An input consists of a positive integer $`d`$, integer coefficients $`c_1,\ldots,c_d`$ with $`c_d\ne0`$, and integer initial values $`u_0,\ldots,u_{d-1}`$, all given by finite binary encodings. These data determine the sequence

```math
u_{n+d}=c_1u_{n+d-1}+\cdots+c_du_n,
\qquad n\in\mathbb N_0=\{0,1,2,\ldots\}.
```

Does there exist an algorithm which, for every such input, halts and correctly decides whether

```math
\exists n\in\mathbb N_0:\quad u_n=0?
```

This is the discrete Skolem problem. The order is unbounded across inputs, and the search has no supplied upper bound on $`n`$. Repeated characteristic roots are allowed. No running-time bound is requested: the question concerns decidability itself. The nonzero trailing coefficient is the standard nonsingular recurrence convention; rational coefficients and rational initial values give an equivalent decision problem by an effective scaling that preserves zeros.

To see its dynamical meaning, set $`x_n=(u_n,\ldots,u_{n+d-1})^T`$. The recurrence gives an integer companion matrix $`A`$ with $`x_{n+1}=Ax_n`$, and $`u_n=e_1^TA^nx_0`$, where $`e_1`$ is the first coordinate vector. Thus the question asks whether this discrete orbit ever meets the hyperplane whose first coordinate is zero. The recurrence and hyperplane formulations are one problem, not separate additions.

## Applied significance

Exact reachability is a basic verification task for systems updated at discrete time steps. For example, a program that repeatedly replaces $`x`$ by $`Ax`$ while $`e_1^Tx\ne0`$ terminates from the specified initial state exactly when the corresponding recurrence has a zero. A general decision procedure would therefore settle termination for this simple class of linear loops, including a reliable negative answer when no terminating step exists. The connection also informs verification of switching boundaries in discrete linear models. This is a foundational question about exact dynamics; floating-point simulation over a long finite horizon cannot certify that a later zero is impossible.

## References

1. Piotr Bacik, Toghrul Karimov, Florian Luca, Joris Nieuwveld, Joël Ouaknine, David Purser and James Worrell, *A Survey of the Skolem and Positivity Problems for Linear Recurrence Sequences*, [author manuscript](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf), dated July 26, 2026; listed as submitted on Ouaknine's publication page. §1, Problem 2 and Theorem 5, pp. 2–3; §5.3, Theorem 25; §6.2, Theorem 33; §§9.1 and 9.3. Formulation, background, conditional results and the distinction from continuous time.
2. Ruiwen Dong and Doron Shafrir, *The Skolem Problem in rings of positive characteristic*, [arXiv:2510.27603](https://arxiv.org/abs/2510.27603), author manuscript, v3 (March 11, 2026). §1 and Theorem 1.1. Independent explicit status assessment over the integers, alongside a theorem for a different coefficient structure; v3 incorporates a correction to Lemma 3.2.
3. Piotr Bacik, Joël Ouaknine and James Worrell, *On the Complexity of the Skolem Problem at Low Orders*, SODA 2026, pp. 5255–5269, [DOI](https://doi.org/10.1137/1.9781611978971.191), [author PDF](https://people.mpi-sws.org/~joel/publications/skolem-complexity25.pdf). Problems 1.1–1.2, Theorem 3.1 and Corollary 3.7. Distinguishes a supplied finite horizon from the unrestricted problem.
4. Florian Luca, Joël Ouaknine and James Worrell, *Conjectural Decidability of the Skolem Problem*, [arXiv:2607.15510](https://arxiv.org/abs/2607.15510), preprint, v1 (July 16, 2026). Conjecture 4.2, Theorem 4.3, Theorem 5.1, Corollary 5.2 and §6.
5. Piotr Bacik and Anton Varonka, *On the Subspace Orbit Problem and the Simultaneous Skolem Problem*, [arXiv:2601.18349](https://arxiv.org/abs/2601.18349), v2 (May 14, 2026), full version of the LICS 2026 paper. §1, reduced-system definitions and Theorem 2. The theorem uses the inherent orbit dimension, not an arbitrarily enlarged ambient space.
6. Piotr Bacik, *Twisted Rational Zeros and Local-Global Principles for Linear Recurrence Sequences*, [arXiv:2609.16392](https://arxiv.org/abs/2609.16392), preprint, v1 (September 14, 2026). §1.1, Problem 0; §1.3, Example 3 and Theorem 4. A recent status statement and a counterexample to a different, stronger local-global assertion.
7. Ruiwen Dong and Doron Shafrir, *Skolem-Mahler-Lech in rings of positive characteristic: a shorter proof and a multi-dimensional generalization*, [arXiv:2609.03127](https://arxiv.org/abs/2609.03127), preprint, v1 (September 2, 2026). §1.3 and Theorems 1.5–1.6. Further status corroboration and a higher-dimensional result that retains a positive-characteristic hypothesis.

## Status review

The survey states the problem explicitly, Dong–Shafrir independently retain the integer case as open, and Bacik's September 14 manuscript still identifies the unresolved decidability question. Dong–Shafrir's September follow-up also retains the characteristic-zero gap. The Skolem–Mahler–Lech theorem describes the zero set as finitely many arithmetic progressions and a finite exceptional set, but does not provide the general effective information needed to decide emptiness.

Unconditional decidability is known through order four; Bacik–Ouaknine–Worrell place this case in randomized polynomial time. Their algorithm for higher fixed orders takes a finite horizon as part of its input. Iterating finite-horizon searches does not supply a halting negative answer. The survey also records conditional decidability for simple recurrences under the exponential local-global principle and the weak $`p`$-adic Schanuel conjecture.

Luca–Ouaknine–Worrell obtain general decidability assuming a strengthened Cramér-type prime-gap conjecture. Their unconditional density-one result still leaves an exceptional set of possible zero indices. Dong–Shafrir's theorem requires positive characteristic, whereas the integers have characteristic zero. Bacik–Varonka decide specified relations between inherent orbit dimension and target dimension; these do not include arbitrary hyperplanes. Bacik's September counterexample concerns a prime-power strengthening of a local-global principle and is not an undecidability proof for the displayed problem.

The September 17 search covered the problem's name, recurrence-zero and orbit formulations, recent and unrestricted dates, principal authors, resolution and counterexample claims, corrections and version histories. A title advertising a resolution for generalized Lucas sequences fixes a special recurrence family. A preliminary toric-certificate note explicitly requires certificates that it cannot produce for all inputs. Neither supplies a general decision procedure; the [candidate ledger](../candidates/discrete-skolem-decidability.json) records the theorem comparisons and access limits. This literature review does not certify the nonexistence of an unindexed result.

The existing [continuous Skolem entry](../../../problems/263-continuous-skolem-decidability.md) asks about $`c^Te^{tA}x_0=0`$ at a real time $`t\ge0`$. Here the evolution is by integer powers at integer times. The sources treat them as separate decision problems. No separate entries are counted for particular orders, restricted root patterns or the equivalent discrete hyperplane formulation.

The separated A28 adversarial self-pass passed on September 17, 2026.

Integrated as [entry 317](../../../problems/316-discrete-skolem-decidability.md) after the September 17, 2026 batch refresh.
