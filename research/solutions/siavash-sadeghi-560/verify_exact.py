#!/usr/bin/env python3
"""Exact supporting checks for the proposed proof of AIM Problem 560.

Python standard library only. No network access and no floating-point arithmetic
are used in the checks or the certified example enclosures. This is NOT a
proof-assistant verification of the universal analytic theorem. The PDF contains
that proof; this program checks finite polynomial identities and examples.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
from typing import Iterable

COUNT = 0


def require(condition: bool, label: str) -> None:
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1


def c(n: int) -> F:
    return F(comb(2 * n, n), 4**n)


def eval_poly(p: Iterable[F], u: F) -> F:
    out = F(0)
    for a in reversed(list(p)):
        out = out * u + a
    return out


def sqrt_interval(a: F, digits: int = 50) -> tuple[F, F]:
    if a < 0:
        raise ValueError("Cannot enclose a negative real square root")
    scale = 10**digits
    k = isqrt(a.numerator * scale * scale // a.denominator)
    lo, hi = F(k, scale), F(k + 1, scale)
    require(lo * lo <= a < hi * hi, "square-root enclosure")
    return lo, hi


def interval_product(a: tuple[F, F], b: tuple[F, F]) -> tuple[F, F]:
    vals = [x * y for x in a for y in b]
    return min(vals), max(vals)


def tail_geometric(u: F, first: int) -> F:
    return u**first / (1 - u)


def tail_n_geometric(u: F, first: int) -> F:
    return u**first * (first - (first - 1) * u) / (1 - u)**2


def outward_decimal(a: F, digits: int, upper: bool) -> str:
    """Round a rational toward +/- infinity, not to nearest."""
    scale = 10**digits
    numerator = a.numerator * scale
    k = -((-numerator) // a.denominator) if upper else numerator // a.denominator
    sign = "-" if k < 0 else ""
    k = abs(k)
    return f"{sign}{k // scale}.{k % scale:0{digits}d}"


def certify_example(q: F, z: F, lam: F, cutoff: int = 100) -> dict:
    """Enclose the full, infinite-series value of I(s,v,lambda) exactly.

    a_n = rational_part_n + sqrt((1-q^2)/(1-qz))*radical_part_n.
    The tail uses c_n <= 1 and w_n <= (1-q)q^(2n)/lambda.
    """
    require(0 < q < 1 and -1 < z < q and lam > 0, "example domain")
    A = 1 - q * z
    R = sqrt_interval((1 - q*q) / A)
    rat = F(0)
    rad = F(0)
    for n in range(cutoff + 1):
        zn = z**n
        dz = n * z**(n - 1) if n else F(0)
        weight = (1-q) * q**(2*n) / ((1-q)*q**(2*n) + lam)
        rat += weight*c(n)*(A*zn*dz - q*zn*zn/2)
        rad += weight*c(n)*(-A*q**n*dz + q*(q*z)**n/2)
    partial = interval_product((rad, rad), R)
    partial = (partial[0]+rat, partial[1]+rat)
    x = abs(z)
    if x == 0:
        require(cutoff >= 1, "zero-z tail cutoff")
        tail = F(0)
    else:
        first = cutoff + 1
        u, t = q*q*x*x, q**3*x
        tail = (1-q)/lam*(
            A/x*(tail_n_geometric(u, first)+tail_n_geometric(t, first))
            + q/2*(tail_geometric(u, first)+tail_geometric(t, first))
        )
    S = (partial[0]-tail, partial[1]+tail)
    s = q/(1-q)**2
    v = q*(1+z)/((1-q)*(1-q*z))
    zp = (1-q*q)/(q*(1+(1-q)*v)**2)
    K2 = sqrt_interval(1/(1-q*q))
    Iv = interval_product(S, K2)
    Iv = (2*v*zp*Iv[0], 2*v*zp*Iv[1])
    require(Iv[1] < 0, "certified strictly negative infinite-series value")
    lo = outward_decimal(Iv[0], 20, False)
    hi = outward_decimal(Iv[1], 20, True)
    require(F(lo) <= Iv[0] <= Iv[1] <= F(hi), "outward-rounded report")
    return {
        "q": str(q), "z": str(z), "s": str(s), "v": str(v),
        "lambda": str(lam), "cutoff": cutoff,
        "certified_I_lower": lo, "certified_I_upper": hi,
        "method": "rational arithmetic, integer-square-root enclosures, geometric tail bound"
    }


def run(output: Path | None) -> None:
    # Differential identity: 2(1-u) P_N'(u)-P_N(u) = -(2N+1)c_N u^N.
    for N in range(101):
        p = [c(n) for n in range(N+1)]
        C = (2*N+1)*c(N)
        lhs = [-a for a in p]
        for n in range(1, N+1):
            lhs[n-1] += 2*n*p[n]
            lhs[n] -= 2*n*p[n]
        rhs = [F(0)]*N + [-C]
        require(lhs == rhs, f"polynomial differential identity N={N}")
        require(sum(p) == C, f"P_N(1) identity N={N}")
        require(C*C <= 2*N+1, f"central coefficient bound N={N}")
        if N:
            lhs_rec = (2*N+1)*c(N)**2
            rhs_rec = (2*N-1)*c(N-1)**2*(1-F(1,4*N*N))
            require(lhs_rec == rhs_rec, f"coefficient bound recurrence N={N}")
        # sum u^k - (2N+1)u^N = sum_{k<N} u^k(1-u^(N-k))^2.
        lhs_sos = [F(1)]*(2*N+1)
        lhs_sos[N] -= 2*N+1
        rhs_sos = [F(0)]*(2*N+1)
        for k in range(N):
            rhs_sos[k] += 1
            rhs_sos[N] -= 2
            rhs_sos[2*N-k] += 1
        require(lhs_sos == rhs_sos, f"geometric SOS identity N={N}")
        for u in (F(1,100), F(1,4), F(1,2), F(9,10), F(99,100)):
            P = eval_poly(p, u)
            mu = sum(n*p[n]*u**n for n in range(N+1))/P
            mu_inf = u/(2*(1-u))
            require(mu < mu_inf, f"truncated mean bound N={N},u={u}")
            require(mu == mu_inf*(1-C*u**N/P), f"truncated mean identity N={N},u={u}")
            require(C*C*(1-u)*u**N < 1, f"boundary coefficient bound N={N},u={u}")

    # Mixed derivative positivity, checked after eliminating all square roots.
    for q in (F(1,10), F(1,2), F(2,3), F(9,10), F(99,100)):
        for fx, fy in ((F(1,4),F(1,2)),(F(1,2),F(3,4)),(F(1),F(1))):
            x, y = q*fx, q*fy
            u=x*y
            ax=q*x/(2*(1-q*x)); ay=q*y/(2*(1-q*y))
            for N in (0,1,2,5,10,30):
                weights=[c(n)*u**n for n in range(N+1)]
                P=sum(weights)
                mu=sum(n*weights[n] for n in range(N+1))/P
                var=sum((n-mu)**2*weights[n] for n in range(N+1))/P
                direct=sum(weights[n]*(n-ax)*(n-ay) for n in range(N+1))/P
                require(direct == var+(mu-ax)*(mu-ay), "mixed-derivative covariance identity")
                require(direct > 0, "mixed-derivative positivity sample")

    # A positive individual summand: the proof is not a termwise sign argument.
    q,z=F(9,10),F(3,5)
    require((1-q*z)*z*z > (1-q*q)*q*q, "positive individual coefficient difference")
    require(1-F(3,2)*q*z > 0, "positive individual coefficient derivative")

    examples = [
        (F(1,3), F(-1,2), F(1,5)),
        (F(2,3), F(-1,2), F(1,100)),
        (F(2,3), F(0), F(1,10)),
        (F(2,3), F(1,3), F(1)),
        (F(2,3), F(3,5), F(1,1000)),
        (F(4,5), F(1,2), F(1,20)),
        (F(9,10), F(3,5), F(1,10)),
    ]
    certificates=[certify_example(*args) for args in examples]
    print(f"PASS: {COUNT} exact supporting checks")
    print("Certified enclosures of I = integral y h'(y) dN(0,v):")
    for item in certificates:
        print(f"  s={item['s']}, v={item['v']}, lambda={item['lambda']}: "
              f"[{item['certified_I_lower']}, {item['certified_I_upper']}]")
    print("Scope: supporting identities and examples, NOT formal verification of the universal theorem.")
    if output:
        output.write_text(json.dumps({"checks": COUNT, "certificates":certificates}, indent=2)+"\n")
        print(f"Wrote {output.name}")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write exact outward-rounded certificates")
    args=parser.parse_args()
    run(args.json)
