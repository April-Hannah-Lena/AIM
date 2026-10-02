# 223. Do finite-energy elastic minimizers satisfy force balance?

**Area:** Nonlinear elasticity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be smooth and bounded, and let $`y_0`$ be a smooth orientation-preserving diffeomorphism on a neighborhood of $`\overline\Omega`$. Consider a frame-indifferent, polyconvex stored energy $`W\in C^1(GL^+(3))`$, extended by $`+\infty`$ when $`\det F\leq0`$. Assume, for some $`p>3`$ and positive constants,

```math
W(F)\geq c|F|^p-C,\qquad W(F)\to\infty\ \text{as }\det F\downarrow0,
```

and $`|DW(F)F^T|+|F^TDW(F)|\leq C(1+W(F))`$, after adding a constant so that $`W\geq0`$.

If $`y`$ globally minimizes $`\int_\Omega W(Dy)\,dx`$ over $`W^{1,p}`$ maps of trace $`y_0`$, must $`DW(Dy)\in L^1_{\mathrm{loc}}`$ and

```math
\int_\Omega DW(Dy):D\varphi\,dx=0\qquad(\varphi\in C_c^\infty(\Omega;\mathbb R^3))?
```

Polyconvex means $`W(F)`$ is a convex function of $`(F,\mathop{\mathrm{cof}}\nolimits F,\det F)`$. The class includes energies with inverse powers of the determinant; additive perturbations need not preserve positive determinant.

## Application

Energy minimization is a foundation of elastic equilibrium computation. This question asks whether the resulting deformation necessarily obeys the usual distributional balance of forces.

## References

- John M. Ball, [*Some Open Problems in Elasticity*](https://doi.org/10.1007/0-387-21791-6_1) (2002), §2.4, Problem 5: deriving the weak Euler–Lagrange equation from minimization under physical growth conditions.
- John M. Ball, [*Minimizers and the Euler–Lagrange equations*](https://people.maths.ox.ac.uk/ball/Articles%20in%20Conference%20Proceedings%20and%20Books/Ball%201983.pdf) (1983), discussion of admissible variations: alternative equilibrium identities and the determinant obstruction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “elastic minimizer weak Euler Lagrange Ball Problem 5 solved”, “physical growth stored energy Euler Lagrange 2025 2026”, and second-gradient variants. The statement specifies a coercive standard subclass of the published question. Energy-momentum or inner-variation identities do not imply the displayed identity without additional control. Results adding second-gradient regularization impose a different energy.
