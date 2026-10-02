# 278. Beat factor two for scheduling on unrelated machines

**Area:** Scheduling and production planning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Input consists of $`m`$ machines, $`n`$ jobs, and nonnegative rational processing times $`p_{ij}`$ for running job $`j`$ on machine $`i`$. An assignment $`f:\{1,\ldots,n\}\to\{1,\ldots,m\}`$ has makespan $`C(f)=\max_i\sum_{j:f(j)=i}p_{ij}`$. Is there an absolute $`\varepsilon>0`$ and an algorithm, polynomial in the binary input length, that always returns $`f`$ with $`C(f)\le(2-\varepsilon)\min_g C(g)`$? A randomized algorithm succeeding with probability at least $`2/3`$ also counts.

## Application

Machine-dependent processing times model heterogeneous manufacturing equipment and computing resources. The makespan is the time by which all assigned work finishes. A positive answer would give a uniform improvement over the factor-two guarantee for this completion time, even when different jobs favor different machines.

## References

- [Jan Karel Lenstra, David B. Shmoys and Éva Tardos, *Approximation algorithms for scheduling unrelated parallel machines*, Mathematical Programming 46 (1990)](https://doi.org/10.1007/BF01585745), factor-two algorithm and hardness bounds.
- [Étienne Bamas et al., *Santa Claus meets Makespan and Matroids: Algorithms and Reductions* (2023; SODA 2024)](https://arxiv.org/abs/2307.08453), Introduction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Improved ratios for restricted assignment and small sets of processing times do not handle arbitrary machine-dependent times. The newer paper relates this question to fair allocation but does not supply a better-than-two algorithm for the stated model.

Search topics checked on 2026-09-13: `unrelated machines makespan approximation below two breakthrough 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
