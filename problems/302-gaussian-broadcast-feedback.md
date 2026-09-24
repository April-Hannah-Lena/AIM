# 302. Capacity of the two-receiver Gaussian broadcast channel with feedback

**Area:** Applied geometry, control and information

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Fix $P,N_1,N_2>0$. At time $t$, a real memoryless broadcast channel has outputs

$$
Y_{k,t}=X_t+Z_{k,t},\qquad k\in\{1,2\},
$$

where all $Z_{k,t}$ are mutually independent, $Z_{k,t}\sim\mathcal N(0,N_k)$, and the noises are independent of the messages. The transmitter knows two independent uniform messages $W_k\in\{1,\ldots,M_k\}$, with $W_k$ intended only for receiver $k$. It receives noiseless feedback of both past output sequences and may use arbitrary measurable encoders

$$
X_t=f_t(W_1,W_2,Y_1^{t-1},Y_2^{t-1}),\qquad
\frac1n\sum_{t=1}^n\mathbb E[X_t^2]\le P.
$$

Receiver $k$ estimates its message using only $Y_k^n$. Define $\mathcal C_{\mathrm{fb}}(P,N_1,N_2)$ as the closure of all nonnegative rate pairs obtainable by a sequence of such codes with $\liminf_{n\to\infty}n^{-1}\log_2 M_k\ge R_k$ and

$$
\Pr\{\widehat W_1\ne W_1\ \text{or}\ \widehat W_2\ne W_2\}\longrightarrow0.
$$

Determine this capacity region for every fixed $P,N_1,N_2>0$, with matching achievability and converse bounds. Encoding is not restricted to linear feedback schemes. [1, 2]

## Application

This is the basic model of one transmitter sending separate data streams to two receivers while using returned observations to correct earlier transmission errors. Its capacity region would give the ultimate throughput benchmark for feedback coding and learned communication schemes. [1, 5]

## References

1. Michael Gastpar, Amos Lapidoth, Yossef Steinberg and Michèle Wigger, *Coding Schemes and Asymptotic Capacity for the Gaussian Broadcast and Interference Channels With Feedback*, IEEE Transactions on Information Theory 60(1), 2014, 54–71, DOI [10.1109/TIT.2013.2287531](https://doi.org/10.1109/TIT.2013.2287531). [Author manuscript, arXiv:1003.6082v3](https://arxiv.org/html/1003.6082v3), §§I–II, especially §II-A and Theorem 1.
2. Ehsan Ardestanizadeh, Paolo Minero and Massimo Franceschetti, *LQG Control Approach to Gaussian Broadcast Channels With Feedback*, IEEE Transactions on Information Theory 58(8), 2012, 5267–5278, DOI [10.1109/TIT.2012.2196789](https://doi.org/10.1109/TIT.2012.2196789). Scope checked in [arXiv:1102.3214v1](https://arxiv.org/pdf/1102.3214), §§I–II and §V, Theorem 2.
3. Selma Belhadj Amor, Yossef Steinberg and Michèle Wigger, *MIMO MAC–BC Duality with Linear-Feedback Coding Schemes*, [arXiv:1404.2584v1](https://arxiv.org/pdf/1404.2584), 9 April 2014, §V-A, Theorem 1 and Corollaries 1–4.
4. Lan V. Truong and Hirosuke Yamamoto, *Posterior Matching for Gaussian Broadcast Channels with Feedback*, IEICE Transactions on Fundamentals E100-A(5), 2017, 1165–1178. [Author manuscript, arXiv:1404.2520v7](https://arxiv.org/pdf/1404.2520), §I and §6, Theorem 2.
5. Jacqueline Malayter, Yingyao Zhou, Natasha Devroye, Chih-Chun Wang, Christopher Brinton and David J. Love, *Deep Broadcast Feedback Codes*, [arXiv:2512.00608v1](https://arxiv.org/html/2512.00608v1), 29 November 2025, §§I–II, IV–V.
6. Abbas El Gamal, *The Capacity of the Physically Degraded Gaussian Broadcast Channel with Feedback*, IEEE Transactions on Information Theory 27(4), 1981, 508–511, DOI [10.1109/TIT.1981.1056372](https://doi.org/10.1109/TIT.1981.1056372). [Author-hosted full text](https://isl.stanford.edu/groups/elgamal/abbas_publications/J009.pdf), §III, Eq. (10) and Theorem 3.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Sources [1] and the independent work [2] explicitly identify the unrestricted capacity problem as open. The duality theorem [3] characterizes the linear-feedback region through a multiple-access channel; its linearity restriction does not supply a converse for all broadcast codes. Posterior matching [4] attains the symmetric linear-feedback sum rate, leaving the same restriction.

The high-signal-to-noise result [1] determines a sum-capacity asymptotic as $P\to\infty$, rather than the full region at fixed power. The 2025 learned-code study [5] improves finite-block error performance and supplies no unrestricted capacity characterization. The no-feedback-gain theorem [6] assumes physically degraded, correlated receiver noises; it does not apply to the independent-noise channel above. Targeted later-result and resolution searches found no theorem settling this exact formulation as of the review date.

The [evidence record](../research/expansion-2026-09/candidates/gaussian-broadcast-feedback.json) documents exact searches, source access, scope comparisons, duplicate screening and the separate adversarial self-review.

The September 17, 2026 review included named and mathematical formulations, author/citation searches, 2025–2026 results, and unrestricted proof, counterexample, resolution and correction searches; these were refreshed before integration.
