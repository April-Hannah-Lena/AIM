---
schema_version: 1
revision: 2
current_problem: "001"
phase: research
status: open
sol_attempts: 1
astra_reviews: 1
campaign_number: 1
current_bottleneck: "First untreated full-chain index k=3: quantify lower-side planar third-mode stability through the full possible interval; independently control Neumann mu_3. Geometric half-Riesz is a secondary route."
strongest_verified_result: "Known full k=1,2 chain in every dimension and Dirichlet nodal band (including k<=4 in d=3) confirmed from Sol 1; exact disk obstruction, cylinder equivalence, and scalar-method countermodels. No complete proof or novel arbitrary-domain bound."
strongest_conjectural_lead: "Use de Villeroché's lower-side stability theorem quantitatively at d=2,k=3; the excluded width eta depends on an unevaluated constant. Separately test three-center Neumann orthogonality and mass displacement."
next_actions:
  - "Sol 2: quantify or sharpen lower-side third-mode stability on area-pi domains with lambda_3<=12; see 001/artifacts/2026-09-08_third_mode_stability.md."
  - "Sol 3: formulate and attack three-center Neumann mu_3 orthogonality and mass displacement separately."
  - "Sol 4: attack geometric half-Riesz or Fourier compensation for actual domains; avoid scalar desmoothing and impossible operator domination."
  - "Sol 5: adversarially consolidate the strongest new actual-domain lemma or rigorously certify a finite cylinder violation."
priorities:
  - "Quantitative lower-side third-mode stability before repeating already available generic two-ball stability."
  - "Neumann third mode and geometric half-Riesz as independent routes."
  - "Preserve both Dirichlet and Neumann inequalities and the full all-dimensional target."
  - "Review after four new Sol attempts, or earlier if a full proof candidate appears."
failed_or_exhausted_routes:
  - "Sol 1: the equal-k-ball Dirichlet lower bound is false at d=2,k=3; the exact unit-disk trial space has maximal quotient 16."
  - "Sol 1: Courant gives r<=k, not r>=k; connected thin-neck dumbbells exclude a uniform improvement of the sharp lambda_2 constant."
  - "The positive-part exponent-1/2 stability theorem cannot be used for the required lower-side estimate."
  - "Sharp heat or fixed-positive-order Riesz bounds alone do not imply pointwise counting."
  - "Adding planar Yang and an actual square spectral tail does not force half-Riesz for an abstract sequence."
  - "Differentiating Riesz inequalities, ignoring epsilon-dependent thresholds, or substituting positive-order asymptotics for counting are invalid."
  - "Fourier-ball compression cannot dominate a nonzero Dirichlet spectral projection."
verification_needed:
  - "No complete candidate exists; quantify the lower-side stability constant or establish a new geometric estimate."
  - "The de Villeroché stability consequence is external-theorem-dependent; its proof and effective constants require further checking before any full candidate relies on it."
  - "External literature statements are source-audited, not fully independently proved or computationally rerun."
  - "Any complete candidate requires two separate Astra invocations primarily devoted to adversarial verification."
candidate_proof: null
successful_principal_verification_reviews: 0
current_campaign:
  id: "001-campaign-1"
  decision: continue
  sol_attempts_completed: 1
  astra_reviews_completed: 1
  campaigns_completed_for_problem: 0
  nominal_sol_budget: 16
  nominal_astra_budget: 4
  next_checkpoint_after_new_sol_attempts: 4
  next_checkpoint_at_sol_attempt: 5
  next_block_allocation: "Planar third-mode stability; Neumann third-mode construction; geometric half-Riesz alternative; adversarial consolidation."
  strongest_result_class: "Known low-index domain results verified by transfer, exact reductions, and abstract method obstructions; no novel publishable domain theorem claimed."
  transition_rule: "Only Astra selects from the latest synchronized unresolved queue; prefer unstarted work before routine deferred revisits and prevent starvation."
last_sol_run: "research/automated_attempts/001/attempts/2026-09-08_0825_sol.md"
last_astra_run: "2026-09-08T08:34:00Z"
last_astra_review: "research/automated_attempts/001/reviews/2026-09-08_0834_astra.md"
last_queue_sync: "2026-09-08"
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
queue_sync_notes:
  - "Every current problem heading matches all JSON metadata, main README index, and queue; no missing files or renames."
  - "Existing research/queued statuses are preserved as legacy active/unstarted aliases."
  - "scripts/catalogue.py has fixed initial ranges; it remains read-only and must never cap discovery."
  - "This is an observed snapshot count, not a maximum; preserve noncontiguous and longer identifiers."
  - "Concurrent revision 1 was reread, audited, and preserved; this senior invocation increments from it once."
---
