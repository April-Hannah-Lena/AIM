---
schema_version: 1
revision: 1
current_problem: "001"
phase: research
status: open
sol_attempts: 1
astra_reviews: 0
campaign_number: 1
current_bottleneck: "The first untreated full-chain index is k=3: the Neumann side lacks an arbitrary-domain mu_3 bound, while the first uncovered Dirichlet case is d=2, k=3, where two-nodal-domain Faber--Krahn falls short of 12*pi."
strongest_verified_result: "For every bounded connected Lipschitz domain in every d>=2, the full two-sided Polya chain holds at k=1,2. Dirichlet Polya also holds for 2<=k<=floor(2*beta_d), beta_d=j_{d/2-1,1}^d*omega_d^2/(2*pi)^d; in d=3 this includes k<=4."
strongest_conjectural_lead: "Use the third min-max dimension to obtain a stability gap away from the two-ball lambda_2 degeneration; separately test whether a three-center Weinberger/Bucur--Henrot construction can control mu_3."
next_actions:
  - "Formulate the exact three-center trial family for mu_3 and separate simultaneous orthogonality from radial mass displacement."
  - "For planar lambda_3, prove a dichotomy between three nodal domains and a third-mode stability refinement of Hong--Krahn--Szego."
  - "Attack any claimed extension against thin-neck dumbbells and the unit-disk k=3 equal-ball obstruction before accepting it."
failed_or_exhausted_routes:
  - "The generalized claim lambda_k(Omega)>=lambda_1(B_{|Omega|/k}) is false already for d=2,k=3; an exact unit-disk polynomial trial space gives lambda_3<=16<3*j_{0,1}^2."
  - "Courant nodal theory cannot justify replacing the nodal count r by k, since it gives r<=k."
  - "No uniform connected-domain improvement of the sharp lambda_2 two-ball constant can hold because thin-neck dumbbells approach it."
verification_needed:
  - "Astra should independently check the four shape-optimization transfers, especially indexing and regularity in the Bucur--Henrot mu_2 theorem."
  - "Astra should verify the nodal-domain argument and the exact unit-disk Rayleigh quotients 6 and 16."
new_problem_ids_this_run: []
queue_integrity_issue: null
last_queue_sync: "2026-09-08T08:25:00Z"
last_sol_run: "research/automated_attempts/001/attempts/2026-09-08_0825_sol.md"
last_astra_run: null
run_history:
  - "revision 1: Sol attempt 1 established the full k=1,2 chain, a Dirichlet nodal band, and a rigorous obstruction to the equal-ball extension."
---
