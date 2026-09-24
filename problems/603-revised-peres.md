# 603. Can bound entanglement produce a device-independent secret key?

**Area:** Quantum information and cryptography

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $\rho_{AB}$ be a finite-dimensional bipartite bound-entangled state: it is entangled, but its distillable entanglement under local quantum operations and public classical communication is zero.

Prove or disprove that independent copies of $\rho_{AB}$ cannot yield a positive asymptotic secret-key rate in any device-independent quantum key distribution protocol. This is the revised Peres conjecture [1, Conjecture 11].

Device-independent security means that the shared output key must approach a uniform key independent of the adversary for every quantum realization consistent with the observed input-output statistics. Local measurements and classical public communication are allowed; the shared quantum resource is the supplied state. The target includes arbitrary protocols, beyond a fixed Bell test or one-way classical processing. Bell nonlocality alone is insufficient to answer this key-generation question.

## Application

The conjecture asks which entanglement resources can support cryptography when measurement devices are untrusted. It would separate ordinary secret-key distillation from key extraction certified solely by observed correlations.

## References

1. R. Arnon-Friedman and F. Leditzky, [Upper Bounds on Device-Independent Quantum Key Distribution Rates and a Revised Peres Conjecture](https://doi.org/10.1109/TIT.2021.3086505), *IEEE Transactions on Information Theory* **67**(10) (2021), 6606–6618. [Author manuscript](https://arxiv.org/pdf/2005.12325), Section III, Conjecture 11; Section II.A defines the security and rate framework.

## Status review

**Known cases:** Reference [1, Section III.B] rules out key generation by a specified one-way protocol using the Vértesi–Brunner bound-entangled state and measurements. It expressly leaves more general protocols unresolved.

**Remaining target:** Establish zero rate for every bound-entangled state and every device-independent protocol, or give a state and a positive-rate secure protocol. The original Peres conjecture about Bell violations is false; that does not settle this revised statement.

The 2025 review [The future of secure communications: Device independence in quantum key distribution](https://www.quantum.physics.sk/rcqi/research/publications/2025/rcqi2025ghoreishi_review_device_independent_qkd.pdf) retains the revised conjecture and reviews restricted impossibility results. Searches through 24 September 2026 found no matching resolution announcement or repository duplicate. Native GitHub issues, Zenodo, and Palomar searches returned no matching record; the sole GitHub repository search result was unrelated.
