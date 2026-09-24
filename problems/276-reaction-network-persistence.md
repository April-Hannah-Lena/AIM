# 276. No asymptotic extinction in bounded weakly reversible mass-action kinetics

**Area:** Deterministic chemical reaction networks

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`\mathcal R`$ be a finite set of reactions $`y\to y'`$ in $`\mathbb N_0^d`$, each lying on a directed cycle of the complex graph, and fix positive reaction constants $`\kappa_{y\to y'}`$. Consider $`\dot x=\sum_{y\to y'\in\mathcal R}\kappa_{y\to y'}x^y(y'-y)`$ with $`x(0)\in(0,\infty)^d`$ and $`x^y=\prod_i x_i^{y_i}`$. For every solution defined and bounded on $`[0,\infty)`$, must $`\liminf_{t\to\infty}x_i(t)>0`$ for every species $`i`$? No complex-balance assumption is permitted.

## Application

A proof would rule out eventual loss of a chemical species solely from the network’s cycle structure, within bounded concentration regimes.

## References

- [Manoj Gopalkrishnan, Ezra Miller and Anne Shiu, *A geometric approach to the Global Attractor Conjecture* (2014)](https://people.tamu.edu/~annejls/geometricGAC.pdf), Conjecture 4.4.
- [Gheorghe Craciun, *Polynomial Dynamical Systems, Reaction Networks, and Toric Differential Inclusions*, SIAM Journal on Applied Algebra and Geometry (2019)](https://people.math.wisc.edu/~craciun/PAPERS_NEW/1_SIAG_Feb_2018_Revision_3.pdf), §2.2, persistence and permanence questions.
- [Praneet Nandan, Philippe Nghe and Jérémie Unterberger, *Autocatalytic cores in the diluted regime: classification and properties*, Journal of Mathematical Biology (2026)](https://link.springer.com/article/10.1007/s00285-026-02357-7), §4.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The bounded-trajectory version is retained to separate extinction from the additional boundedness problem. Claims about complex-balanced global attraction do not settle general weak reversibility. The 2026 paper continues to identify persistence as a conjecture.

Search topics checked on 2026-09-13: `weakly reversible persistence conjecture bounded trajectories proof counterexample 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
