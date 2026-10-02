# 530. Classifying Gaussian models with rational maximum-likelihood estimators

**Area:** Statistical inference and algebraic statistics

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For each integer $`m\ge2`$, let $`V=\mathop{\mathrm{Sym}}\nolimits_m(\mathbb C)`$, with independent coordinates $`s_{ij}`$ for $`i\le j`$. Use the trace pairing to define the symmetric matrix gradient:

```math
(\nabla_S f)_{ij}=\frac{1}{2-\delta_{ij}}\frac{\partial f}{\partial s_{ij}},\qquad i\le j,
```

where $`\delta_{ij}`$ is the Kronecker delta and the lower-triangular entries are obtained by symmetry.

Give an explicit structural parametrization of all nonzero rational functions $`\Phi`$ on $`V`$ satisfying

```math
\Phi(tS)=t^{-m}\Phi(S),\qquad
\Phi(S)=\det\!\left(-\frac{\nabla_S\Phi(S)}{\Phi(S)}\right).
```

The first identity holds for nonzero complex $`t`$, and both identities are rational identities on their domains of definition. Equality of solutions means equality as rational functions, without quotienting by arbitrary nonzero scalar factors.

The requested parametrization should construct solutions from specified algebraic or combinatorial data and prove that every solution arises. An implicit restatement of the differential equation, a test of a supplied candidate, or a classification with a fixed bound on numerator and denominator degrees does not complete the target. This is the determinant specialization of the open parametrization problem in the introduction of [1].

## Application

For a centered Gaussian model with concentration matrix $`K`$ and sample covariance $`S`$, the log-likelihood is proportional, up to an additive constant, to $`\log\det K-\mathop{\mathrm{tr}}\nolimits(KS)`$. Solutions encode models whose algebraic likelihood equations have one complex critical point for generic data, yielding rational formulas for estimation. Real positive-definite points are required when using such a complex algebraic model as a statistical model.

## References

1. C. Améndola, L. Gustafsson, K. Kohn, O. Marigliano and A. Seigal, [Differential Equations for Gaussian Statistical Models with Rational Maximum Likelihood Estimator](https://doi.org/10.1137/23M1569228), SIAM Journal on Applied Algebra and Geometry **8**(3), 465–492 (2024). [arXiv:2304.12054v2](https://arxiv.org/abs/2304.12054v2), introduction, Definition 3.3, Theorem 3.5 and §5.1. [Companion computations](https://mathrepo.mis.mpg.de/GaussianMLDeg1/).
2. S. Cox, P. Misra and P. Semnani, [Homaloidal polynomials and Gaussian models of maximum likelihood degree one](https://doi.org/10.2140/astat.2024.15.167), Algebraic Statistics **15**(2), 167–198 (2024). [arXiv:2402.06090v3](https://arxiv.org/abs/2402.06090v3).

## Status review

**Known cases:** Theorem 3.5 and Corollary 5.3 of [1] give a bijection between these solutions and projective varieties of Gaussian maximum-likelihood degree one:

```math
\Phi\longmapsto\mathbb P\!\left(\mathop{\mathrm{cl}}\nolimits_{\mathrm{Zar}}\bigl(\mathop{\mathrm{im}}\nolimits(-\nabla_S\Phi/\Phi)\bigr)\right),
```

where $`\mathop{\mathrm{cl}}\nolimits_{\mathrm{Zar}}`$ denotes Zariski closure. The associated estimator is $`-\nabla_S\Phi/\Phi`$.

Known solutions include $`\Phi(S)=1/\det S`$ for the unrestricted model and formulas for chordal undirected graphical models and directed acyclic graphical models. The paper also constructs nonlinear and colored examples. Linear concentration models have a further characterization through homaloidal determinant restrictions; later constructions in [2] supply additional families.

**Remaining target:** Obtain a complete constructive description for arbitrary $`m`$ and arbitrary rational degree, including the nonlinear models. The established model–equation correspondence and known families do not provide this parametrization.

Current primary versions retain the general classification problem. The companion software checks proposed solutions and constructs examples; it does not parametrize every solution. Results on one-dimensional discrete statistical models concern a different likelihood problem.

Primary-literature, indexed arXiv/Zenodo/GitHub and official Palomar API checks on 24 September 2026 located no complete parametrization or matching announcement.
