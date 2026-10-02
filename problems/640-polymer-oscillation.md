# 640. Oscillation of partition functions under very strong disorder

**Area:** Probability and statistical mechanics

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`d\ge2`$, $`\mathcal R=\{e_1,\ldots,e_d\}`$, and let $`(X_n)`$ start at $`0`$ with independent increments uniform on $`\mathcal R`$. Let $`\omega=(\omega_x)_{x\in\mathbb Z^d}`$ be an independent, identically distributed environment, independent of the walk, with values in a Borel subset of $`\mathbb R`$. Write $`(T_x\omega)_y=\omega_{x+y}`$. A measurable local potential has the form $`V(\omega,z)=V_o(\omega_0,z)\in\mathbb R`$; it may depend on the next step $`z`$.

Impose the source's condition $`V\in\mathcal L`$: for every $`z,z'\in\mathcal R`$, $`\mathbb E|V(\omega,z)|<\infty`$ and, almost surely,

```math
\limsup_{\delta\downarrow0}\limsup_{n\to\infty}\max_{x\in\bigcup_{j=1}^nD_j}\frac1n\sum_{0\le i\le\delta n}|V(T_{x+iz'}\omega,z)|=0,
```

where $`D_j=\{x\in\mathbb Z_+^d:|x|_1=j\}`$. For example, a finite $`p`$th moment for every step with some $`p>d`$ suffices.

With $`E_0`$ denoting expectation over the walk with the environment fixed, define

```math
Z_n^\omega=E_0\exp\!\left\{\sum_{i=0}^{n-1}V(T_{X_i}\omega,X_{i+1}-X_i)\right\},
```



```math
\Lambda_q=\lim_{n\to\infty}\frac1n\log Z_n^\omega,\qquad
\Lambda_a=\log\left(\frac1d\sum_{z\in\mathcal R}\mathbb E e^{V(\omega,z)}\right).
```

Assume $`\Lambda_q<\infty`$ and very strong disorder, meaning $`\Lambda_q<\Lambda_a\le\infty`$. Is it always true that

```math
\mathbb P\left(\liminf_{n\to\infty}e^{-n\Lambda_q}Z_n^\omega=0
\quad\text{and}\quad
\limsup_{n\to\infty}e^{-n\Lambda_q}Z_n^\omega=\infty\right)=1?
```

This is Conjecture 2.13 of Rassoul-Agha, Seppäläinen and Yilmaz. The normalization uses the quenched free energy $`\Lambda_q`$.

## Application

Partition functions describe directed polymers in disordered media. Their fluctuations after removing exponential growth would distinguish disorder regimes more finely and imply nonexistence of minimizers in two variational formulas for quenched free energy, which also enter large-deviation rate functions.

## References

1. F. Rassoul-Agha, T. Seppäläinen and A. Yilmaz, [Variational formulas and disorder regimes of random walks in random potentials](https://www.math.utah.edu/~firas/Papers/VarDisRWRP-bernoulli.pdf), *Bernoulli* **23**(1) (2017), 405–431, Definition 1.4 and equation (2.2), Theorems 2.9–2.10, Proposition 2.11 and Conjecture 2.13; [DOI](https://doi.org/10.3150/15-BEJ747).
2. E. Bates and S. Chatterjee, [The endpoint distribution of directed polymers](https://projecteuclid.org/journals/annals-of-probability/volume-48/issue-2/The-endpoint-distribution-of-directed-polymers/10.1214/19-AOP1376.pdf), *Annals of Probability* **48**(2) (2020), 817–871, Section 1.2.2, discussion of Conjecture 2.13.
3. S. Junk and H. Lacoin, [Coincidence of critical points for directed polymers for general environments and random walks](https://arxiv.org/abs/2502.04113), *Orbita Mathematicae* **3**(1) (2026), 89–125, Theorem 2.1.

## Status review

**Known cases:** The source proves zero-one laws for the possible values of the liminf and limsup. Proposition 2.11 gives a sufficient fluctuation condition on bridge partition functions for the infinite-limsup conclusion; the condition holds for the specified small-parameter log-gamma example. These results do not prove both limits in the stated generality.

**Remaining target:** Establish both almost-sure limits for every local, possibly step-dependent potential satisfying the hypotheses, or produce a counterexample.

The later critical-point coincidence theorem concerns annealed-normalized partition functions with additional moment assumptions. It does not establish the quenched-normalized oscillation asserted here. Current web, arXiv, GitHub, Zenodo and Palomar searches found no matching resolution announcement.
