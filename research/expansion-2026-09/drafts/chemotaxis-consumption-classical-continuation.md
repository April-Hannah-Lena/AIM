# Global classical continuation in the chemotaxis-consumption system

**Area:** Mathematical biology / chemotaxis and cross-diffusion

**Status:** Accepted; integrated as entry 327

**Last checked:** 2026-09-18

## Problem statement

Let $`n\ge3`$ and let $`\Omega\subset\mathbb R^n`$ be a bounded connected domain with smooth boundary. Let $`u_0,v_0\in W^{1,\infty}(\Omega)`$, with $`u_0\ge0`$, $`u_0\not\equiv0`$, and $`v_0>0`$ on $`\overline\Omega`$. Consider

```math
\begin{aligned}
\partial_tu&=\Delta u-\nabla\!\cdot(u\nabla v),\\
\partial_tv&=\Delta v-uv
\end{aligned}
\qquad\text{in }\Omega\times(0,\infty),
```

with homogeneous Neumann conditions $`\partial_\nu u=\partial_\nu v=0`$ on $`\partial\Omega`$, where $`\nu`$ is the outward unit normal, and initial values $`(u,v)|_{t=0}=(u_0,v_0)`$.

Does the maximal local classical solution extend to all positive times for every such domain and initial pair, without any smallness assumption? The required solution class is

```math
\begin{aligned}
u&\in C^0(\overline\Omega\times[0,\infty))
       \cap C^{2,1}(\overline\Omega\times(0,\infty)),\\
v&\in C^{2,1}(\overline\Omega\times(0,\infty))
       \cap\bigcap_{n<q<\infty}C^0([0,\infty);W^{1,q}(\Omega)),
\end{aligned}
```

with $`u\ge0`$ and $`v>0`$ for positive times. Here $`C^{2,1}`$ means continuous spatial derivatives through order two and a continuous first time derivative; the equations and boundary conditions hold pointwise. The initial conditions are attained in the displayed spaces. No derivative compatibility at time zero is imposed beyond these data assumptions. [1]

Both diffusivities, the attraction coefficient and the consumption coefficient are fixed at one. The question concerns classical continuation through every finite time; a uniform bound as $`t\to\infty`$ or a specified convergence rate is not an additional requirement. All dimensions $`n\ge3`$ form one problem family. [1, 3, 6]

## Applied significance

The variables represent a bacterial or cell density and the concentration of a nutrient that attracts those organisms and is consumed by them. The Neumann boundary conditions describe an isolated region. Consumption keeps the nutrient concentration bounded, but migration is driven by its gradient, so this bound alone does not control cell aggregation. A positive answer would justify continuing the classical concentration model over every finite observation interval, including large and spatially uneven initial populations and nutrient supplies. This concerns the model without fluid motion or additional population-growth terms. [1, 2, 4]

## References

1. Johannes Lankeit and Michael Winkler, [*Depleting the signal: Analysis of chemotaxis-consumption models – A survey*](https://arxiv.org/html/2304.02449v1), *Studies in Applied Mathematics* 151(4) (2023), 1197–1229, [DOI](https://doi.org/10.1111/sapm.12625). Author version §1, (CC1), and §2, (2.7)–(2.8): the open question immediately after Theorem 2.2 supplies the formulation.
2. André Luiz Corrêa Vianna Filho and Francisco Guillén-González, [*A Review on the Analysis and Optimal Control of Chemotaxis-Consumption Models*](https://link.springer.com/article/10.1007/s40324-024-00362-8), *SeMA Journal* 82 (2025), 317–350; first published online July 19, 2024. §§1–2, equation (1) with $`s=1`$, and the discussion of the unresolved three-dimensional case provide independent corroboration.
3. Johannes Lankeit and Michael Winkler, [*Chemotaxis-consumption interaction: Solvability and asymptotics in general high-dimensional domains*](https://arxiv.org/html/2502.17338v1), *Nonlinear Analysis* 260 (2025), 113853, [DOI](https://doi.org/10.1016/j.na.2025.113853). Author-version Definition 1.1 and Theorem 1.2 give global weak solutions with eventual smoothness.
4. Jie Jiang, Hao Wu and Songmu Zheng, [*Blow-up for a Three Dimensional Keller-Segel Model with Consumption of Chemoattractant*](https://arxiv.org/pdf/1610.06684), *Journal of Differential Equations* 264(8) (2018), 5432–5464. §1, Theorems 1.1–1.3, gives criteria and lower rates conditional on finite-time blow-up.
5. Jiashan Zheng and Yuying Wang, [*Blow-up prevention and rate of convergence of solutions for N-dimensional parabolic-parabolic systems with consumption of chemoattractant*](https://ejde.math.txstate.edu/Volumes/2025/98/zheng.pdf), *Electronic Journal of Differential Equations* 2025, No. 98, 1–21. Theorem 2.1 and (2.5) retain an explicit initial-signal smallness condition.
6. Michael Winkler, [*A dimension-independent critical exponent in a nutrient taxis system*](https://arxiv.org/html/2601.05338v1), January 2026 preprint. §1 retains the fully parabolic higher-dimensional gap; Theorem 1.1 instead treats the radial parabolic-elliptic problem (1.7) with Dirichlet signal data.

## Status review

The planar version has global classical solutions. In higher dimensions, [3] provides global weak solutions on arbitrary smooth bounded domains and proves that they become smooth after some waiting time. It does not establish classical regularity throughout the preceding interval. The later theorem [5] improves the permitted initial-signal size but retains a smallness restriction. The apparent blow-up result [4] assumes finite maximal existence time in each relevant theorem and therefore does not construct a counterexample. The 2026 result [6] changes the signal equation, boundary conditions and symmetry class.

Searches on 2026-09-17 covered chemotaxis-consumption, nutrient taxis, classical continuation, arbitrary data, proofs, counterexamples, author/version histories and corrections. A separated adversarial self-pass also compared a 2026 Robin-boundary result with an elliptic signal and a 2026 global theorem with an independently evolving migration velocity. Neither supplies the stated continuation result. The [evidence ledger](../candidates/chemotaxis-consumption-classical-continuation.json) records the full relevant theorem comparisons, the supplementary fluid-coupled weak-solution result, and access limitations. A 2025 small-data paper was accessible only through its publisher preview and is not used as decisive status evidence. The review was conducted by the same agent in separate passes.

Related entry [305](../../../problems/305-reversible-reaction-classical-continuation.md) concerns reversible mass-action reactions with diagonal diffusion. Its formulation does not include the directed cross-diffusion flux in this problem.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../batch-04-review.md). No matching later resolution was located.

Integrated page: [335. Global classical continuation in the chemotaxis-consumption system](../../../problems/325-chemotaxis-consumption-classical-continuation.md).
