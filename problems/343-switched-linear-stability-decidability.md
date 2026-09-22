# 343. Decidability of stability under arbitrary switching

**Area:** Switched systems, robust control and formal verification

**Status:** 🔵 OPEN

**Last checked:** 2026-09-18

## Problem statement

An input consists of positive integers $n,m$ and matrices $A_1,\ldots,A_m\in\mathbb Q^{n\times n}$. Each rational entry is specified exactly by a finite binary encoding of its integer numerator and nonzero integer denominator. For an arbitrary switching signal $\sigma:\mathbb N_0\to\{1,\ldots,m\}$, consider

$$
x_{k+1}=A_{\sigma(k)}x_k,\qquad k\in\mathbb N_0=\{0,1,2,\ldots\}.
$$

Does there exist an algorithm that halts on every such input and correctly decides whether

$$
\text{for every }x_0\in\mathbb R^n\text{ and every }\sigma,
\qquad \lim_{k\to\infty}\|x_k\|_2=0?
$$

Here $\|\cdot\|_2$ is the Euclidean norm. This property is called absolute asymptotic stability. Both the number of modes $m$ and the dimension $n$ may vary across inputs. Switching is unrestricted, and no running-time bound is imposed on the requested decision algorithm.

Equivalently, with $\mathcal A=\{A_1,\ldots,A_m\}$ and the induced matrix norm, define the joint spectral radius

$$
\widehat\rho(\mathcal A)
=\lim_{\ell\to\infty}
\max_{i_1,\ldots,i_\ell\in\{1,\ldots,m\}}
\bigl\|A_{i_\ell}\cdots A_{i_1}\bigr\|_2^{1/\ell}.
$$

The limit exists, is independent of the norm, and the displayed stability property holds exactly when $\widehat\rho(\mathcal A)<1$. Thus the algorithm must decide this **strict** inequality without a promised gap around one. An input with $\widehat\rho(\mathcal A)=1$ requires a negative answer. The dynamical and spectral formulations constitute one problem.

## Application

Finite-mode linear systems model dynamics that change with an operating mode or with time-varying uncertainty. For a controller already incorporated into the matrices, the question asks whether perturbations decay whatever sequence of modes occurs. A decision procedure would establish the possibility of complete automated stability verification for these exact rational models. The finite-mode model is an idealization: the result would not automatically verify nonlinear dynamics, unmodeled disturbances or every real-valued uncertainty set. The target is a fundamental limit of control verification, rather than the speed or accuracy of a numerical eigenvalue routine.

## References

1. Raphaël M. Jungers, *The Joint Spectral Radius: Theory and Applications*, Springer, 2009; [author manuscript](https://perso.uclouvain.be/raphael.jungers/sites/default/files/kcfinder/files/book.pdf), dated March 5, 2009. Definition 1.3, Theorem 1.2, and §2.2.3, Open question 1, printed p. 29.
2. Amir Ali Ahmadi, Etienne de Klerk and Georgina Hall, *Polynomial Norms*, SIAM Journal on Optimization 29(1) (2019), 399–422, [DOI](https://doi.org/10.1137/18M1172843); [author version, arXiv:1704.07462v3](https://arxiv.org/html/1704.07462v3), July 16, 2018. §5.2, equations (21)–(22) and Theorem 5.2.
3. Vincent D. Blondel and John N. Tsitsiklis, *The boundedness of all products of a pair of matrices is undecidable*, Systems & Control Letters 41(2) (2000), 135–140, [author PDF](https://www.mit.edu/~jnt/Papers/J081-00-vb-products.pdf). §1, rational-input problems in §2 and Theorem 2, printed p. 138.
4. Raphaël M. Jungers and Vincent D. Blondel, *On the finiteness property for rational matrices*, Linear Algebra and its Applications 428 (2008), 2283–2295, [author PDF](https://perso.uclouvain.be/vincent.blondel/publications/08JB.pdf). §1, equations (1.1)–(1.2), finiteness-property definition and Proposition 1, printed p. 2285.
5. Léa Ninite and Raphaël M. Jungers, *Iterative graph lifting for automatic design of path-complete stability certificates*, [arXiv:2607.00637v2](https://arxiv.org/html/2607.00637v2), September 10, 2026. Extended preprint of an accepted CDC 2026 paper; §IV-C, Theorem 4, and §V, Algorithm 1 and Remark 2.
6. Thomas Mejstrik and Ulrich Reif, *A hybrid approach to joint spectral radius computation*, Linear Algebra and its Applications 744 (2026), 204–223, [DOI](https://doi.org/10.1016/j.laa.2025.06.024); [accessible author version, arXiv:2308.05244v2](https://arxiv.org/html/2308.05244v2), July 8, 2024. Theorems 2.5–2.7 and Algorithm 3.1 in that version. The publisher's full text was not retrieved.
7. Vuong Bui, *Growth of bilinear maps III: Decidability*, Theoretical Computer Science 1056 (2025), article 115515; [author version, arXiv:2201.09850v3](https://arxiv.org/html/2201.09850v3), August 6, 2025. §1, Theorem 1, §6.3, Theorem 7, and §8, Theorem 8.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Jungers poses the strict-threshold decision question explicitly, and the independently authored *Polynomial Norms* retains it as unresolved. The latter's contracting-polynomial-norm characterization certifies stability when an appropriate degree and form are found; it does not provide a procedure guaranteed to terminate on every unstable input.

Blondel–Tsitsiklis prove undecidability for boundedness of all products and for $\widehat\rho\le1$. Their §1 explicitly distinguishes the strict inequality. Bui's later bilinear-growth undecidability results likewise concern a nonstrict threshold or a different model; his computable approximation theorem is not an exact threshold decider.

Finite products give upper and lower bounds on the joint spectral radius. Under the finiteness property, some finite product attains it through its normalized ordinary spectral radius, and Jungers–Blondel's Proposition 1 gives decidability for that class. Such a class assumption cannot simply be imposed on arbitrary rational inputs. Approximation bounds alone do not guarantee a finite stopping rule at the boundary value one.

The September 2026 Ninite–Jungers version makes the limitation explicit: its Theorem 4 assumes an attained optimum and a specified structure of the graph's tight edges; Remark 2 leaves termination and convergence guarantees for future work. The reviewed Mejstrik–Reif author version also establishes certificate-based results with additional hypotheses, and Algorithm 3.1 describes its output upon termination. Neither reviewed algorithm supplies the requested total decider.

The September 18 search covered strict stability, absolute asymptotic stability, rational matrix products, original and later authors, recent and unrestricted resolution claims, counterexamples, corrections and version histories. The [evidence ledger](../research/expansion-2026-09/candidates/switched-linear-stability-decidability.json) gives the comparisons and source-access limits. Explicit formulations are older than the recent algorithm papers; this is a dated literature review, not a certification that an unindexed resolution cannot exist.

The [continuous Skolem problem](273-continuous-skolem-decidability.md) and [discrete Skolem problem](327-discrete-skolem-decidability.md) concern reaching a hyperplane under one fixed evolution. The [static output-feedback entry](330-generic-static-output-feedback-stabilization.md) classifies dimensions for generic existence of a controller. Here the modes are supplied as input, and the quantifier ranges over every infinite switching sequence.

A separated adversarial self-pass passed on September 18, 2026. No independent agent or human review is claimed.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
