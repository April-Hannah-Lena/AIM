# 453. Almost-everywhere Fourier reconstruction of L log L signals

**Area:** Fourier analysis and endpoint signal reconstruction

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $\mathbb T=\mathbb R/\mathbb Z$ with normalized Lebesgue measure. Suppose $f:\mathbb T\to\mathbb C$ is measurable and

$$
\int_{\mathbb T}|f(x)|\log(e+|f(x)|)\,dx<\infty.
$$

Define $\widehat f(k)=\int_{\mathbb T}f(x)e^{-2\pi ikx}\,dx$ and the symmetric partial sums $S_Nf(x)=\sum_{k=-N}^{N}\widehat f(k)e^{2\pi ikx}$. Must $S_Nf(x)\to f(x)$ for almost every $x$ as $N\to\infty$? The assertion concerns the full sequence of partial sums, without averaging or restriction to a sparse subsequence.

## Application

The question identifies a near-integrable signal class for which direct spectral reconstruction recovers pointwise values despite large localized amplitudes. It is an endpoint stability issue for Fourier approximations.

## References

1. F. Di Plinio, [Weak-Lp bounds for the Carleson and Walsh–Carleson operators](https://doi.org/10.1016/j.crma.2014.02.005), *Comptes Rendus Mathématique* **352** (2014), 327–331, introduction and discussion of the L log L conjecture; [preprint](https://arxiv.org/abs/1312.0398).
2. F. Di Plinio and A. Fragkos, [The weak-type Carleson theorem via wave packet estimates](https://arxiv.org/abs/2204.08051), *Transactions of the American Mathematical Society* (2025), §1, Theorem A and Remark 1.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 paper improves weak-type bounds near p=1 but still describes the known pointwise endpoint using an extra iterated logarithm beyond L log L. Review-date searches for endpoint Carleson convergence and the L log L conjecture found no full-sequence proof or counterexample. Results for lacunary sums or logarithmically averaged sums address different statements.
