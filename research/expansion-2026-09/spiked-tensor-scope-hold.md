# Tensor-detection candidate: unresolved theorem scope

Review date: **2026-09-18**. Decision: **hold_claimed_resolution**. This is a primary-agent review observation, with no independent mathematical adjudication. The candidate is outside the accepted count and active catalogue.

## Source and version checks

Agrawal, Bagchi and Kumar's *Spectral Method attacks Sparse LWE, Sparse LPN and Beyond* is available as [arXiv:2603.27190v2](https://arxiv.org/html/2603.27190v2) and [IACR ePrint 2026/614](https://eprint.iacr.org/2026/614). Both records identify July 2, 2026 as the latest revision inspected. The original March version had the title *Attacks on Sparse LWE and Sparse LPN with new Sample-Time tradeoffs*.

The arXiv HTML, arXiv PDF and directly downloaded IACR PDF were checked. The IACR PDF repeats the relevant parameter ranges and formulas in Corollary 5.18 and Theorem 5.21, pp. 20–21. The issue is therefore not confined to the HTML conversion. The contribution paragraph on p. 3 describes results for $|R|>2$. Section 3.1 defines a finite commutative ring with identity without repeating this size restriction; the formal sparse-LPN theorem quantifies over positive integer moduli. That scope distinction matters below.

## Substitution that prevents admission

The candidate asks about exact-arity binary parity observations with $m=n^k$ and bias $\delta_n=n^{-k/4-\varepsilon}$. Consider the fixed case

$$
k=4,\qquad 0<\varepsilon<\tfrac12,\qquad
m=n^4,\qquad \rho=\delta_n=n^{-1-\varepsilon}.
$$

If Corollary 5.18 or the first branch of Theorem 5.21 is applicable to $R=\mathbb Z_2$ with hierarchy parameter $\ell=n-2$, its displayed sufficient sample bound has order

$$
\rho^{-2}\ell\log n\left(\frac{\alpha n}{\ell}\right)^2
=\Theta(n^{3+2\varepsilon}\log n)=o(n^4).
$$

Here $\alpha>0$ is the theorem's fixed constant. Its displayed matrix size is

$$
N=\binom{n}{\ell}(|R|-1)^\ell
=\binom n2,
$$

so the stated runtime is polynomial and the stated error tends to zero. Reading the input also takes polynomial time. Under this interpretation, the theorem would directly contradict a case of the proposed tensor-detection conjecture. The assumption that only fixed, small $\ell$ can give polynomial time is therefore insufficient for screening this particular formula.

## Why the intended scope needs clarification

For the same binary parameters, equation (6) gives $\theta^{(n,n-2,4)}=12$, and therefore the average-degree quantity used in Theorems 5.9 and 5.15 is

$$
\Delta=\frac{m\theta^{(n,n-2,4)}}{N}=\Theta(n^2),
\qquad \rho^2\Delta=\Theta(n^{-2\varepsilon}).
$$

The proof's separation step chooses its error tolerances proportional to $\rho$. Its preceding sufficient degree condition then requires $\rho^2\Delta$ to be at least a constant multiple of $\log N$, which the substitution above does not satisfy. Thus the displayed corollary, interpreted at this boundary and at modulus two, is not justified by directly substituting into the preceding sufficient conditions.

This calculation does not certify the whole proof, prove that every algorithm fails, or determine whether the authors intend to include the binary endpoint. The introduction's $|R|>2$ scope could be decisive: for fixed $|R|>2$, the factor $(|R|-1)^\ell$ is exponential when $\ell$ is close to $n$. A missing restriction on the modulus or on $\ell$ would change the comparison. The review does not silently supply one.

The general problem is accordingly held, with no claim that this paper has resolved it or that its results in the intended larger-ring setting are incorrect. Admission requires an authoritative clarification, correction, or adequate mathematical adjudication of the applicable parameter domain. No author contact was initiated.

## Other checks retained

The [candidate ledger](candidates/spiked-tensor-detection-hardness.json) records the explicit original formulation, independent spiked-tensor corroboration, model normalization, duplicate checks and comparisons with threshold algorithms and low-degree counterexamples. The [draft](drafts/spiked-tensor-detection-hardness.md) is preserved only as research work. A52 queries and follow-ups are in the [actual search log](search-log.json).

No accepted, integrated or published-problem count increases because of this record. Continue investigating other distinct problem families while this source issue remains unresolved.
