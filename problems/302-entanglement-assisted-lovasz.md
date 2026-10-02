# 302. Does entanglement-assisted capacity equal the Lovász bound?

**Area:** Quantum information and zero-error communication

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

Let $`G=(V,E)`$ be a finite nonempty simple graph. Define $`\alpha_*(G)`$ as the largest integer $`m`$ for which there are a finite dimension $`d`$, a positive semidefinite matrix $`\rho\in\mathbb C^{d\times d}`$ with $`\mathop{\mathrm{Tr}}\nolimits\rho=1`$, and positive semidefinite matrices $`\rho_{i,x}`$, for $`1\le i\le m`$ and $`x\in V`$, satisfying

```math
\sum_{x\in V}\rho_{i,x}=\rho\quad(1\le i\le m),\qquad
\rho_{i,x}\rho_{j,y}=0\quad\text{if }i\ne j\text{ and }(x=y\text{ or }\{x,y\}\in E).
```

For $`n\ge1`$, the strong power $`G^{\boxtimes n}`$ has vertex set $`V^n`$; two distinct words are adjacent exactly when their entries are equal or adjacent in every coordinate. Set

```math
\Theta_*(G)=\sup_{n\ge1}\alpha_*(G^{\boxtimes n})^{1/n}.
```

This also equals the limit as $`n\to\infty`$. The dimension and shared state may vary with $`n`$.

Define the Lovász number by

```math
\vartheta(G)=\inf_{c,(u_x)}\max_{x\in V}\frac{1}{|c^Tu_x|^2},
```

where $`c`$ and the $`u_x`$ are real unit vectors in a common finite-dimensional space, and $`u_x^Tu_y=0`$ whenever $`x\ne y`$ and $`\{x,y\}\notin E`$. A zero denominator has value $`+\infty`$.

Is $`\Theta_*(G)=\vartheta(G)`$ for every such graph? The inequality $`\Theta_*(G)\le\vartheta(G)`$ is known. The question allows arbitrary finite-dimensional shared entanglement and local measurements and concerns exact zero error at each block length.

## Application

The graph records which input symbols a noisy classical channel can confuse. The matrices describe coding with a shared quantum state, and the logarithm of $`\Theta_*`$ gives the rate in bits per use with no decoding errors. Equality would turn a regularized optimization over arbitrarily large codes and quantum resources into an efficiently approximable semidefinite quantity. A strict gap would identify a limitation of entanglement that this familiar upper bound misses.

## References

1. Yinan Li and Jeroen Zuiddam, *Quantum asymptotic spectra of graphs and non-commutative graphs, and quantum Shannon capacities*, IEEE Transactions on Information Theory 67 (2021), 416–432, DOI [10.1109/TIT.2020.3032686](https://doi.org/10.1109/TIT.2020.3032686). [Author v3](https://arxiv.org/html/1810.00744v3), §§2.1–2.5, Conjecture 19 and Corollary 27.
2. Toby Cubitt, Laura Mančinska, David Roberson, Simone Severini, Dan Stahlke and Andreas Winter, *Bounds on Entanglement Assisted Source-channel Coding via the Lovász Theta Number and its Variants*, IEEE Transactions on Information Theory 60 (2014), 7330–7344. [Author v3](https://arxiv.org/html/1310.7120v3), Corollary 11 and §V.
3. Xin Wang and Runyao Duan, *Separation between quantum Lovász number and entanglement-assisted zero-error classical capacity*. [Author manuscript v3](https://arxiv.org/pdf/1608.04508v3), January 18, 2018, §III Theorem 3.

4. Runyao Duan and Andreas Winter, *No-Signalling Assisted Zero-Error Capacity of Quantum Channels and an Information Theoretic Interpretation of the Lovász Number*, IEEE Transactions on Information Theory 62 (2016), 891–914. [Author v3](https://arxiv.org/html/1409.3426v3), Theorem 5.
5. Archishna Bhattacharyya, Arthur Mehta and Yuming Zhao, *On the undecidability of quantum channel capacities*, [preprint v3](https://arxiv.org/html/2601.22471v3), March 30, 2026, Definition 2.3 and Corollary 4.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Li–Zuiddam explicitly pose this classical-graph equality; the independent Cubitt et al. paper explains why its single-use counterexample leaves the asymptotic question open. Li–Zuiddam prove that this conjecture and a separate conjecture restricting assistance to maximally entangled states and projective measurements cannot both hold, without deciding which fails. Wang–Duan's counterexample instead uses a quantum channel. Duan–Winter's operational theta interpretation allows stronger no-signalling resources. Bhattacharyya–Mehta–Zhao's corrected 2026 undecidability result concerns one-use capacity with maximal entanglement and projective encoding.

The current search covered classical versus quantum channels, one-shot versus asymptotic capacity, proof/counterexample claims, 2025–2026 and unrestricted dates, and version/correction checks. No matching resolution was located. The [evidence ledger](../research/expansion-2026-09/candidates/entanglement-assisted-lovasz.json) records exact scope comparisons and the lack of a newer explicit primary status statement. A separate adversarial self-pass passed on September 17, 2026; no independent agent or human review occurred. Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration.
