# 551. Low-degree convergence of relaxed minimal-deformation surface elements

**Area:** Numerical analysis of evolving surfaces

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $\Gamma^0\subset\mathbb R^3$ be a smooth closed oriented surface and let $u:\mathbb R^3\times[0,T]\to\mathbb R^3$ be smooth. Assume that the relaxed minimal-deformation equations

$$
\partial_tX=v,\qquad v\cdot(n\circ X)=(u\circ X)\cdot(n\circ X),\qquad \partial_tX-\Delta_{\Gamma^0}X=\kappa(n\circ X)
$$

have a smooth solution with $X(\cdot,0)=\mathop{\mathrm{id}}\nolimits$, where $\Gamma(t)=X(\Gamma^0,t)$, $n$ is its unit normal, and $X(\cdot,t)$ and its inverse are smooth throughout $[0,T]$. The scalar $\kappa$ is a constraint multiplier.

Fix $k\in\{1,2,3\}$. Let $\Gamma_h^0$ be degree-$k$ nodal interpolants of $\Gamma^0$ on an admissible, shape-regular, quasi-uniform family of curved triangular meshes. For each curved triangle $K$, let $K_f$ be its flat triangle with the same vertices and let $F_K:K_f\to K$ be its polynomial parametrization. Assume

$$
\max_K\bigl(\|F_K\|_{W^{k,\infty}(K_f)}+\|F_K^{-1}\|_{W^{1,\infty}(K)}\bigr)\le C_0,
$$

where $C_0$ is independent of $h$, as in [1, (2.1)]. Let $S_h$ be the continuous degree-$k$ parametric finite element space on $\Gamma_h^0$.

Use exactly the semidiscrete scheme [1, (2.2)]: find $(X_h,v_h,\kappa_h)\in S_h^3\times S_h^3\times S_h$, initially $X_h=\mathop{\mathrm{id}}\nolimits$, such that $\partial_tX_h=v_h$ and

$$
\int_{\Gamma_h^0}(v_h-u(X_h,t))\cdot N_h\,\chi=0\qquad(\chi\in S_h),
$$



$$
\int_{\Gamma_h^0}v_h\cdot\eta+\int_{\Gamma_h^0}\nabla_{\Gamma_h^0}X_h:\nabla_{\Gamma_h^0}\eta=\int_{\Gamma_h^0}\kappa_hN_h\cdot\eta\qquad(\eta\in S_h^3).
$$

Here $N_h=\widetilde n_h\circ X_h$ and $\widetilde n_h$ is the elementwise geometric unit normal of $X_h(\Gamma_h^0)$; it can jump across element edges. All integrals are exact, and no normal averaging or additional stabilization is introduced.

Does this scheme admit a unique solution with nondegenerate evolving elements on $[0,T]$ for all sufficiently small $h$, and satisfy

$$
\sup_{0\le t\le T}\|X_h^\ell(\cdot,t)-X(\cdot,t)\|_{L^2(\Gamma^0)}\longrightarrow0\qquad(h\to0)
$$

for every such smooth solution and mesh family, for each $k=1,2,3$? The lift uses the closest-point projection $a_h:\Gamma_h^0\to\Gamma^0$, with $X_h^\ell=X_h\circ a_h^{-1}$. Establish convergence with a quantitative error bound, or exhibit a counterexample under these assumptions. The three degrees form one convergence question.

## Application

Tangential mesh motion can preserve element quality during simulations of moving surfaces. Low-degree elements are inexpensive and widely used; a convergence theorem would justify the RMD method in this practical regime before the smooth surface develops a singularity.

## References

1. G. Gao, B. Li and R. Tang, [Convergent finite element approximations of surface evolution with relaxed minimal deformation](https://doi.org/10.1007/s00211-026-01529-3), Numerische Mathematik **158** (2026), 671–714; equations (1.5), (2.1)–(2.2), Theorem 2.1 and §7. [Author manuscript](https://libuyang.com/NM-15.pdf).
2. T. Huang, B. Li and R. Tang, [A convergent finite element method with minimal deformation rate for mean curvature flow](https://arxiv.org/abs/2602.14405v1), preprint (2026); equations (1.6)–(1.8) and Theorem 2.1 concern a different MDR scheme.

## Status review

Reference [1] proves convergence for $k\ge4$ and explicitly leaves $k=1,2,3$ unresolved in §7. Its error estimate controls the flow map in $L^\infty(0,T;L^2)$ and the tangential component in $L^2(0,T;H^1)$. These proved high-degree cases lie outside the displayed target.

Reference [2] proves convergence for degree $k\ge3$ for a fully discrete MDR mean-curvature scheme with an $L^2$-projected normal. Its velocity-gradient equation differs from the position-gradient RMD equation above. It therefore does not settle even the cubic case here. Energy stability and observed numerical convergence also do not establish the requested theorem.

No matching resolution or announcement was found in the literature, author-page, conference, arXiv, GitHub-indexed, Zenodo-indexed and native Palomar checks on the date above. Native Zenodo access returned HTTP 403; the individual conference contribution required login.
