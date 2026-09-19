# Expansion batch 6 audit

Target: private MColbrook/AIM, upstream `73c787d1add623ce7ede59766e018b51ea4e1a1e`. Review date: **2026-09-19**. The user authorizes direct pushes to main; no PR is required.

## Admission and refresh

Ten accepted additions are integrated and published on main as 351–360. Each has a scholarly formulation, independently authored corroboration, resolution-scope comparisons, duplicate screening and a separated adversarial self-pass. No independent agent or human review is claimed.

| ID | Topic | Primary section |
| --- | --- | --- |
| 351 | Modern integer 3SUM hardness | operators |
| 352 | Modified integer round-up for cutting stock | stochastic3 |
| 353 | Entanglement-of-purification additivity | spectral3 |
| 354 | Private PAC VC/log-star sample cost | applied |
| 355 | Sharp strong edge-colouring bound | inverse3 |
| 356 | Subset-sum support and concentration | applied |
| 357 | Near-linear planar halving-line count | inverse3 |
| 358 | Proper univariate Gaussian-mixture learning | applied |
| 359 | Brownian Fleming–Viot non-explosion | stochastic2 |
| 360 | The ball as least densely packable convex solid | continuum3 |

The immediate publication queries are R6-1 through R6-21 in the [actual search log](search-log.json), following A53–A62. All ten complete drafts were reread. Primary arXiv histories for the July 19 strong-colouring, August 28 Rényi-purification and September 1 entropy-comparison preprints still list the reviewed versions. Existing scope comparisons remain applicable.

Two additional full-statement checks were added to the evidence records:

- Kopelowitz–Porat, [*The Strong 3SUM-INDEXING Conjecture is False*](https://arxiv.org/html/1907.11206v1), Theorems 1.1 and 2.1–2.2, §2 and footnote 1: the space/query-time result explicitly permits unlimited preprocessing. Entry 351 counts total computation, including preprocessing.
- Villemonais, [*Uniform tightness for time-inhomogeneous particle systems and for conditional distributions of time-inhomogeneous diffusion processes*](https://arxiv.org/pdf/1203.4825v1), §2, Hypotheses 1–2 and complete Theorem 1, internal pp. 4–6: the non-explosion criterion requires a twice continuously differentiable boundary-distance function with bounded derivatives near the boundary. Entry 359 imposes no boundary regularity.

The packing review also inspected the model, full theorem and proof of Kuchel's [2025 complementary-body paper](https://arxiv.org/pdf/2508.11633v1), §§3.3, 3.6 and 4.1–4.3. Its fixed-FCC spherical-sector identity does not optimize congruent packings of an arbitrary convex solid. The paper's formulas were not independently certified. The packing entry preserves reflections, the weak inequality and the exact scope of the symmetric/local and directional partial results.

Fresh searches otherwise recovered previously reviewed restricted classes, indexing models, random-packing observables, or different notions of learning. Discovery pages, AI reviews, snippets and inaccessible papers were not used as admission evidence. The halving-line July 2026 small-set lower-bound preprint remains an explicitly recorded access limitation.

SSH fetch found HEAD equal to origin/main at the commit above. Connected GitHub metadata confirms the private repository, main default and push permission. The complete paginated branch search returned only main; the open-PR search was empty. The established complete baseline, all 350 current active entries, ten pending statements and their nearest-family comparisons supplied the duplicate check. No new upstream addition or equivalent accepted target was found.

## Validation

- Catalogue write/check passed for 360 unique entries, headings, metadata, required sections, math delimiters, local links and generated README freshness. Git whitespace checks passed.
- All 350 previously published pages match upstream byte-for-byte, including the original 300. Every previous metadata row, date and path is unchanged; original JSON escaping was preserved.
- Counts reconcile: 66 formal records, 60 accepted and integrated additions, six holds, no pending accepted drafts, and 2,269 distinct actual search identifiers.
- All 249 mathematical expressions in the ten public pages passed strict KaTeX. Public and archived-draft expressions match exactly. All nine previously accepted drafts retain their reviewed expressions. Their full-page visual checks are recorded in the individual ledgers; the final numbered packing page received a full-page browser inspection after integration, with no failed or clipped mathematics.
- All 520 checked relative links across the index, updated navigation, ten new pages, draft archives and batch audit resolve. The catalogue validator also checks the complete active collection. Public pages have permanent headings and no pending-ID wording.
- Of 74 external targets on the ten pages, 69 returned HTTP 200 by direct GET. Three restricted publisher DOI URLs have successful primary alternatives on the same pages. The strong-colouring original scan succeeded through the web reader. The previously inspected halving-line original scan now refuses access; its two explicit scholarly restatements remain accessible. The [link report](batch-06-link-check.json) preserves every restriction and alternative.
- Catalogue machinery is unchanged; no new infrastructure tests were needed for this content batch.

## Publication

Validation passed, and the final upstream fetch still matched the reviewed target. Content commit [a79a6d8](https://github.com/MColbrook/AIM/commit/a79a6d875675959d143bcf4bc7396e1e2a61d1ee) was pushed directly to main on September 19, 2026. The normal fast-forward push succeeded; a separate `git ls-remote --heads origin main` returned the exact full content commit. All sixty additions are now published. No PR was opened.

## Counts and limits

Sixty accepted, integrated and published additions; 360 active entries; 66 formal candidate records and six holds. No accepted drafts remain pending integration. The minimum requires 140 more additions and the working target requires 190. This batch spans seven primary sections, and the accepted additions cover all twelve. No further numerical linear algebra was added.

The original 300 historical review dates are preserved. Literature searches and structural checks do not certify mathematical truth or exhaustive absence of later resolutions.
