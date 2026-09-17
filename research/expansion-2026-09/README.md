# September 2026 expansion research

The requested expansion is 200–300 accepted problems (target 250). **Seventeen additions have passed the formulation, evidence, duplicate and adversarial-review gates.** The first batch has passed its prepublication resolution and upstream duplicate refresh and is published on `main` as entries 301–310. The active catalogue is now 310. These research records do not count separately from their linked problem pages.

- [Progress and reading coverage](progress.json): exact counts, completed baseline reading, and next actions.
- [Baseline inventory](baseline-inventory.json): complete mechanical extraction of all 300 statements, references, metadata, and page hashes at `a602073d986b7f5ce57b1aa0db1687d1bd87761d`. Extraction alone does not constitute semantic review or status revalidation.
- [Candidate records](candidates/): accepted drafts and held leads, with source locators, actual searches and scope comparisons.
- [Search log](search-log.json): searches actually run on 2026-09-17.
- [Source map](source-map.md), [exclusions](exclusions.md), and [infrastructure audit](infrastructure-audit.md).

The original 300 pages and their historical review dates are preserved. Candidate IDs are descriptive research keys; permanent IDs 301–310 were assigned centrally after acceptance. The first batch was pushed directly to `main` in commit `ce50f8b` on 2026-09-17. The user authorized direct pushes; no PR is required. Accepted additions cover log-rank, Černý, planted-clique detection, Unique Games, balanced Gaussian simplex noise stability, convex Dirichlet spectral determination, three-dimensional Edwards–Anderson order, inhomogeneous Landau–Coulomb continuation, the Li–Li multiple-unicast conjecture and Gaussian broadcast feedback capacity. Morrey’s planar conjecture and Yang–Mills existence and mass gap remain held because matching proof claims have not been adjudicated. The ten handoff seeds are now investigated; substantial discovery beyond them remains necessary.

The FIFO queue-feedback candidate is held after an adversarial model check; see [exclusions](exclusions.md) and the [discovery queue](discovery-queue.md).

The Gaussian multiple-access feedback candidate is also held on an older conflicting claim; see its candidate record.

The carrying-simplex interior smoothness question has passed a separate adversarial self-pass and is an accepted draft for the next batch. It is not yet an active or published entry. See its [evidence ledger](candidates/carrying-simplex-interior.json).

The exact three-processor unit-job scheduling question has also passed formulation, theorem-scope and separate adversarial review. Its [accepted draft record](candidates/three-processor-unit-scheduling.json) awaits the next batch.

The entanglement-assisted Lovász equality passed a separate adversarial self-pass, including the corrected March 2026 restricted-capacity result. Its [accepted draft record](candidates/entanglement-assisted-lovasz.json) awaits the next batch. There are now seven accepted drafts beyond the ten published entries.

Fixed-disorder quantum diffusion passed the separate A15 adversarial self-pass. Its [accepted draft record](candidates/anderson-fixed-disorder-diffusion.json) distinguishes disorder-averaged linear growth from spectral delocalization, finite-time estimates and vanishing-disorder scaling limits. It awaits the next batch.

The reversible mass-action reaction–diffusion continuation question passed the separate A16 adversarial self-pass. Its [accepted draft record](candidates/reversible-reaction-classical-continuation.json) distinguishes arbitrary-order deterministic classical continuation from renormalized existence, restricted-growth or diffusion theorems, transport-noise regularization and generic mass-control blowup. All twelve primary sections now have at least one accepted addition; substantial further work remains toward the minimum of 200.

Splay-tree dynamic optimality and classical learning-parity-with-noise hardness passed the separate A17 and A18 self-passes. Their accepted records distinguish initialization conventions, conditional competitive bounds and heap models, and fixed-noise random examples, preprocessing, sparsity and quantum inputs: [splay](candidates/splay-dynamic-optimality.json), [LPN](candidates/learning-parity-noise.json). Both await the next batch; 183 further accepted additions are needed to reach the minimum.
