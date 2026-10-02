# 526. Exact motion-planning complexity of real projective spaces

**Area:** Applied topology and robot motion planning

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For each integer $`n\ge1`$, let $`X_n=\mathbb{RP}^n=S^n/(x\sim-x)`$. Give $`P X_n=C([0,1],X_n)`$ the compact-open topology and define $`e:P X_n\to X_n\times X_n`$ by $`e(\gamma)=(\gamma(0),\gamma(1))`$.

Determine $`\mathop{\mathrm{TC}}\nolimits(X_n)`$ exactly for every $`n`$, where the unreduced topological complexity is the least integer $`r`$ for which $`X_n\times X_n`$ has an open cover $`U_1,\ldots,U_r`$ and continuous maps $`s_i:U_i\to P X_n`$ satisfying $`e\circ s_i=\mathop{\mathrm{id}}\nolimits_{U_i}`$.

The requested result is a complete numerical determination as a function of $`n`$, including the dimensions where current lower and upper bounds differ. For $`n\notin\{1,3,7\}`$, the established identity

```math
\mathop{\mathrm{TC}}\nolimits(\mathbb{RP}^n)=1+\mathop{\mathrm{Imm}}\nolimits(\mathbb{RP}^n)
```

expresses the same problem in terms of the least dimension of a Euclidean space admitting a smooth immersion of $`\mathbb{RP}^n`$. This equivalence is a tool, not a numerical solution.

## Application

Real projective space describes an unoriented line through a fixed pivot in Euclidean space. The invariant counts the minimum number of continuous local rules needed to move between any two configurations. Its exact value therefore measures unavoidable discontinuities in this idealized planning problem; it does not incorporate obstacles or dynamic constraints.

## References

1. R. Ghrist, *Elementary Applied Topology* (2014), Chapter 8, Example 8.21 and notes, pp.174,178. [Author's chapter downloads](https://www2.math.upenn.edu/~ghrist/notes.html).
2. M. Farber, S. Tabachnikov and S. Yuzvinsky, [Topological robotics: motion planning in projective spaces](https://arxiv.org/abs/math/0210018), Theorem 12, Corollaries 13–14 and the table following Corollary 21.
3. D. Davis, [Table of immersions and embeddings of real projective spaces](https://www.lehigh.edu/~dmd1/immtable), expert-maintained compilation accessed 24 September 2026; [explanatory page](https://www.lehigh.edu/~dmd1/imms.html).
4. M. Guo, J. Morris, A. Waugh and A. J. Yang, [Immersions of C2-projective spaces via KR-theory](https://arxiv.org/abs/2604.25260), preprint v1 (2026), Main Theorem 1 and §1.3.

## Status review

**Known cases:** Reference [2] determines all dimensions through 23 and proves $`\mathop{\mathrm{TC}}\nolimits(\mathbb{RP}^n)=2n`$ when $`n`$ is a power of two, and $`n+1`$ when $`n=1,3,7`$.

**Remaining target:** Determine the outstanding dimensions in the full family. For example, [3] records a nonimmersion of $`\mathbb{RP}^{24}`$ into $`\mathbb R^{37}`$ and an immersion into $`\mathbb R^{39}`$, leaving $`\mathop{\mathrm{TC}}\nolimits(\mathbb{RP}^{24})\in\{39,40\}`$ by [2]. No separate entry is made for that example.

Reference [4] constructs equivariant immersions for projectivizations of multiples of the regular $`C_2`$ representation. Their underlying dimensions are odd, and the result does not determine the least ordinary immersion dimension in general. It therefore does not close the displayed target.

Primary-source, announcement and duplicate checks on 24 September 2026 found no matching complete determination.  These checks are not a proof of the absence of unpublished work.
