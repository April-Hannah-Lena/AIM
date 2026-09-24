# 506. Small-ball ratios for general symmetric product priors

**Area:** Bayesian inverse problems and infinite-dimensional probability

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Fix $1\le p<\infty$ and positive sequences $\alpha=(\alpha_k)$ and $\gamma=(\gamma_k)$. Equip
$$X=\left\{x\in\mathbb R^{\mathbb N}:\sum_{k=1}^\infty|x_k/\alpha_k|^p<\infty\right\}$$
with norm $\|x\|_X=(\sum_k|x_k/\alpha_k|^p)^{1/p}$. Let $\rho$ be a continuous, even probability density on $\mathbb R$, strictly decreasing on $[0,\infty)$. Fix $m\in X$. For independent random variables $Z_k$ with density $\rho$, let $\mu$ be the law of $(m_k+\gamma_k Z_k)_{k\ge1}$, and assume $\mu(X)=1$.

For $h\in X$, define
$$Q(h)=\sum_{k=1}^\infty\log\frac{\rho(0)}{\rho((h_k-m_k)/\gamma_k)}\in[0,\infty].$$
The assumptions imply $\rho(t)>0$ for every finite $t$. With $B_r(h)=\{x\in X:\|x-h\|_X<r\}$, prove or disprove that
$$\lim_{r\downarrow0}\frac{\mu(B_r(h))}{\mu(B_r(m))}=e^{-Q(h)}\qquad\text{for every }h\in X,$$
where $e^{-\infty}=0$.

This is Conjecture 4.12 of [1]. The balls use the stated weighted $\ell^p$ norm. No differentiability, log-concavity or finite Fisher information assumption may be added to $\rho$.

## Application

Product priors specify random coefficients in Bayesian inverse problems. The formula would identify their Onsager–Machlup functional, which plays the role of a negative log density in infinite dimensions. It would extend the class of priors for which posterior modes can be studied through variational optimization and approximation limits.

## References

1. B. Ayanbayev, I. Klebanov, H. C. Lie and T. J. Sullivan, [Gamma-convergence of Onsager–Machlup functionals: II. Infinite product measures on Banach spaces](https://doi.org/10.1088/1361-6420/ac3f82), Inverse Problems **38** (2022), 025006. Equation (3.1), Assumption 4.1(A1)–(A3), Definition 4.9, Theorem 4.10 and Conjecture 4.12, printed pp.4–12; [published open-access PDF](https://wrap.warwick.ac.uk/161670/7/WRAP-convergence-Onsager-Machlup-functionals-II-Banach-spaces-2021.pdf).
2. B. Ayanbayev, I. Klebanov, H. C. Lie and T. J. Sullivan, [Gamma-convergence of Onsager–Machlup functionals: I. With applications to maximum a posteriori estimation in Bayesian inverse problems](https://doi.org/10.1088/1361-6420/ac3f81), Inverse Problems **38** (2022), 025005; [author preprint](https://arxiv.org/abs/2108.04597).

## Status review

**Known cases:** Theorem 4.10 of [1] proves the upper bound for the limsup under the displayed assumptions, including the zero limit when $Q(h)=\infty$. It proves equality for all $h$ if additionally $\rho\in C^2$, $\rho''\in L^1$, and $Q(h)<\infty$ implies $\sum_k|(h_k-m_k)/\gamma_k|^2<\infty$. This includes the Gaussian reference density and gives substantive cases within the target. The paper also proves specified Besov and Cauchy cases.

**Remaining target:** The matching lower bound for arbitrary permitted $\rho$ and every finite-energy center $h$, or a counterexample.

The 23 September 2026 review found no matching general proof or announced counterexample. The 2026 results for interacting $\Phi^4$ field measures concern different measures and metrics.  Searches are not exhaustive registry exports.
