# 038. Arveson–Douglas essential normality for homogeneous ideals

**Area:** Multivariable operator theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`d\ge1`$. Define the Drury–Arveson space $`H_d^2`$ on the unit ball of $`\mathbb C^d`$ as the reproducing-kernel Hilbert space with kernel $`K(z,w)=(1-\langle z,w\rangle)^{-1}`$. For a proper homogeneous polynomial ideal $`I\subseteq\mathbb C[z_1,\ldots,z_d]`$, let $`Q=H_d^2\ominus\overline I`$ and $`S_j=P_QM_{z_j}|_Q`$.

Prove or disprove that

```math
[S_i,S_j^*]\in\mathcal S_p\qquad(1\le i,j\le d,\ p>\dim_{\mathbb C}V(I)),
```

where $`[A,B]=AB-BA`$, $`V(I)=\{z:f(z)=0\ \forall f\in I\}`$, and $`\mathcal S_p`$ consists of compact operators whose singular values have summable $`p`$th powers. The closure is in $`H_d^2`$.

## Application

Compressed coordinate multipliers model constrained multivariable systems. Quantitative compactness of their commutators supports index theory and stable operator models; this is a foundational operator-theory application.

## References

1. O. M. Shalit, [Operator theory and function theory in Drury–Arveson space and its quotients](https://arxiv.org/abs/1308.1081), survey (2013); section 10, Arveson–Douglas conjectures.
2. M. Engliš and J. Eschmeier, [Geometric Arveson–Douglas conjecture](https://arxiv.org/abs/1312.6777), 2013. Geometric formulations and partial cases.
3. S. Raum, [Around the Arveson–Douglas conjecture](https://www.raum-brothers.eu/sven/AD-2026-07.html), University of Potsdam workshop, 15–17 July 2026. Recent research context.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The surveys formulate the general homogeneous-ideal problem; the 2026 workshop and recent papers focus on partial settings. Results for smooth boundary varieties or polydisc Hardy modules do not cover arbitrary homogeneous ideals in the Drury–Arveson ball setting. No general resolution was located.

Searches included: `Arveson Douglas conjecture homogeneous ideals 2025 2026`; `Arveson Douglas conjecture solved 2026`; `Around Arveson Douglas July 2026`. This is a documented literature check, not a certification that no solution exists.
