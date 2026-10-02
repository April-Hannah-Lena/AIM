# 401. Continuity of manifold transport under MTW and convex injectivity domains

**Area:** Monge–Ampère PDEs / transport on manifolds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`(M,g)`$ be a compact connected smooth Riemannian manifold without boundary, of dimension $`n\ge3`$, and $`c(x,y)=d_g(x,y)^2/2`$. For each $`x`$ let $`I_x\subset T_xM`$ be the open set of vectors along which $`\exp_x`$ is minimizing beyond time one. Assume $`I_x`$ is convex, and assume the weak MTW condition

```math
-\frac32\left.\partial_s^2\partial_t^2 c(\exp_x(t\xi),\exp_x(v+s\eta))\right|_{s=t=0}\ge0\quad(v\in I_x,\ \xi\perp\eta).
```

For every pair of probability densities $`f,g_1`$ with respect to Riemannian volume satisfying $`0<a\le f,g_1\le b<\infty`$ almost everywhere, must the unique almost-everywhere optimal map transporting $`f`$ to $`g_1`$ for cost $`c`$ have a continuous representative on $`M`$?

## Application

Continuity prevents arbitrarily close source locations from being assigned distant destinations. The problem identifies whether known geometric necessities suffice for stable mass redistribution on curved spaces.

## References

1. G. De Philippis and A. Figalli, *The Monge–Ampère equation and its link to optimal transportation*, Bulletin of the American Mathematical Society 51 (2014), 527–580, §5.2, open problem (7). [Author manuscript](https://arxiv.org/abs/1310.6167).
2. A. Figalli, L. Rifford and C. Villani, *Necessary and sufficient conditions for continuity of optimal transport maps on Riemannian manifolds*, Tohoku Mathematical Journal 63 (2011), 855–876, introduction and continuity criteria. [Journal full text](https://www.jstage.jst.go.jp/article/tmj/63/4/63_855/_pdf/-char/ja).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited sources establish necessity and sufficiency in dimension two and pose higher-dimensional sufficiency. The 2026 paper “A quantitative stability result for regularity of optimal transport on compact manifolds” (DOI 10.1007/s00526-026-03367-5, Theorem 1) requires smooth densities close in Wasserstein distance, so does not resolve this global assertion. Searches through 22 September 2026 for MTW, convex injectivity domains and higher-dimensional continuity found no resolution.
