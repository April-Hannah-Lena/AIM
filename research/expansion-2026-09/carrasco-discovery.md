# Continuous-time Carrasco necessity lead

Discovery checkpoint, September 18, 2026. No candidate admission, accepted draft, catalogue ID or additional count is assigned. The continuous-time formulation was selected before the July 2026 discrete-time claim was found. The remaining model and claim comparisons must be completed before a fingerprint and draft are written. This is source research by the primary agent; no separated adversarial pass has yet occurred.

## Original formulation: CHT16

Joaquin Carrasco, Matthew C. Turner and William P. Heath, *Zames–Falb multipliers for absolute stability: From O'Shea's contribution to convex searches*, European Journal of Control 28 (2016), 1–19, DOI [10.1016/j.ejcon.2015.10.003](https://doi.org/10.1016/j.ejcon.2015.10.003), [author PDF](https://personalpages.manchester.ac.uk/staff/joaquin.carrasco/Carrasco16.pdf).

Read the introduction, application discussion, complete §3.1 model, Definition 2, Theorem 1, Definitions 3–4 and §8 Conjecture 1. The plant is stable, proper, real-rational and SISO; feedback is negative, with a static slope restriction between zero and k, where k is strictly below the Nyquist value. Stability in §3.1 is preservation of square-integrable inputs, without an explicit uniform gain over nonlinearities. The question asks whether absence of a suitable multiplier implies an actually destabilizing nonlinearity.

The multiplier permits a noncausal integrable kernel and countably many real-time atoms, with strict total variation below one. Nonnegative coefficients are required for general nonlinearities; signed coefficients are allowed for odd ones. Conjecture 1 uses generic multiplier wording. Before drafting, reconcile that wording with Definitions 3–4, and the implicit zero-equilibrium convention with the slope definition. Do not silently strengthen stability, restrict multipliers to finite-order searches, or enlarge the measure class.

## Independent corroboration and partial theorem: KS21

Sei Zhen Khong and Lanlan Su, *On the Necessity and Sufficiency of the Zames-Falb Multipliers for Bounded Operators*, [arXiv:2009.13571](https://arxiv.org/abs/2009.13571), [v3 PDF](https://arxiv.org/pdf/2009.13571v3). History inspected: v1 September 28, 2020; v2 July 18, 2021; v3 August 18, 2021. The author teams of this work and CHT16 are disjoint.

Read the explicit unsolved-conjecture discussion, Definitions 1–2, the zero-preserving operator class, shift inequalities and Lemma 9; static Lemma 13 and Remark 17; complete Theorem 24, Lemma 26, Corollary 27, Lemma 28 and Corollary 29. The paper distinguishes finite-gain and uniform stability, uses the opposite feedback sign, and retains the static necessity question. In v3, Theorem 24 gives sufficiency over one dynamic class and necessity under uniform stability over a larger finite-shift class. Older v1 theorem numbering and stronger-looking snippets must not replace v3. Corollary 29's failure of necessity over constant gains does not address all static nonlinearities.

Pending: read the complete finite-slope dynamic-class definition around Eq. (24), and reconcile the precise stability conventions with CHT16. The v3 PDF was accessible through the web reader; direct download returned HTTP 406. No technical proof certification is claimed.

## July 2026 claimed disproof: K26

Andrey Kharitenko, *Existence of stable Lur'e systems for which the O'Shea-Zames-Falb stability test fails*, [arXiv:2607.23599](https://arxiv.org/abs/2607.23599), [v1 full text](https://arxiv.org/html/2607.23599v1), July 26, 2026; only v1 in the inspected history.

Read the discrete-time signal model, Theorems 1–3, the copositive characterization, finite-horizon Example 1, Lemma 4, Corollary 1, infinite-horizon Example 2 and §5. The counterexample uses G(z) = (1.1z + 0.6)/(z² + 1.8z + 0.9) and slope bound two, with a shift-register certificate. The complete main-body formulation and conclusion are discrete-time. The finite-horizon example alone is not the infinite-horizon counterexample. Appendix certificate matrices were not independently rerun.

The title and abstract's general disproof wording must not be used to assert a continuous-time theorem. Conversely, a possible transfer from discrete time must not be ruled out without investigation. No transfer theorem was located in the inspected main body or searches S374–S376. Whether such a bridge settles the selected continuous-time formulation remains an explicit admission question. The unrestricted Carrasco conjecture must not simply be labelled open.

## Further primary sources and limits

- Su, Seiler, Carrasco and Khong, *On the necessity and sufficiency of discrete-time O'Shea–Zames–Falb multipliers*, Automatica 150 (2023), 110872, DOI 10.1016/j.automatica.2023.110872: [author PDF](https://personalpages.manchester.ac.uk/staff/joaquin.carrasco/Su_2023), dated December 8, 2022. The introduction and concluding continuous-time open-status paragraph were read. This differs from the sole December 2021 [arXiv version](https://arxiv.org/abs/2112.07456); do not mix their numbering. Complete discrete-time conjecture/model comparison remains due. This team overlaps both earlier teams, so it is not an additional disjoint corroboration source.
- Heath and Carrasco, *Phase Limitations of Multipliers for Nonlinearities With Monotone Bounds*: [author PDF](https://pure.bangor.ac.uk/ws/portalfiles/portal/75375265/TAC_24_third_submission-10.pdf). The introduction retains a necessity conjecture. Publication year/version identity and full relevant theorem remain unverified; no partial-result conclusion is adopted from the introduction alone.
- Wang, Carrasco and Heath, *Phase limitations of Zames-Falb multipliers*: [arXiv:1704.02484](https://arxiv.org/abs/1704.02484). Search leads describe a correction to a phase limitation for signed multipliers and simulated instability. Read the full definitions and theorem before comparing these claims with necessity. This is currently a lead, not an admission source.
- Kharitenko and Scherer, *On the exactness of a stability test for discrete-time Lur'e systems with slope-restricted nonlinearities*, IEEE Transactions on Automatic Control 69(7) (2024), 4851–4858, was identified through K26's reference list. Full-text/model inspection remains due, including whether any continuous-time transfer is relevant.

## Duplicate and search checkpoint

Searches for Carrasco, Zames, Falb, absolute stability and Lur'e across the baseline inventory, active pages, metadata and candidate records found no matches. Three nearby complete statements were read: catalogue 330 (generic static output feedback), 319 (Belgian chocolate threshold) and the pending arbitrary-switching stability draft. Their targets concern, respectively, existence of a constant controller, stable polynomial design and algorithmic decidability for rational matrix products. These comparisons are provisional until this lead has an exact fingerprint.

All 24 actual queries S371–S376 are saved in [search-log.json](search-log.json), including unrestricted resolution searches, literal recent years, correction/withdrawal searches and discrete/continuous scope searches. S375's generic O'Shea query returned substantial unrelated noise; it is not counted as positive status evidence. There are now 1,694 distinct search identifiers. A49 has not been performed. Counts remain 47 accepted, 40 integrated/published, seven pending accepted drafts, five formal holds, 52 formal records and 340 active catalogue entries.
