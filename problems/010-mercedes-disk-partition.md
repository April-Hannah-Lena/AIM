# 010. The Mercedes-star partition of a disk

**Area:** Spectral partitions

## Problem statement

Let $B=\{x\in\mathbb R^2:|x|<1\}$. Among triples of pairwise disjoint nonempty connected open subsets $(D_1,D_2,D_3)$ of $B$, minimize $\max_i\lambda_1(D_i)$, where $\lambda_1$ is the first Dirichlet eigenvalue. Prove or disprove that the three sectors obtained by three radii separated by angles $2\pi/3$ attain the minimum. Equivalently, is

$$\inf_{(D_1,D_2,D_3)}\max_i\lambda_1(D_i)=j_{3/2,1}^2?$$

Here $j_{3/2,1}$ is the first positive zero of the Bessel function $J_{3/2}$. The optimization is over all such triples, with no prescribed interface topology or symmetry.

## Applied significance

This provides a concrete three-cell benchmark for partition algorithms used to balance fundamental modes. It isolates the finite-cell geometry behind asymptotic honeycomb design.

## References

1. V. Bonnaillie-Noël and B. Helffer, [On spectral minimal partitions: the disk revisited](https://www.math.ens.psl.eu/~bonnaillie/articles/BoHe13.pdf), Annals of the University of Bucharest, mathematical series (2013), introduction.
2. G. Berkolaiko, Y. Canzani, G. Cox and J. L. Marzuola, [Homology of spectral minimal partitions](https://doi.org/10.1112/jlms.70065), Journal of the London Mathematical Society 111 (2025), introduction and disk example; [preprint](https://arxiv.org/abs/2406.04225).

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

The 2013 paper studies the conjecture, and the 2025 paper still labels the Mercedes partition conjectural. Its minimality results within specified topological classes do not establish unrestricted global minimality. The analogous Y-partition result on the sphere is a different, solved problem.

**Search audit:** “minimal 3 partition disk Mercedes conjecture 2025 2026”; “Mercedes star disk partition proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
