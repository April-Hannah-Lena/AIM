# 291. The Černý synchronizing-automaton conjecture

**Area:** Finite-state control and synchronization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $`Q`$ be a nonempty set of $`n`$ states, let $`\Sigma`$ be a nonempty finite alphabet, and let $`\delta:Q\times\Sigma\to Q`$ be a total transition map. Extend $`\delta`$ to words by successive application of their letters. A word $`w\in\Sigma^*`$ is a **reset word** if $`\delta(q,w)`$ is the same state for every $`q\in Q`$. The automaton is synchronizing when it has at least one reset word.

Must every synchronizing complete deterministic automaton with $`n`$ states have a reset word of length at most

```math
(n-1)^2?
```

Each original alphabet letter costs one step. The question imposes no one-cluster, Eulerian, binary-alphabet or other structural restriction. It asks for existence of a short word, rather than an efficient algorithm for finding a shortest one. For $`n=1`$, the empty word has length zero.

## Application

A reset word drives a finite-state device from an unknown initial state to a known state without observing its intermediate states. The conjecture would bound the worst-case number of control inputs required for this form of synchronization. This is a foundational resource bound for finite-state control and testing.

## References

1. M. V. Volkov, [*List of Results on the Černý Conjecture and Reset Thresholds for Synchronizing Automata*](https://arxiv.org/pdf/2508.15655v4), arXiv:2508.15655v4, version dated January 13, 2026; §§1.1–1.2, especially printed pp. 3–4 and footnote 1. Preprint.
2. M. Szykuła, [*Synchronizing Automata: Open Problems*](https://arxiv.org/pdf/2608.24245v1), EPTCS **451** (2026), 33–47, DOI 10.4204/EPTCS.451.3; §2.1, Conjecture 1 on p. 34. arXiv version posted August 25, 2026.
3. Y. Zhu, [*The Černý Conjecture for One-Cluster Automata via Annular Spectral Descent*](https://arxiv.org/html/2607.19675v1), arXiv:2607.19675v1, July 22, 2026; Theorem 2.4. Preprint claiming a restricted-class result.
4. A. N. Trahtman, [*The Černy conjecture*](https://arxiv.org/pdf/1202.4626v11), arXiv:1202.4626v11, January 18, 2022; Theorem 2, p. 11. Historical full-proof claim; see the error report in Volkov's footnote 1.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 17, 2026 review included Černý/Cerny/Starke aliases, reset-word wording, proof and counterexample searches, 2025–2026 updates, unrestricted searches and version/withdrawal checks. Szykuła's August 2026 specialist survey independently lists the full conjecture as open. The general upper bound reported by that survey and Volkov is

```math
\left(\frac7{48}+\frac{15625}{798768}\right)n^3+o(n^3),
```

which leaves the quadratic target unresolved.

Trahtman's Theorem 2 claims the full result. Volkov specifically reports that Trahtman acknowledged a proof error in February 2024; this review attributes that report to Volkov and does not claim an independent proof-error audit. Berlinkov's separate 2012 claimed proof is explicitly withdrawn in its arXiv record. Zhu's Theorem 2.4 requires an alphabet letter having exactly one directed cycle and does not treat arbitrary synchronizing automata. Replacing a long reset word by a new letter would change the cost and cannot transfer that bound.

The accessed Volkov HTML and PDF have inconsistent update dates. This entry uses the versioned PDF and obtains later corroboration from Szykuła. The [evidence record](../research/expansion-2026-09/candidates/cerny.json) records the comparison, full theorem locators, baseline distinctness from differential-control/reachability problems, and a separate adversarial self-review. No independent expert review is claimed.
