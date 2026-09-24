# 597. Extending a symmetric one-dependent four-color law across a branch

**Area:** Applied probability and random graph coloring

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $G$ have vertices $\{o,a,b,v_1,v_2,\ldots\}$ and edges $oa$, $ob$, $ov_1$ and $v_jv_{j+1}$ for $j\ge1$. Thus two arms of the three-arm star have length one and the third is infinite.

Can there exist a random proper four-coloring $X$ of $G$ and a stationary proper four-coloring $Y=(Y_j)_{j\in\mathbb Z}$ such that both are one-dependent, both laws are invariant under all permutations of the color names, $Y$ is also reflection-invariant, and for every ordered simple path $(w_1,\ldots,w_m)$ in $G$,
$$ (X_{w_1},\ldots,X_{w_m})\ \stackrel{\mathrm{law}}=\ (Y_1,\ldots,Y_m)? $$
Here one-dependence means that restrictions to vertex sets at graph distance greater than one are independent. Prove nonexistence or construct such a pair $(X,Y)$. The line law $Y$ is not prescribed to be the known Holroyd–Liggett law.

This is the minimal branched-ray case of [1, Section 6, question 1]. Nonexistence on $G$ implies nonexistence when either finite arm is extended, by restriction.

## Application

The question asks whether a symmetric random assignment with no dependencies beyond adjacent sites can remain locally identical to a line process when a network acquires a branch. It probes a precise obstruction to transferring one-dimensional random scheduling and coloring constructions to networks.

## References

1. T. M. Liggett and W. Tang, [One-dependent colorings of the star graph](https://doi.org/10.1214/22-AAP1920), *Annals of Applied Probability* **33**(6A) (2023), 4341–4365. Proposition 1.4, its following discussion, and Section 6, question 1; [author manuscript](https://arxiv.org/abs/1804.06877).

## Status review

Proposition 1.4 rules out the extension when every path must have the particular line law given by the source's equation (1). The question here permits any symmetric stationary one-dependent four-color law. The paper explicitly distinguishes these assertions; its uniqueness discussion explains why the proved obstruction does not settle the unrestricted statement. Its constructions with five or more colors concern a different alphabet size.

The three-infinite-ray graph cannot have a color-symmetric one-dependent four-coloring by a separate hard-core bound; that larger-graph obstruction does not imply nonexistence on $G$. Current literature and announcement checks found no matching solution.
