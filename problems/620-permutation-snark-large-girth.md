# 620. Permutation snarks without five-cycles

**Area:** Computational graph theory and edge colouring

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

A *cycle permutation graph* is a finite simple cubic graph consisting of two disjoint cycles of equal length, with a perfect matching between their vertex sets. Equivalently, it admits a spanning 2-factor with exactly two chordless cycles. A *permutation snark* is such a graph that has no proper 3-edge-colouring.

Does there exist a permutation snark with girth at least six, where girth is the length of a shortest cycle? Construct an example, or prove that every cycle permutation graph of girth at least six has a proper 3-edge-colouring.

This asks for one example with girth at least six, without prescribing its order modulo eight or requiring arbitrarily large girth.

## Application

High-girth examples would separate global edge-colouring obstructions from the short cycles appearing in all currently known permutation snarks. The question provides a concrete benchmark for graph generators, colouring solvers and verifiable exhaustive searches.

## References

1. J. Goedgebeur, J. Renders and S. Van Overberghe, [Generation of cycle permutation graphs and permutation snarks](https://doi.org/10.1090/mcom/4247), *Mathematics of Computation*, electronically published 13 August 2026. Section 3, Proposition 5 and the preceding discussion; [arXiv:2411.12606v4](https://arxiv.org/abs/2411.12606v4).
2. E. Máčajová and M. Škoviera, [Permutation snarks of order 2 (mod 8)](https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/1313), *Acta Mathematica Universitatis Comenianae* **88** (2019), 929–934. Section 4.

## Status review

**Known cases:** Every permutation snark has girth at least five, and all known examples have girth exactly five. Cycle permutation graphs with arbitrarily large girth exist, but this does not establish failure of 3-edge-colourability. The exhaustive computations in [1] imply that a permutation snark of girth at least six would have at least 50 vertices.

**Remaining target:** Determine whether the girth-five restriction holds for every permutation snark, beyond the finite orders already checked. This is distinct from the missing order-residue problem: no residue class is fixed here.

The August 2026 journal article still reports this existence question unresolved. Current literature, arXiv, public GitHub, native Zenodo and Palomar searches found no resolution or matching announcement. The authors' public generator repository reports finite computations and no larger-girth example. No equivalent catalogue problem was found.
