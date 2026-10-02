# 188. A phase transition for continuum hard disks

**Area:** Equilibrium fluids and phase transitions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega`$ be the locally finite subsets $`\omega\subset\mathbb R^2`$ satisfying $`|x-y|\ge1`$ for distinct points. For $`z>0`$, call a probability law $`\mu`$ on $`\Omega`$ a hard-disk Gibbs law if, for every bounded Borel set $`\Lambda`$, its conditional law inside $`\Lambda`$ given the outside configuration is the Poisson process of intensity $`z`$ restricted to $`\Lambda`$, conditioned on the combined configuration having all pair distances at least one.

Does there exist a finite activity $`z>0`$ for which two distinct such infinite-volume Gibbs laws exist? The particles have only the hard-core interaction; no extra attraction, lattice restriction or particle labels are allowed.

## Application

Hard disks isolate the role of excluded volume in freezing. Gibbs nonuniqueness would give a rigorous equilibrium phase transition for this basic continuum fluid model.

## References

- [Marcus Michelen and Will Perkins, *Potential-weighted connective constants and uniqueness of Gibbs measures*, author preprint (2021)](https://arxiv.org/abs/2109.01094), §1 and §1.1.1, unresolved nonuniqueness versus low-activity uniqueness.
- [Heng Guo and Mark Jerrum, *Perfect Simulation of the Hard Disks Model by Partial Rejection Sampling* (2018)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2018.69), introduction and low-density sampling regime.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Michelen–Perkins explicitly distinguish the still-unproved nonuniqueness of finite-range rotationally symmetric continuum interactions from rigorous uniqueness at small activity. Percolation of enlarged disks and numerical liquid–hexatic transition observations do not prove two Gibbs laws for the stated interaction.

Search topics checked on 2026-09-08: continuum hard disks Gibbs nonuniqueness phase transition proof 2025 2026; hard disk rigorous phase transition.
