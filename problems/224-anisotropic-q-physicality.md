# 224. Strict physicality for anisotropic singular Q-tensor minimizers

**Area:** Liquid-crystal continuum theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`S_0`$ be the symmetric trace-free real $`3\times3`$ matrices. Define

```math
f(Q)=\inf_\rho\left\{\int_{\mathbb S^2}\rho\log\rho\,dS:\rho\geq0,\ \int\rho\,dS=1,\ \int(p\otimes p-I/3)\rho(p)\,dS=Q\right\},
```

with the infimum $`+\infty`$ when no admissible density exists. Let $`\Omega\subset\mathbb R^3`$ be bounded and smooth, and prescribe smooth boundary values $`Q_b`$ whose eigenvalues lie in $`[-1/3+\delta_0,2/3-\delta_0]`$ for some $`\delta_0>0`$.

For arbitrary $`L_1,L_2,\theta,\kappa>0`$, minimize

```math
\int_\Omega\left[L_1|\nabla Q|^2+L_2|\mathop{\mathrm{div}}\nolimits Q|^2+\theta f(Q)-\kappa|Q|^2\right]dx
```

over $`H^1(\Omega;S_0)`$ with trace $`Q_b`$, where $`(\mathop{\mathrm{div}}\nolimits Q)_i=\sum_j\partial_jQ_{ij}`$. Must every global minimizer admit some $`\delta>0`$ with $`\lambda_{\min}(Q(x))\geq-1/3+\delta`$ almost everywhere? Trace zero then also separates the largest eigenvalue from $`2/3`$.

## Application

The eigenvalue constraint expresses realizability by an orientational probability distribution. Uniform separation would justify smooth equilibrium equations and approximation schemes for anisotropic materials.

## References

- John M. Ball, [*Mathematics and liquid crystals*](https://arxiv.org/abs/1612.03792) (2017), §6, equations (6.5)–(6.6): strict physicality and the general elastic-energy question.
- Heiko Gimperlein and Ruma R. Maity, [*Numerical analysis for constrained and unconstrained Q-tensor energies for liquid crystals*](https://arxiv.org/html/2506.04880v1) (2025 preprint), Remark 2.3: explicit unresolved status for elastic anisotropy.
- Zhiyuan Geng and Jiajun Tong, [*Regularity of minimizers of a tensor-valued variational obstacle problem in three dimensions*](https://arxiv.org/abs/1908.10889) (2019 preprint; 2020 publication), introduction and main regularity theorems: partial results depending on the singular potential.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “anisotropic Ball Majumdar strict physicality proof 2025 2026” and “Geng Tong singular potential separation”. The 2025 analysis assumes strict physicality for anisotropic minimizers. One-constant maximum-principle results and the stronger blow-up hypotheses used in some obstacle-problem theorems do not settle the entropic potential with arbitrary positive divergence coupling above.
