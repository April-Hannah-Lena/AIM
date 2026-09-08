# 144 — Exact capacity of the binary deletion channel

**Area:** Information theory / synchronization errors

## Problem statement

Fix $d\in(0,1)$. A channel takes an input word $x_1\cdots x_N\in\{0,1\}^N$, independently deletes each bit with probability $d$, and returns the surviving subsequence in order. Deleted positions are not reported, and the transmitter receives no feedback.

Determine $C(d)$ for all $d\in(0,1)$, where $C(d)$ is the supremum of rates $R$ admitting binary block codes of length $N$ with at least $2^{NR}$ codewords and decoding error tending to zero as $N\to\infty$. Error is averaged over a uniform message and the independent deletions, and rate is measured per input bit.

## Applied significance

Deletions model loss of synchronization in communication and molecular storage. Their capacity gives the ultimate redundancy needed when the receiver does not know which positions disappeared.

## References

1. M. Cheraghchi and J. Ribeiro, *An Overview of Capacity Results for Synchronization Channels* (2021), [IEEE Transactions on Information Theory; arXiv:1910.07199](https://arxiv.org/abs/1910.07199), §§1–2 and §§3–5. Defines operational capacity and describes the unresolved exact deletion capacity.
2. M. Pinto and J. Ribeiro, *Improved Capacity Upper Bounds for the Deletion Channel using a Parallelized Blahut-Arimoto Algorithm* (2026), [arXiv:2604.05867](https://arxiv.org/abs/2604.05867), abstract and main upper bounds. Provides updated numerical converse bounds.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

The survey explicitly identifies exact synchronization-channel capacity as open. The April 2026 work improves upper bounds, including a high-deletion estimate, while leaving the exact curve undetermined. Searches included “binary deletion channel exact capacity solved 2026”, “Pinto Ribeiro 2604.05867” and “deletion capacity 2025 2026 resolution”. Results for adversarial list decoding, erasures with known positions, or multiple independently deleted traces do not settle this channel.
