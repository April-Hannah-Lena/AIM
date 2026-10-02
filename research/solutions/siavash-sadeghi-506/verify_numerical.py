#!/usr/bin/env python3
"""Numerical cross-checks for the proposed AIM 506 counterexample.

Requires mpmath and scipy. These are floating-point corroborations, NOT a proof
or rigorous quadrature certificates. The omitted-coordinate tail bound used
below is analytic, but the finite prefix is evaluated numerically.

Run: python3 verify_numerical.py --output numerical_results.json
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
import math
from pathlib import Path
import sys
import mpmath as mp
from scipy.integrate import quad


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def half_integral(fn):
    return mp.quad(fn, [0, mp.mpf('0.5'), 1, 2, 4, mp.inf])


@lru_cache(maxsize=None)
def centered_integral(a_string: str):
    a = mp.mpf(a_string)
    if a <= 1:
        return half_integral(lambda z: mp.exp(-z**4-a*z*z))
    return half_integral(lambda y: mp.exp(-y*y-y**4/(a*a)))


def log_ratio(a, d):
    """Stable log of integral exp[-z^4-a(z-d)^2] / centered integral."""
    a, d = mp.mpf(a), abs(mp.mpf(d))
    if a <= 0:
        raise ValueError('a must be positive')
    denominator = centered_integral(mp.nstr(a, mp.mp.dps))
    if a <= 1:
        # cosh(2ad z)-1 = 2*sinh(ad z)^2 avoids cancellation at tiny a.
        excess = half_integral(
            lambda z: 2*mp.exp(-z**4-a*z*z)*mp.sinh(a*d*z)**2)
        result = -a*d*d + mp.log1p(excess/denominator)
    else:
        root = mp.sqrt(a)
        numerator = half_integral(lambda y: mp.exp(-y*y) * (
            mp.exp(-(d+y/root)**4) + mp.exp(-(d-y/root)**4)))
        result = mp.log(numerator/(2*denominator))
    require(mp.isfinite(result), 'Non-finite log ratio')
    return result


def scipy_direct(a: float, d: float) -> tuple[float, float]:
    # Independent direct convolution quadrature. For a>=1, rescale about
    # each Gaussian center to prevent unresolved narrow integration peaks.
    if a >= 1:
        root = math.sqrt(a)
        num, en = quad(lambda y: math.exp(-y*y-(d+y/root)**4),
                       -math.inf, math.inf, epsabs=2e-13, epsrel=2e-13, limit=300)
        den, ed = quad(lambda y: math.exp(-y*y-y**4/(a*a)),
                       -math.inf, math.inf, epsabs=2e-13, epsrel=2e-13, limit=300)
    else:
        num, en = quad(lambda z: math.exp(-z**4-a*(z-d)**2),
                       -math.inf, math.inf, epsabs=2e-13, epsrel=2e-13, limit=300)
        den, ed = quad(lambda z: math.exp(-z**4-a*z*z),
                       -math.inf, math.inf, epsabs=2e-13, epsrel=2e-13, limit=300)
    require(all(math.isfinite(value) for value in (num, den, en, ed)),
            'Non-finite numerical integral or error estimate')
    require(num > 0 and den > 0, 'Nonpositive numerical integral')
    require(en >= 0 and ed >= 0, 'Negative quadrature error estimate')
    value, estimated_error = math.log(num/den), en/num+ed/den
    require(math.isfinite(value) and math.isfinite(estimated_error),
            'Non-finite numerical log ratio or error estimate')
    return value, estimated_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('numerical_results.json'))
    parser.add_argument('--dps', type=int, default=60)
    args = parser.parse_args()
    if args.dps < 55:
        raise ValueError('At least 55 decimal digits are required')
    mp.mp.dps = args.dps
    checks: list[str] = []
    def check(name, condition):
        require(bool(condition), name)
        checks.append(name)
    def text(x):
        return mp.nstr(x, 45)

    a0 = 2*half_integral(lambda z: mp.exp(-z**4-z*z))
    a2 = 2*half_integral(lambda z: z*z*mp.exp(-z**4-z*z))
    a4 = 2*half_integral(lambda z: z**4*mp.exp(-z**4-z*z))
    kappa = a4/a0
    moment_residual = abs(4*a4+2*a2-a0)
    check('Integration-by-parts moment identity', moment_residual < mp.mpf('1e-50'))
    check('kappa in exact-certificate display interval',
          mp.mpf('0.1330200193') < kappa < mp.mpf('0.1330200209'))
    check('Local quadratic coefficient positive', 1-2*a2/a0 > 0)

    comparisons = []
    for a in [mp.mpf(1)/16, mp.mpf(1)/4, mp.mpf(1), mp.mpf(4), mp.mpf(16)]:
        for d in [mp.mpf(1)/16, mp.mpf(1)/8, mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(1)]:
            value = log_ratio(a,d)
            direct, estimated_error = scipy_direct(float(a),float(d))
            discrepancy = abs(value-mp.mpf(direct))
            check(f'Direct scipy convolution a={a},d={d}', discrepancy < mp.mpf('3e-12'))
            check(f'Universal ratio bounds a={a},d={d}', -a*d*d <= value <= 0)
            if a == 1:
                check(f'Analytic quadratic penalty d={d}', value <= -d*d/144)
                check(f'Certificate-improved penalty d={d}', value <= -d*d/4)
            comparisons.append({'a':text(a),'d':text(d),'log_ratio_mpmath':text(value),
                                'log_ratio_scipy':repr(direct),
                                'absolute_discrepancy':text(discrepancy),
                                'scipy_estimated_log_error':repr(estimated_error)})
    print('Direct convolution checks complete', flush=True)

    blocks = []
    for j in range(1,9):
        d = mp.mpf(2)**(-j)
        value = log_ratio(1,d)
        block = 8**j*value
        check(f'Block suppression j={j}', block <= -mp.mpf(2)**j/144)
        blocks.append({'j':j,'d':text(d),'log_R_over_d_squared':text(value/(d*d)),
                       'log_single_block_factor':text(block),
                       'analytic_log_upper_bound':text(-mp.mpf(2)**j/144)})
    small = mp.mpf('0.0001')
    local_error = abs(-log_ratio(1,small)/(small*small)-4*kappa)
    check('Local quadratic asymptotic', local_error < mp.mpf('1e-8'))

    products = []
    for j in [1,2,4,6]:
        tau = mp.mpf(16)**j
        cutoff = 24
        prefix = mp.fsum(8**i*log_ratio(tau*mp.mpf(16)**(-i), mp.mpf(2)**(-i))
                          for i in range(1,cutoff+1))
        tail = tau*mp.mpf(8)**(-cutoff)/7
        single = 8**j*log_ratio(1,mp.mpf(2)**(-j))
        check(f'Product bounded by selected block j={j}', prefix <= single)
        check(f'Positive tail bound j={j}', tail > 0)
        products.append({'j':j,'tau':str(16**j),'cutoff_block':cutoff,
                         'numerical_log_product_prefix':text(prefix),
                         'analytic_omitted_log_tail_interval': ['-'+text(tail),'0'],
                         'single_block_log_upper_bound':text(single),
                         'warning':'Finite-prefix quadrature error is not certified.'})
        print(f'Product check j={j}: log prefix {mp.nstr(prefix,16)}', flush=True)

    result = {'problem':'AIM 506', 'status':'Floating-point corroboration, not a proof',
              'working_decimal_digits':args.dps,'passed':len(checks),'checks':checks,
              'A0':text(a0),'A2':text(a2),'A4':text(a4),'kappa':text(kappa),
              'moment_identity_absolute_residual':text(moment_residual),
              'quadratic_coefficient':text(4*kappa),
              'local_quadratic_coefficient_error_at_1e_minus4':text(local_error),
              'max_direct_quadrature_discrepancy':text(max(mp.mpf(x['absolute_discrepancy']) for x in comparisons)),
              'direct_quadrature_comparisons':comparisons,'single_block_factors':blocks,
              'full_product_numerical_prefixes':products}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} numerical supporting checks')
    print('Maximum independent quadrature discrepancy:', result['max_direct_quadrature_discrepancy'])
    print('Saved',args.output)
    return 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except (ArithmeticError,ValueError,OSError) as error:
        print('FAIL:',error,file=sys.stderr)
        sys.exit(1)
