# Problem 001 — Pólya's eigenvalue inequalities

- Source: [exact problem](../../../problems/001-polya-eigenvalue-bound.md).
- Status: active research (legacy queue research), campaign 1.
- Latest senior review: [Astra 2, 2026-09-08 13:14 UTC](reviews/2026-09-08_1314_astra.md).
- Incorporated: Sol [1](attempts/2026-09-08_0825_sol.md), [2](attempts/2026-09-08_1002_sol.md), [3](attempts/2026-09-08_1104_sol.md), [4](attempts/2026-09-08_1206_sol.md); Astra reviews 1–2.
- No complete candidate; zero successful principal candidate-verification reviews.
- **Current evidence summary:** [STATUS.md](STATUS.md). The two-fold variational lemma is conditional and awaits an independent analytic check. Its missing universal moment/overlap existence statement remains unproved; algebra checks do not establish it.

## Exact target

For every bounded connected Lipschitz Omega in R^d, d>=2, and k>=1, with multiplicity and mu_0=0:
mu_k <= 4*pi^2*(k/(omega_d*|Omega|))^(2/d) <= lambda_k.

Endpoint form: N_D^le(E)<=C_d*V*E^(d/2)<=N_N^lt(E), C_d=omega_d/(2*pi)^d. The Neumann count includes zero at positive energy. Neither a planar third-mode result nor a product result solves this full target.

## Verified results from previous programme reviews

1. **Known full k=1,2 chain and Dirichlet nodal band.** Classical shape inequalities and Bucur--Henrot give both low-index sides. With beta_d=j_(d/2-1,1)^d*omega_d^2/(2*pi)^d, r nodal domains suffice when k<=r*beta_d. Universally 2<=k<=floor(2*beta_d) is covered, including k<=4 in d=3. The universal band follows from lambda_2 and monotonicity without regularity assumptions on nodal boundaries.
2. **Equal-ball obstruction.** Exact disk quotients 6,16,16 and sum j_(0,n)^(-4)=1/32 give lambda_3(D)<=16<3*j_(0,1)^2. Equal k balls cannot supply the proposed all-k Dirichlet lower bound.
3. **Shared-global stability obstruction (Sol 2; Astra 2 confirmed).** Normalize area pi, a=j_(0,1)^2, b=j_(1,1)^2, A=2a, B=2b. De Villeroché's all-k constant satisfies C_2>sqrt(2)/4 by the disk at k=1. Its direct planar k=3 exclusion strip is <2^-18, while the interval needing coverage has width 12-A>22/51. Exact trials give a<295/51, a>4*sqrt(2), b<16. Extracting this shared constant is exhausted, not specialized one-sided stability.
4. **Odd-cycle gluing obstruction (Sol 3; Astra 2 confirmed).** Three noncollinear Voronoi radial fields cannot glue with invertible constant frames across all three active faces. Traces force Q_i=Q_j R_ij, hence three reflections multiply to I, contradicting determinant -1. Singular/variable frames and genuinely acyclic active interfaces remain possible.
5. **Product closure (Sol 4; correct but novelty downgraded).** Counting implies every positive-order sharp Riesz bound by layer-cake. Tensorization uses C_b L_(b/2,a)^cl=C_(a+b). Products of known balls and intervals inherit the chain. This reconstructs standard product machinery, not a new domain-class breakthrough: stronger Laptev-type results allow an arbitrary partner when the valid factor has dimension >=2. Higher-dimensional Neumann balls use the July 2026 preprint, not just the 2023 paper. See Astra 2 for primary sources.
6. **Cylinder/Abel reductions.** Sharp half-Riesz on a fixed base is equivalent to Pólya for every interval cylinder, separately on each side. Floor/ceiling formulas give a finite witness length L>pi*N(E)/delta from an actual half-Riesz violation (Dirichlet: active-term count m suffices). Such a violation forces a base counting violation >=delta/sqrt(E) below E, so it cannot occur on a Pólya-valid base.
7. **Scalar and Fourier obstructions.** Synthetic exact sequences satisfying heat/positive Riesz or Li--Yau/Yang constraints, even with an eventual actual-square tail, do not force counting/half-Riesz. They are not domain counterexamples. The Fourier counting deficit is Tr((I-P)T)-Tr(P(I-T)); T>=P is impossible for nonzero P. No favorable compensation sign is proved.

Earlier proofs and artifacts remain intact: the first Astra review, third-mode stability notes, cylinder/Yang/square-tail notes, and Sol 2–4 certificates.

## Promising but unproved claims: the conditional Neumann route

**Rejected inherited claim:** a binary construction need not have a tree-shaped interface graph. The cells x<0, x>0/y>0, x>0/y<0 form a triangle. A transverse second affine fold applied to only one child produces unmatched traces on part of the first interface. Special fixed-domain and parallel-cut cases are not excluded.

**Positive replacement:** two GLOBAL halfspace folds phi=f_H2 o f_H1 give a continuous 1-Lipschitz piecewise isometry with at most four sheets. Its pushforward density rho has 0<=rho<=4 and integral rho=V. Set e=integral(rho-3)_+: four-sheet IMAGE area, not preimage mass.

The [recorded conditional lemma](artifacts/2026-09-08_1310_fold_overlap.md) uses
R^2=(V-e)/(3*pi), g(s)=s-s^3/3 for s<=1 and 2/3 thereafter.
If F=W_A o phi has all six moments against u_0,u_1,u_2 zero, then
mu_3 V/pi <= (3+q)n(q)/d(q), q=3e/(V-e),
n(q)=28/9+2q-4q^2/3+10q^3/27,
d(q)=11/12+q^2/2-2q^3/9+q^4/36.
Increasing mass/decreasing energy profiles and capacity-3/capacity-1 rearrangements prove this.

It implies planar third-mode Pólya when
P(q)=q^4+66q^3-216q^2+246q-45<=0.
P is strictly increasing on [0,1], with P(3/14)<0<P(3/13). Thus **e<=V/15 suffices**; the best threshold from this polynomial profile lies between 1/15 and 1/14.

**The mean equations are solved:** for any folds, minimize the coercive strictly convex potential integral Psi_R(|phi-A|), Psi_R'=G_R. Its unique minimizer cancels both u_0 moments and varies continuously with the folds. Branch densities vary in L^1, hence e and R are continuous. The remaining signed moments define a continuous map (S^1 times R)^2 -> R^4.

**Still unproved:** a zero of this reduced four-moment map with the overlap budget. Perpendicular disk folds solve all moments but have e=V/4; this does not rule out other disk parameters. The new result is a conditional variational lemma, not a complete solution or yet a publishable partial result. Independent adversarial checking is next.

## Computational evidence and its limits

Sol 2's exact verifier was rerun successfully. The new [Fraction verifier](artifacts/2026-09-08_1310_verify_fold_overlap.py) and [JSON results](artifacts/2026-09-08_1310_fold_overlap.json) pass all checks. They certify finite algebra, not eigenfunction moment existence. The analytic artifact contains an argument for the conditional statement; an independent analytic check remains outstanding. No PDE numerics or arbitrary-domain spectral counterexample is claimed. External literature proofs, including ball computer-assisted components, are source-audited rather than independently reconstructed.

## Current bottleneck

Primary: construct or rigorously obstruct a zero of the reduced four-moment map on the low-overlap subset. Need actual compactness, degree, and boundary control; equal dimensions do not imply a zero.

Dirichlet alternative: on A<=lambda_2<=12 prove B-lambda_3<=K*sqrt(lambda_2-A), with K<=(B-12)/sqrt(12-A), or an adequate k=3-specific lower-side coefficient. Neither is proved; positive-part stability has the wrong direction.

Independent alternative: genuinely non-product spatial compensation for the Fourier deficit. Do not repeat scalar unsmoothing, shared-global-C_2 extraction, triangular constant-frame folds, automatic hierarchical-tree claims, or standard product rediscovery.

## Failed / exhausted routes

The obstructions recorded above rule out the specified methods, not the full conjecture. Also exhausted: replacing Courant's r<=k by r>=k, ignoring epsilon-dependent thresholds, and uniform improvement of the sharp lambda_2 bound on connected dumbbells.

## Next high-value attacks and campaign allocation

Continue 001, campaign 1: Sol 4, Astra 2. The prior Sol 5 checkpoint is superseded; next checkpoint after Sol 8 or immediately on a complete candidate.

1. Sol 5: independently audit the new conditional theorem, mean-center uniqueness/continuity, and exact verifier.
2. Sol 6: attack moment-map existence, including escaping/degenerate folds and the overlap boundary. Stress-test known domains; sampled numerics are not proof.
3. Sol 7: close a concrete degree lemma, or rigorously obstruct the low-overlap ansatz and seek spatially sensitive compensation.
4. Sol 8: if Neumann has no credible route, attack specialized planar Dirichlet stability; otherwise adversarially consolidate the promising result.

Only Astra may change current_problem. Complete candidates require verification phase, CANDIDATE_PROOF.md, and two separate principal-verification Astra runs before solved status.

Administrative synchronization on 2026-09-23 covers 501 active entries; see [QUEUE.md](../QUEUE.md). It preserves the current campaign, four Sol attempts, two Astra reviews and zero successful principal candidate-verification reviews. No new research attempt or proof verification was performed.
