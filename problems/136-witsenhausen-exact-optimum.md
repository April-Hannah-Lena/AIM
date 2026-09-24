# 136 — Exact optimal control in the scalar Witsenhausen benchmark

**Area:** Decentralized stochastic control

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $X_0\sim N(0,25)$ and $Z\sim N(0,1)$ be independent. Controller one sees $X_0$ and chooses $U_1=f(X_0)$; controller two sees only $Y=X_0+U_1+Z$ and chooses $U_2=g(Y)$. Determine the exact value and an optimal measurable pair for

$$
J_*=\inf_{f,g}\mathbb E\!\left[0.04\,f(X_0)^2+
\bigl(X_0+f(X_0)-g(X_0+f(X_0)+Z)\bigr)^2\right],
$$

where the infimum runs over Borel functions $f,g:\mathbb R\to\mathbb R$ of finite cost. A characterization must establish global optimality over this class; stationarity or numerical optimization over a chosen family of functions is insufficient.

## Application

The first action both changes a state and communicates information through that change. An exact optimum would provide a certified benchmark for decentralized-control algorithms whose controllers have unequal information, including a way to measure how far a proposed strategy is from the best achievable performance.

## References

1. H. S. Witsenhausen, *A counterexample in stochastic optimum control* (1968), [SIAM Journal on Control 6, 131–147](https://doi.org/10.1137/0306011), problem formulation and nonlinear counterexample to affine optimality.
2. M. Zhao, M. Le Treust and T. J. Oechtering, *Low-Power Optimal Strategy for Witsenhausen Counterexample* (2025), [arXiv:2509.02381](https://arxiv.org/abs/2509.02381), §§I and III. Gives first-order low-power optimality, not the exact benchmark optimum.
3. B. Telsang, S. Djouadi and C. D. Charalambous, *General Decentralized Stochastic Optimal Control via Change of Measure: Applications to the Witsenhausen Counterexample* (2025), [arXiv:2509.11013](https://arxiv.org/abs/2509.11013), abstract and Witsenhausen application. Develops optimality conditions and numerical methods.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 low-power paper still treats exact optimal strategy design as unresolved. Existence results, person-by-person conditions, asymptotic vector versions and local numerical improvements are distinct from the exact scalar global optimum above. Searches included “Witsenhausen 0.2 sigma 5 global optimal solution 2026”, “Low-Power Optimal Strategy Witsenhausen” and “Telsang 2025 Witsenhausen global optimality”. No certified exact value with a globally optimal benchmark pair was located.
