# Problem 001 — Pólya's eigenvalue inequalities

- Source: [`problems/001-polya-eigenvalue-bound.md`](../../../problems/001-polya-eigenvalue-bound.md).
- Status: active research (`research` in the legacy queue); campaign 1 continues.
- Latest senior record: [2026-09-08_0834_astra.md](reviews/2026-09-08_0834_astra.md).
- Sol attempts incorporated: [attempt 1](attempts/2026-09-08_0825_sol.md), [attempt 2](attempts/2026-09-08_1002_sol.md), and [attempt 3](attempts/2026-09-08_1104_sol.md).

## Exact target

For every bounded connected Lipschitz `Omega` in `R^d`, `d>=2`, and every `k>=1`, with multiplicity and `mu_0=0`, prove or disprove
\[
\mu_k\le4\pi^2\left(\frac{k}{\omega_d|\Omega|}\right)^{2/d}\le\lambda_k.
\]
Equivalent endpoint convention: `N_D^le(E)<=C_d*|Omega|*E^(d/2)<=N_N^lt(E)`, where `C_d=omega_d/(2*pi)^d` and the Neumann count includes zero for `E>0`.

## 1. VERIFIED RESULTS

**No complete proof, arbitrary-domain counterexample, or new all-index inequality is claimed.** The programme has verified the following exact low-index results, reductions, and method obstructions.

- **Full chain at `k=1,2`:** known shape inequalities give both Pólya sides for every admissible domain in every dimension. Bucur--Henrot has the correct `mu_0=0` indexing and includes bounded Lipschitz sets.
- **Dirichlet nodal band:** with `beta_d=j_(d/2-1,1)^d*omega_d^2/(2*pi)^d`, an eigenfunction with `r` nodal domains proves its Pólya inequality when `k<=r*beta_d`. Universally, `2<=k<=floor(2*beta_d)` is covered, including `k<=4` in `d=3`. Hong--Krahn--Szegő plus monotonicity proves the universal band without boundary regularity assumptions on nodal sets.
- **Equal-ball obstruction:** the unit-disk trial space has exact quotients `6,16,16`, and `sum j_(0,n)^(-4)=1/32`; hence `lambda_3(D)<=16<3*j_(0,1)^2`. Thus equal `k` balls do not give a lower bound for `lambda_k` at planar `k=3`.
- **New in Sol 2 — the published global stability constant cannot close planar `k=3`:** normalize area to `pi`, put `a=j_(0,1)^2`, `b=j_(1,1)^2`, `A=2a`, `B=2b`. De Villeroché Theorem 1.1 has one constant `C_2` shared by all `k`. Substitution of the unit disk at `k=1`, together with `a>4*sqrt(2)` and `b<16`, forces `C_2>sqrt(2)/4`. Therefore its direct `k=3` exclusion width satisfies
  \[
  \eta(C_2)<\left(\frac{40}{81\sqrt2}\right)^{18}<2^{-18},
  \]
  while the radial trial `(1-r^2)(1-2r^2/5)` gives `a<295/51` and hence the interval requiring coverage has width `12-A>22/51>1/4`. Thus no valid constant in that all-`k` theorem can make the direct stability strip cover the full interval, even if every hidden proof constant is optimized. This exhausts global-constant extraction, not specialized lower-side stability. See [attempt 2](attempts/2026-09-08_1002_sol.md).
- **New in Sol 3 — exact `mu_3` reduction and three-center holonomy obstruction:** a vector test field must satisfy the `3d` moment equations `int_Omega F u_l=0` for `l=0,1,2`; then summing componentwise min--max inequalities gives `mu_3 int|F|^2<=int|DF|_F^2`. The canonical three-site Voronoi extension `F=Q_i W_{A_i}` cannot be made globally `H^1` with nonsingular constant frames when the sites are noncollinear. Trace matching on face `ij` forces `Q_i=Q_jR_ij`; around the triangular adjacency cycle this gives `R_12R_23R_31=I`, impossible because its determinant is `-1`. The obstruction applies on a fixed domain when all three faces are active, but does not exclude tree-like induced adjacencies, hierarchical binary folds, variable or singular frames, or scalar constructions. See [attempt 3](attempts/2026-09-08_1104_sol.md) and the [standalone certificate](artifacts/2026-09-08_three_center_holonomy.md).
- **Cylinder equivalence:** sharp half-Riesz on a fixed base is equivalent to Pólya for every interval cylinder over it, separately for Dirichlet and Neumann. Floor/ceiling formulas give a finite counterexample length `L>pi*N(E)/delta` from an actual half-Riesz violation; a Dirichlet witness with `m` terms needs `L>pi*m/delta`.
- **Scalar-method countermodels:** exact modified sequences show that sharp heat, fixed-positive-order Riesz, Li--Yau, Yang, scalar asymptotics, and even an eventual actual-square tail do not by themselves imply counting or half-Riesz. These spectra are synthetic and are not domain counterexamples.
- **Fourier compression identity:** the Dirichlet counting deficit equals `Tr((I-P_E)T_E)-Tr(P_E(I-T_E))`. Direct operator domination `T_E>=P_E` is impossible for nonzero `P_E`; no favorable sign of the trace difference is proved.

Detailed earlier proofs and audits remain in the Astra-linked artifacts: `2026-09-08_research_notes.tex`, `spectral_attack_yang_and_cylinders_2026-09-08.md`, `spectral_attack_square_tail_obstruction_2026-09-08.md`, and `concurrent_sol_audit_2026-09-08.md`.

## 2. PROMISING BUT UNPROVED CLAIMS

- **Dirichlet `k=3` specialized stability:** the shared global constant is unusable, but a restricted one-sided estimate may still close the planar interval. With the notation above, the exponent-`1/18` form would suffice with
  \[
  C_{2,3}\le\frac{B-12}{81\,12^{17/18}(12-A)^{1/18}}.
  \]
  A more natural target is `B-lambda_3<=K*sqrt(lambda_2-A)` on `A<=lambda_2<=12`, with `K<=(B-12)/sqrt(12-A)`. Neither estimate is established. The positive-part Theorem 1.2 has the wrong direction.
- **Neumann `mu_3`:** the moment problem and radial quotient are now separated exactly. The direct noncollinear Voronoi fold is obstructed. A hierarchical two-stage fold has tree adjacency and avoids this obstruction, but still needs a `3d` center-selection theorem and an equal-third mass-displacement inequality.
- A geometric half-Riesz estimate or spatial control of the two Fourier compensation traces could bypass scalar impossibility results.

## 3. COMPUTATIONAL EVIDENCE

All computations used for programme results are exact arithmetic verifiers, not floating-point evidence for a domain-level solution. Sol 2's [verifier](artifacts/2026-09-08_verify_global_stability_obstruction.py) passes and records [JSON output](artifacts/2026-09-08_global_stability_obstruction.json). Sol 3 is analytic and required no numerical computation. Earlier exact verifiers for the scalar obstructions and disk audit also passed. External literature proofs were source-audited but not fully rerun.

## 4. FAILED / EXHAUSTED ROUTES

- Equal-`k`-ball minimization for `lambda_k`; replacing nodal count by `k`; and a uniform connected-domain improvement of the sharp `lambda_2` constant.
- **New:** extracting the shared all-index `C_2` in de Villeroché Theorem 1.1 cannot close planar `k=3`; the theorem itself forces `C_2>sqrt(2)/4`, making its strip `<2^-18` versus required width `>22/51`.
- **New:** the direct three-noncollinear-center Voronoi analogue of the Bucur--Henrot reflected field has odd-cycle holonomy and cannot be globally `H^1` with nonsingular constant frames. This is a method obstruction, not a failure of all three-center families.
- Positive-part stability cannot be read backwards. Sharp heat/Riesz bounds cannot be differentiated into counting; Yang and scalar asymptotics do not repair this. Epsilon-dependent thresholds cannot be ignored.
- Fourier-ball compression cannot dominate a nonzero Dirichlet spectral projection.

## 5. CURRENT BOTTLENECK

The first untreated full-chain index is `k=3`. On the Neumann side, the symmetric noncollinear Voronoi fold is now eliminated; the surviving sharp-looking variant is a hierarchical tree fold, whose center-selection and equal-third mass displacement are both open. On the planar Dirichlet side, only a genuinely `k=3`-specific lower-side stability estimate can continue the two-ball route. Under Astra's allocation, geometric half-Riesz/Fourier compensation is the next run.

## 6. NEXT HIGH-VALUE ATTACKS

1. **Sol 4:** attack geometric half-Riesz or spatial Fourier compensation for actual domains, respecting the cylinder certification requirements.
2. On the next Neumann return, define a two-stage hierarchical fold, count its genuine free parameters, and test its `3d` moment map separately from equal-third mass displacement. Do not reuse the triangular Voronoi constant-frame ansatz.
3. On returning to planar Dirichlet `lambda_3`, optimize the restricted one-sided coefficient above or establish the square-root estimate; do not continue global `C_2` bookkeeping.
4. **Sol 5:** adversarially consolidate the strongest actual-domain lemma or rigorously certify a finite cylinder violation. Reassess at the Astra checkpoint after Sol 5 unless a proof candidate appears earlier.

Campaign decision remains Astra's: continue problem 001. No queue additions or integrity issues were observed in Sol 2.
