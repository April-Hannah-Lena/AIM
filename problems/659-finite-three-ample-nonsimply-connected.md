# 659. A finite three-ample complex with nontrivial fundamental group

**Area:** Applied topology / simplicial complexes
**Status:** 🟡 PARTIAL
**Last checked:** 2026-09-24

## Problem statement

For a simplicial complex $`X`$ and a vertex subset $`U`$, write $`X[U]`$ for its induced subcomplex. Call a nonempty complex $`X`$ **three-ample** if, for every $`U\subseteq V(X)`$ with $`|U|\le3`$ and every simplicial subcomplex $`A\subseteq X[U]`$, there is a vertex $`v\in V(X)\setminus U`$ such that

```math
\mathop{\mathrm{Lk}}\nolimits_X(v)\cap X[U]=A.
```

Here $`A`$ can be empty and need not be induced. The link consists of simplices $`\sigma`$ not containing $`v`$ for which $`\sigma\cup\{v\}`$ is a simplex of $`X`$.

Does there exist a **finite** three-ample simplicial complex with

```math
\pi_1(|X|)\ne\{1\}?
```

Every three-ample complex is connected, so the fundamental group can be taken at any basepoint. No restriction to flag complexes is imposed.

## Application

Ampleness requires prescribed patterns of higher-order interactions to have local extensions. A finite example would show that this strong extension property on sets of at most three vertices can coexist with a global obstruction to contracting loops in a finite network model.

## References

1. M. Farber, [Large simplicial complexes: universality, randomness, and ampleness](https://doi.org/10.1007/s41468-023-00134-9), Journal of Applied and Computational Topology **8** (2024), 1551–1574, Definition 2.1, Example 2.5 and Proposition 6.1. [Preprint](https://arxiv.org/abs/2301.07404).
2. J. A. Barmak, [Connectivity of ample, conic, and random simplicial complexes](https://doi.org/10.1093/imrn/rnac030), International Mathematics Research Notices **2023**, 6579–6597, Theorem 1.

## Status review

**Known cases:** Infinite three-ample complexes that are not simply connected are known. Finite two-ample examples with nontrivial fundamental group are also known. Every four-ample complex is simply connected.

**Remaining target:** A finite three-ample example, or a proof that finiteness forces simple connectivity at this intermediate ampleness level.

The journal source explicitly asks for a finite example after describing the infinite construction. Current searches found no matching solution or announced construction. Results using ampleness in model theory or algebraic geometry concern different definitions.
