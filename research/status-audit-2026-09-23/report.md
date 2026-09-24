# Solution-status audit — 23 September 2026

Repository baseline: `a1c0794ee946eea5c145c1aad63610554c4380ff`.

This report retains assessments for **493 active problem statements**. Entries subsequently removed from the repository have also been removed from these audit records. Seven retained entries have older or otherwise unverified full-solution claims. These categories describe evidence, not independent certification of mathematical correctness.

## Other full-solution claims located

These are included because the request explicitly includes announced solutions. **They are not established resolutions in this audit.** Later literature may continue to treat the problem as open.

| ID | Problem | Claim | Qualification |
| --- | --- | --- | --- |
| 028 | Hadamard conjecture | Sopin, [EasyChair 8250](https://easychair.org/publications/preprint/tkTH), 2022. | Claims a descent from order 4nm to 4n and all orders. Acceptance of the argument was not established. |
| 034 | NPT bound entanglement | Sperling–Vogel, [2009, v2](https://arxiv.org/abs/0910.0744v2). | Claims every NPT state is distillable. Revision acknowledges criticism of the earlier proof; no accepted general resolution established. |
| 056 | One-pattern smooth obstacle uniqueness | Ramm, [Applied Mathematics Letters 58 (2016), Theorem 1](https://math.k-state.edu/~ramm/papers/661j.pdf). | Explicit unrestricted claim, but the later [Colton–Kress survey](https://num.math.uni-goettingen.de/kress/looking-back.pdf) still identifies the general problem as open. |
| 073 | Unforced periodic 3D Navier–Stokes regularity | Pavesi, [Zenodo v3, 4 July 2026](https://zenodo.org/records/21194906). | The abstract explicitly claims all smooth divergence-free initial data on the torus. No independent validation established. |
| 093 | Planar self-avoiding-walk exponent | Hueter, [2001, v2](https://arxiv.org/abs/math/0108077v2). | Claims the RMS exponent 3/4; already acknowledged in the repository, while later literature retains the problem. |
| 095 | Strongly polynomial simplex pivot rule | Yan–Li–Guo, [2020; current v14, 2022](https://arxiv.org/abs/2006.11466v14). | Claims a strongly polynomial algorithm and at most n pivots. This audit did not validate auxiliary arithmetic costs or all the catalogue's ordinary-pivot requirements. |
| 276 | Weakly reversible mass-action persistence | August–Barahona, [2010 proceedings paper](https://doi.org/10.3182/20100707-3-BE-2012.0018). | Claims general persistence, but later primary literature still treats it as conjectural. Independent confirmation was not established. |

For 076, Aksman's [25 August Zenodo posting](https://zenodo.org/records/22098919) makes another global-regularity claim. Its PDF could not be retrieved for an exact domain check, so the precise match above rests on Pavesi's explicit torus statement. Pavesi's earlier [spectral-confinement posting](https://zenodo.org/records/20812093) is conditional and does not settle ideal MHD problem 081.

## Disputed or incomplete claims

| ID | Claim | Why it should not be reported as a settlement |
| --- | --- | --- |
| 054 | Ramm's [2010 backscattering uniqueness claim](https://arxiv.org/abs/1007.2918). | [Rakesh–Uhlmann, p.8](https://arxiv.org/pdf/1307.0877), explicitly identify a gap: the proof confuses analytic scattering solutions with CGO solutions. |
| 294 | Trahtman's [Černý proof claims](https://arxiv.org/abs/1202.4626). | [Volkov's survey](https://arxiv.org/abs/2508.15655), footnote 1, records Trahtman's acknowledgement of an error in February 2024. |
| 296 | Vega's [Hallelujah algorithm paper](https://www.tandfonline.com/doi/full/10.1080/17445760.2026.2660724), and DeSantis's [2019 informal-proof posting](https://lists.w3.org/Archives/Public/public-bitcoin/2019Oct/0001.html). | A graph-dependent ratio strictly below 2 does not alone contradict UGC's uniform 2-epsilon barrier. The mailing-list announcement supplies proposed primitives, not a complete proof. |

## Withdrawn or corrected full-proof headlines

- **001, Pólya:** [He, v2](https://arxiv.org/abs/1411.1135v2), withdrawn because of a crucial error.
- **067, standard-map entropy:** [Knill, revised record](https://arxiv.org/abs/math/9908014v2), explicitly deletes the incorrect 1999 proof.
- **131, Saari:** [Tibboel, v5](https://arxiv.org/abs/2212.09718v5), withdrawn because of a proof error.
- **191, planar spin glass:** [Itoi, v6 erratum](https://arxiv.org/html/2012.11801v6), says the infinite-volume conclusion was not proved.
- **210, Fourier extension:** [Sawyer's current record](https://arxiv.org/abs/2411.18457v8) replaces the full-proof claim with a narrower testing-conditions paper.

## Important scope exclusions

- **025:** scalar Crouzeix is not complete Crouzeix. The [Palomar operator-theory entry](https://palomar-registry.org/entry?id=PALOMAR-2026-09-01-000002&version=1) concerns the 1+sqrt(2) polynomial bound, not complete constant 2.
- **028:** the [Palomar Hadamard entry](https://palomar-registry.org/entry?id=PALOMAR-2026-08-31-000001&version=1) constructs particular orders, not every multiple of four.
- **073:** the [OpenAI announcement](https://openai.com/index/navier-stokes-solution/) concerns forced Navier–Stokes blowup. It does not settle the unforced formulation retained here.
- **129:** the [new Cartan–Hadamard result](https://arxiv.org/abs/2609.20517) covers dimensions 3–9, leaving the catalogue's dimensions >=10.
- **149:** [Li–Sun, Theorem 1.2](https://arxiv.org/html/1910.05939v1) concerns a prepared equation with modified nonlinearity, not the required global invariant graph for the original semigroup. The [authors' 2026 conference abstract](https://aimsconference.org/AIMS-Conference/conf-reg2026/ss/detail1.php?abs_no=854) still calls the original problem open.
- **203:** [critical boson-star uniqueness](https://arxiv.org/abs/2609.23771) does not give uniqueness for every massive subcritical state.
- **333:** [the matroid-secretary announcement](https://arxiv.org/abs/2609.14555) gives a constant guarantee; the repository asks for the sharper 1/e guarantee for all abstract matroids.

Further scope decisions, including different dimensions, equations, stochastic models and parameter endpoints, are in `decisions.json` and the complete ledger.


## Coverage and limits

Every active entry received a broad problem-specific web search and a second search scoped to arXiv, Zenodo, GitHub and Palomar. Potential matches were compared with the mathematical scope of the repository statement and followed to primary abstracts, theorem statements, version histories or correction notices where available. Publisher sites, author pages, ECCC, proceedings and other repositories were also used. Palomar coverage included screening its 200 recent displayed registrations and opening relevant registrations; this was not an exhaustive export of every historical Palomar record. Search-engine indexing of GitHub and Zenodo is incomplete.

The audit establishes that the listed announcements exist and identifies their stated scope. It does not referee all proofs, rerun computer-assisted certificates, or prove that every unflagged problem is open. “No matching announcement located” in the ledger is a search outcome, not a mathematical status theorem. Some direct document fetches failed; material limitations are noted above.

The remaining entries retain their catalogue statuses.

Files:
- `ledger.md`: one row for each of the 493 active problems.
- `ledger.json`: machine-readable coverage and assessments.
- `decisions.json`: 68 detailed lead decisions, with primary URLs where available.
- `baseline.json`: original statements and status at the audited commit.
- `source-filtered-screen.json`: 493 individual second-pass search records.
- `S001.json`–`S012.json`, `screen-050-185.json`, `screen-186-501.json`: first-pass search evidence.
