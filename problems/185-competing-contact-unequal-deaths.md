# 185. Competitive exclusion with unequal death rates

**Area:** Spatial epidemics and population competition

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $\mathbb Z^2$, let each site be vacant or occupied by one individual of type $1$ or $2$. A vacant site changes to type $i$ at rate $\beta_i f_i$, where $f_i$ is the fraction of its four nearest neighbors of type $i$, and a type-$i$ individual dies at rate $\delta_i>0$. Let $\lambda_c$ be the critical birth parameter for the one-type contact process with death rate one and birth rate $\lambda f$.

Assume $\beta_2/\delta_2>\max\{\beta_1/\delta_1,\lambda_c\}$. Starting from any iid site distribution assigning positive probability to each type, must the law converge on finite sets to the upper stationary distribution of the type-$2$ contact process (the limit starting from all type $2$)?

## Application

Mean-field competition predicts that the larger birth-to-death ratio determines the winner. This asks whether that prediction survives local crowding when the two populations have different time scales.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, book manuscript of 2 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf), §4.1, Open Problem 4.1.3.
- [Claudia Neuhauser, *Ergodic theorems for the multitype contact process* (1992)](https://doi.org/10.1007/BF01192067), the equal-death-rate theory.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 manuscript retains the unequal-death-rate extension. The initial law here is specified to contain both populations and the winning one is assumed supercritical; these avoid degenerate readings of an informal exclusion claim. The equal-death graphical coupling does not prove the proposed ratio criterion.

Search topics checked on 2026-09-08: multitype contact process unequal death rates birth death ratio competitive exclusion; Neuhauser unequal rates conjecture 2025 2026.
