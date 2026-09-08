#!/usr/bin/env python3
"""Exact finite algebra supporting 2026-09-08_1310_fold_overlap.md.
No numerical eigenfunction moments or all-domain assertion is certified here.
"""
from fractions import Fraction as F
import json


def add(a, b):
    return [(a[i] if i < len(a) else F(0)) +
            (b[i] if i < len(b) else F(0)) for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [c*x for x in a]


def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def deriv(a):
    return [i*a[i] for i in range(1, len(a))]


def integ(a):
    return [F(0)] + [x/F(i+1) for i, x in enumerate(a)]


def val(a, t):
    return sum((x*t**i for i, x in enumerate(a)), F(0))


# t=(r/R)^2: G^2=t(1-t/3)^2; R^2 H=(1-t)^2+(1-t/3)^2.
mass = mul([F(0), F(1)], mul([F(1), -F(1, 3)], [F(1), -F(1, 3)]))
energy = add(mul([F(1), -F(1)], [F(1), -F(1)]),
             mul([F(1), -F(1, 3)], [F(1), -F(1, 3)]))
mass_integral = val(integ(mass), F(1))
energy_integral = val(integ(energy), F(1))

# n(q)=3 int_0^1 H + int_0^q H; d(q)=3 int_0^1 G^2 + int_0^q G^2.
n = add([3*energy_integral], integ(energy))
d = add([3*mass_integral], integ(mass))
P = scale(add(mul([F(3), F(1)], n), scale(d, -12)), F(27))
derivative_certificate = add(
    add([F(16)], scale([F(1), -F(1)], F(24))),
    mul([F(206), F(4)], mul([F(1), -F(1)], [F(1), -F(1)])))
theta = F(1, 20)
coarse_bound_without_pi = F(3)/(1-theta)*(F(112, 33)+F(72, 11)*theta/(1-theta))
# Four distinct preimages, using rational points away from the axes.
preimages = [(F(sx, 3), F(sy, 5)) for sx in (-1, 1) for sy in (-1, 1)]

checks = {
    "mass_polynomial": mass == [0, 1, -F(2, 3), F(1, 9)],
    "energy_polynomial": energy == [2, -F(8, 3), F(10, 9)],
    "mass_integral_11_over_36": mass_integral == F(11, 36),
    "energy_integral_28_over_27": energy_integral == F(28, 27),
    "radial_energy_derivative_negative_on_unit_interval":
        deriv(energy) == [-F(8, 3), F(20, 9)] and val(deriv(energy), F(1)) == -F(4, 9),
    "energy_joins_constant_extension": val(energy, F(1)) == F(4, 9),
    "coarse_bound_at_one_twentieth": coarse_bound_without_pi == F(46880, 3971),
    "coarse_margin": 12-coarse_bound_without_pi == F(772, 3971),
    "quartic_threshold_identity": P == [-45, 246, -216, 66, 1],
    "positive_derivative_certificate": deriv(P) == derivative_certificate,
    "threshold_bracket": val(P, F(3, 14)) < 0 < val(P, F(3, 13)),
    "one_fifteenth_maps_to_three_fourteenths": 3*F(1, 15)/(1-F(1, 15)) == F(3, 14),
    "four_distinct_preimages": len(set(preimages)) == 4 and
        {(abs(x), abs(y)) for x, y in preimages} == {(F(1, 3), F(1, 5))},
}
result = {
    "all_checks_pass": all(checks.values()),
    "checks": checks,
    "P_at_three_fourteenths": str(val(P, F(3, 14))),
    "P_at_three_thirteenths": str(val(P, F(3, 13))),
    "sharp_density_quotient_over_pi_at_one_fifteenth":
        str((3+F(3, 14))*val(n, F(3, 14))/val(d, F(3, 14))),
    "scope": "Finite algebra only; analytic proof and unproved moment-existence conditions are in the companion note.",
}
print(json.dumps(result, indent=2, sort_keys=True))
assert result["all_checks_pass"]

