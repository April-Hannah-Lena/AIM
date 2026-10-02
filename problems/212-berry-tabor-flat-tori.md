# 212. Poisson nearest-neighbor spacings on almost every flat torus

**Area:** Quantum integrability; spectral statistics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For $`\alpha=(\alpha_1,\alpha_2,\alpha_3)\in\mathbb R^3`$ with $`\alpha_1>0`$ and $`4\alpha_1\alpha_3>\alpha_2^2`$, define

```math
q_\alpha(m,n)=\alpha_1m^2+\alpha_2mn+\alpha_3n^2.
```

Arrange the positive numbers

```math
\frac{\pi q_\alpha(m,n)}{\sqrt{4\alpha_1\alpha_3-\alpha_2^2}},\qquad (m,n)\in\mathbb Z^2,\quad m>0\text{ or }(m=0,n>0),
```

in increasing order with multiplicity as $`\lambda_1\le\lambda_2\le\cdots`$. The normalization gives asymptotic mean spacing one and removes the automatic multiplicity from $`(m,n)\leftrightarrow(-m,-n)`$.

For Lebesgue-almost every such $`\alpha`$, is it true simultaneously for every $`s\ge0`$ that

```math
\lim_{N\to\infty}\frac1N\#\{j\le N:\lambda_{j+1}-\lambda_j\le s\}=1-e^{-s}?
```

## Application

These quadratic-form values are the energy levels of a free quantum particle on a flat torus. The conjecture tests whether integrable classical dynamics produces statistically uncorrelated quantum levels.

## References

1. Christoph Aistleitner, Valentin Blomer, and Maksym Radziwiłł, [Triple correlation and long gaps in the spectrum of flat tori](https://arxiv.org/abs/1809.07881), *J. Eur. Math. Soc.* 26 (2024), 41–74. Sections 1.1–1.2, equations (1.1)–(1.2) and the following nearest-neighbor discussion, specify the model and conjecture.
2. Jens Marklof, [Spectral form factors of rectangle billiards](https://people.maths.bris.ac.uk/~majm/bib/spectral.pdf), *Commun. Math. Phys.* 199 (1998), 169–202. Introduction, equations (1)–(6), explains the Berry–Tabor prediction and why pair correlations are a weaker assertion.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2024 theorem controls averaged triple correlations and gives lower bounds on long gaps. Neither it nor Poisson pair correlation proves the nearest-neighbor distribution. Searches, including a February 2026 research lecture by Marklof on progress toward these conjectures, did not locate the full almost-everywhere spacing law.

**Search audit:** Queries: “flat tori Poisson nearest neighbor gaps proof 2026”, “Berry Tabor rectangular billiards Poisson 2026”, “Aistleitner Blomer Radziwill triple correlation later results”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
