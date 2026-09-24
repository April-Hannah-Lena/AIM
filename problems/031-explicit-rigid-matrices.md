# 031. Explicit matrices with Valiant-scale rigidity

**Area:** Matrix computation and complexity lower bounds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For a matrix $A\in\mathbb Q^{n\times n}$ define
$$R_A(r)=\min_{\operatorname{rank}_{\mathbb C}B\le r}\#\{(i,j):a_{ij}\ne b_{ij}\}.$$
Construct a deterministic algorithm, polynomial in $n$, that outputs matrices $A_n$ with polynomial-bit rational entries, and constants $\alpha\in(0,1)$ and $\beta>0$, such that for all sufficiently large $n$,
$$R_{A_n}(\lfloor\alpha n\rfloor)\ge n^{1+\beta}.$$
Equivalently, establish an explicit family at this linear target rank and superlinear alteration threshold. The field in the minimization is part of the requirement.

## Application

Rigidity measures whether a linear transform can be decomposed into a low-rank part plus a sparse correction. Explicit lower bounds constrain fast shallow circuits and clarify limits of such compression schemes.

## References

1. C.-N. Chou and A. Golovnev, [Matrix rigidity lecture notes](https://golovnev.org/rigidity/notes21.pdf), 2021; discussion of Valiant’s theorem. Definitions and complexity connection.
2. N. Chukhin, A. Kulikov, I. Mihajlin and A. Smirnova, [Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank Under NSETH and Beyond](https://eccc.weizmann.ac.il/report/2025/038/), 2025, revision 3 (March 2026). Conditional advances.
3. L. Hambardzumyan, K. Myasnikov, A. Riazanov, M. Shirley and A. Shraibman, [Spiky Rank and Its Applications to Rigidity and Circuits](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.106/LIPIcs.ICALP.2026.106.html), ICALP 2026; introduction and open challenges. Confirms the explicit-construction gap.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The 2026 sources still separate conditional or weaker constructions from the rigidity needed for Valiant’s application. No polynomial-time rational construction satisfying this bound over the complex numbers was located. Results for random matrices, exponentially encoded algebraic entries, or a different field do not automatically meet this formulation.

Searches included: `explicit rigid matrices 2025 2026`; `Valiant rigidity explicit polynomial time complex field`; `matrix rigidity construction solved 2026`. This is a documented literature check, not a certification that no solution exists.
