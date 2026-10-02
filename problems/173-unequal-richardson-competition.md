# 173. Exclusion of coexistence for unequal Richardson growth rates

**Area:** Competing infections and stochastic growth

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Consider a continuous-time process on $`\mathbb Z^2`$ with states $`0,1,2`$. Initially only two distinct sites $`x_1,x_2`$ are occupied, with types $`1,2`$ respectively. A vacant site $`x`$ changes to type $`i`$ at rate $`\lambda_i`$ times the number of its nearest neighbors of type $`i`$, where $`\lambda_1,\lambda_2>0`$. Occupied sites never change type. Write $`C_i`$ for the set of sites that eventually receive type $`i`$. For every $`\lambda_1\ne\lambda_2`$, is

```math
\mathbb P(|C_1|=\infty,\ |C_2|=\infty)=0?
```

This asks about every unequal pair of rates, not almost every ratio.

## Application

This gives a precise version of competitive exclusion when two irreversible infections compete for unoccupied space.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §6.4, Question 34.
- [Daniel Ahlberg, Maria Deijfen and Christopher Hoffman, *The two-type Richardson model in the half-plane* (2020)](https://arxiv.org/abs/1808.10796), a restricted-domain resolution.

## Status review

**Known cases:** The classical full-plane argument excludes coexistence outside a possible countable exceptional set of rate ratios.

**Remaining target:** Exclusion of coexistence for every unequal pair of infection rates, including any exceptional ratios.

**Literature check:** Open in cited literature; no later resolution located.

The classical argument excludes coexistence outside a possible countable exceptional set of rate ratios. The later half-plane theorem assumes seeds on its boundary. Neither treats all rate ratios for two finite seeds in the full plane; targeted later searches found no such resolution.

Search topics checked on 2026-09-08: `Richardson model unequal intensities coexistence conjecture; two-type Richardson full plane unequal rates 2025 2026`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
