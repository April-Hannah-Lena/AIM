# 152. Surjectivity of the two-dimensional Euler endpoint map

**Area:** Geometric hydrodynamics

## Problem statement

Let $(M,g)$ be a closed connected oriented Riemannian surface, $s>2$, and $\phi$ an area-preserving $H^s$ diffeomorphism in the identity component. Is there a divergence-free $u_0\in H^s(TM)$ such that the Euler solution

$$
\partial_tu+\nabla_u u=-\operatorname{grad}p,\qquad \operatorname{div}u=0
$$

has particle map $\eta(1)=\phi$, where $\partial_t\eta(t,x)=u(t,\eta(t,x))$ and $\eta(0,x)=x$? The assertion is quantified over every such $M,s,\phi$.

## Applied significance

This asks whether an unforced ideal fluid can realize an arbitrary prescribed rearrangement of its particles.

## References

1. Boris Khesin, Gerard Misiołek and Alexander Shnirelman, *Geometric Hydrodynamics in Open Problems*, Archive for Rational Mechanics and Analysis 247 (2023), article 15. [Author copy](https://www.math.toronto.edu/khesin/papers/Problems_in_GHD_ARMA.pdf). §5.2, Problem 8(i), is the source question; the identity-component restriction removes the elementary isotopy obstruction.

2. David Ebin and Jerrold Marsden, *Groups of diffeomorphisms and the motion of an incompressible fluid*, Annals of Mathematics 92 (1970), 102–163. [Publisher record](https://doi.org/10.2307/1970699). Geodesic formulation and local endpoint-map theory.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

Problem 8(i) is posed as open in the 2023 source. Its local version follows from the inverse function theorem; global existence of two-dimensional Euler trajectories does not imply that their endpoint map is onto. Searches for “Euler exponential map surjectivity 2025 2026” and “hydrodynamics two point boundary value problem surjectivity” did not locate a later global theorem. No minimization of kinetic action is requested here.
