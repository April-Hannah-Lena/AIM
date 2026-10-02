#!/usr/bin/env python3
"""Exact supporting certificates for the proposed AIM 506 counterexample.

Python standard library only. All tests and integral enclosures use integers and
fractions, never floating-point decisions. These certificates verify arithmetic
and a one-dimensional integral bound; they do NOT formally verify the analytic
arguments about probability measures, differentiation, or limits in the paper.

Run: python3 verify_exact.py --output exact_results.json
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def exp_bounds(x: Q, n: int = 100) -> tuple[Q, Q]:
    """Rational bounds on exp(x), x >= 0, by a positive series and tail."""
    if x < 0 or n < 0 or Q(n + 2) <= x:
        raise ValueError("Need x >= 0, n >= 0, and n + 2 > x")
    term = Q(1)
    lower = term
    for k in range(1, n + 1):
        term *= x / k
        lower += term
    first_omitted = term * x / (n + 1)
    upper = lower + first_omitted / (1 - x / (n + 2))
    return lower, upper


def integrated_taylor(moment: int, degree: int, cutoff: int = 2) -> Q:
    """Integral over [-L,L] of x^moment * S_degree(x^4+x^2).

    S_N(u) = sum_{m=0}^N (-u)^m/m!. For u>=0, odd N is a lower
    bound for exp(-u), and even N is an upper bound (Taylor remainder).
    Every polynomial integral here is evaluated as an exact rational.
    """
    if moment < 0 or moment % 2 or degree < 0 or cutoff <= 0:
        raise ValueError("Need a nonnegative even moment and valid cutoff/degree")
    total = Q(0)
    for m in range(degree + 1):
        power_integral = sum(
            (Q(2 * comb(m, k) * cutoff ** (moment + 2*m + 2*k + 1),
               moment + 2*m + 2*k + 1) for k in range(m + 1)), Q(0)
        )
        total += (-1 if m % 2 else 1) * power_integral / factorial(m)
    return total


def decimal_string(x: Q, digits: int = 45) -> str:
    """Display only; exact comparisons never use this decimal conversion."""
    with localcontext() as context:
        context.prec = digits
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def interval_record(lo: Q, hi: Q) -> dict[str, str]:
    require(lo <= hi, "Reversed interval")
    return {"lower_fraction": str(lo), "upper_fraction": str(hi),
            "lower_decimal_approx": decimal_string(lo),
            "upper_decimal_approx": decimal_string(hi)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("exact_results.json"))
    args = parser.parse_args()
    checks: list[str] = []

    def check(name: str, value: bool) -> None:
        require(value, name)
        checks.append(name)

    check("block endpoints for j=1,...,16", all(
        sum(8**i for i in range(1, j+1)) == 8*(8**j-1)//7
        for j in range(1, 17)))
    check("block scale square sum = 2^-j", all(
        8**j * Q(1,4**j)**2 == Q(1,2**j) for j in range(1, 17)))
    check("block formal energy = 2^-j", all(
        8**j * Q(1,2**j)**4 == Q(1,2**j) for j in range(1, 17)))
    check("block shift norm square = 8^-j", all(
        8**j * Q(1,8**j)**2 == Q(1,8**j) for j in range(1, 17)))
    check("sum gamma_k^2 = 1", Q(1,2)/(1-Q(1,2)) == 1)
    check("Q(h) = 1", Q(1,2)/(1-Q(1,2)) == 1)
    check("norm(h)^2 = 1/7", Q(1,8)/(1-Q(1,8)) == Q(1,7))
    check("standardized shift h/gamma = 2^-j", all(
        Q(1,8**j)/Q(1,4**j) == Q(1,2**j) for j in range(1, 17)))
    check("quadratic standardized shift in block = 2^j", all(
        8**j * Q(1,2**j)**2 == 2**j for j in range(1, 17)))
    check("tau_j gamma_j^2 = 1", all(
        16**j * Q(1,4**j)**2 == 1 for j in range(1, 17)))
    check("analytic block exponent = 2^j/144", all(
        Q(8**j,144) * Q(1,2**j)**2 == Q(2**j,144)
        for j in range(1, 17)))
    check("finite-prefix log-product tail coefficient", all(
        Q(1,8**(k+1))/(1-Q(1,8)) == Q(1,7*8**k)
        for k in range(0, 17)))

    elo, ehi = exp_bounds(Q(1), 40)
    check("5/2 < e < 3", elo > Q(5,2) and ehi < 3)
    check("e^2 < 9", ehi**2 < 9)
    check("e^2 > 4", elo**2 > 4)
    check("e^3 > 27/2", elo**3 > Q(27,2))
    check("elementary kappa lower-bound arithmetic", Q(1,16*9*2) == Q(1,288))
    check("elementary quadratic penalty constant", 2*Q(1,288) == Q(1,144))

    r = Q(1,8)
    s0 = 1/(1-r)
    s1 = r/(1-r)**2
    check("head sum constant = 184/49", 3*s0+2*s1 == Q(184,49))
    check("total Laplace lower-bound constant < 5", 3*s0+2*s1+Q(1,2) == Q(417,98) < 5)
    check("quantitative radius exponent tau r^2 = 9*64^j", all(
        16**(2*j) * Q(3,2**j)**2 == 9*64**j for j in range(1, 13)))
    check("quantitative tail exponent = 4*64^j", all(
        9*64**j - 5*8**(2*j) == 4*64**j for j in range(1, 13)))
    check("j=4 ratio bound below e^-1", exp_bounds(Q(7,9),40)[0] > 2)

    # P(2)=20, P'(2)=36. For x>=2, P(x)>=20+36(x-2).
    # x^4<=16 exp(2(x-2)), so two-sided tails are bounded by
    # exp(-20)/18 for moment 0, and 16 exp(-20)/17 for moment 4.
    e20lo, e20hi = exp_bounds(Q(20), 100)
    e_minus20_upper = 1/e20lo
    a0lo = integrated_taylor(0,101)
    a0hi = integrated_taylor(0,100) + e_minus20_upper/18
    a4lo = integrated_taylor(4,101)
    a4hi = integrated_taylor(4,100) + Q(16,17)*e_minus20_upper
    check("positive ordered A0 integral enclosure", 0 < a0lo < a0hi)
    check("positive ordered A4 integral enclosure", 0 < a4lo < a4hi)
    klo, khi = a4lo/a0hi, a4hi/a0lo
    check("certified kappa > 1/8", klo > Q(1,8))
    check("certified kappa < 1/4", khi < Q(1,4))
    check("certified kappa in (0.13302001,0.13302003)",
          Q(13302001,10**8) < klo < khi < Q(13302003,10**8))
    check("improved quadratic penalty constant exceeds 1/4", 2*klo > Q(1,4))
    check("A0 enclosure width < 2e-10", a0hi-a0lo < Q(2,10**10))
    check("A4 enclosure width < 2e-9", a4hi-a4lo < Q(2,10**9))

    result = {
        "problem": "AIM 506, aa776a01d7d48a79f93251af11fde9454b0aea95",
        "evidence_status": "Supporting exact certificates, not a formal proof audit",
        "passed": len(checks), "checks": checks,
        "construction": {"block_size": "8^j", "gamma_on_block": "4^-j",
                         "h_on_block": "8^-j", "Q_h": "1", "h_norm_squared": "1/7"},
        "A0": interval_record(a0lo,a0hi), "A4": interval_record(a4lo,a4hi),
        "kappa": interval_record(klo,khi),
        "bounds": {"analytic": "L_h(16^j)/L_0(16^j) <= exp(-2^j/144)",
                   "certificate_improved": "L_h(16^j)/L_0(16^j) <= exp(-2^j/4)",
                   "ball_sequence": "exists 0<r_j<3*2^-j with ball_ratio < 2*exp(-4^j/144)"},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(checks)} exact supporting checks")
    print("kappa lower (decimal display):", decimal_string(klo,30))
    print("kappa upper (decimal display):", decimal_string(khi,30))
    print("Certified improvement: kappa > 1/8; quadratic penalty >= 1/4.")
    print("Saved", args.output)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ArithmeticError, OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
