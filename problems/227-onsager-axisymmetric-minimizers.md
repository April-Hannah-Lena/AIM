# 227. Axisymmetry of equilibrium distributions for Onsager rods

**Area:** Liquid-crystal statistical mechanics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For $\kappa>0$ and probability densities $\rho\geq0$ on $\mathbb S^2$ with respect to surface area, define
$$\mathcal F_\kappa(\rho)=\int_{\mathbb S^2}\rho\log\rho\,dS+\frac\kappa2\iint_{\mathbb S^2\times\mathbb S^2}\sqrt{1-(p\cdot q)^2}\,\rho(p)\rho(q)\,dS_p\,dS_q,$$
with $0\log0=0$ and value $+\infty$ when the entropy is infinite. Is every global minimizer, for every $\kappa>0$, axisymmetric: does there exist $e\in\mathbb S^2$ such that $\rho(Rp)=\rho(p)$ almost everywhere for every rotation $R$ fixing $e$?

## Application

The answer determines whether equilibrium orientational order of hard rods can always be represented by one preferred axis, as commonly assumed in reduced liquid-crystal models.

## References

- John M. Ball, [*Axisymmetry of critical points for the Onsager functional*](https://arxiv.org/abs/2008.04009) (2020), concluding discussion of §3: the minimizer-axisymmetry question for the Onsager kernel.
- Jianyuan Yin, Lei Zhang and Pingwen Zhang, [*Solution landscape of the Onsager model identifies non-axisymmetric critical points*](https://www.sciencedirect.com/science/article/abs/pii/S0167278921002384) (2022), §4 and conclusions: computed solution landscapes and non-axisymmetric critical points.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “Onsager minimizers axisymmetric conjecture proof” and “Onsager kernel global minimizer 2025 2026”. The cited numerical work finds non-axisymmetric critical points, which does not make them global minimizers. Axisymmetry theorems for the Maier–Saupe kernel or coupled dipolar models do not settle the square-root kernel specified here.
