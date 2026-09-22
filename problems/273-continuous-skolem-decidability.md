# 273 — Decidability of exact hyperplane reachability for a linear ODE

**Area:** Continuous dynamics / formal verification

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Is there an algorithm which, for every positive integer $n$, rational matrix $A\in\mathbb Q^{n\times n}$ and rational vectors $x_0,c\in\mathbb Q^n$, halts and correctly decides whether

$$
\exists t\geq0:\quad c^T e^{tA}x_0=0?
$$

The matrix exponential is $e^{tA}=\sum_{j\geq0}(tA)^j/j!$. Thus the question asks whether the exact solution of $x'=Ax$, $x(0)=x_0$, ever intersects the hyperplane $c^Tx=0$. Inputs are finite binary encodings of rational numbers; time is a real variable and is not discretized.

## Application

A decision procedure would settle whether a linear continuous-time model can reach an exactly specified switching or safety boundary, a basic operation in verification of hybrid systems.

## References

1. V. Chonev, J. Ouaknine and J. Worrell, *On the Skolem Problem for Continuous Linear Dynamical Systems* (2016), [ICALP, LIPIcs 55, article 100](https://doi.org/10.4230/LIPIcs.ICALP.2016.100); [author manuscript](https://people.mpi-sws.org/~joel/publications/cont-skolem16.pdf), §1. Explicit open decidability problem, conditional bounded-time results and hardness barriers.
2. P. Bacik, T. Karimov, F. Luca, J. Nieuwveld, J. Ouaknine, D. Purser and J. Worrell, *A survey of the Skolem and Positivity Problems for linear recurrence sequences* (2026), [author manuscript](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf), §9.1, “Continuous-time analogues”, p. 48. Places this version beside current discrete, robust and positive-characteristic results.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Unconditional low-dimensional results and conditional bounded-time algorithms do not decide all dimensions over an unbounded time interval. The 2026 positive-characteristic Skolem theorem concerns discrete recurrences over a different coefficient structure. Searches included “continuous Skolem problem decidability 2026”, “linear ODE hyperplane reachability solved”, and “Chonev Ouaknine Worrell zeros exponential polynomials”. No general algorithm or undecidability proof for the displayed rational-input problem was located.
