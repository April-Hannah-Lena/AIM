# 422. Subunit-moment eigenvalue bounds for complex Schrödinger potentials

**Area:** Nonselfadjoint Schrödinger PDEs and spectral bounds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`d\ge1`$, $`0<\gamma<1`$ with $`\gamma\ge1/2`$ when $`d=1`$, and $`\sigma>d/2`$. For complex $`V\in L^{\gamma+d/2}(\mathbb R^d)`$ let $`H=-\Delta+V`$ be its sectorial-form realization on $`L^2`$. List the discrete eigenvalues $`E_j\in\mathbb C\setminus[0,\infty)`$ with algebraic multiplicity, and set $`\delta(z)=\mathop{\mathrm{dist}}\nolimits(z,[0,\infty))`$.

Is there a constant $`C_{d,\gamma,\sigma}`$, independent of $`V`$, such that

```math
\sum_j |E_j|^{-\sigma}\delta(E_j)^{\gamma+\sigma}\le C_{d,\gamma,\sigma}\int_{\mathbb R^d}|V(x)|^{\gamma+d/2}\,dx?
```

An infinite eigenvalue list is interpreted as a nonnegative series.

## Application

Complex potentials model absorption and amplification. Such bounds constrain the aggregate unstable or damped modes using only the spatial strength of the medium.

## References

1. J.-C. Cuenin and R. L. Frank, [Open problem: Violation of locality for Schrödinger operators with complex potentials](https://arxiv.org/abs/2409.11285), preprint (2024), §1.2, Question 1, equation (7).
2. M. Demuth, M. Hansmann and G. Katriel, [On the discrete spectrum of non-selfadjoint operators](https://doi.org/10.1016/j.jfa.2009.07.018), *Journal of Functional Analysis* **257** (2009), 2742–2759, eigenvalue bounds and Schrödinger applications.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The known estimate quoted in the source assumes $`\gamma\ge1`$. Searches for Cuenin–Frank Question 1, complex Lieb–Thirring bounds with $`\gamma<1`$, and 2025–2026 eigenvalue-sum results found no unrestricted resolution. Counterexamples at $`\sigma=d/2`$ and to the unweighted Laptev–Safronov bound concern different estimates.
