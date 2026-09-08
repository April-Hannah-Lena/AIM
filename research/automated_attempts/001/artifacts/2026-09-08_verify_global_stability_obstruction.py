#!/usr/bin/env python3
"""Exact checks for Sol attempt 2's global-stability-constant obstruction.

Only Python's standard-library rational arithmetic is used.  The script checks
the polynomial Rayleigh quotients and the rational/integer comparisons used in
the analytic proof; the Bessel Rayleigh-sum identity itself is derived in the
attempt note from the first coefficients of the J_0 product.
"""

from fractions import Fraction as F
import json


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_derivative(a):
    return [F(i) * a[i] for i in range(1, len(a))]


def integral_01(a):
    return sum((x / F(i + 1) for i, x in enumerate(a)), F(0))


def radial_2d_quotient_in_t(f):
    # t=r^2: ||f||^2 = pi*int f(t)^2 dt and
    # ||grad f||^2 = 4*pi*int t*f'(t)^2 dt.
    mass = integral_01(poly_mul(f, f))
    df2 = poly_mul(poly_derivative(f), poly_derivative(f))
    energy_without_pi = F(4) * integral_01([F(0)] + df2)
    return energy_without_pi / mass


c = F(-2, 5)
f = [F(1), c - 1, -c]  # (1-t)(1+c*t)
radial_q = radial_2d_quotient_in_t(f)

# g(r)=r-r^3, angular mode g(r)cos(theta).  The common angular
# integral cancels from numerator and denominator.
angular_mass = F(1, 4) - F(2, 6) + F(1, 8)
angular_energy = (
    F(1, 2) - F(6, 4) + F(9, 6)
    + F(1, 2) - F(2, 4) + F(1, 6)
)
angular_q = angular_energy / angular_mass

sigma_1 = F(1, 4)
elementary_pair_sum = F(1, 64)
sigma_2 = sigma_1 * sigma_1 - 2 * elementary_pair_sum

checks = {
    "radial_trial_quotient_is_295_over_51": radial_q == F(295, 51),
    "angular_trial_quotient_is_16": angular_q == 16,
    "bessel_fourth_rayleigh_sum_is_1_over_32": sigma_2 == F(1, 32),
    "width_lower_bound_22_over_51_exceeds_1_over_4": F(22, 51) > F(1, 4),
    "twelve_to_17_over_18_exceeds_2_after_powering": 12**17 > 2**18,
    "forty_over_81_sqrt2_is_below_one_half": 80**2 < 2 * 81**2,
}

result = {
    "radial_trial_quotient": f"{radial_q.numerator}/{radial_q.denominator}",
    "angular_trial_quotient": str(angular_q),
    "bessel_fourth_rayleigh_sum": f"{sigma_2.numerator}/{sigma_2.denominator}",
    "width_rational_lower_bound": "22/51",
    "stability_strip_upper_bound": "(40/(81*sqrt(2)))^18 < 2^-18",
    "checks": checks,
    "all_checks_pass": all(checks.values()),
}
print(json.dumps(result, indent=2, sort_keys=True))

if not result["all_checks_pass"]:
    raise SystemExit(1)
