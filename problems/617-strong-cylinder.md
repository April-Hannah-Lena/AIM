# 617. Divisible point sets as unions of parallel lines

**Area:** Coding theory and finite geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $p$ be a prime and let $S\subseteq\mathbb F_p^3$ contain exactly $p^2$ points. Suppose every affine plane $H\subseteq\mathbb F_p^3$ satisfies

$$
|S\cap H|\equiv0\pmod p.
$$

Must $S$ be the union of $p$ distinct parallel affine lines?

Equivalently, must there exist $v\in\mathbb F_p^3\setminus\{0\}$ and $a_1,\ldots,a_p\in\mathbb F_p^3$ such that

$$
S=\bigsqcup_{j=1}^{p}\bigl(a_j+\mathbb F_pv\bigr)?
$$

This is Ball's strong cylinder conjecture. The condition concerns sets without repeated points, and $p$ must be prime.

## Application

Point configurations over finite fields encode linear codes through generator matrices. Divisibility of hyperplane intersections translates into restrictions on codeword weights. The conjecture would turn those arithmetic restrictions into an explicit geometric structure for the associated codes.

## References

1. S. Kurz and S. Mattheus, [A Generalization of the Cylinder Conjecture for Divisible Codes](https://doi.org/10.1109/TIT.2021.3134201), *IEEE Transactions on Information Theory* **68**(4) (2022). [Author manuscript](https://arxiv.org/html/2011.02923v1), introduction, Question 9, and Section 5.
2. G. Kiss, Á. Markó, Z. L. Nagy, and G. Somlai, [Cylinder type and p-divisible sets in finite affine three-space](https://arxiv.org/html/2601.09910v1), arXiv:2601.09910 (2026), Definition 1.5, Conjecture 1.6, and Theorem 1.12.

## Status review

**Known cases:** The conjecture holds for primes $p\leq7$. A qualifying set containing a complete affine line is also known to be a cylinder. Reference [2] proves that every qualifying set's characteristic function is an integer linear combination of characteristic functions of cylinders.

**Remaining target:** Show that every qualifying set is itself one cylinder. A signed integer combination of cylinder indicators does not establish this. Counterexamples over non-prime fields concern a broader statement.

Reference [2] explicitly retains the prime-field conjecture in January 2026. Searches through 24 September 2026 found no matching resolution or repository duplicate. Native Zenodo and exact-paper GitHub searches returned no matching announcement; Palomar's cylinder results concerned other subjects. Broader GitHub searches produced many unrelated lexical matches, so they are not treated as exhaustive negative checks.
