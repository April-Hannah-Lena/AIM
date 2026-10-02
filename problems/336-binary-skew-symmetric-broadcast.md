# 336. Capacity of the binary skew-symmetric broadcast channel

**Area:** Network information theory and broadcast communication

**Status:** 🔵 OPEN

**Last checked:** 2026-09-18

## Problem statement

A transmitter sends a bit $`X`$ to two receivers with binary outputs $`Y`$ and $`Z`$. Fix the memoryless channel whose transition matrices are

```math
P_{Y\mid X}=
\begin{pmatrix}
1&0\\
1/2&1/2
\end{pmatrix},
\qquad
P_{Z\mid X}=
\begin{pmatrix}
1/2&1/2\\
0&1
\end{pmatrix}.
```

Rows correspond to $`X=0,1`$ and columns to the output values $`0,1`$. Thus input zero is received without error by the first receiver, while input one is received without error by the second. The other output is a fair bit. The joint law is $`W(y,z\mid x)=P_{Y\mid X}(y\mid x)P_{Z\mid X}(z\mid x)`$; successive uses are conditionally independent given the transmitted sequence. [1, §5]

For each block length $`n`$, let $`W_1,W_2`$ be independent uniform messages with respective message-set sizes $`M_{1,n},M_{2,n}`$. An arbitrary encoder maps the message pair to $`X^n\in\{0,1\}^n`$. Receiver one estimates $`W_1`$ from $`Y^n`$, and receiver two estimates $`W_2`$ from $`Z^n`$. The transmitter receives no feedback, and the receivers cannot communicate. There is no separately requested common message; common coding layers are allowed.

A nonnegative rate pair $`(R_1,R_2)`$ is achievable if a sequence of these codes satisfies

```math
\liminf_{n\to\infty}\frac{\log_2 M_{i,n}}{n}\ge R_i
\quad(i=1,2),
\qquad
\Pr\{\widehat W_1\ne W_1\ \text{or}\ \widehat W_2\ne W_2\}\longrightarrow0.
```

Let $`\mathcal C_{\mathrm{BSSC}}`$ be the closure of the achievable rate pairs. **Determine $`\mathcal C_{\mathrm{BSSC}}`$ exactly, with matching achievability and converse bounds.** Rates are measured in bits per channel use. Codes need not be linear or computationally efficient, and the input distribution is unrestricted. This is the standard private-message problem for the fixed channel above. [1, §5; 2, §1.1]

## Application

This channel is a basic model of one sender delivering separate data streams to two users whose reception quality depends differently on the transmitted symbol. A transmission strategy must balance their rates even though neither receiver has uniformly better observations. Its capacity region would identify the fundamental throughput tradeoff for this setting and test whether existing broadcast coding methods extract all the available information. The significance is foundational: the binary model isolates an obstacle to optimal multiuser coding without continuous alphabets or a power-allocation problem. [1, §§1, 5; 2, §1]

## References

1. Yanan Dou, Yanqing Liu, Xueyan Niu, Bo Bai, Wei Han and Yanlin Geng, *Blahut–Arimoto Algorithms for Inner and Outer Bounds on Capacity Regions of Broadcast Channels*, Entropy 26(3) (2024), 178, [DOI](https://doi.org/10.3390/e26030178). [Full-text archive](https://pmc.ncbi.nlm.nih.gov/articles/PMC10969477/), §§3.2–3.3, 4.2–4.3, 5 and 6.2. The relevant full-text sections were read through its [Europe PMC XML copy](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10969477/fullTextXML) where the HTML endpoints failed.
2. Chandra Nair, *On Marton's Achievable Region: Local Tensorization for Product Channels with a Binary Component*, [author manuscript](https://staff.ie.cuhk.edu.hk/~cnair/pub/papers/BC/loc-ten-bin.pdf), February 7, 2020; presented at the Information Theory and Applications Workshop. §1, restatement of textbook Problem 8.3; §1.1, coding definitions; Definitions 1.4–1.5, Proposition 2.6 and the final summary.
3. Varun Jog and Chandra Nair, *An information inequality for the BSSC channel*, [arXiv:0901.1492v3](https://arxiv.org/html/0901.1492v3), December 11, 2009, author preprint. §1, Figure 1 and Bounds 1–2; §§3.1.1–3.2.1 and conclusion. Version 3 supplies a new proof after the withdrawn version 2.
4. Yanlin Geng, Varun Jog, Chandra Nair and Zizhou Vincent Wang, *An information inequality and evaluation of Marton's inner bound for binary input broadcast channels*, IEEE Transactions on Information Theory 59(7) (2013), 4095–4105. [Author manuscript](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/inineq.pdf), §I-B, Theorems 1–4; §III. The published bibliographic details are confirmed by [Nair's publication list](https://staff.ie.cuhk.edu.hk/~cnair/pub/publications.html).
5. Amin Gohari and Chandra Nair, *Outer Bounds for Multiuser Settings: The Auxiliary Receiver Approach*, IEEE Transactions on Information Theory 68(2) (2022), 701–736, [DOI](https://doi.org/10.1109/TIT.2021.3128136). [Author manuscript](https://staff.ie.cuhk.edu.hk/~cnair/pub/papers/NIT/Auxiliary-Receiver.pdf), §4.1, Theorem 7 and Eqs.(18)–(20); §4.2.
6. Amin Gohari, Yi Liu and Chandra Nair, *A Two Auxiliary Receiver Outer Bound to the Capacity Region of a Two-Receiver Discrete Memoryless Broadcast Channel*, [author manuscript](https://chandra.ie.cuhk.edu.hk/pub/papers/BC/GK-outer.pdf), January 2026 according to the author's publication list. §III-A, fixed-channel definition and status; §III-B, Theorem 7; §IV, Eqs.(15)–(18) and numerical evaluations.
7. Amin Gohari, Yi Liu and Chandra Nair, *The Capacity Region for Classes of Sum-Broadcast Channels*, [arXiv:2606.12839v1](https://arxiv.org/html/2606.12839v1), June 11, 2026, preprint. Definitions 1–3, Lemma 5 and Theorem 4. This expanded version was checked separately from the January author manuscript.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Dou and coauthors [1] explicitly retain the fixed channel's capacity-region question, independently of Nair's account [2]. The January 2026 manuscript [6] still states that even its sum capacity is unknown. These sources use equivalent conventions obtained by interchanging receiver names or relabelling bits.

The established information inequality in [3, 4] evaluates Marton's achievable sum rate as approximately $`0.36164288`$ bits per use, while the older UV upper bound is approximately $`0.3725562`$. This proves a gap between those two descriptions; their equality is not the open question. Source [5] develops stronger auxiliary-receiver converses. Source [6] reports a numerical evaluation of approximately $`0.36929634`$ for its newer bound, which still exceeds the achievable sum rate. That numerical optimization was not independently reproduced or certified here. Determining even the maximum sum rate would not by itself characterize the entire capacity boundary.

The local tensorization result [2] concerns products of local optimizers and does not establish the global optimality needed for a capacity theorem. The algorithms in [1] evaluate inner and outer bounds under stated convergence hypotheses; they do not prove that a bound equals capacity. The June 2026 exact-capacity theorem [7] requires a disjoint sum of component channels, with the component identifiable from either output. From the matrices above, both inputs can produce $`Y=0`$, and both can produce $`Z=1`$. Thus this BSSC fails the theorem's output-disjointness requirement for a nontrivial sum.

The September 18, 2026 investigation covered channel aliases, the exact matrices and coding model, current and unrestricted resolution searches, author publications, revisions and corrections. The withdrawn 2009 preprint was replaced by version 3; the later combined journal article [4] supplies the same pertinent inequality and bound evaluations. Bibliography access limitations and the complete theorem comparisons are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/binary-skew-symmetric-broadcast.json). A separated adversarial self-pass checked the newer version of [7] and distinguished a solved single-user channel with the same acronym. No independent agent or human review has occurred.

This is one canonical channel problem. [Entry 300](299-gaussian-broadcast-feedback.md) has continuous Gaussian outputs, a power constraint and causal feedback. [Entry 136](135-binary-multiplying-two-way-capacity.md) concerns interactive two-way transmission, while [entry 137](136-gaussian-relay-capacity.md) has a cooperating relay. The [binary-code rate problem](331-binary-code-asymptotic-rate.md) requires worst-case codeword separation rather than vanishing average error on this broadcast channel. Other BSSC crossover probabilities and scalar objectives are not counted separately.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
