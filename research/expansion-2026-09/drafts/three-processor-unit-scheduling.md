# Exact complexity of unit-job precedence scheduling on three processors

**Area:** Scheduling and operations research

**Status:** Accepted; published as entry 304

**Last checked:** 2026-09-17

## Problem statement

Let $`G=(J,E)`$ be a directed acyclic graph with $`n`$ vertices, one for each job, and let $`T`$ be a nonnegative integer supplied in binary. Every job takes exactly one unit of time on any of three identical processors. A job must finish before any of its successors begins. Jobs cannot be interrupted; each processor runs at most one job at a time; all jobs are available at time zero subject to the precedence constraints.

Decide whether there is a schedule that completes all jobs by time $`T`$. Equivalently, does there exist a map $`s:J\to\{0,\ldots,T-1\}`$ such that

```math
s(v)\ge s(u)+1\quad((u,v)\in E),\qquad
|\{j\in J:s(j)=t\}|\le3\quad(0\le t<T)?
```

Determine the computational complexity of this decision problem, conventionally written $`P3\mid\mathrm{prec},p_j=1\mid C_{\max}`$. In particular, is it solvable by a deterministic algorithm polynomial in the input length, or can NP-completeness be established under polynomial-time many-one reductions? No dichotomy between these outcomes is assumed. The number of processors is fixed at three, while the job graph and deadline are unrestricted input. The goal is exact feasibility, not an approximation to the minimum completion time.

## Applied significance

Precedence edges represent dependencies between computational tasks or project activities. Fixing three identical processors removes machine heterogeneity and numerical processing-time encoding, isolating the algorithmic difficulty created by dependencies and limited parallelism. Resolving exact tractability would clarify when an optimal schedule can be computed efficiently for this basic resource-allocation model.

## References

1. Jesper Nederlof, Céline M. F. Swennenhuis and Karol Węgrzycki, *A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints*, SODA 2025, 535–552. [Published paper](https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf), §1 Open Question 1 and Theorem 1.1; §9 Theorem 9.1.
2. Syamantak Das and Andreas Wiese, *A Simpler QPTAS for Scheduling Jobs with Precedence Constraints*, ESA 2022, 40:1–40:11. [Published paper](https://doi.org/10.4230/LIPIcs.ESA.2022.40), §1. The arXiv upload appeared in 2025.
3. Christina Büsing, Maurice Draeger and Corinna Mathwieser, *Parameterized Complexity of Scheduling Unit-Time Jobs with Generalized Precedence Constraints*, IPEC 2025, 7:1–7:16. [Published paper](https://doi.org/10.4230/LIPIcs.IPEC.2025.7), §5 and Theorem 13.

## Status review

Nederlof–Swennenhuis–Węgrzycki pose the exact three-processor problem and give an algorithm with running time $`2^{O(\sqrt n\log n)}`$. Independent papers by Das–Wiese and Büsing–Draeger–Mathwieser identify the remaining fixed-machine gap. Approximation schemes do not give exact polynomial-time feasibility by taking arbitrarily small error. The inspected hardness reductions either let the number of processors grow or introduce OR dependencies; a makespan of three must not be confused with three processors.

Current resolution searches cover the three-field notation, unit execution times, three machines/processors, author names, proof and counterexample claims, 2025–2026 and unrestricted dates, and version/correction checks. The [candidate ledger](../candidates/three-processor-unit-scheduling.json) records the comparisons and access limits. A separate adversarial self-pass also checked processor-allocation hardness and the outforest restriction in an older linear-time algorithm. Integrated as [entry 304](../../../problems/304-three-processor-unit-scheduling.md) after the September 17, 2026 batch refresh.
