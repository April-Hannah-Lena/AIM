# Feedback gain for FIFO timing channels with non-exponential service

**Area:** Stochastic dynamics, reaction networks and applied optimization

**Status:** HELD — the proposed formulation failed the adversarial check; not an accepted open problem.

**Last checked:** 2026-09-17

This is an unaccepted working formulation. The review found a potential shifted-exponential counterexample; see the [research record](../candidates/fifo-queue-feedback.json). It must not be integrated as an open page.

## Problem statement

Let $S$ be a nonnegative, absolutely continuous random variable with $0<\mathbb E S<\infty$ and finite differential entropy. Consider an initially empty, work-conserving, first-in-first-out single-server queue with unlimited buffer. Packets carry information only in their arrival times. For ordered arrivals $0\le a_1\le\cdots\le a_n$, departure times satisfy

$$
d_0=0,\qquad d_i=\max\{a_i,d_{i-1}\}+S_i,
$$

where the $S_i$ are independent copies of $S$, independent of the message.

An $n$-packet code sends one of $M_n$ equiprobable messages. A decoder observes all $n$ departure times; require its average error to tend to zero and $\mathbb E d_n\le T_n$. The rate is $\log_2(M_n)/T_n$, with $n,T_n\to\infty$. Let $C(S)$ be the supremum of achievable rates when all arrival times depend only on the message. Define $C_F(S)$ similarly when the encoder also receives instantaneous, noiseless, causal feedback of departures and can adapt subsequent arrivals.

If $S$ is not exponentially distributed, must

$$
C_F(S)>C(S)?
$$

The question includes unbounded service-time distributions. The finite-entropy density assumption excludes singular or deterministic service laws that can have infinite continuous-time timing capacity. Capacities are measured per expected time of the final **departure**, with no fixed packet-output rate imposed.

## Applied significance

Packet timing can convey information through a server even when packets have identical contents. The question asks whether acknowledgements can improve the best reliable information rate for every non-exponential service law.

## References

1. V. Anantharam and S. Verdú, “Bits through queues,” *IEEE Transactions on Information Theory* **42** (1996), 4–18. [DOI](https://doi.org/10.1109/18.481773); [author copy](https://people.eecs.berkeley.edu/~ananth/1996-1998/Sergio/BTQ96.pdf). Operational definitions: §II.A, p. 6; feedback capacity and conjectural strictness: §III, Theorem 8 and discussion, p. 14.
2. K. R. Sahasranand and A. Tchamkerten, “Feedback Increases the Capacity of Queues with Bounded Service Times,” *IEEE Transactions on Information Theory* **70** (2024), 6823–6833. [Author manuscript, arXiv:2309.14145v2](https://arxiv.org/html/2309.14145v2). Model: §II, Definitions 1–3; partial results: §III, Theorems 2–3; remaining open case: §V.
3. L. Aptel and A. Tchamkerten, “Bits Through Queues With Feedback.” [Published article DOI](https://doi.org/10.1109/TIT.2020.2970421); [arXiv:1710.06190v1](https://arxiv.org/html/1710.06190v1). The locators used here refer to v1: §3.1, Example 1, and §3.2, Corollary 10.

## Status review

Anantharam–Verdú establish equality for exponential service. Sahasranand–Tchamkerten independently retain the general conjecture and prove strict gain for the bounded, interval-supported continuous distributions covered by their Theorem 2. Their §V explicitly leaves unbounded service unresolved.

Their Theorem 3 refutes an earlier conjecture about an entropy upper bound. Equality of those bounds does not establish equality of the operational capacities. The no-gain result for preemptive last-come-first-served queues also uses a different discipline.

Searches on 2026-09-17 included later work, proof and counterexample claims, corrections and version histories. No matching full resolution was located. The [research record](../candidates/fifo-queue-feedback.json) documents the scope comparisons, source access and review.
