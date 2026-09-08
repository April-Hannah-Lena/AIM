# Problem 001 — Pólya's eigenvalue inequalities

- Source: [`problems/001-polya-eigenvalue-bound.md`](../../../problems/001-polya-eigenvalue-bound.md).
- Status: active research (`research` in the legacy queue); campaign 1 continues.
- Latest senior record: [2026-09-08_0834_astra.md](reviews/2026-09-08_0834_astra.md).
- Evidence incorporated: Sol attempt 1, committed concurrently as revision 1, and this first senior review. This run is one senior research/audit invocation, not a candidate-verification run. The original Sol attempt is preserved unchanged.

## Exact target

For every bounded connected Lipschitz `Omega` in `R^d`, `d>=2`, and every `k>=1`, with multiplicity and `mu_0=0`, prove or disprove

\[
\mu_k\le4\pi^2\left(\frac{k}{\omega_d|\Omega|}\right)^{2/d}\le\lambda_k.
\]

Equivalent endpoint convention: `N_D^le(E)<=C_d*|Omega|*E^(d/2)<=N_N^lt(E)`, where `C_d=omega_d/(2*pi)^d` and the Neumann count includes zero for `E>0`.

## 1. VERIFIED RESULTS

**No newly discovered arbitrary-domain inequality, actual-domain counterexample, or complete proof candidate.** Known low-index cases, exact reductions, and method obstructions are verified below; novelty is not claimed.

- **Sol 1 confirmed:** the full chain at `k=1,2` holds for every admissible domain in every dimension by the four established shape inequalities. Bucur–Henrot's theorem has the correct `mu_0=0` indexing and includes bounded Lipschitz sets. The first Neumann ball estimate also has an elementary coordinate/Gamma proof, so this transfer needs no recent full-ball preprint.
- **Dirichlet nodal criterion:** set `beta_d=j_(d/2-1,1)^d*omega_d^2/(2*pi)^d`. An eigenfunction with `r` nodal domains establishes its Pólya inequality when `k<=r*beta_d`. Universally, `2<=k<=floor(2*beta_d)` is covered, including `k<=4` in `d=3`. For the universal band one can use Hong–Krahn–Szegő and eigenvalue monotonicity directly, without assuming nodal boundaries are Lipschitz.
- **Actual-domain obstruction to a stronger claim:** the disk trial space has Rayleigh quotients `6,16,16`, and `sum j_(0,n)^(-4)=1/32`; hence `lambda_3(D)<=16<3*j_(0,1)^2`. The proposed equal-`k`-ball lower bound fails already at `k=3`, without refuting Pólya itself. See the unchanged [Sol attempt](attempts/2026-09-08_0825_sol.md) and [independent audit](artifacts/concurrent_sol_audit_2026-09-08.md).

- **Actual-domain reduction:** sharp half-Riesz on a fixed base is equivalent to Pólya on every interval cylinder over it, separately for Dirichlet/Neumann. Floor/ceiling formulas give an explicit finite counterexample length `L>pi*N(E)/delta` from an actual half-Riesz violation; a Dirichlet witness with `m` terms needs only `L>pi*m/delta`. In a planar base the sharp coefficient is `|Omega|/(6*pi)`.
- **Fixed-positive-order obstruction:** an exact modified sequence `j+ceil(sqrt(j))`, with entries 90–100 lowered to `399/4`, obeys sharp heat and all Riesz bounds of orders `>=1/128` and `N(E)=E-sqrt(E)+O(1)`, yet has `b_100<100`. For each cutoff `s>0` a similar construction exists with `K=O(s^(-2))`. These are synthetic spectra.
- **Yang obstruction:** exact block averaging in `j+1` preserves sharp heat/Riesz bounds of orders `>=1`, Li–Yau, and Yang at every energy but violates half-Riesz by more than `20948/75`. A separate analytic extension preserves an actual square spectral tail as well, using the explicitly stated external two-term positive-order Riesz theorem; it has no effective block threshold. Neither construction is realized by a domain.
- **Geometric identity:** the Dirichlet counting deficit equals `Tr((I-P_E)T_E)-Tr(P_E(I-T_E))` for the Fourier-ball compression `T_E`. The traces are finite. Direct operator domination `T_E>=P_E` is impossible when `P_E` is nonzero. A favorable sign of the trace difference has NOT been proved.

Proofs: [cumulative TeX note](artifacts/2026-09-08_research_notes.tex), [localized deficit lemma](artifacts/obstruction_referee_2026-09-08.md), [Yang and cylinders](artifacts/spectral_attack_yang_and_cylinders_2026-09-08.md), [square-tail extension](artifacts/spectral_attack_square_tail_obstruction_2026-09-08.md).

**External baseline:** tiling cases, balls/sectors, planar concentric Dirichlet annuli, convex-domain positive-order improvements, and epsilon-loss tails have the scopes recorded in the [literature audit](artifacts/literature_audit_2026-09-08.md). The 2026 higher-dimensional Neumann ball proofs were checked at source/theorem level, not independently reverified. No off-repository prior research is accepted as evidence here.

## 2. PROMISING BUT UNPROVED CLAIMS

- **Primary third-mode target:** generic two-ball spectral stability is already available in de Villeroché's May 2026 Theorem 1.1. Conditional on that external theorem, area-`pi` domains with `lambda_3<=12` must satisfy `lambda_2-A>=eta=((B-12)/(81*C_2*12^(17/18)))^18>0`, with `A=2*j_(0,1)^2`, `B=lambda_3(Theta)>12`. The unspecified constant prevents comparison with the full width `12-A`. Obtain usable lower-side constants or a sharper local estimate. The exponent-`1/2` positive-part theorem has the wrong direction. See the [stability addendum](artifacts/2026-09-08_third_mode_stability.md).
- A three-center Neumann trial family for `mu_3` still requires both simultaneous orthogonality and a proved mass-displacement estimate.
- A new geometric estimate may prove the planar sharp half-Riesz bound and thereby Pólya for all its three-dimensional cylinders. The universal half-Riesz inequality remains unproved here.
- Spatial eigenfunction information may control the two Fourier compensation traces. The identity alone is not an estimate.
- A restricted domain-class result must remain explicitly restricted. No numerical candidate domain or spectral enclosure currently exists.

## 3. COMPUTATIONAL EVIDENCE

Three exact arithmetic verifiers passed: [localized obstruction](artifacts/obstruction_referee_2026-09-08.py), [Yang obstruction](artifacts/spectral_attack_verify_yang_obstruction.py), and [Sol disk audit](artifacts/concurrent_sol_audit_2026-09-08.py), with accompanying JSON outputs. They check finite constants or polynomial identities in analytic proofs. There is no floating-point evidence for a domain-level solution. No external literature certificate was rerun.

## 4. FAILED / EXHAUSTED ROUTES

Rejected as logical implications: heat/Riesz bounds imply counting; fixed-positive-order bounds can be differentiated; Yang automatically repairs loss of order; scalar asymptotics determine every finite index; epsilon-dependent thresholds can be ignored; Fourier compression dominates a nonzero low-energy spectral projection. Sol additionally refuted the equal-`k`-ball extension, replacing the actual nodal count by `k`, and a uniform connected-domain improvement of the sharp `lambda_2` constant (thin-neck dumbbells approach equality). Do not use a positive-part stability bound in the lower direction. The overall campaign is not exhausted.

## 5. CURRENT BOTTLENECK

The first untreated full-chain index is `k=3`. Quantify lower-side third-mode stability through the planar interval `A<=lambda_2<=12`, and separately attack the arbitrary-domain Neumann `mu_3` bound. Geometric half-Riesz/cylinder work remains a secondary route. The full all-dimensional, both-boundary-condition target remains unchanged. No candidate-verification phase is justified.

## 6. NEXT HIGH-VALUE ATTACKS

Follow the reconciled four-attempt allocation in the latest review: Sol 2, quantify/sharpen the lower-side planar third-mode stability estimate; Sol 3, Neumann three-center selection and mass displacement; Sol 4, geometric half-Riesz or spatial Fourier compensation; Sol 5, adversarial consolidation or a rigorous finite cylinder certificate. Reassess after four new Sol attempts or earlier for a complete candidate. Do not repeat established scalar obstructions or generic qualitative stability as the main work.

Campaign decision: continue 001. No current queue additions or integrity issues. Preserve all newly discovered problems for fair future campaigns; never select the successor by numeric increment.
