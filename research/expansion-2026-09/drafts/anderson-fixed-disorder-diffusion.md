# Diffusive mean-square displacement at fixed disorder

**Area:** Disordered quantum transport

**Status:** Accepted; published as entry 306

**Last checked:** 2026-09-17

## Problem statement

Let $(V_x)_{x\in\mathbb Z^3}$ be independent random variables, each uniform on $[-\sqrt3,\sqrt3]$. For $\lambda>0$, define the bounded self-adjoint operator

$$
(H_{\lambda,\omega}\psi)(x)=\sum_{|y-x|_1=1}\psi(y)+\lambda V_x(\omega)\psi(x)
$$

on $\ell^2(\mathbb Z^3)$. Let $\delta_0$ be the unit vector at the origin and set

$$
M_\lambda(t)=\mathbb E_\omega\!\left[\sum_{x\in\mathbb Z^3}|x|_2^2\,
\big|\langle\delta_x,e^{-itH_{\lambda,\omega}}\delta_0\rangle\big|^2\right].
$$

Does there exist $\lambda_0>0$ such that, for every $0<\lambda<\lambda_0$, there are constants $0<c_\lambda\le C_\lambda<\infty$ and $t_\lambda<\infty$ with

$$
c_\lambda t\le M_\lambda(t)\le C_\lambda t\qquad(t\ge t_\lambda)?
$$

The expectation averages the static random potential. The lattice is infinite, the initial state is fixed, and $\lambda$ is held fixed as $t\to\infty$. This asks for the disorder-averaged, order-of-growth form of quantum diffusion for a standard bounded single-site law. It does not prescribe a limiting diffusion coefficient or a Brownian path limit.

## Applied significance

This model describes the spreading of an initially localized quantum particle through a crystal with random site energies. Linear growth of the mean-square displacement would justify the diffusive transport scale used to model weakly disordered solids directly from unitary microscopic dynamics. It gives quantitative transport information beyond the existence of extended spectral states.

## References

1. Barry Simon, *Schrödinger operators in the twenty-first century*, Mathematical Physics 2000, pp. 283–288. [Author manuscript](https://math.caltech.edu/papers/bsimon/r40.pdf), §2, Example 2.1 and Problem 3.
2. Thomas Spencer, *Duality, statistical mechanics, and random matrices*, Current Developments in Mathematics 2012, pp. 229–260. [Publisher PDF](https://intlpress.com/site/pub/files/_fulltext/journals/cdm/2012/2012/0001/CDM-2012-2012-0001-a005.pdf), §§1.2 and 1.4, especially Eq. (1.19).
3. László Erdős, *Lecture Notes on Quantum Brownian Motion*, [arXiv:1009.0843v1](https://arxiv.org/html/1009.0843v1), September 4, 2010, §5.3(iii) and the following discussion of fixed disorder.
4. László Erdős, Manfred Salmhofer and Horng-Tzer Yau, *Quantum diffusion for the Anderson model in the scaling limit*, Annales Henri Poincaré 8 (2007), 621–685. [Author v5](https://arxiv.org/pdf/math-ph/0502025v5), Theorem 2.1.
5. Adam Black, Reuben Drogin and Felipe Hernández, *Self-consistent equations and quantum diffusion for the Anderson model*, [arXiv:2506.06468v2](https://arxiv.org/pdf/2506.06468v2), November 6, 2025, §1 and Theorems 1.1–1.3.

## Status review

Spencer explicitly averages the squared propagator over the random potential. Simon and Erdős pose the dynamical diffusion question separately from spectral delocalization. This entry uses the two-sided growth form, with constants allowed to depend on the fixed disorder strength.

Erdős–Salmhofer–Yau prove a heat-equation limit while the disorder tends to zero. Black–Drogin–Hernández obtain stronger finite-time estimates for Gaussian site disorder; their time horizon and resolvent scaling depend on that disorder strength. Neither gives the displayed all-large-time bounds at fixed positive disorder. A 2026 heavy-tail transport paper has random hopping and a large-connectivity approximation. Diffusion-pole identities express coefficients through correlation functions without establishing the required positive finite bounds. The evidence ledger compares these claims explicitly.

[Entry 015](../../../problems/015-anderson-extended-states.md) instead asks for an absolutely continuous spectral interval. Such a spectral statement does not itself prescribe the displacement growth rate. Searches covered proof and counterexample claims, fixed versus vanishing disorder, 2025–2026 updates and corrections. No matching resolution was located. The [evidence ledger](../candidates/anderson-fixed-disorder-diffusion.json) records the sources, scope distinctions and limitations. A separate adversarial self-pass passed on September 17, 2026; no independent agent or human review occurred. Integrated as [entry 306](../../../problems/306-anderson-fixed-disorder-diffusion.md) after the September 17, 2026 batch refresh.
