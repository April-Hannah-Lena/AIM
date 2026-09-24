# 514. Path connectivity of the infinity Z-Gromov–Wasserstein space

**Area:** Applied topology, metric geometry and network comparison

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Let $`(Z,d_Z)`$ be a nonempty, complete, separable, path-connected metric space. A $`Z`$-valued infinity-measure network is a triple $`\mathcal X=(X,\omega_X,\mu_X)`$, where $`X`$ is a Polish space, $`\mu_X`$ is a Borel probability measure, and $`\omega_X:X\times X\to Z`$ is measurable and essentially bounded: for some $`z_0\in Z`$,

```math
\mathop{\mathrm{ess\,sup}}_{\mu_X\otimes\mu_X}d_Z(\omega_X,z_0)<\infty.
```

No symmetry or metric axioms are imposed on the kernel $`\omega_X`$.

For two such networks, define

```math
\mathop{\mathrm{GW}}\nolimits^{Z}_{\infty}(\mathcal X,\mathcal Y)
=\frac12\inf_{\pi\in\Pi(\mu_X,\mu_Y)}
\mathop{\mathrm{ess\,sup}}_{\pi\otimes\pi}
d_Z\bigl(\omega_X(x,x'),\omega_Y(y,y')\bigr),
```

where $`\Pi(\mu_X,\mu_Y)`$ denotes their probability couplings. Let $`\mathcal M_\infty(Z)`$ be the metric space obtained by identifying networks at zero distance.

Must $`\mathcal M_\infty(Z)`$ be path connected? Equivalently, can any two classes be joined by a path $`[0,1]\to\mathcal M_\infty(Z)`$ continuous in $`\mathop{\mathrm{GW}}\nolimits^{Z}_{\infty}`$?

The hypothesis allows path-connected spaces $`Z`$ that are not geodesic. Essential boundedness is required separately for each network along the path.

## Application

The kernels can encode vector-valued or other metric-space-valued attributes of pairs of objects in a network. The question asks whether arbitrary network classes can be continuously interpolated under a worst-case distortion criterion, extending interpolation results for geodesic attribute spaces.

## References

1. M. Bauer, F. Mémoli, T. Needham and M. Nishino, [The Z-Gromov-Wasserstein Distance](https://www.jmlr.org/papers/v26/24-2189.html), Journal of Machine Learning Research **26** (2025), paper 291, pp.1–57. Definitions 10–11 and 28, Theorem 29, Question 41 (p.33) and Theorem 45; [journal PDF](https://www.jmlr.org/papers/volume26/24-2189/24-2189.pdf), [preprint](https://arxiv.org/abs/2408.08233).
2. M. Bauer, F. Mémoli, T. Needham and M. Nishino, [Metric Geometry of Lebesgue, Wasserstein, and Gromov-Wasserstein Spaces: Submetries, Curvature, and Geodesics](https://arxiv.org/abs/2608.11680), 2026 preprint, Theorem 2 and Remarks 2.1 and 2.15.

## Status review

**Known cases:** Theorem 45 of [1] proves that a geodesic $`Z`$ gives a geodesic network space, settling that subclass. Theorem 42 proves contractibility for finite $`p`$, but its argument does not establish the infinity case. The disconnected two-point example in [1] does not satisfy the hypothesis of this question.

The August 2026 preprint [2] resolves the finite-$`p`$ geodesicity questions from [1]; Remark 2.1 restricts its treatment to $`p<\infty`$. It also corrects an earlier separability assertion for the infinity spaces. No separability of $`\mathcal M_\infty(Z)`$ is assumed here. These results do not answer Question 41.

**Remaining target:** Decide path connectivity for every complete separable path-connected attribute space, without assuming it is geodesic.

Searches on 23 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar checks, located no matching solution or announcement for this infinity-path-connectivity target.
