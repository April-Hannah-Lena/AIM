# 544. Triangle inequality for the pullback distance of verbose persistence barcodes

**Area:** Applied topology and persistent homology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix a field $\mathbb F$. For a finite nonempty pseudometric space $(S,d)$, form the Vietoris–Rips filtration with simplex entry time $\mathop{\mathrm{diam}}\nolimits_d(\sigma)$. Let $V_k(S,d)$ be its degree-$k$ verbose barcode over $\mathbb F$: use the usual boundary-matrix persistence pairing, retaining all pairs with equal birth and death times as well as the positive-length pairs. Multiplicities are retained. For $k\ge1$ all bars have finite endpoints, since the filtration eventually becomes a full simplex.

For equally sized finite multisets $A,B$ of such endpoint pairs, set

$$
m(A,B)=\min_{\pi:A\overset{\sim}{\longrightarrow}B}\ \max_{a\in A}\|a-\pi(a)\|_\infty,
$$

where bijections treat repeated elements as separately labelled copies. Set $m(\varnothing,\varnothing)=0$ and $m(A,B)=\infty$ for unequal cardinalities. No extra diagonal points may be introduced in this matching.

For finite nonempty metric spaces $X,Y$, define

$$
D_k(X,Y)=\inf_{S,\,p:S\twoheadrightarrow X,\,q:S\twoheadrightarrow Y}
m\bigl(V_k(S,p^*d_X),V_k(S,q^*d_Y)\bigr),
$$

where $S$ ranges over finite nonempty sets, $p,q$ are surjections, and $p^*d_X(s,t)=d_X(p(s),p(t))$. The pullback pseudometric spaces retain their distinct vertices even when their distance is zero.

Does

$$
D_k(X,Z)\le D_k(X,Y)+D_k(Y,Z)
$$

hold for every field $\mathbb F$, every integer $k\ge1$, and every triple of finite nonempty metric spaces $X,Y,Z$? Prove the universal statement or give a counterexample, specifying the field and degree.

## Application

Verbose barcodes retain features discarded by ordinary persistent homology. A triangle inequality would support their use in consistent comparisons of finite data sets through this pullback construction.

## References

1. F. Mémoli and L. Zhou, [Ephemeral persistence features and the stability of filtered chain complexes](https://doi.org/10.20382/jocg.v15i2a8), Journal of Computational Geometry **15**(2), 258–328, volume labelled 2024; article published in 2025. Remark 1.1, Definitions 4.7 and 5.3, Remark 5.17 and Corollary 6.10. [Latest author version checked: arXiv:2208.11770v8](https://arxiv.org/abs/2208.11770v8).

## Status review

The degree-zero analogue satisfies the triangle inequality. The positive-degree question is explicitly open in the published article and the August 2025 author revision. The pullback interleaving distance has a counterexample, but it takes a common comparison across degrees; it does not settle this fixed-degree question. Replacing $D_k$ by an infimum of sums along chains of metric spaces defines a different quantity.

Checks on 24 September 2026 found no matching solution or announcement in later primary literature, the author's publication list, indexed Zenodo/GitHub searches or the official Palomar registry.
