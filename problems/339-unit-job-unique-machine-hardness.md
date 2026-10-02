# 339. Polynomial-factor hardness of scheduling unit jobs on prescribed machines

**Area:** Scheduling and approximation complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-18

## Problem statement

An instance $`I`$ consists of $`n\geq1`$ jobs, a directed acyclic graph $`G=(J,E)`$ of precedence constraints, and a map $`M:J\to\{1,\ldots,m\}`$ specifying the only machine on which each job may run. Each job requires exactly one unit of uninterrupted processing. Each machine can process at most one job at a time. The machine count is part of the input; unused machines may be discarded.

A feasible schedule gives each job a nonnegative starting time $`s(j)`$ such that

```math
s(v)\geq s(u)+1\quad((u,v)\in E),
```

and, for distinct jobs $`u,v`$ with $`M(u)=M(v)`$, the intervals $`[s(u),s(u)+1)`$ and $`[s(v),s(v)+1)`$ are disjoint. Jobs are executed once, without release dates or additional communication delays. The makespan and optimum are

```math
C_{\max}(s)=\max_{j\in J}(s(j)+1),
\qquad
\mathop{\mathrm{OPT}}\nolimits(I)=\min_{s\text{ feasible}}C_{\max}(s).
```

Integer starting times suffice: keep each machine's job order from any feasible schedule and move jobs to their earliest permitted times. The resulting precedence and machine-order graph is acyclic, so its longest-path schedule has integer times and no larger makespan.

Prove or disprove the **UMPS polynomial-factor hardness conjecture**: there is an absolute constant $`\varepsilon\in(0,1)`$ such that approximating this optimum within a factor $`n^{\varepsilon}`$ is NP-hard. Here an approximation algorithm must return a feasible schedule satisfying

```math
C_{\max}(s)\leq n^{\varepsilon}\mathop{\mathrm{OPT}}\nolimits(I)
```

on every instance and run in time polynomial in the explicit input length. NP-hardness is meant under polynomial-time reductions; it would rule out such a deterministic algorithm if $`\mathsf P\ne\mathsf{NP}`$. The conjecture asks for a fixed positive exponent, not merely exact optimization hardness or a fixed constant approximation barrier. It is Conjecture 1.1 in the published original [1], numbered Conjecture 2 in its preprint.

## Application

This model describes dependent computational or production tasks whose locations are already fixed: each operation must use its assigned processor or piece of equipment, and dependencies determine which results must be available before another operation begins. Scheduling still requires choosing compatible orders on the machines. Equal durations isolate the difficulty caused by dependencies and fixed assignments.

The conjecture asks whether even a guarantee that deteriorates as a power of workload size is computationally unattainable in the worst case. It would strengthen limits on universal schedulers for this model. Reductions in [1, 3] also connect it to scheduling with nonuniform communication delays. These are worst-case complexity implications; they do not predict the performance of a heuristic on a particular workload.

## References

1. Sami Davies, Janardhan Kulkarni, Thomas Rothvoss, Sai Sandeep, Jakub Tarnawski and Yihao Zhang, *On the Hardness of Scheduling With Non-Uniform Communication Delays*, SODA 2022, pp. 316–328. [DOI](https://doi.org/10.1137/1.9781611977073.15); [published text in NSF repository](https://par.nsf.gov/servlets/purl/10342245). §1.1, Conjecture 1.1; §1.3; §2, Definition 2.1; §3, reduction. Compare [arXiv:2105.00111v1](https://arxiv.org/html/2105.00111v1), April 30, 2021, Conjecture 2.
2. Venkatesan Guruswami, Xuandi Ren and Shaoxuan Tang, *Inapproximability of Unique-Machine Precedence Scheduling for Unit-Length Jobs*, [arXiv:2607.26590v1](https://arxiv.org/html/2607.26590v1), July 29, 2026, preprint. Conjecture 1.1, Theorems 1.2–1.3, Definition 2.1 and §3.4.
3. Rajmohan Rajaraman, David Stalfa and Sheng Yang, *Scheduling Under Non-Uniform Job and Machine Delays*, ICALP 2023, LIPIcs **261**, 98:1–98:20. [Published paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol261-icalp2023/LIPIcs.ICALP.2023.98/LIPIcs.ICALP.2023.98.pdf), DOI 10.4230/LIPIcs.ICALP.2023.98. Definition 1; Theorems 1, 3 and 4, pp. 98:3–98:6.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-18. The original published paper [1] explicitly poses the conjecture. The independently authored July 2026 preprint [2] repeats it and identifies its own results as progress toward it.

Theorem 1.2 of [2] establishes NP-hardness for each fixed approximation factor greater than one. Theorem 1.3 rules out a factor $`(\log N)^{\gamma}`$ for some constant $`\gamma>0`$, where $`N`$ is input size, assuming NP has no deterministic quasipolynomial-time algorithms. Its proof uses a quasipolynomial-size reduction. Neither statement gives the conjectured power-of-$`n`$ gap under polynomial-time reductions. The paper's complete model, theorem statements and §3.4 proofs were read for this comparison; its underlying hardness proofs were not independently certified.

The older logarithmic hardness in [1, Corollary 2.1] allows nonunit processing times. The positive algorithms in [3] allow machine assignment and impose additive structure on delays; some also allow duplication or an additive delay term in the guarantee. Its Theorem 4 instead reduces UMPS to an arbitrary job-machine delay model. The direction and hypotheses of those results do not supply an approximation algorithm for the input above.

The review covered aliases, current and unrestricted dates, proof, disproof, algorithm, correction and version searches. Detailed comparisons and source limits appear in the [evidence ledger](../research/expansion-2026-09/candidates/unit-job-unique-machine-hardness.json). The companion conjecture restricting the machine count and the downstream delay problems are not counted as additional entries.

Unlike [three-processor unit-job scheduling](301-three-processor-unit-scheduling.md), machines here are prescribed separately for each job and their number varies; the target is a growing approximation gap. [Unrelated-machine makespan](278-unrelated-machine-makespan.md) has assignment-dependent durations but no precedence constraints. [List edge-colouring](333-list-edge-colouring.md) asks for an existence guarantee for two-resource jobs under availability lists.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
