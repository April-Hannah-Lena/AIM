---
schema_version: 1
revision: 3
current_problem: "001"
phase: research
status: open
sol_attempts: 2
astra_reviews: 1
campaign_number: 1
current_bottleneck: "The first untreated full-chain index is k=3. Next attack Neumann mu_3 via a three-center trial family. For planar Dirichlet lambda_3, the shared global stability constant is structurally incapable of full coverage; only a k=3-specific lower-side estimate remains viable."
strongest_verified_result: "Known full k=1,2 chain and Dirichlet nodal band remain confirmed. New method obstruction: every shared C_2 in de Villeroché Theorem 1.1 exceeds sqrt(2)/4, so its planar k=3 exclusion strip is <2^-18 while the interval needing coverage is >22/51; global-constant extraction cannot close the gap."
strongest_conjectural_lead: "For Dirichlet k=3, prove a restricted one-sided bound B-lambda_3<=K*sqrt(lambda_2-A) on A<=lambda_2<=12 with K<=(B-12)/sqrt(12-A). Independently attack Neumann mu_3 through exact three-center orthogonality and mass displacement."
next_actions:
  - "Sol 3: formulate and attack the three-center Neumann mu_3 trial family, separating center selection from radial mass displacement."
  - "Dirichlet return: optimize a k=3-specific one-sided stability coefficient; do not continue extracting the shared global C_2."
  - "Sol 4: attack geometric half-Riesz or Fourier compensation for actual domains; avoid scalar desmoothing and impossible operator domination."
  - "Sol 5: adversarially consolidate the strongest new actual-domain lemma or rigorously certify a finite cylinder violation."
priorities:
  - "Neumann third mode is next under Astra's four-attempt allocation."
  - "Only specialized lower-side third-mode stability remains viable on the planar Dirichlet route."
  - "Geometric half-Riesz and spatial Fourier compensation remain independent alternatives."
  - "Preserve both boundary conditions, all dimensions, and the full all-index target."
failed_or_exhausted_routes:
  - "Sol 1: the equal-k-ball Dirichlet lower bound is false at d=2,k=3; the exact unit-disk trial space has maximal quotient 16."
  - "Sol 1: Courant gives r<=k, not r>=k; connected thin-neck dumbbells exclude a uniform improvement of the sharp lambda_2 constant."
  - "Sol 2: the shared global C_2 in de Villeroché Theorem 1.1 can never cover the planar k=3 interval: C_2>sqrt(2)/4 forces eta<2^-18, while 12-2*j_(0,1)^2>22/51."
  - "The positive-part exponent-1/2 stability theorem cannot be used for the required lower-side estimate."
  - "Sharp heat or fixed-positive-order Riesz bounds alone do not imply pointwise counting."
  - "Adding planar Yang and an actual square spectral tail does not force half-Riesz for an abstract sequence."
  - "Differentiating Riesz inequalities, ignoring epsilon-dependent thresholds, or substituting positive-order asymptotics for counting are invalid."
  - "Fourier-ball compression cannot dominate a nonzero Dirichlet spectral projection."
verification_needed:
  - "Astra should verify Sol 2's use of one C_2 shared over k and the exact disk substitutions proving the global-constant obstruction."
  - "No complete candidate exists; establish a k=3-specific lower-side estimate or a Neumann mu_3 construction."
  - "External literature statements remain source-audited, not fully independently reconstructed."
  - "Any complete candidate requires two separate Astra invocations primarily devoted to adversarial verification."
candidate_proof: null
successful_principal_verification_reviews: 0
current_campaign:
  id: "001-campaign-1"
  decision: continue
  sol_attempts_completed: 2
  astra_reviews_completed: 1
  campaigns_completed_for_problem: 0
  nominal_sol_budget: 16
  nominal_astra_budget: 4
  next_checkpoint_after_new_sol_attempts: 4
  next_checkpoint_at_sol_attempt: 5
  next_block_allocation: "Neumann third-mode construction; geometric half-Riesz alternative; adversarial consolidation. Planar Dirichlet return must use a k=3-specific lower-side constant."
  strongest_result_class: "Known low-index domain results plus exact reductions and method obstructions; no novel full-domain inequality or complete proof claimed."
  transition_rule: "Only Astra selects from the latest synchronized unresolved queue; prefer unstarted work before routine deferred revisits and prevent starvation."
last_sol_run: "research/automated_attempts/001/attempts/2026-09-08_1002_sol.md"
last_astra_run: "2026-09-08T08:34:00Z"
last_astra_review: "research/automated_attempts/001/reviews/2026-09-08_0834_astra.md"
last_queue_sync: "2026-09-08T10:02:00Z"
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
queue_sync_notes:
  - "Every current problem file agrees with the persistent queue in this observed snapshot; no additions, deletions, duplicate identifiers, or renames were found."
  - "Existing research/queued statuses are preserved as legacy active/unstarted aliases."
  - "scripts/catalogue.py has fixed initial ranges; it remains read-only and must never cap discovery."
  - "The observed count 100 is a snapshot, never a maximum or contiguity assumption."
---
