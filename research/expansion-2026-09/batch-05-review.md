# Expansion batch 5 audit

Target: private MColbrook/AIM, upstream aa3087c2cf59db1e30215f90301f356385ce163c. Review date: **2026-09-18**. The user authorizes direct pushes to main; no PR is required.

## Admission and refresh

Ten accepted additions are integrated and published on main as 341–350. Each has a full scholarly formulation, independently authored status corroboration, comparisons with potential resolutions, duplicate screening and a separated adversarial self-pass. No independent agent or human review is claimed.

| ID | Topic | Primary section |
| --- | --- | --- |
| 341 | Sharp matroid secretary guarantee | stochastic3 |
| 342 | Optimal asymptotic binary-code rate | inverse3 |
| 343 | Stability under arbitrary switching | inverse2 |
| 344 | List edge-colouring | stochastic3 |
| 345 | Chemostat exclusion with unequal removal | stochastic3 |
| 346 | Tuza triangle packing–covering | applied |
| 347 | Binary skew-symmetric broadcast capacity | inverse3 |
| 348 | Reed chromatic-number bound | applied |
| 349 | Polynomial local-stability decidability | inverse2 |
| 350 | Unit-job prescribed-machine scheduling hardness | stochastic3 |

The immediate publication searches are R5-1 through R5-27 in the [actual search log](search-log.json), following A42–A51 research reviews. All ten complete drafts were reread. Primary version records for the September 17 linear-matroid result and September 10 path-complete stability algorithm still match the versions already reviewed. Individual ledgers retain exact models, theorem locations and access limits.

The refresh added three specific comparisons:

- Andrew Salmon's [September 3 preprint](https://arxiv.org/html/2609.03736v1), §1, definitions (1.2)–(1.7) and full Theorem 1.1, computes a half-rate point of the Delsarte relaxation. It explicitly distinguishes that exponent from the rate of realizable codes. The coding entry now includes this distinction; no proof certification is claimed.
- Zhang–Lu–Miao–Wang's [August 20 preprint](https://arxiv.org/html/2608.19852v1), §1, Definition 1.2 and full Theorem 1.3, assumes bounded treewidth and proves a maximum-degree-plus-one list bound. Even its ordinary-colouring specialization does not give the exact chromatic index for arbitrary loopless multigraphs.
- Salah Alsahafi's [2022 UTS thesis](https://opus.lib.uts.edu.au/bitstream/10453/164302/2/02whole.pdf), §1.1.4, complete Proposition 1.2, pp. 6–7, retains additional response-ratio separation conditions in its chemostat convergence statement. The search excerpt had omitted them. Direct PDF retrieval succeeded after the web-reader route returned 429; other chapters were not fully reviewed.

The correction described in Calbet–Freschi's [July 2026 publisher abstract](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i3p1) concerns Tuza's saturation-number conjecture, as its explicit definition confirms. This is an abstract/model screen, not a complete theorem or proof review. The mortality-induced chemostat-cycle title and indexed abstract concern an allelopathic toxin; that full text was not retrieved and is not admission evidence. Other fresh hits concern previously reviewed restricted classes, different access models, relaxation bounds or namesake problems. No new materially matching unresolved resolution claim was located.

The scheduling addition preserves unit processing lengths, prescribed machine assignments, a varying machine count and a fixed positive power of the number of jobs. The July 2026 constant-factor and conditional polylogarithmic hardness theorems do not establish that target. Its [ledger](candidates/unit-job-unique-machine-hardness.json) records the original paper's different published/preprint conjecture numbers, all six scope comparisons and the A51 self-review.

SSH fetch found HEAD equal to origin/main at the commit above. Connected GitHub metadata confirms the private destination, main default and push permission. A paginated branch search returned only main and the open-PR search returned no results. The established complete baseline, all 340 prior active entries, ten pending statements and nearest-family comparisons supplied the duplicate check. No new upstream addition or equivalent accepted target was found.

## Validation

- Catalogue write/check passed for 350 unique entries, headings, metadata, required sections, math delimiters, local links and generated README freshness. Whitespace checks passed after removing two trailing spaces left by draft-status replacement.
- All original 300 problem pages match baseline a602073 byte-for-byte. All 340 previously published pages match upstream aa3087c byte-for-byte. Every prior metadata row, date and file prefix is unchanged.
- Counts reconcile: 55 formal records, 50 accepted and integrated, five holds, no pending accepted drafts, and 1,808 distinct actual search identifiers. This batch spans four primary sections; accepted additions cover all twelve.
- All 201 mathematical expressions in the ten public pages passed strict KaTeX 0.16.22. Public and archived-draft expressions match exactly. All nine previously accepted drafts retain exactly their reviewed mathematical expressions after integration. The new scheduling draft received a full-page visual check; the final coding page received another full-page browser inspection after its source comparison was expanded. Formulae, text and bibliography fit without clipping. Rendering assets remain outside the repository.
- All 717 checked relative links across the catalogue index, updated research navigation, ten new public pages and draft archives resolve. Public pages have permanent headings and contain no pending-integration or unassigned-ID language.
- Of 88 bibliography targets, 69 returned matching content by direct GET. Seven restricted DOI targets have matching author/institutional alternatives on the same pages that succeeded by direct GET. The other twelve have checked web-reader routes; for two arXiv records, canonical PDFs explicitly show the exact cited version after version-specific cache misses. The [link report](batch-05-link-check.json) retains transport failures, alternatives and the distinction between access and proof review.
- Catalogue machinery is unchanged. The earlier infrastructure tests cover that machinery; no new infrastructure tests were needed for this content batch.

## Publication

Validation passed. The final upstream fetch still matched the reviewed target. Content commit [1240ebf](https://github.com/MColbrook/AIM/commit/1240ebfbdae361901472a7d33ca0baa7073c51cb) was pushed directly to main on September 18, 2026. The normal fast-forward push succeeded, and a separate `git ls-remote --heads origin main` returned the exact full content commit. All fifty additions are now published. No PR was opened.

## Counts and limits

Fifty accepted, integrated and published additions; 350 active entries; 55 formal candidate records and five holds. The minimum requires 150 more additions; the working target requires 200. The expansion covers all twelve primary sections and excludes further numerical linear algebra.

The original 300 historical review dates are preserved. Literature searches and structural checks do not certify mathematical truth or exhaustive absence of later resolutions.
