# 184. Coexistence in a three-strain colicin model

**Area:** Spatial microbiology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $\mathbb Z^2$, a site has state $0,1,2$ or $3$, with $0$ vacant. Put $f_i(x,\eta)=\frac14\sum_{|y-x|_1=1}\mathbf1_{\{\eta(y)=i\}}$. Vacant sites change to type $i$ at rate $\beta_i f_i$. Types $1$ and $2$ die at rate one; type $3$ dies at rate $1+\gamma_1f_1+\gamma_2f_2$. Do there exist parameters

$$
0<\beta_1<\beta_2<\beta_3,\qquad 0<\gamma_2<\gamma_1
$$

for which there is a stationary probability measure $\nu$, invariant under lattice translations, satisfying

$$
\nu\bigl(\#\{x\in\mathbb Z^2:\eta(x)=i\}=\infty\text{ for every }i=1,2,3\bigr)=1?
$$

The support condition requires coexistence within a configuration, excluding mixtures of laws in which one or more strains are absent.

## Application

The two slower-growing strains produce different levels of toxin, while the fastest strain is toxin-sensitive. Coexistence would demonstrate how local chemical interference sustains microbial diversity.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, book manuscript of 2 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf), §4.5.2, Open Problem 4.5.3 and its transition-rate table.
- [Rick Durrett and Simon A. Levin, *Allelopathy in spatially distributed populations* (1997)](https://doi.org/10.1006/jtbi.1996.0292), the underlying spatial competition mechanism.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The new book explicitly asks whether three-strain coexistence occurs. The statement asks for existence of suitable parameters, rather than promoting illustrative simulation values to a proved or separately conjectured parameter region.

Search topics checked on 2026-09-08: three species colicin spatial model coexistence proof; Durrett three strain allelopathy open problem 2026.
