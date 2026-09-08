# 038. Exact quantum capacity of the qubit depolarizing channel

**Area:** Quantum communication and operator optimization

**Status:** Open in cited literature; no later resolution located

**Last checked:** 2026-09-08

## Problem statement

For $0\le p\le1/3$, let
$$\mathcal D_p(\rho)=(1-3p)\rho+p(X\rho X+Y\rho Y+Z\rho Z),$$
where $X,Y,Z$ are the Pauli matrices. Determine the unassisted quantum capacity $Q(\mathcal D_p)$ throughout this interval. A precise characterization is
$$Q(\mathcal D_p)=\sup_{k\ge1}\frac1k\max_{\rho_k}
\left[S(\mathcal D_p^{\otimes k}(\rho_k))-S((\mathcal D_p^c)^{\otimes k}(\rho_k))\right],$$
where $\rho_k$ ranges over $k$-qubit density matrices, $S(\rho)=-\operatorname{tr}(\rho\log_2\rho)$ and $\mathcal D_p^c$ is any complementary channel from an isometric dilation. The objective is an exact capacity formula, including the boundary between positive and zero capacity.

## Applied significance

Depolarizing noise is a standard model for quantum hardware. Its capacity specifies the ultimate asymptotic rate of reliable quantum transmission and the benchmark against which error-correcting codes are judged.

## References

1. A. Krohn-Grimberghe, [A certified lower bound on the quantum-capacity threshold of the depolarizing channel](https://arxiv.org/abs/2608.15870), 2026. Explicit certified coding bound, using the same per-Pauli convention.
2. Z. Wu, Z. Ma and J. Fullwood, [Small perturbations of coherent information](https://doi.org/10.1103/nclh-7gdf), Physical Review A 113 (2026), 012431. One-shot capacity and superadditivity methods.

## Status review

Checked on **2026-09-08**. The August 2026 preprint certifies positivity at p=0.064956 in the per-Pauli convention, rather than determining the capacity function or exact threshold. The current search found bounding and coding results, not a matching general formula. One-copy coherent information must not be silently substituted for the regularized capacity.

Searches included: `depolarizing channel quantum capacity 2026 open`; `certified lower bound quantum capacity threshold depolarizing`; `exact depolarizing quantum capacity solved`. This is a documented literature check, not a certification that no solution exists.
