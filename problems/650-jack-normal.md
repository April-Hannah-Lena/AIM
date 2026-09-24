# 650. A uniform Gaussian approximation bound for Jack measures

**Area:** Probability and random matrix models

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For an integer $n\ge3$ and $\alpha\ge1$, draw a partition $\lambda\vdash n$ with Jack probability

$$
\mathbb P_\alpha(\lambda)=\frac{\alpha^n n!}{\prod_{u\in\lambda}(\alpha a(u)+\ell(u)+1)(\alpha a(u)+\ell(u)+\alpha)},
$$

where $a(u)$ and $\ell(u)$ count the boxes to the right of and below $u$ in its Young diagram. Write $\lambda_i$ and $\lambda_i'$ for its row and column lengths, and define

$$
W_{n,\alpha}=\frac{\sum_i\left[\alpha\binom{\lambda_i}{2}-\binom{\lambda_i'}{2}\right]}{\sqrt{\alpha\binom n2}}.
$$

Does a universal constant $C<\infty$, independent of both $n$ and $\alpha$, satisfy

$$
\sup_{x\in\mathbb R}\left|\mathbb P_\alpha(W_{n,\alpha}\le x)-\Phi(x)\right|\le C\max\left\{n^{-1/2},\frac{\sqrt\alpha}{n}\right\}
$$

for all such $n,\alpha$, where $\Phi$ is the standard normal distribution function?

The uniform dependence on $\alpha$ is essential: a bound with a constant depending on a fixed $\alpha$ does not settle the question.

## Application

Jack measures model dependent random partitions and serve as discrete counterparts of Gaussian beta ensembles. A bound uniform in their parameter would quantify the accuracy of Gaussian tail probabilities for character statistics as the model's symmetry parameter varies.

## References

1. L. H. Y. Chen, M. Raič, and L. V. Thành, [On the error bound in the normal approximation for Jack measures](https://bpb-us-w2.wpmucdn.com/blog.nus.edu.sg/dist/3/10976/files/2020/11/BEJ1245.pdf), *Bernoulli* **27**(1) (2021), 442–468, p.445, Theorem 1.1 and Proposition 4.1; [DOI](https://doi.org/10.3150/20-BEJ1245).
2. L. V. Thành and N. N. Tu, [Non-uniform Berry–Esseen bounds for exchangeable pairs with applications to the mean-field classical N-vector models and Jack measures](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.711.pdf), *Comptes Rendus Mathématique* **363** (2025), 757–776, Section 3.2 and Theorem 8.
3. J. Fulman and L. Goldstein, [Zero Biasing and Jack Measures](https://doi.org/10.1017/S0963548311000241), *Combinatorics, Probability and Computing* **20**(5) (2011), 753–762.

## Status review

**Known cases:** The conjectured order holds in Wasserstein distance. In Kolmogorov distance, the 2021 bound is $8.2\max\{n^{-1/2},\sqrt\alpha\log(n)/n\}$; this has the desired order for $1\le\alpha\le n/\log^2 n$. For each fixed $\delta>0$, the desired order also holds when $\alpha\ge n^{1+\delta}$, with a constant depending on $\delta$.

**Remaining target:** Remove the logarithmic loss with one constant valid across the full parameter range, including the transition around $\alpha=n$.

The 2025 follow-up explicitly recalls the logarithmic gap and proves a non-uniform-in-$x$ bound only on a restricted parameter range. Current web and arXiv searches, together with native GitHub, Zenodo and Palomar checks, found no full-scope solution announcement.
