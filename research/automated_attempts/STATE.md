---
schema_version: 1
revision: 5
current_problem: "001"
phase: research
status: open
sol_attempts: 4
astra_reviews: 1
campaign_number: 1
current_bottleneck: "The first untreated full-chain index is k=3. Cartesian products of known Polya domains are now covered at every index, but arbitrary non-product domains remain. Neumann mu_3 needs a hierarchical tree-fold center theorem plus equal-third mass displacement; planar Dirichlet lambda_3 needs k=3-specific lower-side stability."
strongest_verified_result: "Beyond the known k=1,2 chain and nodal band, Polya's inequalities are now proved to be closed under Cartesian products, independently on each boundary side; finite products of balls and intervals satisfy the full chain. Exact method obstructions eliminate the shared global planar stability constant and the triangular constant-frame Neumann fold."
strongest_conjectural_lead: "After Sol 5 consolidation, attack the hierarchical Neumann tree fold through its exact 3d moments and equal-third mass displacement, or prove a genuinely non-product Fourier compensation estimate. Retain only specialized one-sided stability for planar Dirichlet k=3."
next_actions:
  - "Sol 5: adversarially consolidate the product theorem and the two third-mode method obstructions, then prepare the scheduled Astra checkpoint."
  - "Neumann return: formulate a hierarchical two-stage tree fold, then test its 3d moment map separately from equal-third mass displacement; do not reuse the triangular Voronoi constant-frame ansatz."
  - "Dirichlet return: optimize a k=3-specific one-sided stability coefficient; do not continue extracting the shared global C_2."
  - "Fourier return: seek a genuinely non-product spatial compensation estimate; half-Riesz cannot fail on a base already satisfying Polya."
priorities:
  - "Adversarial consolidation is next under Astra's four-attempt allocation."
  - "Cartesian products are a verified arbitrary-index domain class, not a solution for general domains."
  - "Neumann third mode remains open, but its direct triangular Voronoi fold is exhausted; retain the hierarchical tree variant."
  - "Only specialized lower-side third-mode stability remains viable on the planar Dirichlet route."
  - "Geometric half-Riesz and spatial Fourier compensation remain independent alternatives."
  - "Preserve both boundary conditions, all dimensions, and the full all-index target."
failed_or_exhausted_routes:
  - "Sol 1: the equal-k-ball Dirichlet lower bound is false at d=2,k=3; the exact unit-disk trial space has maximal quotient 16."
  - "Sol 1: Courant gives r<=k, not r>=k; connected thin-neck dumbbells exclude a uniform improvement of the sharp lambda_2 constant."
  - "Sol 2: the shared global C_2 in de Villeroché Theorem 1.1 can never cover the planar k=3 interval: C_2>sqrt(2)/4 forces eta<2^-18, while 12-2*j_(0,1)^2>22/51."
  - "Sol 3: three noncollinear Voronoi-centered Weinberger fields cannot be glued by nonsingular constant frames: face matching forces a product of three reflections to equal I, contradicting determinant -1. Fixed-domain tree adjacencies and other ansatzes remain open."
  - "Sol 4: half-Riesz violation over a Polya-valid base is impossible by the positive Abel identity; cylinder search only propagates a genuine base violation. Product closure is the positive replacement."
  - "The positive-part exponent-1/2 stability theorem cannot be used for the required lower-side estimate."
  - "Sharp heat or fixed-positive-order Riesz bounds alone do not imply pointwise counting."
  - "Adding planar Yang and an actual square spectral tail does not force half-Riesz for an abstract sequence."
  - "Differentiating Riesz inequalities, ignoring epsilon-dependent thresholds, or substituting positive-order asymptotics for counting are invalid."
  - "Fourier-ball compression cannot dominate a nonzero Dirichlet spectral projection."
verification_needed:
  - "Astra should verify Sol 2's use of one C_2 shared over k and the exact disk substitutions proving the global-constant obstruction."
  - "Astra should verify Sol 3's Sobolev trace-spanning step, reflection product order, and fixed-domain scope of the odd-cycle obstruction."
  - "Astra should verify Sol 4's tensor-product endpoint conventions, beta-function constant identity, Lipschitz product scope, and half-Riesz localization bound."
  - "No complete candidate exists; establish a k=3-specific lower-side estimate or a Neumann mu_3 construction."
  - "External literature statements remain source-audited, not fully independently reconstructed."
  - "Any complete candidate requires two separate Astra invocations primarily devoted to adversarial verification."
candidate_proof: null
successful_principal_verification_reviews: 0
current_campaign:
  id: "001-campaign-1"
  decision: continue
  sol_attempts_completed: 4
  astra_reviews_completed: 1
  campaigns_completed_for_problem: 0
  nominal_sol_budget: 16
  nominal_astra_budget: 4
  next_checkpoint_after_new_sol_attempts: 4
  next_checkpoint_at_sol_attempt: 5
  next_block_allocation: "Neumann third-mode construction; geometric half-Riesz alternative; adversarial consolidation. Planar Dirichlet return must use a k=3-specific lower-side constant."
  strongest_result_class: "Known low-index results, exact Cartesian-product closure yielding new covered domain classes, and method obstructions; no arbitrary-domain proof or counterexample claimed."
  transition_rule: "Only Astra selects from the latest synchronized unresolved queue; prefer unstarted work before routine deferred revisits and prevent starvation."
last_sol_run: "research/automated_attempts/001/attempts/2026-09-08_1206_sol.md"
last_astra_run: "2026-09-08T08:34:00Z"
last_astra_review: "research/automated_attempts/001/reviews/2026-09-08_0834_astra.md"
last_queue_sync: "2026-09-08T12:06:00Z"
queue_snapshot_commit: "ba319033badbcb53178fc2bac312f0669e3a6a73"
queue_manifest_initial_commit: "05e95237c571731534faaee9d4aa29865b5962b1"
current_problem_count_observed: 100
newly_discovered_problems: []
queue_integrity_issues: []
new_problem_ids_this_run: []
queue_integrity_issue: null
run_history:
  - "revision 1: Sol attempt 1 established the full k=1,2 chain, a Dirichlet nodal band, and a rigorous obstruction to the equal-ball extension."
  - "revision 2: Astra senior review 1 incorporated concurrent Sol 1, confirmed its exact claims, derived cylinder and scalar-obstruction results, and redirected the next block toward quantitative third-mode stability."
  - "revision 3: Sol attempt 2 proved that the shared global stability constant cannot cover planar k=3, independently of hidden-constant bookkeeping."
  - "revision 4: Sol attempt 3 formulated the exact mu_3 moment reduction and proved an odd-cycle H^1 gluing obstruction for the direct noncollinear three-center Voronoi fold."
  - "revision 5: Sol attempt 4 proved sharp Cartesian-product closure for each Polya counting side, yielding full-chain ball and interval products, and localized any half-Riesz violation to a base counting violation."
queue_sync_notes:
  - "Every current problem file agrees with the persistent queue in this observed snapshot; no additions, deletions, duplicate identifiers, or renames were found."
  - "Existing research/queued statuses are preserved as legacy active/unstarted aliases."
  - "scripts/catalogue.py has fixed initial ranges; it remains read-only and must never cap discovery."
  - "The observed count 100 is a snapshot, never a maximum or contiguity assumption."
---
