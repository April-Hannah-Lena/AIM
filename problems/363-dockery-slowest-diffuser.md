# 363. Competitive exclusion by the slowest diffuser in a multispecies habitat

**Area:** Spatial ecology; reaction–diffusion

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^n$ be a bounded connected smooth domain and let $m\in C^\alpha(\overline\Omega)$, $0<\alpha<1$, be nonnegative and nonconstant. For arbitrary $N\ge3$ and $0<d_1<\cdots<d_N$, consider
$$\partial_tu_i=d_i\Delta u_i+u_i\left(m(x)-\sum_{j=1}^Nu_j\right),\qquad\partial_\nu u_i=0\quad\text{on }\partial\Omega.$$
Assume each initial density is continuous, nonnegative and not identically zero. Must
$$u_1(t,\cdot)\to\theta_{d_1},\qquad u_i(t,\cdot)\to0\ (i\ge2)$$
hold uniformly on $\overline\Omega$? Here $\theta_d$ is the unique positive solution of $d\Delta\theta+\theta(m-\theta)=0$ with Neumann boundary condition. The environment is fixed in time; all species have identical local growth and competition parameters.

## Applied significance

This asks whether spatial variation in resources always selects the least mobile phenotype when several otherwise identical populations compete. It isolates an evolutionary prediction about dispersal from other fitness differences.

## References

1. R. S. Cantrell and K.-Y. Lam, [*On the Evolution of Slow Dispersal in MultiSpecies Communities*](https://doi.org/10.1137/20M1361419), SIAM Journal on Mathematical Analysis (2021), introduction and §7; [author preprint](https://arxiv.org/abs/2008.08498).
2. K.-Y. Lam and Y. Lou, [*The principal Floquet bundle and the dynamics of fast diffusing communities*](https://people.math.osu.edu/lam.184/paper/2023tams.pdf), Transactions of the American Mathematical Society (2023), §1.2, Conjecture 1 and Theorem 1.9.

## Status review

Checked on 22 September 2026 using Dockery's conjecture, multispecies slow dispersal, and arbitrary diffusion rates. The SIAM paper proves exclusion for open sets of diffusion-rate configurations. Lam–Lou prove it when all rates are sufficiently large and explicitly retain the general conjecture. The two-species theorem and temporally varying counterexamples have different hypotheses. No later resolution for every finite ordered set of rates in a fixed heterogeneous environment was located.
