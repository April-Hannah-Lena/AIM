# 306. Dirichlet spectral determination of smooth strictly convex planar domains

**Area:** Spectral theory and spectral geometry

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-17

## Problem statement

Let $\Omega_1,\Omega_2\subset\mathbb R^2$ be bounded open strictly convex domains with $C^\infty$ boundaries. Here strict convexity means that the open segment between any two distinct points of $\overline\Omega_i$ lies in $\Omega_i$. Write their Dirichlet eigenvalues, repeated according to multiplicity, as

$$
0<\lambda_1(\Omega_i)\le\lambda_2(\Omega_i)\le\cdots,
\qquad -\Delta u=\lambda u\text{ in }\Omega_i,\quad u|_{\partial\Omega_i}=0.
$$

If $\lambda_j(\Omega_1)=\lambda_j(\Omega_2)$ for every $j\ge1$, must there exist $Q\in O(2)$ and $a\in\mathbb R^2$ such that $\Omega_2=Q\Omega_1+a$? Reflections are allowed. This is the smooth strictly convex case of the planar inverse spectral question in Levitin–Mangoubi–Polterovich, Open Problem 6.2.26; no symmetry, analyticity, or proximity to a special shape is assumed.

## Applied significance

For a homogeneous membrane with fixed boundary, known tension and known mass density, the vibration frequencies are a known constant times $\sqrt{\lambda_j}$. This asks whether complete exact resonance measurements identify the membrane's convex shape. It is an ideal identifiability question underlying vibration-based shape inference; it does not assert reconstruction from finitely many noisy measurements.

## References

- M. Levitin, D. Mangoubi and I. Polterovich, [*Topics in Spectral Geometry*, preliminary author version, May 29, 2023](https://michaellevitin.net/Book/TSG230529.pdf), §6.2.6, Open Problem 6.2.26, p. 223, and pp. 224–225. The published book is AMS Graduate Studies in Mathematics 237 (2023); locators here refer to the linked preliminary version.
- J. De Simoi, V. Kaloshin and Q. Wei, [*Dynamical spectral rigidity among Z2-symmetric strictly convex domains close to a circle*](https://doi.org/10.4007/annals.2017.186.1.7), *Annals of Mathematics* 186 (2017), 277–314, §1 and §2 Main Theorem and Corollary; Appendix B coauthored with H. Hezari.
- H. Hezari and S. Zelditch, [*One can hear the shape of ellipses of small eccentricity*](https://doi.org/10.4007/annals.2022.196.3.4), *Annals of Mathematics* 196 (2022), 1083–1134, §1, Theorems 1.1 and 1.6.
- I. Koval, [*Local strong Birkhoff conjecture and local spectral uniqueness of almost every ellipse*](https://doi.org/10.1007/s00222-025-01397-y), *Inventiones mathematicae* 244 (2026), 221–298, §1.2, Theorem 2 and Remarks 3–5.
- T. Hu, J. Shi and Q. Tang, [*Strictly Convex Steklov-Isospectral Plane Domains*](https://arxiv.org/html/2608.10557v2), arXiv:2608.10557v2, August 15, 2026, §1.1, Theorem 1.1.2, and §2.1 (preprint; different boundary condition).

## Status review

The source book explicitly records the convex planar question as open, and De Simoi–Kaloshin–Wei independently discuss the unresolved smooth convex inverse problem. Disks and sufficiently low-eccentricity ellipses are known special cases. Hezari–Zelditch also prove deformation rigidity within the axially symmetric near-circle class; Koval's theorem concerns domains close to an ellipse outside an exceptional set. Neither supplies uniqueness for an arbitrary pair in the stated class.

The August 2026 Steklov construction gives strictly convex analytic noncongruent pairs, but concerns $\Delta u=0$ with $\partial_\nu u=\sigma u$ on the boundary. It does not produce equal Dirichlet spectra. Searches on September 17, 2026 covered convex drums, smooth planar isospectrality, spectral determination, proof and counterexample claims, and current versions. The source book's January 2025 erratum and addendum were also checked. The relevant full texts were accessible, with the large book downloaded for local reading. Search coverage cannot certify absence of a later result.

A separated adversarial self-pass checked quantifiers, reflections, boundary conditions and overlap with existing entries, and corrected the book subsection locator. The complete source, scope, duplicate and review record is in the [evidence ledger](../research/expansion-2026-09/candidates/convex-dirichlet-spectrum.json). This question differs from boundary-distance rigidity and from billiard-integrability classification already in the catalogue.
