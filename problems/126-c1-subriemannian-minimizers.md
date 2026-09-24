# 126 — Continuous velocity of every sub-Riemannian length minimizer

**Area:** Nonholonomic optimal control / regularity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`M`$ be a smooth manifold, $`\Delta\subset TM`$ a smooth constant-rank distribution whose iterated brackets span $`TM`$, and $`g`$ a smooth inner product on $`\Delta`$. A horizontal curve is an absolutely continuous curve with $`\dot\gamma(t)\in\Delta_{\gamma(t)}`$ almost everywhere, and its length is $`\int|\dot\gamma|_g\,dt`$.

Must every horizontal curve $`\gamma:[0,L]\to M`$ that minimizes length between its endpoints and is parametrized by unit speed belong to $`C^1([0,L];M)`$, with one-sided derivatives at the endpoints?

The question includes strictly abnormal minimizers, which need not arise as projections of ordinary Hamiltonian trajectories.

## Application

For a robot or mechanical system with nonholonomic constraints, this asks whether an optimal path always has a continuous velocity. Such regularity is relevant to reliable trajectory approximation and control synthesis.

## References

1. Y. Chitour, F. Jean, R. Monti, L. Rifford, L. Sacchelli, M. Sigalotti and A. Socionovo, *Not all sub-Riemannian minimizing geodesics are smooth* (2025), [arXiv:2501.18920](https://arxiv.org/abs/2501.18920), §1, discussion following Theorem 1.1. Disproves smoothness while retaining the $`C^1`$ question.
2. E. Le Donne, N. Paddeu and A. Socionovo, *Metabelian distributions and sub-Riemannian geodesics* (2026), [Advances in Calculus of Variations](https://doi.org/10.1515/acv-2025-0104), Theorem 1.1. Gives regularity under analytic, rank and metabelian hypotheses.
3. R. Montgomery, *A Tour of Subriemannian Geometries, Their Geodesics and Applications* (AMS, 2002), [Mathematical Surveys and Monographs 91](https://www.ams.org/books/surv/091/), §10.1. Book treatment of the minimizer-regularity problem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 examples are $`C^2`$ but not $`C^3`$ and therefore do not refute this statement. Known absence of corners also does not by itself imply continuous velocity. Searches included “C1 regularity sub-Riemannian minimizing geodesics 2026” and “sub-Riemannian minimizer not C1 counterexample”. The 2026 metabelian result retains structural assumptions absent here.
