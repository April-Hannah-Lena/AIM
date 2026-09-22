# 231. The critical mass threshold for continuous coagulation–fragmentation

**Area:** Aggregation and fragmentation kinetics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Consider cluster sizes $s>0$, binary coagulation kernel $a(s,r)=sr$, and binary fragmentation kernel $b(s,r)=1$. For nonnegative measures $c_t$, the weak equation is
$$\begin{aligned}
\frac d{dt}\int\phi(s)c_t(ds)={}&\frac12\iint sr[\phi(s+r)-\phi(s)-\phi(r)]c_t(ds)c_t(dr)\\
&+\frac12\int\!\int_0^s[\phi(r)+\phi(s-r)-\phi(s)]\,dr\,c_t(ds).
\end{aligned}$$
Is it true that every nonnegative initial measure with $\int(1+s^2)c_0(ds)<\infty$ and mass $m=\int s\,c_0(ds)\in[1/2,1]$ admits a global nonnegative weak solution satisfying this equation for compactly supported $C^1$ test functions and conserving $\int s\,c_t(ds)=m$ for every $t\geq0$? Require weak continuity in time and locally integrable collision and fragmentation expressions.

## Application

Mass loss in this model represents formation of a macroscopic gel. The question locates the balance between multiplicative aggregation and uniform binary breakup.

## References

- Hung Vinh Tran and Truong-Son Van, [*Coagulation-fragmentation equations with multiplicative coagulation kernel and constant fragmentation kernel*](https://par.nsf.gov/servlets/purl/10330427) (2022), §1.3: the critical-mass conjecture and the proved subcritical range.
- Hung Vinh Tran and Truong-Son Van, [*Local mass-conserving solution for a critical coagulation-fragmentation equation*](https://par.nsf.gov/servlets/purl/10418278) (2023), introduction and Theorem 1.1: local existence above the currently established global range.
- Jiwoong Jang and Hung Vinh Tran, [*Discrete coagulation-fragmentation equations with multiplicative coagulation kernel and constant fragmentation kernel*](https://doi.org/10.1186/s13662-025-03946-4) (2025), introduction: the related discrete problem and comparison with the continuous model.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “critical coagulation fragmentation mass one half one conjecture”, “Tran Van global mass conservation 2025 2026”, and subsequent Bernstein-transform work. Global mass conservation for sufficiently small mass and finite-time gelation above mass one leave the displayed intermediate interval unresolved in the cited literature. Discrete-size results do not settle the continuous-size statement.
