# 143 — Capacity of the Gaussian relay channel with independent receiver noises

**Area:** Network information theory / cooperative communication

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Consider the memoryless real channel

$$
Y_{r,t}=aX_{s,t}+Z_{r,t},\qquad
Y_{d,t}=bX_{s,t}+cX_{r,t}+Z_{d,t},
$$

where $a,b,c>0$ and all noises are independent $N(0,1)$ variables. A source encodes a uniform message $M$ without feedback. A relay uses strictly causal rules $X_{r,t}=f_t(Y_r^{t-1})$, and the destination estimates $M$ from $Y_d^N$. Impose average block-power constraints $N^{-1}\sum_t\mathbb E X_{s,t}^2\le P_s$ and $N^{-1}\sum_t\mathbb E X_{r,t}^2\le P_r$, with $P_s,P_r>0$.

Determine the capacity $C(a,b,c,P_s,P_r)$, the supremum of $(\log_2|\mathcal M|)/N$ achievable with error probability tending to zero as $N\to\infty$, for all these parameters.

## Application

This is a basic wireless link assisted by one cooperating relay. Exact capacity would specify the best possible gain from relaying when decoding, compression and analog forwarding compete.

## References

1. A. El Gamal and Y.-H. Kim, *Network Information Theory* (Cambridge University Press, 2011), [Chapter 16, Relay Channels](https://doi.org/10.1017/CBO9781139030687.018), §§16.5–16.7. Defines the Gaussian model and its principal bounds.
2. A. El Gamal, A. Gohari and C. Nair, *A Strengthened Cutset Upper Bound on the Capacity of the Relay Channel and Applications* (2022), [arXiv:2101.11139](https://arxiv.org/abs/2101.11139), Gaussian specialization, Theorem 2. Improves the converse for nonzero channel gains without matching all achievable rates.
3. X. Wu, L. P. Barnes and A. Özgür, *Cover's Open Problem: “The Capacity of the Relay Channel”* (2017), [arXiv:1701.02043](https://arxiv.org/abs/1701.02043), problem setup and Theorem 1.2. Resolves a particular saturation-threshold question for a different relay model with a noiseless bit pipe.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2022 work supplies a stronger upper bound, not a general capacity formula. The title of the Wu–Barnes–Özgür result should not be interpreted as solving the full Gaussian model above. Searches included “Gaussian relay channel capacity open problem 2025 2026”, “strengthened cutset Gaussian relay capacity” and “Cover relay channel solved capacity”. No matching general coding and converse theorem was located.
