# 286. Optimal deterministic competitiveness for mobile servers

**Area:** Online service and resource allocation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For any finite metric space $(M,d)$, integer $1\le k<|M|$, and initial placement of $k$ servers, requests arrive one at a time at points of $M$. A deterministic online algorithm must move servers so that a server occupies the requested point before seeing the next request, paying total distance moved. Does there always exist such an algorithm $A$ and a finite constant $b$ independent of the request sequence with $\mathrm{cost}_A(\sigma)\le k\,\mathrm{OPT}(\sigma)+b$ for every finite sequence $\sigma$? The offline optimum starts at the same placement and knows the entire sequence.

## Application

The model captures mobile service resources and caching; the target is the best universal loss caused by not knowing future requests.

## References

- [Zhiyi Huang and Hanwen Zhang, *Deterministic 3-server on a circle and the limitation of canonical potentials* (2024)](https://doi.org/10.1016/j.tcs.2024.114844), Introduction.
- [Kirill Brilliantov, Étienne Bamas and Emmanuel Abbé, *k-server-bench: Automating Potential Discovery for the k-Server Conjecture* (2026)](https://arxiv.org/abs/2604.07240), formulation and unresolved cases.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The three-server circle result and partial searches for potential functions leave the universal deterministic question open. Randomized competitiveness is a separate problem; finite verification of candidate inequalities is not treated as a proof.

Search topics checked on 2026-09-13: `deterministic k server conjecture resolved 2026 competitive ratio general metric`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
