# 410. Continuous selection of small-time null controls for analytic systems

**Area:** Nonlinear control / feedback design

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`f_0,f_1:\mathbb R^n\to\mathbb R^n`$ be real analytic with $`f_0(0)=0`$, and consider the scalar-input system

```math
\dot y=f_0(y)+u(t)f_1(y),\qquad y(0)=y_0.
```

Assume that for every $`T>0`$ some $`\delta>0`$ has the following property: every $`|y_0|<\delta`$ admits $`u\in L^1(0,T)`$ with $`\|u\|_1\le T`$ whose solution exists on $`[0,T]`$ and satisfies $`y(T)=0`$. Must it follow that for every $`T>0`$ there are $`\delta_T>0`$ and a continuous map

```math
U_T:B_{\delta_T}(0)\longrightarrow L^1(0,T),\qquad U_T(0)=0,
```

such that the trajectory driven by $`U_T(y_0)`$ exists on $`[0,T]`$ and ends at zero for every $`y_0\in B_{\delta_T}(0)`$? Continuity refers to the norm topology of $`L^1`$.

## Application

A continuously selected steering input changes smoothly under small errors in the measured state. This is a basic bridge from open-loop controllability to continuous time-dependent feedback for nonlinear mechanical systems.

## References

1. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), Definition 4.16 and Open Problem 4.17. [Full text](https://arxiv.org/html/2602.19272v1).
2. J.-M. Coron, *Control and Nonlinearity*, Mathematical Surveys and Monographs 136, AMS (2007), Chapter 11, Proposition 11.22. [Book DOI](https://doi.org/10.1090/surv/136).
3. J.-M. Coron, *Links Between Local Controllability and Local Continuous Stabilization*, IFAC Proceedings Volumes 25(13) (1992), 165–171. [DOI](https://doi.org/10.1016/S1474-6670(17)52276-4).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The February 2026 notes state the analytic implication as an open problem and explain why available sufficient conditions give continuous controls without proving the implication in full. Searches through 22 September 2026 found no later theorem resolving it. This asks for continuity of an actual control selection, distinct from finite-jet tests for controllability.
