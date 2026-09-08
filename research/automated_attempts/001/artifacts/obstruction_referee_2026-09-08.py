#!/usr/bin/env python3
"""Exact constants for an abstract spectral obstruction; no domain asserted."""

from fractions import Fraction
from math import isqrt
from pathlib import Path
import json


def ceil_sqrt(n):
    root = isqrt(n)
    return root if root * root == n else root + 1


def a(j):
    return j + ceil_sqrt(j)


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    K = 100
    epsilon = Fraction(1, 4)
    q = K - epsilon
    changed = [j for j in range(1, K + 1) if a(j) > q]
    assert changed == list(range(90, 101))
    assert a(89) == 99 < q < 112 == a(101)
    delta = sum((Fraction(a(j)) - q for j in changed), Fraction())
    assert delta == Fraction(231, 4)
    all_energy_gap = q - Fraction(1, 2)
    assert all_energy_gap == Fraction(397, 4) > delta
    assert q < K

    # For all E >= q, the order-one classical gap is E-1/2 and
    # hence at least this exact positive margin above the block gain.
    margin = all_energy_gap - delta
    assert margin == Fraction(83, 2)

    # Every x in [q-L,q) has n=N_a(x)>=42 and x-n>=ceil(sqrt(n))>=7.
    # This establishes the entire strip, not merely the checked endpoint.
    L = Fraction(50)
    M = Fraction(7)
    strip_start = q - L
    assert strip_start == Fraction(199, 4)
    assert a(42) == 49 <= strip_start
    assert ceil_sqrt(42) == M
    scale = 1 + L / epsilon
    required_root = 1 + epsilon / M
    assert scale == 201
    assert required_root == Fraction(29, 28)
    order_denominator = 128
    lhs = required_root.numerator ** order_denominator
    rhs = int(scale) * required_root.denominator ** order_denominator
    assert lhs <= rhs

    # A second exact certificate directly from the general L=1, sqrt(K)/2
    # estimate; this one gives the weaker cutoff 1/32 without strip refinement.
    generic_M = Fraction(isqrt(K), 2)
    assert isqrt(K) ** 2 == K
    generic_root = 1 + epsilon / generic_M
    assert generic_root == Fraction(21, 20)
    assert 21 ** 32 <= 5 * 20 ** 32

    result = {
        "status": "exact_certificates_passed",
        "scope": "synthetic sequence only; no domain or realizability claim",
        "K": K,
        "q": q,
        "changed_indices": changed,
        "neighbor_levels": {"a_89": a(89), "a_101": a(101)},
        "polya_violation": {"index": K, "value": q, "required_lower_bound": K},
        "order_one_all_energy_certificate": {
            "total_downward_displacement": delta,
            "minimum_classical_gap_for_E_ge_q": all_energy_gap,
            "certified_margin": margin,
            "analytic_argument": "gain=0 for E<=q; gain<=delta and E-1/2>=gap for E>=q",
        },
        "positive_order_cutoff_certificate": {
            "cutoff": Fraction(1, order_denominator),
            "strip_left": strip_start,
            "strip_right_excluded": q,
            "strip_length": L,
            "counting_deficit_lower_bound": M,
            "maximum_positive_counting_defect": epsilon,
            "scale": scale,
            "required_root": required_root,
            "integer_inequality": "29^128 <= 201 * 28^128",
            "integer_left": lhs,
            "integer_right": rhs,
            "all_orders_at_least_cutoff": True,
            "all_energies": True,
            "method": "localized counting-deficit lemma and beta integration",
        },
        "general_theorem_secondary_certificate": {
            "cutoff": "1/32",
            "integer_inequality": "21^32 <= 5 * 20^32",
        },
        "heat_bound": "sum_j exp(-t*b_j) <= 1/t for all t>0",
        "weyl_law": "N_b(E)=E-sqrt(E)+O(1)",
        "limitation": "not all positive orders on a single counterexample sequence",
        "energy_sampling_used": False,
        "uncontrolled_floating_point_used": False,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2, default=encode) + "\n")
    print(json.dumps({"status": result["status"], "output": str(output),
                      "cutoff": "1/128", "polya_violation": "b_100=399/4<100"}))


if __name__ == "__main__":
    main()
