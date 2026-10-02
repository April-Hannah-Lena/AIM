# The ball as the least densely packable convex solid

**Area:** Convex geometry and particle packing

**Status:** Accepted; integrated as entry 352

**Last checked:** 2026-09-19

## Problem statement

Let $`K\subset\mathbb R^3`$ be a compact convex set with nonempty interior. A packing of congruent copies of $`K`$ is a locally finite family

```math
\mathcal P=\{a_i+Q_iK:i\in I\},
\qquad a_i\in\mathbb R^3,\quad Q_i\in O(3),
```

whose members have pairwise disjoint interiors. Here $`O(3)`$ is the group of orthogonal transformations. Together with the vectors $`a_i`$, this permits reflections, rotations and translations, following the full-isometry convention in Kallus's formulation. Every member has the same shape and size.

Write $`B_R`$ for the ball of radius $`R`$ centred at the origin, and $`|A|`$ for the three-dimensional volume of a measurable set $`A`$. Define

```math
\overline d(\mathcal P)=\limsup_{R\to\infty}
\frac{\left|B_R\cap\bigcup_{P\in\mathcal P}P\right|}{|B_R|},
\qquad
\delta(K)=\sup_{\mathcal P}\overline d(\mathcal P).
```

The supremum ranges over all such packings; periodicity and a common orientation are not required. If $`B`$ is a ball, the Kepler theorem gives $`\delta(B)=\pi/\sqrt{18}`$.

The question known as **Ulam's packing conjecture** asks whether

```math
\delta(K)\ge\frac{\pi}{\sqrt{18}}
\qquad\text{for every compact convex }K\subset\mathbb R^3
\text{ with nonempty interior}.
```

Thus the proposed universal lower bound is the optimal density of congruent balls. There is no symmetry or smoothness assumption on $`K`$. The problem does not ask for a characterization of equality, and it imposes no packing protocol or finite container. Lattice packing, packing by translations alone and random packing have different optimization domains.

## Applied significance

Packing geometry connects particle shape to the occupied volume and remaining void space in granular assemblies and particulate materials. The conjecture asks whether the ball supplies a universal benchmark when the arrangement can be optimized: every convex particle shape would admit at least that occupied fraction in the ideal infinite-volume model. This would constrain geometric shape optimization independently of the particular crystals found by simulation. The model allows reflected copies; for a chiral particle this includes its mirror shape. It is a geometric benchmark, rather than a prediction of the density attained by a pouring or compression experiment. Friction, preparation history, polydispersity and kinetic trapping affect those experiments, as the reviews of Baule and collaborators explain.

## References

- [Yoav Kallus, *Pessimal packing shapes*, Geometry & Topology 19 (2015), 343–363; arXiv:1305.0289v2, December 9, 2014](https://arxiv.org/pdf/1305.0289v2), §1, internal pp. 1–4, for the packing conventions and global conjecture; Theorem 3, p. 10, and §4, p. 14.
- [Yoav Kallus, *The 3-ball is a local pessimum for packing*, Advances in Mathematics 264 (2014), 355–370; arXiv:1212.2551v3, August 2, 2014](https://arxiv.org/pdf/1212.2551v3), §2 for conventions and Theorem 5 with Remark 1, internal pp. 16–17, for the symmetric local result.
- [Adrian Baule, Flaviano Morone, Hans J. Herrmann and Hernán A. Makse, *Edwards statistical mechanics for jammed granular matter*, Reviews of Modern Physics 90 (2018), 015006](https://hmakse.ccny.cuny.edu/wp-content/uploads/2015/06/RevModPhys.90.015006-1.pdf), §IV.G, p. 015006-36, and §VI, p. 015006-49, for the conjecture, its random-packing counterpart and materials motivation.
- [Thomas C. Hales, *A proof of the Kepler conjecture*, Annals of Mathematics 162 (2005), 1065–1185](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n3-p01.pdf), Theorem 1.1, p. 1067, for the exact sphere benchmark.
- [Elizabeth R. Chen, Michael Engel and Sharon C. Glotzer, *Dense crystalline dimer packings of regular tetrahedra*, Discrete & Computational Geometry 44 (2010), 253–280; arXiv:1001.0586v3, July 25, 2010](https://arxiv.org/pdf/1001.0586v3), §I for the historical proposed counterexample and §II.D, Theorem 1, internal p. 7, for a packing exceeding the sphere benchmark.
- [Yoav Kallus, *The random packing density of nearly spherical particles*, Soft Matter 12 (2016), 4123–4128; arXiv:1508.05398v2, March 20, 2016](https://arxiv.org/pdf/1508.05398v2), internal pp. 1–3, especially the protocol assumptions and equations (6)–(11).

## Status review

Open in cited literature; no later resolution located as of 2026-09-19. Kallus states the global three-dimensional question explicitly, and the independently authored Baule–Morone–Herrmann–Makse review retains it. The attribution to Ulam is conventional; Kallus notes that its historical origin is a remark attributed to him by Gardner.

Theorem 5 of Kallus's 2014 paper concerns origin-symmetric bodies sufficiently close to a ball. It proves a strict improvement in lattice density for nonellipsoidal bodies in that neighbourhood. Ellipsoids are excluded from that strict lattice statement because lattice density is invariant under invertible linear maps. The ensuing unrestricted symmetric local result is described in Remark 1. This does not address arbitrary convex bodies far from a ball.

Theorem 3 of the 2015 paper allows nonsymmetric directions, but treats the paths $`(1-\lambda)B+\lambda K`$ for $`K`$ in minimal-mean-width position. Its positive range $`0<\lambda<\lambda_0(K)`$ depends on the chosen direction. It neither gives a uniform neighbourhood for all shapes nor reaches every endpoint $`K`$. The 2016 random-packing calculation assumes a protocol producing isostatic sphere packings and a perturbative deformation model. Its observable is not the supremum $`\delta(K)`$ used here.

The older suggestion that the regular tetrahedron might refute the conjecture is ruled out by explicit denser constructions: Chen–Engel–Glotzer obtain $`4000/4671>\pi/\sqrt{18}`$. Determining its exact optimal density remains the separate question in entry [239](../../../problems/238-regular-tetrahedron-packing.md). Entry [086](../../../problems/085-bcc-quantization.md) minimizes quantization error, and entry [243](../../../problems/242-constant-width-volume.md) minimizes the volume of one constant-width body; neither has the present packing objective.

The [evidence record](../candidates/ulam-convex-solid-packing.json) records the source scopes, access limits, current resolution searches and the separated adversarial self-review. This is one global shape-comparison family.
