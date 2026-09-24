# The optimal asymptotic rate of binary error-correcting codes

**Area:** Coding theory and reliable data transmission

**Status:** Accepted; integrated as entry 334

**Last checked:** 2026-09-18

## Problem statement

For binary words $`x,y\in\{0,1\}^n`$, their Hamming distance is

```math
d_H(x,y)=\bigl|\{i\in\{1,\ldots,n\}:x_i\ne y_i\}\bigr|.
```

For integers $`n\ge1`$ and $`1\le d\le n`$, define

```math
A_2(n,d)=\max\bigl\{|C|:C\subseteq\{0,1\}^n,\quad
d_H(x,y)\ge d\text{ for every distinct }x,y\in C\bigr\}.
```

The maximum ranges over all binary codes, including nonlinear ones. For each fixed real $`\delta\in(0,1/2)`$, set

```math
R_2(\delta)=\limsup_{n\to\infty}\frac{1}{n}
\log_2 A_2\!\left(n,\lceil\delta n\rceil\right).
```

**Determine $`R_2(\delta)`$ throughout $`0<\delta<1/2`$.** This asks for the exact exponential growth rate, not just an improvement of a bound. The distance fraction is fixed before taking the limsup. The ceiling convention follows [2, 3]; [1] states the asymptotic question using floor rounding. No efficient construction, encoder or decoder is required. [1, §1; 2, §1; 3, §1.2]

A classical benchmark is the Gilbert–Varshamov lower bound

```math
R_2(\delta)\ge 1-h_2(\delta),\qquad
h_2(t)=-t\log_2t-(1-t)\log_2(1-t).
```

Whether this benchmark gives the exact unrestricted rate is not assumed in the question. [1, 2]

## Applied significance

A code assigns a different binary word to each message. Minimum distance $`d`$ permits unambiguous recovery after any set of at most $`\lfloor(d-1)/2\rfloor`$ bit substitutions: two such error balls cannot intersect. Thus $`R_2`$ describes the greatest asymptotic information density compatible with a prescribed worst-case separation, and hence a fundamental redundancy cost in communication and storage. This is an existence limit; practical encoding and decoding impose additional requirements. [2, §1]

The noise model matters. Shannon capacity for independent random bit errors permits an average probability of decoding error tending to zero. Here separation must hold for every pair of codewords, supporting correction of arbitrary error locations within the radius. A formula for the stochastic channel capacity does not determine this tradeoff. [2, §1]

## References

1. Leonardo Nagami Coregliano, Fernando Granha Jeronimo and Chris Jones, *A Complete Linear Programming Hierarchy for Linear Codes*, ITCS 2022, LIPIcs 215, 51:1–51:22. [Publication and full text](https://doi.org/10.4230/LIPIcs.ITCS.2022.51), §1, p.51:2; §1.1, Theorem 1 and Proposition 2, p.51:4.
2. Omar Alrabiah and Venkatesan Guruswami, *Binary code rate bounds via classical–quantum channels*, [arXiv:2608.09347v1](https://arxiv.org/html/2608.09347v1), August 10, 2026, preprint. §1; Theorems 1–3; §5.2.3, Corollary 24 and Eq.(46).
3. William Gay, Fernando Granha Jeronimo and Lenny Liu, *The Honeycomb Framework for Code Bounds*, [arXiv:2608.20287v1](https://arxiv.org/html/2608.20287v1), August 20, 2026, preprint. §§1–1.3, Definition 1.1 and Theorem 1.2; §9.2, Theorem 9.2.
4. Alexander Barg, *Comments on the recent improvements of the MRRW bounds*, [arXiv:2609.01860v1](https://arxiv.org/html/2609.01860v1), September 1, 2026, preprint. §§1–2 and 7.
5. Tao Jiang and Alexander Vardy, *Asymptotic Improvement of the Gilbert–Varshamov Bound on the Size of Binary Codes*, IEEE Transactions on Information Theory 50(8) (2004), 1655–1664, [DOI](https://doi.org/10.1109/TIT.2004.831751). [Author manuscript](https://arxiv.org/abs/math/0404325), §I, Theorem 2 and Eq.(7).
6. Chen Yuan and Ruiqi Zhu, *Improvement of the Gilbert-Varshamov Bound for Linear Codes and Quantum Codes*, [arXiv:2601.18590v1](https://arxiv.org/html/2601.18590v1), January 26, 2026, preprint. §1.1, Theorems 1.2–1.3.
7. Vladimir Blinovsky, *Proof of Tightness of Varshamov–Gilbert Bound for Linear Binary Codes* (title in the PDF), [arXiv:1606.01592v5](https://arxiv.org/abs/1606.01592v5), June 12, 2017, preprint. Entire three-page manuscript, including its linear-subspace and parity-check formulation.
8. OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, [research manuscript](https://cdn.openai.com/pdf/ten-proofs-oai.pdf), 2026. Chapter 2, “Improved Bounds for Binary and Spherical Codes,” §1.1, Eqs.(1)–(8) and Theorem 1.1, printed pp.28–30.

9. Andrew Salmon, *The half-rate linear programming bound for binary codes is 1/2 − 1/π*, [arXiv:2609.03736v1](https://arxiv.org/html/2609.03736v1), September 3, 2026, preprint. §1, definitions (1.2)–(1.7) and Theorem 1.1.

## Status review

The published question in [1] remains unresolved in the current accounts [2, 3]. The author lists of [1] and [2] are disjoint. The August 2026 papers report upper bounds improving the historical McEliece–Rodemich–Rumsey–Welch bounds: [2] uses classical–quantum channels, [8] uses moving projections, and [3] develops further representation-based bounds. Barg [4] gives a subsequent specialist account. These advances do not identify the exact rate. The recent manuscripts are reported with their stated scope; their proofs have not been independently certified here.

Theorem 9.2 of [3] recovers $`A_2(n,d)`$ at sufficiently high hierarchy order, specifically at anchor order at least $`A_2(n,d)`$. This finite completeness statement does not evaluate the asymptotic rate function. The linear-code hierarchy in [1] likewise supplies finite relaxations, while its unrestricted version collapses to the original Delsarte program. Neither result closes the stated asymptotic question.

Salmon's September 2026 preprint [9] claims an exact half-rate point for the asymptotic Delsarte linear-programming relaxation. Its definitions explicitly distinguish the relaxation exponent from the rate of realizable binary codes. Theorem 1.1 evaluates the former; it does not give a matching code construction or determine the unrestricted rate function. The complete definitions and theorem were checked, without independently certifying the proof.

The lower-bound improvements in [5, 6] require a separate distinction. Jiang–Vardy adds a factor proportional to $`\log_2 V(n,d-1)`$, where $`V(n,r)=\sum_{i=0}^r\binom ni`$, in its stated range. Yuan–Zhu obtains a square-root-in-$`n`$ gain in its linear-code existence criterion. At fixed positive relative distance, these factors contribute only $`O(\log n/n)`$ to normalized logarithmic rate. They do not establish a larger limiting exponent or determine $`R_2`$.

The older preprint [7] claims asymptotic tightness for linear codes. Its model uses linear subspaces and parity-check matrices; it supplies no matching upper bound for all nonlinear codes. Its proof has not been adjudicated here, and the claim is not used as an established rate theorem. No separate linear-code variant is admitted.

Searches on September 18, 2026 covered the rate–distance problem and its aliases, Gilbert–Varshamov tightness, proofs and counterexamples, current and unrestricted dates, versions, corrections and author records. Exact queries, additional theorem comparisons, source-access details and duplicate checks are in the [evidence ledger](../candidates/binary-code-asymptotic-rate.json). Review consisted of source research followed by a separated adversarial self-pass; no independent agent or human review occurred.

Two arXiv URLs rejected the direct automated link check, although their full texts were accessible through the research tool. The publisher DOI for [5] returned an empty HTTP 202 response; its accessible author manuscript supplied the theorem. These access details are retained in the ledger.

[Entry 139](../../../problems/139-binary-deletion-channel-capacity.md) concerns stochastic deletion capacity. [Entry 263](../../../problems/263-seven-cycle-shannon-capacity.md) uses strong powers of a fixed seven-symbol confusability graph. [Entry 324](../../../problems/324-polynomial-trace-reconstruction.md) asks for a number of independent deletion traces. Their channel models and success criteria differ from this binary minimum-distance question.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../batch-05-review.md). No matching later resolution was located.

Integrated page: [342. The optimal asymptotic rate of binary error-correcting codes](../../../problems/334-binary-code-asymptotic-rate.md).
