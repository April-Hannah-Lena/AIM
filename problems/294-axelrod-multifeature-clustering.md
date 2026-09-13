# 294. Consensus in the one-dimensional Axelrod model above the feature threshold

**Area:** Cultural transmission and interacting populations

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Fix integers $F>q\ge3$. At each $x\in\mathbb Z$ a culture $\eta_t(x)$ has $F$ coordinates in $\{1,\ldots,q\}$, initially independent and uniform across all sites and coordinates. Every unordered nearest-neighbor edge rings at rate one. If its endpoints agree on $a$ features with $0<a<F$, then with probability $a/F$ choose a uniformly random disagreeing feature and a uniformly random direction, and copy that feature from the source to the target. Otherwise do nothing. Must $\mathbb P(\eta_t(x)\ne\eta_t(y))\to0$ as $t\to\infty$ for every fixed pair $x,y$? This is convergence of local disagreement probabilities, not almost-sure stabilization of each site.

## Applied significance

The conjecture identifies when homophily and social influence erase cultural differences on a spatial network.

## References

- [Nicolas Lanchier and Jason Schweinsberg, *Consensus in the two-state Axelrod model*, Stochastic Processes and their Applications 122 (2012)](https://arxiv.org/abs/1107.4413), Introduction, general clustering conjecture and the two-state theorem.
- [Nicolas Lanchier and Stylianos Scarlatos, *Fixation in the one-dimensional Axelrod model* (2013 preprint)](https://arxiv.org/abs/1301.0130), fixation results in other parameter regimes.

## Status review

The two-state theorem covers q=2. Existing fixation theorems address parameter regions with sufficiently many available traits. The general F>q clustering direction for three or more traits remains the retained question.

Search topics checked on 2026-09-13: `one dimensional Axelrod clustering F greater q three traits conjecture solved 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
