#!/usr/bin/env python3
"""Exact finite arithmetic certificate for the accompanying infinite proof.

No floating point, external packages, or finite truncation of an infinite claim.
The infinite extension is the convexity and block-variance proof in the note.
"""

from fractions import Fraction as Q
import json


def main():
    n, m = 262144, 1024
    a = Q(n) + Q(m + 1, 2)
    E = n + m
    E0 = a + Q(1, 4)
    count = n + m - 1

    assert (m - 3) ** 2 <= 6 * n + 4
    yang_at_plateau_per_term = Q((m - 3) ** 2, 4) - Q(3 * n + 2, 2)
    assert yang_at_plateau_per_term < 0

    # Verify the plateau-end polynomial by exact summation formulas.
    k = n - 1
    S1 = Q(k * (k + 3), 2)
    S2 = Q(k * (2 * k * k + 9 * k + 13), 6)
    assert k * a * a - 4 * a * S1 + 3 * S2 == k * yang_at_plateau_per_term

    # The lost variance controls all energies after the block, identically.
    variance = Q(m * (m * m - 1), 12)
    direct_variance = sum((Q(i) - Q(m + 1, 2)) ** 2 for i in range(1, m + 1))
    assert variance == direct_variance

    sqrt_lower = Q(2261, 100)
    assert sqrt_lower > 0
    assert sqrt_lower * sqrt_lower < Q(m - 1, 2)
    assert 32 * 32 == m
    assert E < 514 * 514
    gain_lower = m * sqrt_lower - Q(2, 3) * m * 32
    assert gain_lower == Q(98048, 75)
    assert gain_lower > 2 * 514

    assert count > E0
    assert a < count

    report = {
        "status": "PASS",
        "arithmetic": "integers and exact rational fractions only",
        "n": n,
        "m": m,
        "plateau": str(a),
        "yang_at_plateau_per_active_term": str(yang_at_plateau_per_term),
        "block_variance": str(variance),
        "counting_test_energy": str(E0),
        "counting_excess": str(count - E0),
        "half_riesz_test_energy": E,
        "half_riesz_gain_lower_bound": str(gain_lower),
        "baseline_half_riesz_deficit_upper_bound": 1028,
        "certified_half_riesz_excess_lower_bound": str(gain_lower - 1028),
        "scope": "abstract sequence; no Euclidean-domain realization asserted",
        "infinite_proof": "see companion note: Jensen, exact gap quadratics, and variance identity",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
