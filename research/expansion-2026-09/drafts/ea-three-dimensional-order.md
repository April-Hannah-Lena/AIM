# Positive-temperature order in the three-dimensional Edwards–Anderson spin glass

**Area:** Stochastic growth, populations and statistical mechanics

**Status:** Open in cited literature; no later resolution located as of 2026-09-17.

**Last checked:** 2026-09-17

## Problem statement

Let $\Lambda_L=\{1,\ldots,L\}^3\subset\mathbb Z^3$. Give each unordered nearest-neighbor edge $e=\{x,y\}$ an independent standard normal coupling $J_e$. With free boundary conditions and zero external field, define

$$
H_{L,J}(\sigma)=-\sum_{\substack{\{x,y\}\subset\Lambda_L\\|x-y|_1=1}}J_{\{x,y\}}\sigma_x\sigma_y,
\qquad \mu_{L,\beta,J}(\sigma)=Z_{L,\beta,J}^{-1}e^{-\beta H_{L,J}(\sigma)},
\quad\sigma\in\{-1,1\}^{\Lambda_L}.
$$

Conditionally on the same $J$, sample $\sigma^1,\sigma^2$ independently from $\mu_{L,\beta,J}$ and set $R_L=L^{-3}\sum_{x\in\Lambda_L}\sigma_x^1\sigma_x^2$. Does there exist $0<\beta_0<\infty$ such that, for every fixed $\beta>\beta_0$,

$$
\limsup_{L\to\infty}\mathbb E_J\!\left[\mathbb E_{\mu_{L,\beta,J}^{\otimes2}} R_L^2\right]>0?
$$

This uses the overlap-broadening criterion of Itoi–Mukaida–Tasaki, Eq. (3.3), for the expected low-temperature order in dimension three. The volume limit is taken at a fixed finite inverse temperature. The limsup convention does not presuppose convergence of the full overlap distribution.

## Applied significance

The model represents a magnet with frozen random interactions that favor incompatible local spin alignments. A positive squared overlap means that two independent equilibrium samples retain macroscopic common spin structure. This detects order hidden by the zero signed mean overlap imposed by spin-flip symmetry, and would give a rigorous basis for a finite-temperature glassy phase in a three-dimensional short-range model.

## References

- C. Itoi, H. Mukaida and H. Tasaki, [*Griffiths-Type Theorems for Short-Range Spin Glass Models*](https://doi.org/10.1007/s10955-024-03246-3), *Journal of Statistical Physics* 191 (2024), 28, §§2.1–2.2 and §3.1, Eq. (3.3) and Theorem 3.1.
- C. M. Newman and D. L. Stein, [*Short-Range Spin Glasses*](https://web.math.princeton.edu/~aizenman/OpenProblems_MathPhys/9803.SpinGlass.html), IAMP open-problem contribution, September 18, 1998, model paragraph and Questions 1–2.
- K. Hukushima and W. Krauth, [*Damage spreading and coupling in spin glasses and hard spheres*](https://doi.org/10.3389/fphy.2024.1507250), *Frontiers in Physics* 12, 1507250, published February 13, 2025, §3.1.
- S. Chatterjee, [*Spin glass phase at zero temperature in the Edwards–Anderson model*](https://arxiv.org/html/2301.04112v6), arXiv:2301.04112v6, May 2, 2026, §§1–1.2, especially Theorem 1 and Corollary 1 (preprint).
- C. Itoi and Y. Sakamoto, [*Self-averaging of replica overlaps in the random field Edwards-Anderson model*](https://arxiv.org/html/2606.18752v2), arXiv:2606.18752v2, June 18, 2026, §3.3 Theorem 3.1 and §5.2 (preprint).

## Status review

Itoi–Mukaida–Tasaki give the precise order parameter and state the expected low-temperature order for $d\ge3$. Their theorem shows that positive overlap broadening implies a positive Edwards–Anderson order parameter; it does not prove positivity. Newman–Stein independently formulate the finite-temperature transition problem, and Hukushima–Krauth report that the three-dimensional transition remains without a rigorous proof.

Chatterjee's results concern zero-temperature ground states, including overlaps under changes of disorder. They do not establish positive overlap for thermal replicas at fixed finite $\beta$. Itoi–Sakamoto's site-overlap self-averaging theorem assumes a positive random field; §5.2 explicitly leaves its zero-field argument unavailable. Their separate zero-field bond-overlap result concerns a different observable and does not refute the assertion above.

Searches on September 17, 2026 covered finite-temperature EA order, squared overlap, phase-transition proof and disproof claims, recent versions and corrections. Relevant source sections and both recent preprint version histories were read. The problem is distinct from the catalogue's two-dimensional ground-state uniqueness question. No independent expert review has occurred; full evidence and the separate adversarial self-pass are recorded in the [evidence ledger](../candidates/ea-three-dimensional-order.json).
