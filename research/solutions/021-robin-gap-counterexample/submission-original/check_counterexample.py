#!/usr/bin/env python3
"""Arithmetic and geometric checks for the proposed AIM #021 counterexample.

Run with Python 3.10+; no third-party packages are needed:
    python check_counterexample.py --output checks.json

Exact rational checks verify inequalities used in the analytic manuscript.
Floating-point checks independently reproduce elementary geometric formulas.
This is NOT a finite-element calculation or a formal verification of the PDE proof.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Callable, Sequence


def bisect(fn: Callable[[float], float], left: float, right: float,
           iterations: int = 100) -> float:
    fl, fr = fn(left), fn(right)
    if not (math.isfinite(fl) and math.isfinite(fr)) or fl * fr >= 0:
        raise ValueError("A finite, strict sign-changing bracket is required.")
    for _ in range(iterations):
        middle = (left + right) / 2
        fm = fn(middle)
        if fm == 0:
            return middle
        if fl * fm < 0:
            right = middle
        else:
            left, fl = middle, fm
    return (left + right) / 2


def polygon_measures(t: float) -> tuple[float, float]:
    """Shoelace area and edge-length perimeter of the actual fiber polygon."""
    vertices = [(-1., -1.), (1., -1.), (1.+9.*t, -(1.-t)),
                (1.+9.*t, 1.-t), (1., 1.), (-1., 1.)]
    twice_area = perimeter = 0.0
    for i, (x, y) in enumerate(vertices):
        xx, yy = vertices[(i+1) % len(vertices)]
        twice_area += x*yy-y*xx
        perimeter += math.hypot(xx-x, yy-y)
    return abs(twice_area)/2, perimeter


def facet_vectors(epsilon: float) -> list[tuple[float, float, float]]:
    """The polytope is {X: a dot X < 1 for every returned vector a}."""
    if not math.isfinite(epsilon) or epsilon <= 0:
        raise ValueError("epsilon must be finite and positive")
    e = epsilon
    return [(1.,0.,0.), (-1.,0.,0.), (0.,0.,1/e), (0.,0.,-1/e),
            (0.,-1/e,0.), (0.,1/(10*e),9/(10*e)),
            (0.,1/(10*e),-9/(10*e)),
            (0.9,1/(10*e),0.), (-0.9,1/(10*e),0.)]


def smooth_gauge(point: Sequence[float], epsilon: float, delta: float) -> float:
    """Explicit C-infinity strongly convex defining function Phi_delta.

    Its sublevel set Phi_delta < 1 is the smooth approximating domain.
    The analytic proof establishes a sufficiently-small-delta regime;
    this routine does not supply a certified numerical choice of delta.
    """
    if len(point) != 3 or not all(math.isfinite(v) for v in point):
        raise ValueError("point must contain three finite coordinates")
    if not math.isfinite(delta) or delta <= 0:
        raise ValueError("delta must be finite and positive")
    values = [sum(a*x for a, x in zip(row, point))
              for row in facet_vectors(epsilon)]
    maximum = max(values)
    return (maximum + delta*math.log(sum(math.exp((v-maximum)/delta)
                                         for v in values))
            + delta*sum(x*x for x in point))


def frac_record(x: F) -> dict[str, str | float]:
    return {"exact": str(x), "decimal": float(x)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("checks.json"))
    args = parser.parse_args()

    exact_checks: list[str] = []
    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(name)
        exact_checks.append(name)

    sqrt_lo, sqrt_hi = F(9055,1000), F(9056,1000)
    check("rational enclosure of sqrt(82)", sqrt_lo**2 < 82 < sqrt_hi**2)
    k_lo, k_hi = 2*sqrt_lo-2, 2*sqrt_hi-2
    check("16 < kappa < 17", 16 < k_lo < k_hi < 17)
    check("p(1/2) < 3/2", 4*(7+sqrt_hi)/43 < F(3,2))
    check("central barrier numerator is positive at t=3/4",
          F(3,2)*sqrt_lo-F(67,5) > 0)
    check("central barrier numerator is increasing on [3/4,1]",
          k_lo-F(36,5) > 0)
    check("minimizer t_* > 1/3", 5*k_hi-96 < 0)
    check("minimizer t_* < 1/2", F(25,4)*k_lo-72 > 0)
    check("p(t) <= 2 follows from kappa < 18", k_hi < 18)
    check("uniform Poincare constant is 244", 2*122 == 244)
    check("sqrt(244) < 16", 244 < 16**2)
    check("uniform trace bound < 808", 2*244+20*16 == 808)
    check("fiber perimeter < 25", 6+2*sqrt_hi < 25)
    check("uniform Robin remainder <= 10100", F(25*808,2) == 10100)
    second_derivative_bound = F(450,16)+F(2*221*18,64)
    check("global |p''| bound is below 200", second_derivative_bound < 200)
    check("axial coefficient is below 9, using pi^2 < 10", F(13*10,16) < 9)

    epsilon = F(1,10**12)
    sqrt_epsilon, width = F(1,10**6), F(1,1000)
    check("epsilon roots are exact", sqrt_epsilon**2 == epsilon and width**4 == epsilon)
    check("small-beta condition", epsilon <= F(1,976))
    check("trial support stays away from the ends and x=0", width <= F(1,4))
    check("diameter is the opposite-endpoint distance",
          4+8*epsilon**2 >= 1+122*epsilon**2)
    mass_upper = 1300*sqrt_epsilon+101000*epsilon
    gap_upper = 16*mass_upper/(1-mass_upper)
    check("mass upper bound is below 1", mass_upper < 1)
    check("polyhedral gap upper bound is below 0.021", gap_upper < F(21,1000))

    # Alternating Taylor bounds: sin(2) > sin_lo and cos(2) > cos_lo.
    sin_lo = F(2)-F(2**3,math.factorial(3))+F(2**5,math.factorial(5))-F(2**7,math.factorial(7))
    cos_lo = F(1)-F(2**2,math.factorial(2))+F(2**4,math.factorial(4))-F(2**6,math.factorial(6))
    check("sin(2)+2cos(2)>0, so -2cot(2)<1", sin_lo+2*cos_lo == F(4,63) > 0)
    half_length_squared = 1+2*epsilon**2
    check("half-length < 1.01 < 4/3 < tan(1)",
          half_length_squared < F(101,100)**2 and F(101,100) < F(4,3))
    interval_gap_lower = 3/half_length_squared
    check("interval gap lower bound exceeds 2.9", interval_gap_lower > F(29,10))
    check("strict polyhedral counterexample margin", gap_upper < interval_gap_lower)

    # Independent floating-point elementary checks, not PDE eigenvalue estimates.
    kappa = 2*math.sqrt(82)-2
    area = lambda t: 4+18*t-9*t*t
    perimeter = lambda t: 8+kappa*t
    samples = []
    for t in (0., .125, .25, .375, .5, .625, .75, .875, 1.):
        ag, pg = polygon_measures(t)
        if abs(ag-area(t)) > 1e-12 or abs(pg-perimeter(t)) > 1e-12:
            raise AssertionError("Independent polygon formula check failed")
        samples.append({"t": t, "area": ag, "perimeter": pg, "p": pg/ag})
    t_star = bisect(lambda t: 4*kappa-144+144*t+9*kappa*t*t, 0., 1.)
    q1 = bisect(lambda q: q*math.tan(q)-1, 1e-6, math.pi/2-1e-6)
    q2 = bisect(lambda q: -q/math.tan(q)-1, math.pi/2+1e-6, math.pi-1e-6)

    result = {
        "status": "Arithmetic checks passed; analytic proof is not independently or formally verified.",
        "exact_check_count": len(exact_checks),
        "exact_checks": exact_checks,
        "epsilon": frac_record(epsilon),
        "central_mass_upper": frac_record(mass_upper),
        "polyhedral_gap_upper": frac_record(gap_upper),
        "interval_gap_lower": frac_record(interval_gap_lower),
        "floating_diagnostics": {
            "t_star": t_star, "x_star": 1-t_star,
            "minimum_perimeter_area_ratio": perimeter(t_star)/area(t_star),
            "interval_length_2_first_two_eigenvalues": [q1*q1, q2*q2],
            "interval_length_2_gap": q2*q2-q1*q1,
            "independent_fiber_polygon_checks": samples,
        },
        "limitations": [
            "No continuum eigenvalues of the three-dimensional example were numerically computed.",
            "No quantitative smooth-approximation parameter delta is certified by this script.",
            "The smoothing step and the PDE estimates are justified analytically in the manuscript.",
            "No novelty, peer-review, or formal proof-assistant verification claim is made."
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(f"Passed {len(exact_checks)} exact arithmetic checks and {len(samples)} polygon checks.")
    print("Certified comparison: polyhedral gap < 0.021; interval gap > 2.9.")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
