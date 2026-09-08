---
schema_version: 1
revision: 6
current_problem: "001"
phase: research
status: open
sol_attempts: 4
astra_reviews: 2
campaign_number: 1
current_bottleneck: "The first untreated full-chain index is k=3. For planar Neumann mu_3, prove or refute a zero of the continuous reduced four-moment map for two global folds with four-sheet IMAGE overlap e<=V/15 (or the sharper quartic threshold). The mean center is uniquely solved. Planar Dirichlet needs k=3-specific lower-side stability."
strongest_verified_result: "Known low-index chain, nodal band, exact method obstructions and standard product closure are confirmed. Astra 2 proves a conditional planar mu_3 bound using two continuous folds, an exact one-fifteenth overlap budget, and a unique continuous mean center; existence of the remaining four-moment zero is unproved."
strongest_conjectural_lead: "A degree or continuation theorem for the reduced R^4 moment map on its low-overlap parameter subset. First independently verify the new conditional lemma; neither equal dimension nor a numerical zero proves the required universal existence."
next_actions:
  - "Sol 5: adversarially reconstruct the new fold/overlap theorem, its H^1 and multiplicity issues, both density rearrangements, quartic algebra, and unique mean-center continuity; run the exact Fraction verifier."
  - "Sol 6: attack a zero of the reduced four-moment map, handling escaping, parallel and coincident folds and the overlap-boundary condition. Stress-test disks, rectangles and three-lobe limits."
  - "Sol 7: close a concrete existence lemma; otherwise rigorously obstruct the low-overlap ansatz or develop a spatially sensitive quotient improvement."
  - "Sol 8: if Neumann has no credible route, attack restricted planar Dirichlet lower-side stability; otherwise adversarially consolidate. Astra checkpoint after Sol 8 or immediately on a complete candidate."
priorities:
  - "Verify the conditional two-global-fold Neumann theorem independently before using it."
  - "Mean cancellation is solved uniquely and continuously; four signed moments plus simultaneous overlap control remain open."
  - "Correct binary-construction versus geometric-adjacency confusion; only globally continuous or explicitly trace-matched folds are admissible."
  - "Product closure is standard rediscovered machinery, not a novel domain-class breakthrough; do not allocate another attempt to it."
  - "Retain specialized Dirichlet lower-side k=3 stability and genuinely non-product Fourier compensation as alternatives."
  - "Preserve both boundary conditions, all dimensions, the full all-index target, and fair future campaigns from the current dynamic queue."
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
  - "Astra 2: a hierarchical binary construction need not have an acyclic interface graph; one-child transverse affine folding generally violates trace matching. Special fixed-domain and parallel-cut cases remain."
  - "Astra 2: standard product closure is confirmed but its novelty is downgraded; stronger known product results already cover the advertised classes."
verification_needed:
  - "Independently verify artifacts/2026-09-08_1310_fold_overlap.md, especially the pushforward overlap convention, two capacity rearrangements, quartic threshold, and strict-convexity/L^1-continuity proof for the mean center."
  - "Prove or refute a zero of the reduced four-moment map with e/V<=1/15 or the exact quartic threshold; no compactification or nonzero degree is established."
  - "Sol 2 global-constant obstruction, Sol 3 trace/holonomy theorem and Sol 4 endpoint-safe product/Abel reductions passed Astra 2; the inherited hierarchy escape and product novelty did not."
  - "External literature proofs and the July 2026 higher-dimensional Neumann-ball computer-assisted certificates remain external, not independently reconstructed."
  - "No complete candidate exists. Any complete candidate requires verification phase and two separate Astra invocations principally devoted to adversarial verification."
candidate_proof: null
successful_principal_verification_reviews: 0
current_campaign:
  id: "001-campaign-1"
  decision: continue
  sol_attempts_completed: 4
  astra_reviews_completed: 2
  campaigns_completed_for_problem: 0
  nominal_sol_budget: 16
  nominal_astra_budget: 4
  next_checkpoint_after_new_sol_attempts: 4
  next_checkpoint_at_sol_attempt: 8
  next_block_allocation: "Sol 5 independently verifies the fold-overlap lemma; Sol 6 attacks the reduced moment map; Sol 7 closes or obstructs that route; Sol 8 uses specialized Dirichlet stability if needed, otherwise consolidates."
  strongest_result_class: "Conditional variational lemma and continuous mean-center reduction, known low-index results, standard product reconstruction and method obstructions. No new unconditional generic-domain theorem or complete proof."
  transition_rule: "Only Astra selects from the latest synchronized unresolved queue; prefer unstarted work before routine deferred revisits and prevent starvation."
last_sol_run: "research/automated_attempts/001/attempts/2026-09-08_1206_sol.md"
last_astra_run: "2026-09-08T13:14:00Z"
last_astra_review: "research/automated_attempts/001/reviews/2026-09-08_1314_astra.md"
last_queue_sync: "2026-09-08T13:14:00Z"
queue_snapshot_commit: "547378abf3ebdb35c2b36da09b474afd39b9594d"
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
  - "revision 6: Astra senior review 2 confirmed Sol 2–4 mathematics, rejected automatic hierarchical tree adjacency, downgraded product novelty, and derived an exact conditional planar mu_3 fold-overlap theorem with unique continuous mean centering; four signed moments and low overlap remain open."
queue_sync_notes:
  - "Every current problem file agrees with the persistent queue in this observed snapshot; no additions, deletions, duplicate identifiers, or renames were found."
  - "Existing research/queued statuses are preserved as legacy active/unstarted aliases."
  - "scripts/catalogue.py has fixed initial ranges; it remains read-only and must never cap discovery."
  - "The observed count 100 is a snapshot, never a maximum or contiguity assumption."
---
