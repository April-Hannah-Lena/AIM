# The sharp number of directions illuminating a convex body

**Integrated:** [502 — canonical entry](../../../problems/494-hadwiger-boltyanski-illumination.md) on 2026-09-23. This file preserves the September 19 research draft; use the canonical page for current status and wording.

**Area:** Convex geometry and geometric coverage

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-19

## Problem statement

Let $d\ge3$ be an integer and let $K\subset\mathbb R^d$ be compact and convex with nonempty interior. A direction $v\in S^{d-1}$ illuminates a boundary point $x\in\partial K$ if

$$
x+t v\in\mathop{\mathrm{int}}\nolimits K
\qquad\text{for some }t>0.
$$

Here $S^{d-1}$ is the unit sphere. The vector points in the direction in which the light travels; a source at infinity lies in the opposite direction. A finite set of directions illuminates $K$ when every boundary point is illuminated by at least one of them. Define

$$
I(K)=\min\left\{|V|:
\begin{array}{l}
V\subset S^{d-1}\text{ is finite, and}\\
\forall x\in\partial K\ \exists v\in V\ \exists t>0:
x+t v\in\mathop{\mathrm{int}}\nolimits K
\end{array}\right\}.
$$

The choices of $v$ and $t$ can depend on $x$, and the illuminating set can depend on $K$.

The **Hadwiger–Boltyanski illumination conjecture** asks whether, for every such body,

$$
I(K)\le 2^d,
\qquad
I(K)=2^d\ \Longleftrightarrow\ K=a+A[0,1]^d
$$

for some $a\in\mathbb R^d$ and invertible linear map $A$. Thus the conjecture includes the assertion that only affine cubes require the full number of directions. All boundary points, including corners and edges, must be illuminated; smoothness and symmetry are not assumed.

An equivalent covering formulation minimizes the integer $m$ for which

$$
K\subseteq\bigcup_{i=1}^{m}(a_i+\lambda_i K),
\qquad a_i\in\mathbb R^d,\quad 0<\lambda_i<1.
$$

The minimum is $I(K)$. These are smaller positive homothetic copies: overlaps are allowed, and each copy may have its own translation and scale, but individual rotations and reflections are not allowed. The whole closed body must be covered. This covering formulation and the equivalent model using exterior point lights belong to the same problem. The planar case is already settled.

## Applied significance

In the ideal ray model, illumination is a geometric coverage requirement for inspecting the boundary of a convex object. The resource being minimized is the number of lighting directions needed to leave no boundary point in shadow. The conjecture would provide a sharp limit depending only on dimension, even for objects with many corners and faces; the affine cube would be the extremal obstruction. Its equivalent covering formulation makes the same resource question a finite optimization over translated, scaled copies of one shape. This is a foundational benchmark for geometric coverage planning. It concerns existence of a placement, with no guarantee about the time needed to find one, the minimum incidence angle, light intensity, reflectance, or the ability to reconstruct the object from photographs.

## References

- [Károly Bezdek and Muhammad A. Khan, *The geometry of homothetic covering and illumination*, in Discrete Geometry and Symmetry, Springer Proceedings in Mathematics & Statistics 234 (2018), 1–30; arXiv:1602.06040v2, July 18, 2016](https://arxiv.org/pdf/1602.06040v2), §1, Conjectures 1.1–1.2 and equation (1), internal pp. 1–3; §2.1, p. 4, for the historical proof claim and its reported gaps.
- [Liran Rotem, Alon Schejter and Boaz A. Slomka, *The complex Illumination problem*, Combinatorica 46 (2026), Article 3](https://link.springer.com/article/10.1007/s00493-025-00195-7), §1.1 for the classical real conjecture and current progress; §§1.2–1.4 for fractional and complex variants and their distinct scopes.
- [Andriy Prymak, *A New Bound for Hadwiger’s Covering Problem in $\mathbb E^3$*, SIAM Journal on Discrete Mathematics 37 (2023), 17–24; arXiv:2112.10698v2, September 20, 2022](https://arxiv.org/pdf/2112.10698v2), §1 and Theorem 1.1, internal p. 2, for the general three-dimensional bound.
- [Marcelo Campos, Peter van Hintum, Robert Morris and Marius Tiba, *Towards Hadwiger’s Conjecture via Bourgain Slicing*, International Mathematics Research Notices 2024, 8282–8295; arXiv:2206.11227v1, June 22, 2022](https://arxiv.org/pdf/2206.11227v1), §1, Theorems 1.1–1.3, internal pp. 2–3, for the dependence on the isotropic constant.
- [Boaz Klartag and Joseph Lehec, *Affirmative Resolution of Bourgain’s Slicing Problem using Guan’s Bound*, Geometric and Functional Analysis 35 (2025), 1147–1168; arXiv:2412.15044v1, December 19, 2024](https://arxiv.org/pdf/2412.15044v1), §1, Theorem 1.2 and equation (2), internal p. 2, for the uniform isotropic-constant bound.
- [Wen Rui Sun and Beatrice-Helen Vritsiou, *Illuminating 1-unconditional convex bodies in $\mathbb R^3$ and $\mathbb R^4$, and certain cases in higher dimensions*, arXiv:2407.11331v1, July 16, 2024](https://arxiv.org/pdf/2407.11331v1), §1, Theorems 1–2 and 5 and Proposition 3, internal pp. 3–4. The associated Canadian Journal of Mathematics article has DOI [10.4153/S0008414X25101260](https://doi.org/10.4153/S0008414X25101260); the locators here refer to the inspected preprint.
- [Andrii Arman, Jaskaran Singh Kaire and Andriy Prymak, *Hadwiger’s conjecture for cap bodies*, arXiv:2510.25968v3, August 18, 2026](https://arxiv.org/pdf/2510.25968v3), §1, Theorems 1–2 and Corollary 3, internal pp. 1–2; §2.1 for the cap-body class. Preprint.
- [Illya Ivanov, *Illuminating Primitive Polytopes*, arXiv:2607.08944v1, July 9, 2026](https://arxiv.org/pdf/2607.08944v1), §§1.2–1.3, Conjecture 1, Theorem 2 and Remark 2, internal pp. 2–3. Preprint.

## Status review

Open in cited literature; no later resolution located as of 2026-09-19. Bezdek–Khan give the full classical formulation, and the independently authored 2026 papers of Rotem–Schejter–Slomka and Arman–Kaire–Prymak retain the unrestricted real problem. Searches covered its illumination and covering names, mathematical wording, author chains, recent versions, proof claims, counterexamples and corrections.

Prymak's Theorem 1.1 gives $I(K)\le14$ for every three-dimensional convex body, leaving the conjectured bound eight unresolved. In high dimensions, combining Campos and coauthors' Theorem 1.2 with Klartag–Lehec's uniform bound on the isotropic constant gives an upper bound of the form $4^d e^{-c d}$ for some universal $c>0$ and all sufficiently large $d$. Rotem and coauthors explicitly note this consequence. This improvement does not give the sharp $2^d$ bound or its equality classification.

Sun–Vritsiou handle bodies invariant under every coordinate sign change in dimensions three and four, together with specified subclasses in higher dimensions. The August 2026 cap-body preprint proves the conjecture in every dimension for convex unions of finitely many spikes attached to a ball. Ivanov proves it for primitive polytopes, whose defining facet halfspaces are all essential for boundedness. These geometric restrictions do not include every convex body. Fractional illumination permits weighted directions, while the complex results impose phase symmetry in even real dimension; neither substitutes for the integral real statement here.

Bezdek–Khan §2.1 explicitly reports gaps in Boltyanski's 2000 announced three-dimensional proof and states the subsequent restricted result. The original announcement was not available in full text in this review; its disposition is taken from that specialist survey and checked against the later explicit open formulations, rather than independently adjudicated. The primary-source scope audit also distinguishes a separate corrected argument for complex polydiscs. Computer certificates underlying numerical covering bounds were not rerun.

Entry [124](../../../problems/124-shortest-opaque-square-barrier.md) minimizes the length of a line-blocking barrier, entry [265](../../../problems/265-lebesgue-universal-cover.md) minimizes one universal planar container, and entry [352](../../../problems/352-ulam-convex-solid-packing.md) concerns infinite packing density with disjoint interiors. Their objectives differ from the present finite illumination number. The [evidence record](../candidates/hadwiger-boltyanski-illumination.json) preserves the full comparisons, access limits and review checks. This is one problem family across all dimensions and equivalent formulations.
