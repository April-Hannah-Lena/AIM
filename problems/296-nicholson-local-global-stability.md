# 296. Does local stability imply global attraction for Nicholson’s blowflies equation?

**Area:** Population dynamics with maturation delay

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

For $p>1$ and $\tau>0$ consider $x'(t)=-x(t)+p\,x(t-\tau)e^{-x(t-\tau)}$ with arbitrary continuous history $x(s)>0$ on $[-\tau,0]$. The positive equilibrium is $x_* =\log p$. Suppose every root of $z+1-(1-\log p)e^{-z\tau}=0$ has strictly negative real part, so the equilibrium is locally exponentially stable. Must every such positive solution satisfy $x(t)\to\log p$ as $t\to\infty$? Parameter values with imaginary characteristic roots are excluded from the premise.

## Applied significance

This asks whether the linear stability test predicts eventual population recovery even after a large perturbation.

## References

- [Gergely Röst and Jianhong Wu, *Domain-decomposition method for the global dynamics of delay differential equations with unimodal feedback*, Proceedings of the Royal Society A 463 (2007)](https://www.math.u-szeged.hu/~rost/papers/Rost2007ProcRSocAWu.pdf), Introduction and the Nicholson example.
- [Leonid Berezansky, Elena Braverman and Lev Idels, *Nicholson’s blowflies differential equations revisited: Main results and open problems*, Applied Mathematical Modelling 34 (2010), 1405–1417](https://doi.org/10.1016/j.apm.2009.08.027), global stability questions.

## Status review

Known sufficient global-stability conditions cover only part of the locally stable parameter region. Results on models with delay-dependent survival factors or generalized periodic coefficients do not establish this exact implication for the original autonomous equation. The resolved Wright equation conjecture is a different delay equation.

Search topics checked on 2026-09-13: `Nicholson blowflies local stability implies global attractivity Smith conjecture proof 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
