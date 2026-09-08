#!/usr/bin/env python3
"""Independent rational audit of disk trial matrices and low-index constants."""

from fractions import Fraction as Q
from math import factorial
import json


def add(p, q):
    result = p.copy()
    for key, value in q.items():
        result[key] = result.get(key, Q(0)) + value
    return result


def multiply(p, q):
    result = {}
    for (a, b), u in p.items():
        for (c, d), v in q.items():
            key = (a+c, b+d)
            result[key] = result.get(key, Q(0)) + u*v
    return result


def derivative(p, axis):
    result = {}
    for exponents, coefficient in p.items():
        power = exponents[axis]
        if power:
            changed = list(exponents)
            changed[axis] -= 1
            result[tuple(changed)] = coefficient*power
    return result


def disk_integral_divided_by_pi(p):
    total = Q(0)
    for (i, j), coefficient in p.items():
        if i % 2 or j % 2:
            continue
        a, b = i//2, j//2
        moment = Q(factorial(2*a)*factorial(2*b),
                   4**(a+b)*factorial(a)*factorial(b)*factorial(a+b+1))
        total += coefficient*moment
    return total


def main():
    f0 = {(0,0):Q(1), (2,0):Q(-1), (0,2):Q(-1)}
    functions = [f0, multiply(f0,{(1,0):Q(1)}), multiply(f0,{(0,1):Q(1)})]
    mass = [[disk_integral_divided_by_pi(multiply(f,g)) for g in functions] for f in functions]
    stiffness = [[disk_integral_divided_by_pi(add(
        multiply(derivative(f,0),derivative(g,0)),
        multiply(derivative(f,1),derivative(g,1)))) for g in functions] for f in functions]
    assert mass == [[Q(1,3),0,0],[0,Q(1,24),0],[0,0,Q(1,24)]]
    assert stiffness == [[2,0,0],[0,Q(2,3),0],[0,0,Q(2,3)]]
    quotients = [stiffness[j][j]/mass[j][j] for j in range(3)]
    assert quotients == [6,16,16]

    # J0(z)=1-z^2/4+z^4/64+O(z^6), together with its canonical product.
    c2, c4 = -Q(1,4), Q(1,64)
    log_c4 = c4-c2*c2/2
    rayleigh_sum_4 = -2*log_c4
    assert rayleigh_sum_4 == Q(1,32)
    # Positive terms beyond the first imply j01^4>32. Hence 3*j01^2>16.
    assert 9*32 > 16**2

    # Classical 3<pi<22/7 certifies floor(4*pi^2/9)=4.
    dimension3_lower = Q(4,9)*3**2
    dimension3_upper = Q(4,9)*Q(22,7)**2
    assert dimension3_lower == 4
    assert dimension3_upper < 5

    report = {
        "status":"PASS",
        "arithmetic":"exact rational polynomial integration; no numerical Bessel zeros",
        "mass_divided_by_pi":[[str(x) for x in row] for row in mass],
        "stiffness_divided_by_pi":[[str(x) for x in row] for row in stiffness],
        "rayleigh_quotients":[str(x) for x in quotients],
        "rayleigh_sum_inverse_fourth_zeros":str(rayleigh_sum_4),
        "disk_stronger_claim_counterexample":"lambda_3<=16<3*j_01^2=3*lambda_1",
        "dimension3_2beta":"4*pi^2/9",
        "dimension3_2beta_rational_upper":str(dimension3_upper),
        "dimension3_guaranteed_dirichlet_indices":[1,2,3,4],
        "limitations":"standard min-max, Faber-Krahn, Bessel canonical product are analytic dependencies"
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
