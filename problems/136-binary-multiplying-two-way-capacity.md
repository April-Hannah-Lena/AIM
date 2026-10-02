# 136 — Symmetric capacity of the binary multiplying two-way channel

**Area:** Interactive communication / information theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Two terminals have independent uniform messages $`M_1,M_2`$. At use $`t`$ they send bits $`X_{1,t},X_{2,t}`$ and both receive

```math
Y_t=X_{1,t}X_{2,t}.
```

Terminal $`i`$ may choose $`X_{i,t}`$ as any function of $`(M_i,Y_1,\ldots,Y_{t-1})`$. After $`N`$ uses it estimates the other message from its own message and $`Y^N`$.

Determine the symmetric capacity $`C_{\mathrm{sym}}`$: the supremum of rates $`R`$ for which both message sets can have size at least $`2^{NR}`$ along a sequence of block lengths tending to infinity, while the probability that either decoder errs tends to zero. Rates are bits per terminal per channel use.

## Application

This channel models two-way communication through a shared logical-AND connection. Its unresolved capacity measures the full benefit of adaptive interaction even in a deterministic binary network.

## References

1. A. El Gamal and Y.-H. Kim, *Network Information Theory* (Cambridge University Press, 2011), [Chapter 17, Interactive Channel Coding](https://doi.org/10.1017/CBO9781139030687.019), §17.5. Book formulation of two-way coding and unmatched capacity bounds.
2. R. Tandon and S. Ulukus, *On dependence balance bounds for two way channels* (2007), [Asilomar Conference, pp. 868–872](https://doi.org/10.1109/ACSSC.2007.4487342), abstract and binary-multiplying-channel analysis. Studies the dependence-balance converse bound.
3. Y.-H. Kim, *On the Role of Interaction in Network Information Theory* (2012), [author lecture, slide 19](https://citeseerx.ist.psu.edu/document?doi=442f81f9e76685461fb97f9b19d12bcaea3a3c54&repid=rep1&type=pdf). Records the explicit unmatched symmetric lower and upper bounds.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited discussion gives a lower bound about $`0.6307`$ and a converse about $`0.6463`$, without equality. Searches included “binary multiplying two-way channel capacity solved 2025 2026” and “Shannon Blackwell binary multiplying symmetric capacity”. Non-adaptive zero-error results and the binary adder channel address different operational problems. No exact adaptive vanishing-error capacity was located.
