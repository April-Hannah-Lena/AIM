# 549. Ordinary posterior contraction for heavy-tailed neural-network priors

**Area:** Bayesian nonparametrics and neural networks

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Observe independent pairs

```math
X_i\sim P_X,\qquad Y_i=f_0(X_i)+\varepsilon_i,\qquad
\varepsilon_i\sim N(0,1),\quad i=1,\ldots,n,
```

where $`P_X`$ is a probability distribution on $`[0,1]^d`$ and the errors are independent of the design. The noise variance is known and fixed.

Fix $`\delta>0`$. Let $`\Pi_n`$ be the law of a fully connected ReLU network with $`L_n=\lceil(\log n)^{1+\delta}\rceil`$ hidden layers, each of width $`\lceil\sqrt n\rceil`$, and an affine scalar output. Draw every weight and bias independently as

```math
\theta_k=\sigma_n Z_k,\qquad
\sigma_n=\exp\{-(\log n)^{2(1+\delta)}\}.
```

The common density $`h`$ of $`Z_k`$ is positive, bounded, symmetric and nonincreasing on $`[0,\infty)`$. For some $`c_1,c_2>0`$ and $`\kappa\ge0`$, require

```math
\log\frac1{h(x)}\le c_1\bigl[1+\{\log(1+x)\}^{1+\kappa}\bigr]\quad(x\ge0),
\qquad \int_x^\infty h(u)\,du\le c_2/x\quad(x\ge1).
```

Cauchy and Student densities with at least one degree of freedom are examples.

Suppose $`f_0=g_q\circ\cdots\circ g_0`$ belongs to a fixed compositional class $`\mathcal G(q,\mathbf d,\mathbf t,\boldsymbol\beta,K)`$ from [1, Section 2.1]: $`d_0=d`$, $`d_{q+1}=1`$, and each coordinate of $`g_i`$ depends on at most $`t_i\le d_i`$ variables and has $`\beta_i`$-Hölder norm at most $`K`$ on its input box. All intermediate boxes have endpoints bounded by $`K`$, and each map takes its input box into the next. Use the source's Hölder convention: derivatives through order $`\lceil\beta_i\rceil-1`$, with the last derivatives Hölder of order $`\beta_i-(\lceil\beta_i\rceil-1)`$.

Set

```math
\beta_i^*=\beta_i\prod_{j=i+1}^q\min(\beta_j,1),\qquad
\gamma=2(1+\delta)(1+\kappa)+1,\qquad
\phi_n=\max_{0\le i\le q}\left(\frac{(\log n)^\gamma}{n}\right)^{\beta_i^*/(2\beta_i^*+t_i)}.
```

Form the ordinary posterior

```math
d\Pi_n(f\mid X,Y)\ \propto
\exp\!\left[-\frac12\sum_{i=1}^n(Y_i-f(X_i))^2\right]d\Pi_n(f).
```

For fixed $`B>\|f_0\|_\infty`$, let $`C_B(f)(x)=\max(-B,\min(B,f(x)))`$.

Prove or disprove that, for every such fixed model and prior, some constant $`M>0`$ independent of $`n`$ satisfies

```math
\mathbb E_{f_0}\Pi_n\!\left(\|C_B(f)-f_0\|_{L^2(P_X)}>M\phi_n\mid X,Y\right)\longrightarrow0.
```

This is the compositional-regression, common-scaling instance of the conjecture in [1]. Clipping is applied to posterior draws; the likelihood uses the original network output.

## Application

The result would justify automatic adaptation to smoothness and hidden low-dimensional structure using an ordinary Bayesian update, without selecting the network architecture from the data.

## References

1. I. Castillo and P. Egels, [Posterior and Variational Inference for Deep Neural Networks with Heavy-Tailed Weights](https://www.jmlr.org/papers/v26/24-0894.html), *Journal of Machine Learning Research* **26**(122) (2025), 1–58. Sections 2.1–2.3, Theorem 2 and Corollary 3; conjecture in Sections 3.8 and 4.6. [Published PDF](https://www.jmlr.org/papers/volume26/24-0894/24-0894.pdf); [arXiv:2406.03369v2](https://arxiv.org/abs/2406.03369v2).
2. S. Agapiou, I. Castillo and P. Egels, [Leveraging tails for adaptation](https://arxiv.org/html/2606.20480v1), arXiv:2606.20480v1 (2026), Section 5.

## Status review

Theorem 2 and Corollary 3 of [1] establish the analogous contraction for each fixed likelihood power $`0<\alpha<1`$. Theorem 13 obtains an ordinary-posterior result after adding a particular prior on the noise variance, which changes the model used here. Neither establishes the fixed-variance target. The 2026 follow-up [2] still identifies the ordinary-posterior extension in random-design regression as open; its new neural-network results concern shallow networks with different priors.

The main obstacle is controlling posterior mass outside sets of manageable complexity under both heavy tails and overparameterization. The fractional-posterior bounds cannot simply be evaluated at $`\alpha=1`$.

Checks through 24 September 2026 found no matching solution announcement or repository duplicate.
