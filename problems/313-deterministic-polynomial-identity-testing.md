# 313. Deterministic identity testing for arithmetic circuits

**Area:** Symbolic computation and derandomization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

An arithmetic circuit is a finite directed acyclic graph with one designated output. Input gates contain variables $`x_1,\ldots,x_n`$ or rational constants; every other gate has two inputs and applies addition or multiplication. Gates may feed more than one later gate. Operations take place in the ordinary commutative, associative polynomial ring $`\mathbb Q[x_1,\ldots,x_n]`$; subtraction can be implemented using the constant $`-1`$.

Let $`L`$ be the bit length of an explicit encoding of the graph, its gate labels and its rational constants, whose numerators and nonzero denominators are written in binary. The input also contains an integer $`d\ge1`$ in unary, with the promise that the polynomial computed at every gate has total degree at most $`d`$. The zero polynomial is permitted at any gate. Write $`f_C`$ for the output polynomial.

Do there exist a deterministic Turing machine $`A`$ and absolute constants $`K,c>0`$ such that, for every valid input $`(C,d)`$, $`A`$ uses at most $`K(L+d)^c`$ bit operations and correctly decides whether

```math
f_C\equiv0\quad\text{in }\mathbb Q[x_1,\ldots,x_n]?
```

The machine receives the entire circuit and must work for all inputs satisfying the degree promise. There is no restriction on circuit depth, number of occurrences of a variable, or number of monomials. The conclusion is unconditional and requires no random choices. This is the rational-coefficient, bounded-degree, white-box version of polynomial identity testing (PIT).

## Application

Testing whether two symbolic computations are exactly equivalent reduces to applying PIT to their difference. Circuits retain shared intermediate computations and can describe polynomials whose expanded coefficient lists are exponentially larger. A deterministic polynomial-time test would give a worst-case guarantee for such identity checks without expanding the expressions. PIT also controls deterministic multivariate factorization when both the input polynomial and its factors are represented by circuits; the relevant reduction preserves this compact representation.

## References

1. Amir Shpilka and Amir Yehudayoff, *Arithmetic Circuits: A Survey of Recent Results and Open Questions*, Foundations and Trends in Theoretical Computer Science 5(3–4) (2010), 207–388, [DOI 10.1561/0400000039](https://doi.org/10.1561/0400000039); [author PDF](https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf), Definition 1.1 and Chapter 4, especially author-manuscript pp. 53–55. Circuit model, identity-testing question and randomized baseline.
2. Swastik Kopparty, Shubhangi Saraf and Amir Shpilka, *Equivalence of Polynomial Identity Testing and Deterministic Multivariate Polynomial Factorization*, [ECCC TR14-001](https://eccc.weizmann.ac.il/report/2014/001/), January 4, 2014; [author PDF](https://www.math.toronto.edu/ssaraf/PITfactoring.pdf), §1.1, Theorem 1 and Observation 1. Gate-degree convention and factorization connection, including rational-constant bit complexity.
3. Nitin Saxena, *Progress on Polynomial Identity Testing – II*, [arXiv:1401.0976v1](https://arxiv.org/html/1401.0976v1), January 6, 2014, §§1–2.1. Independent survey and the limits of depth reduction.
4. Partha Mukhopadhyay, C. Ramya and Pratik Shastri, *Efficient Polynomial Identity Testing Over Nonassociative Algebras*, [arXiv:2509.11349v1](https://arxiv.org/html/2509.11349v1), September 14, 2025, §1 and Theorem 3. Independent statement of the ordinary PIT gap and a result for a different algebra.
5. Robert Andrews, Deepanshu Kush and Roei Tell, *Polynomial-Time PIT from (Almost) Necessary Assumptions*, [ECCC TR25-042](https://eccc.weizmann.ac.il/report/2025/042/), April 8, 2025, Theorems 1.2–1.4 and 7.3–7.4, and Remark 1.5. Conditional derandomization and its computational model.
6. Amir Shpilka and Yann Tal, *Polynomial Identity Testing and Reconstruction for Depth-4 Powering Circuits of High Degree*, [arXiv:2602.20832v1](https://arxiv.org/abs/2602.20832v1), February 24, 2026; [full text](https://eccc.weizmann.ac.il/report/2026/029/download), Theorem 1.1. Restricted powering circuits.
7. Zeyu Guo, *A Note on Deterministic PIT for $`\Sigma^{[3]}\Pi\Sigma\Pi^{[\delta]}`$ Circuits*, [ECCC TR26-168](https://eccc.weizmann.ac.il/report/2026/168/), posted September 6, 2026, Theorem 2.6 and Corollary 2.7. Three summands and fixed bottom degree.
8. Nimrod Kaplan and Amir Shpilka, *Polynomial Identity Testing for Read-4 Arithmetic Formulas*, CCC 2026, LIPIcs 383, 25:1–25:18, [published paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2026.25), July 23, 2026, §1.1, Theorems 2–3.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 nonassociative-algebra paper and the 2026 powering-circuit paper retain ordinary commutative PIT as unresolved. Randomized polynomial-time testing is known. No unconditional deterministic polynomial-time algorithm for the stated general circuit model was located in searches through September 17, 2026.

Shpilka–Tal require a special depth-four sum-of-powers structure and a relation between the powering exponent and the number of summands. Guo treats at most three product terms and fixed bottom degree; the exponent in the runtime depends on that bottom degree. These restrictions do not cover arbitrary input circuits. Depth reduction alone can increase circuit size beyond a polynomial.

Kaplan–Shpilka's Theorem 3 gives polynomial-time white-box testing for formulas whose tree representation uses each variable at most four times. General circuits may reuse intermediate gates and have unbounded variable occurrences, so this result does not give the displayed algorithm.

Andrews–Kush–Tell assume uniform arithmetic hardness that their paper does not establish. Their arithmetic-network conclusions must also be distinguished from the explicit rational bit-cost formulation here. The polynomial-time result for commutative nonassociative algebras retains bracketings of products and does not test equality in the associative ring used here. Noncommutative rational identity testing likewise concerns a different algebra.

White-box PIT, stronger black-box hitting-set constructions, and the associated factorization equivalence are treated as one problem family for this expansion. The [evidence ledger](../research/expansion-2026-09/candidates/deterministic-polynomial-identity-testing.json) records exact theorem scopes, source access, aliases and duplicate comparisons. The separated A22 adversarial self-pass passed on September 17, 2026; no independent agent or human review occurred.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
