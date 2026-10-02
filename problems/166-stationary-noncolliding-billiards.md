# 166. A stationary isotropic gas of freely moving non-colliding disks

**Area:** Kinetic geometry and hard-particle systems

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a probability law for a nonempty locally finite set $`S\subset\mathbb R^2`$ with velocity marks $`v:S\to\mathbb R^2`$ satisfying all of the following almost surely?

For deterministic $`0<m<M<\infty`$, every speed lies in $`[m,M]`$ and distinct particles have different velocities. For all $`x\ne y`$ in $`S`$ and all $`t\in\mathbb R`$,

```math
|(x+tv(x))-(y+tv(y))|\ge1.
```

The law must be invariant under translations, simultaneous rotations of positions and velocities, and the evolution $`(x,v(x))\mapsto(x+tv(x),v(x))`$. It must also be ergodic under translations: every translation-invariant event has probability zero or one.

## Application

This asks whether a statistically homogeneous and isotropic hard-disk system can move forever without any collisions while retaining distinct particle velocities.

## References

1. Itai Benjamini, Alexander Shamov and Barak Weiss, *Non-colliding billiards in the plane* (2026), §1. [Version 2](https://arxiv.org/html/2605.23575v2). The May 27 revision adds Weiss and discusses ergodic and isotropic formulations; the May 22 version states the positive lower-speed requirement used here.

2. Yaar Solomon and Barak Weiss, *Dense forests and Danzer sets*, Annales Scientifiques de l’École Normale Supérieure 49 (2016), 1049–1070. [Paper](https://arxiv.org/abs/1406.3807). Geometric background on uniformly discrete configurations, cited by Benjamini–Shamov; it is not a solution of the moving-disk question.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The May 2026 primary paper explicitly poses this problem. Both May 22 and May 27 versions were checked. Searches for “Non-colliding billiards in the plane Benjamini Shamov” and “2605.23575 stationary isotropic solution” found no later resolution. The revision also asks a weaker ergodic version without the positive lower-speed bound. Its lattice construction does not supply all the invariances required here.
