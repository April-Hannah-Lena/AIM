# 601. Uniqueness of the stationary one-dependent four-coloring

**Area:** Probability and constrained stochastic processes

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Is there exactly one probability law for a stationary process $`X=(X_j)_{j\in\mathbb Z}`$ with values in $`\{1,2,3,4\}`$ such that $`X_j\ne X_{j+1}`$ almost surely and the restrictions to any two finite index sets at distance greater than one are independent?

The known Holroyd–Liggett law has cylinder probabilities $`P_*(x)`$ specified as follows. Set $`P_*(\varnothing)=1`$. For any nonempty word $`x=(x_1,\ldots,x_m)`$ that has two equal neighboring symbols, set $`P_*(x)=0`$. For every other word, set

```math
P_*(x)=\frac1{2(m+1)}\sum_{j=1}^{m}P_*(x_1,\ldots,x_{j-1},x_{j+1},\ldots,x_m).
```

Prove that every stationary one-dependent proper four-coloring has these cylinder probabilities, or construct a different law. Reflection symmetry and invariance under permutations of colors are not assumed of a competing process; they hold for the proposed unique law.

## Application

This is a rigidity question for stochastic systems constrained by nearest-neighbor exclusion and exact independence beyond neighbors. Uniqueness would identify a canonical random assignment at the smallest possible alphabet size, giving a concrete model for studying how local constraints determine a global stationary law.

## References

1. A. E. Holroyd and T. M. Liggett, [Finitely dependent coloring](https://doi.org/10.1017/fmp.2016.7), *Forum of Mathematics, Pi* **4** (2016), e9. Introduction and final open question (i).
2. T. M. Liggett and W. Tang, [One-dependent colorings of the star graph](https://doi.org/10.1214/22-AAP1920), *Annals of Applied Probability* **33**(6A) (2023), 4341–4365. Equation (1), its specialization to four colors, and the discussion of uniqueness in Section 3.2; [author manuscript](https://arxiv.org/abs/1804.06877).

## Status review

Existence of the displayed law is proved. The original paper explicitly asks for uniqueness among stationary one-dependent four-colorings. The later star-graph paper still treats uniqueness as unresolved even under color and reflection symmetry; its finite cylinder calculations leave parameters that might only be forced by consistency and nonnegativity at arbitrarily large lengths.

Uniqueness within a particular insertion or finitary-factor construction is not uniqueness among all processes in the statement. Likewise, uniqueness of a one-color hard-core marginal does not determine the full four-color joint law. Current searches found no matching resolution or announcement. Public GitHub queries returned no matches; Palomar's coloring result concerned a finite graph certificate unrelated to this process. Native Zenodo returned HTTP 403.
