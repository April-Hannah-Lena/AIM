# 233. The attainable stiffness tensors of two-phase elastic composites

**Area:** Composite materials and homogenization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Fix isotropic tensors $`C_iE=2\mu_iE+\lambda_i\mathop{\mathrm{tr}}\nolimits(E)I`$ on symmetric $`3\times3`$ strains, with $`\mu_i>0`$, $`3\lambda_i+2\mu_i>0`$, and $`C_2-C_1`$ positive definite. Fix a volume fraction $`\theta\in(0,1)`$. For every measurable periodic indicator $`\chi:(\mathbb R/\mathbb Z)^3\to\{0,1\}`$ with $`\int_{[0,1]^3}\chi=\theta`$, let $`C_\chi=\chi C_1+(1-\chi)C_2`$ and define its effective tensor by

```math
E:C_\chi^{\mathrm{hom}}E=\inf_{\varphi\in H^1_{\mathrm{per}}([0,1]^3;\mathbb R^3)}\int_{[0,1]^3}(E+e(\varphi)):C_\chi:(E+e(\varphi))\,dx,
```

where $`e(\varphi)=(D\varphi+D\varphi^T)/2`$.

Give explicit necessary and sufficient conditions on a tensor $`C`$ for membership in the finite-dimensional closure

```math
G_\theta(C_1,C_2)=\mathop{\mathrm{cl}}\nolimits\{C_\chi^{\mathrm{hom}}:\chi\text{ as above}\}.
```

Here $`\mathop{\mathrm{cl}}\nolimits`$ denotes closure in the finite-dimensional space of elasticity tensors, including limits of attainable effective tensors. The characterization must cover arbitrary microstructures and the full tensor, rather than one selected loading energy.

## Application

This set describes all stiffnesses that can be manufactured from two elastic constituents in fixed proportions. Its characterization would give exact feasibility constraints for structural optimization.

## References

- Graeme W. Milton, [*The Theory of Composites*, Chapter 30: Properties of the G-closure and extremal families of composites](https://doi.org/10.1017/CBO9780511613357.031) (2002), pp. 643–670: the G-closure framework and extremal microstructures.
- Krešimir Burazin, Ivana Crnjac and Marko Vrdoljak, [*Explicit Hashin–Shtrikman bounds in 3D linearized elasticity*](https://doi.org/10.2298/FIL2417033B) (2024), §1, especially pp. 6034–6035: explicitly states that the elastic G-closure remains unknown and specifies two ordered isotropic phases.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “two isotropic elastic phases G closure characterization solved 2025 2026” and “three dimensional elastic G closure”. The 2024 paper computes sharp bounds for selected primal and complementary energies; this does not characterize simultaneous attainability of all tensor components. The analogous two-phase scalar conductivity problem has a complete characterization, but its field equations differ.
