#!/usr/bin/env python3
"""Independent numerical cross-checks for AIM 560 (not a proof).

Requires numpy, scipy, and mpmath. Includes a direct Gaussian-kernel Nystrom
calculation that does not use the proposed spectral reduction, a finite-prefix
stress test, and comparisons with the two known endpoint formulas.
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
from scipy.linalg import solve
from scipy.special import roots_hermitenorm


def spectral_integral(s: float, v: float, lam: float | str, dps: int = 70) -> mp.mpf:
    """High-precision series, with a conservative fixed cutoff.

    This routine is numerical, not interval arithmetic; see verify_exact.py
    for certified infinite-series enclosures at the listed rational examples.
    """
    with mp.workdps(dps):
        s,v=mp.mpf(str(s)),mp.mpf(str(v))
        q=(mp.sqrt(1+4*s)-1)/(mp.sqrt(1+4*s)+1)
        z=((1-q)*v/q-1)/(1+(1-q)*v)
        A=1-q*z; R=mp.sqrt((1-q*q)/A)
        zp=(1-q*q)/(q*(1+(1-q)*v)**2)
        # All modes including the nonconstant degree-zero eigenfunction.
        r=max(abs(z)**2,q*abs(z))
        cutoff=max(60,int(mp.ceil((dps+15)*mp.log(10)/(-mp.log(r)))) if r else 60)
        total=mp.mpf(0); cn=mp.mpf(1)
        for n in range(cutoff+1):
            zn=z**n
            dz=n*z**(n-1) if n else mp.mpf(0)
            rho=(1-q)*q**(2*n)
            if lam == "chi2": w=mp.mpf(1)
            elif lam == "mmd": w=rho
            else: w=rho/(rho+mp.mpf(str(lam)))
            an=cn*(A*zn*dz-q*zn*zn/2+R*(-A*q**n*dz+q*(q*z)**n/2))
            total+=w*an
            cn*=mp.mpf(2*n+1)/(2*n+2)
        return +(2*v*zp/mp.sqrt(1-q*q)*total)


def nystrom_integral(s: float, v: float, lam: float, nodes: int) -> float:
    """Discretize T on L2(N(0,s)), solve its resolvent, integrate in y exactly."""
    x,weights=roots_hermitenorm(nodes)
    weights=weights/np.sqrt(2*np.pi)
    # Extreme zero quadrature weights add no information and cannot be divided by.
    keep=weights>0
    x=np.sqrt(s)*x[keep]; weights=weights[keep]
    sw=np.sqrt(weights)
    kernel=np.exp(-0.5*(x[:,None]-x[None,:])**2)
    T=sw[:,None]*kernel*sw[None,:]
    ratio=np.sqrt(s/v)*np.exp(-0.5*(1/v-1/s)*x*x)
    rhs=sw*(ratio-1)
    a=solve(T+lam*np.eye(len(x)),rhs,assume_a="pos",check_finite=True)
    # E[Y (x-Y) k(x,Y)] for Y~N(0,v): an elementary Gaussian integral.
    inner=v/(1+v)*(x*x/(1+v)-1)*np.exp(-x*x/(2*(1+v)))/np.sqrt(1+v)
    return float(np.dot(sw*a,inner))


def prefix_stress_test() -> tuple[int,float]:
    qvals=np.array([.01,.05,.1,.25,.5,.65,.8,.9,.97,.99])
    checked=0; maximum=-np.inf
    for q in qvals:
        z=np.linspace(-.995,q-1e-5,181)
        A=np.sqrt(1-q*z); B=np.sqrt(1-q*q)
        cn=1.; zn=np.ones_like(z); qn=1.; dz=np.zeros_like(z)
        S=np.zeros_like(z)
        for n in range(201):
            delta=A*zn-B*qn
            # Stabilize subtraction near z=q for nonnegative z.
            positive=z>0
            delta[positive]=B*qn*np.expm1(
                .5*np.log1p(q*(q-z[positive])/(1-q*q))
                +n*np.log1p((z[positive]-q)/q))
            S+=cn*delta*(A*dz-q*zn/(2*A))
            if not np.all(np.isfinite(S)) or not np.all(S<0):
                raise AssertionError(f"Nonfinite or nonnegative prefix detected at q={q}, n={n}")
            checked+=len(z)
            maximum=max(maximum,float(np.max(S)))
            dz=(n+1)*zn
            zn=zn*z;qn*=q;cn*=(2*n+1)/(2*n+2)
    return checked,maximum


def main(out: Path | None) -> None:
    rows=[]
    cases=[(.75,3/14,.2),(3.,.75,.01),(3.,1.5,.1),(3.,2.7,1.),
           (6.,.75,.01),(6.,2.,.1),(6.,24/7,1.),(6.,16/3,.001),
           (20.,5.,.02),(20.,10.,.05),(20.,18.,1.),(90.,720/23,.1)]
    for s,v,lam in cases:
        spec=float(spectral_integral(s,v,lam))
        n256=nystrom_integral(s,v,lam,256)
        n512=nystrom_integral(s,v,lam,512)
        n2048=nystrom_integral(s,v,lam,2048)
        values=(spec,n256,n512,n2048)
        if not all(np.isfinite(value) and value<0 for value in values):
            raise AssertionError(f"Nonfinite or nonnegative integral for {(s,v,lam)}: {values}")
        err=abs(n2048-spec)
        if not np.isfinite(err) or err>2e-10:
            raise AssertionError(f"Nystrom comparison error {err} for {(s,v,lam)}")
        rows.append({"s":s,"v":v,"lambda":lam,"spectral":spec,
                     "nystrom_256":n256,"nystrom_512":n512,
                     "nystrom_2048":n2048,"absolute_error_2048":err})
    # Independent closed-form endpoint checks, using 70-digit arithmetic.
    endpoint_errors=[]
    mp.mp.dps=70
    for s0,v0 in [(3,1),(6,2),(20,10)]:
        s,v=mp.mpf(s0),mp.mpf(v0)
        chi=-s*(s-v)/(mp.sqrt(v)*(2*s-v)**mp.mpf("1.5"))
        mmd=v*((1+s+v)**mp.mpf("-1.5")-(1+2*v)**mp.mpf("-1.5"))
        for label,exact in [("chi2",chi),("mmd",mmd)]:
            value=spectral_integral(s0,v0,label)
            if not all(mp.isfinite(item) and item<0 for item in (value,exact)):
                raise AssertionError(f"Nonfinite or nonnegative endpoint value: {label}: {value}")
            err=abs(value-exact)
            if not mp.isfinite(err) or err>mp.mpf("1e-60"):
                raise AssertionError(f"Endpoint mismatch: {label}: {err}")
            endpoint_errors.append(str(err))
    count,maximum=prefix_stress_test()
    report={"python":platform.python_version(),"numpy":np.__version__,
            "scipy":scipy.__version__,"mpmath":mp.__version__,
            "nystrom_comparisons":rows,"endpoint_absolute_errors":endpoint_errors,
            "prefixes_checked":count,"maximum_prefix_value":maximum,
            "warning":"Numerical checks are not a proof or independent mathematical review."}
    print(f"PASS: {len(rows)} direct-kernel Nystrom comparisons")
    print(f"Largest absolute error (2048 nodes): {max(r['absolute_error_2048'] for r in rows):.3e}")
    print(f"PASS: {len(endpoint_errors)} endpoint comparisons at 70-digit precision (error < 1e-60)")
    print(f"PASS: {count} finite-prefix sign checks (degrees 0 through 400)")
    print(f"Versions: Python {report['python']}; NumPy {report['numpy']}; "
          f"SciPy {report['scipy']}; mpmath {report['mpmath']}")
    print(report["warning"])
    if out:
        out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
        print(f"Wrote {out.name}")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json",type=Path,help="write numerical validation report")
    args=parser.parse_args()
    main(args.json)
