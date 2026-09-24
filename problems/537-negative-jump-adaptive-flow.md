# 537. Existence for adaptive porous flow with a negative drag jump

**Area:** Numerical PDEs and porous-media flow

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`d\ge2`$ and let $`\Omega\subset\mathbb R^d`$ be bounded, connected and Lipschitz. Partition its boundary, up to surface measure zero, into relatively open pressure and flux parts $`\Sigma_p,\Sigma_v`$. Let $`2\le r<\infty`$ and $`s=r/(r-1)`$. Suppose $`\phi_1:[0,1]\to[0,\infty)`$ and $`\phi_2:[1,\infty)\to[0,\infty)`$ are continuous and nondecreasing, with

```math
c a^{(r-2)/2}\le\phi_2(a)\le C(1+a^{(r-2)/2})\quad(a\ge1),\qquad 0<\phi_2(1)<\phi_1(1),
```

for constants $`c,C>0`$. The last inequality is a negative jump in inverse permeability (drag) at the normalized speed threshold one.

For $`u\in L^r(\Omega;\mathbb R^d)`$ define the multivalued constitutive law

```math
\Lambda(u)=\left\{\phi_1(|u|^2)u\,\mathbf1_{\{|u|<1\}}+\phi_2(|u|^2)u\,\mathbf1_{\{|u|>1\}}+h\,\mathbf1_{\{|u|=1\}}:h\in L^s(\Omega;\mathbb R^d)\right\}.
```

The transition law is free on $`\{|u|=1\}`$; it is neither a prescribed branch value nor a prescribed convex combination.

Take $`q\in L^r(\Omega)`$, $`f\in L^s(\Omega;\mathbb R^d)`$ and $`u_0\in L^r(\Sigma_v)`$. If $`\Sigma_p`$ has positive surface measure, prescribe pressure through an extension $`P\in W^{1,s}(\Omega)`$ and put

```math
V=\{\psi\in W^{1,s}(\Omega):\mathop{\mathrm{Tr}}\nolimits\psi=0\text{ on }\Sigma_p\}.
```

If $`\Sigma_p=\varnothing`$, put $`P=0`$, $`V=\{\psi\in W^{1,s}(\Omega):\int_\Omega\psi=0\}`$ and impose $`\int_\Omega q=\int_{\partial\Omega}u_0`$.

Does every such choice of domain, laws and data admit $`u\in L^r(\Omega;\mathbb R^d)`$, $`p\in P+V`$ and $`\zeta\in\Lambda(u)`$ satisfying

```math
\zeta=f-\nabla p\quad\text{a.e. in }\Omega,\qquad
\int_\Omega u\cdot\nabla\psi=-\int_\Omega q\psi+\int_{\Sigma_v}u_0\psi\quad(\psi\in V)?
```

Prove this existence assertion or construct admissible data for which it fails. The target is a weak solution of the stated law, without an additional requirement that it minimize an energy.

## Application

Adaptive porous-flow models switch constitutive laws according to the computed speed, reserving a more expensive nonlinear law for selected regions. Existence is needed to determine whether such a switch defines a solvable continuum model before assessing a numerical method.

## References

1. A. Fumagalli and F. S. Patacchini, [Model adaptation for non-linear elliptic equations in mixed form: existence of solutions and numerical strategies](https://doi.org/10.1051/m2an/2022016), *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 565–592, §§3–4 and conclusion; [full text](https://www.numdam.org/item/10.1051/m2an/2022016.pdf).
2. A. Fumagalli and F. S. Patacchini, [Well-posedness and variational numerical scheme for an adaptive model in highly heterogeneous porous media](https://doi.org/10.1016/j.jcp.2022.111844), *Journal of Computational Physics* (2023); [preprint](https://arxiv.org/abs/2206.07970), nonmonotone existence discussion and conclusion.
3. [Numerical validation of an adaptive model for the determination of nonlinear-flow regions in highly heterogeneous porous media](https://arxiv.org/abs/2405.02094), preprint (2024), §§2.4–2.7.

## Status review

Reference [1] proves existence for nonnegative inverse-permeability jumps in arbitrary dimension and treats the negative-jump case in one dimension. Reference [2] extends the framework but still leaves nonmonotone existence in higher dimensions open. These established cases lie outside the displayed residual target.

The Darcy-to-Forchheimer switching law in [3] adds nonnegative inertial corrections and invokes the monotone theory; its regularization convergence does not settle the negative-jump case above. Later numerical and neural-network classification work likewise supplies no general existence theorem for this target.

Primary-source, duplicate and solution-announcement checks on 24 September 2026 found no matching resolution.
