# 232. Giga’s embedded curve-diffusion conjecture

**Area:** Surface diffusion and geometric evolution

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\gamma:S^1\times[0,T)\to\mathbb R^2$ be the maximal smooth evolution of a smooth closed regular curve by curve diffusion:
$$\partial_t\gamma\cdot\nu=-\partial_s^2\kappa,$$
where $s$ is arclength, $\nu$ is a chosen unit normal and $\kappa$ is the signed curvature in the compatible convention. Tangential velocity only reparametrizes the curve.

If $\gamma(\cdot,t)$ is an embedding for every $0\leq t<T$, must $T=\infty$? Equivalently, must every finite-time singular evolution have lost embeddedness at a strictly earlier regular time?

## Application

Curve diffusion models interface relaxation driven by surface transport. The conjecture asks whether singular behavior can occur while the interface remains a simple closed curve.

## References

- Glen Wheeler, [*Convergence for global curve diffusion flows*](https://doi.org/10.3934/mine.2022001) (2022), the explicitly labeled Giga conjecture following Remark 1.4: precise source of the question.
- Glen Wheeler, [*On the curve diffusion flow of closed plane curves*](https://arxiv.org/abs/1201.3735) (2012 preprint; 2013 publication), abstract and global-existence theorem: stability near circles and the failure of preservation of embeddedness in general.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “Giga conjecture curve diffusion proof 2025 2026” and “embedded curve diffusion finite time singularity”. The cited global-convergence result assumes global existence; it does not prove it from embeddedness. An initially embedded curve can develop a self-intersection, so the hypothesis deliberately concerns every regular time.
