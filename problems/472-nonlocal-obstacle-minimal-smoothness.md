# 472. Optimal nonlocal obstacle regularity with a minimally smooth obstacle

**Area:** Nonlocal free-boundary PDEs; optimal stopping

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $n\ge2$, $0<s<1$, $\beta>1+s$ be noninteger, and $a\in\mathop{\mathrm{Lip}}\nolimits(S^{n-1})$ be even with $0<\lambda\le a\le\Lambda$. Define

$$
Lu(x)=\mathop{\mathrm{PV}}\nolimits\int_{\mathbb R^n}[u(x)-u(x+y)]\frac{a(y/|y|)}{|y|^{n+2s}}dy.
$$

For every $\phi\in C^\beta(B_1)$ and bounded continuous viscosity solution of

$$
\min\{Lu,u-\phi\}=0\qquad\text{in }B_1,
$$

is the interior estimate

$$
\|u\|_{C^{1+s}(B_{1/2})}\le C\bigl(\|\phi\|_{C^\beta(B_1)}+\|u\|_{L^\infty(\mathbb R^n)}\bigr)
$$

valid with $C$ depending only on $n,s,\beta,\lambda,\Lambda$ and $\|a\|_{\mathop{\mathrm{Lip}}\nolimits}$? The interesting range is $1+s<\beta\le1+2s$. Exterior values of $u$ are arbitrary bounded data; the coincidence set need not be separated from $\partial B_1$.

## Application

This would obtain the expected regularity of a jump-process stopping value with less smooth payoff data, uniformly away from the observation boundary.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton, C. Torres-Latorre and M. Weidner, *Semiconvexity estimates for nonlinear integro-differential equations*, Comm. Pure Appl. Math. (2025), Theorem 1.3. [Article](https://doi.org/10.1002/cpa.22237).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This is Open Question 4.1 in §4.6.1. The cited theorem proves the estimate with $\beta>1+2s$; lowering that threshold to every $\beta>1+s$ is the gap. Searches on 2026-09-22 checked optimal obstacle regularity, low-regularity obstacles and later work of the authors. Results for the fractional Laplacian, smooth obstacles, or higher regularity of an already regular free boundary do not cover this anisotropic local estimate. No matching extension was located.
