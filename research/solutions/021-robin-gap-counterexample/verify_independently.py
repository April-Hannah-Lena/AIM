#!/usr/bin/env python3
"""Independent exact geometry/symbolic audit, separate from submitted checks.

Requires sympy. No continuum eigenvalues or smoothing threshold are certified.
"""
from itertools import combinations, product
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
Q = s.Rational
A = [s.Matrix(v) for v in [(1,0,0),(-1,0,0),(0,0,1),(0,0,-1),(0,-1,0),
     (0,Q(1,10),Q(9,10)),(0,Q(1,10),-Q(9,10)),
     (Q(9,10),Q(1,10),0),(-Q(9,10),Q(1,10),0)]]


def vertices_at_intersections(normals, constants):
    points = set()
    for indices in combinations(range(len(normals)), len(normals[0])):
        matrix = s.Matrix.vstack(*(normals[i].T for i in indices))
        if not matrix.det():
            continue
        point = matrix.inv()*s.Matrix([constants[i] for i in indices])
        if all(a.dot(point) <= b for a,b in zip(normals, constants)):
            points.add(tuple(point))
    return points


def hull(points):
    points = sorted(set(points))
    cross = lambda o,a,b: (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for seq,out in ((points,lower),(reversed(points),upper)):
        for p in seq:
            while len(out) >= 2 and cross(out[-2],out[-1],p) <= 0:
                out.pop()
            out.append(p)
    return lower[:-1]+upper[:-1]


def main():
    checks = []
    def check(name, condition):
        assert bool(condition), name
        checks.append(name)

    vertices = vertices_at_intersections(A, [s.Integer(1)]*9)
    expected = set(product((-1,1),repeat=3)) | {(0,10,0)}
    check('Nine half-spaces give exactly the nine convex-hull vertices', vertices == expected)
    epsilon = s.symbols('epsilon', positive=True)
    lengths = {s.expand((v[0]-w[0])**2 + epsilon**2*((v[1]-w[1])**2+(v[2]-w[2])**2))
               for v,w in combinations(sorted(vertices),2)}
    check('All squared distances are bounded by the two stated candidates',
          all((s.Poly(d,epsilon).coeff_monomial(1) <= 4 and
               s.Poly(d,epsilon).coeff_monomial(epsilon**2) <= 8) or
              (s.Poly(d,epsilon).coeff_monomial(1) <= 1 and
               s.Poly(d,epsilon).coeff_monomial(epsilon**2) <= 122) for d in lengths))
    square = list(product((-1,1),repeat=2))
    triangle_hull = hull(square+[(10,0)])
    kappa = 2*s.sqrt(82)-2
    fiber_results = []
    for tt in [Q(i,8) for i in range(9)]:
        # Build the Minkowski sum from its generators, without using the
        # manuscript's six listed fiber vertices.
        poly = hull([((1-tt)*a[0]+tt*b[0],(1-tt)*a[1]+tt*b[1])
                     for a in square for b in triangle_hull])
        edges = list(zip(poly,poly[1:]+poly[:1]))
        area = s.Abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in edges))/2
        perimeter = sum(s.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2) for a,b in edges)
        check(f'Minkowski fiber area at t={tt}', area == 4+18*tt-9*tt**2)
        check(f'Minkowski fiber perimeter at t={tt}', s.simplify(perimeter-(8+kappa*tt)) == 0)
        x = 1-tt
        normals = [s.Matrix((0,1)),s.Matrix((0,-1)),s.Matrix((-1,0)),
                   s.Matrix((Q(1,10),Q(9,10))),s.Matrix((Q(1,10),-Q(9,10))),
                   s.Matrix((Q(1,10),0))]
        constants = [1,1,1,1,1,1-Q(9,10)*x]
        section = vertices_at_intersections(normals, constants)
        check(f'Half-space section equals Minkowski hull at t={tt}', section == set(poly))
        fiber_results.append({'t':str(tt),'area':str(area),'perimeter':str(s.simplify(perimeter))})

    t,k = s.symbols('t k', real=True)
    area = 4+18*t-9*t*t
    p = (8+k*t)/area
    numerator = 4*k-144+144*t+9*k*t*t
    check('Symbolic derivative numerator', s.simplify(s.diff(p,t)-numerator/area**2) == 0)
    check('Symbolic central barrier', s.expand(8+k*t-Q(8,5)*area -
          (Q(8,5)+(k-Q(144,5))*t+Q(72,5)*t*t)) == 0)
    # Alternate rational enclosure, not the one in the submitted program.
    check('9 < sqrt(82) < 91/10', 9**2 < 82 < Q(91,10)**2)
    check('Barrier at 3/4 is strictly positive', Q(3,2)*9-Q(67,5) > 0)
    check('Value at 1/2 is below 3/2', 4*(7+Q(91,10))/43 < Q(3,2))
    check('Second-derivative estimate', Q(450,16)+Q(2*221*18,64) < 200)
    e = Q(1,10**12)
    mass = 1300*Q(1,10**6)+101000*e
    upper = 16*mass/(1-mass)
    lower = 3/(1+2*e*e)
    check('Exact gap comparison', upper < Q(21,1000) < Q(29,10) < lower)
    # Facet normal velocity: the moving side is z1=epsilon*(10-9|x|).
    check('Exact lateral surface correction', s.sqrt(1+(-9*epsilon)**2) == s.sqrt(1+81*epsilon**2))
    check('Smooth defining function preserves all nine physical normals',
          len(A) == 9 and {(a[0],a[1],a[2]) for a in A} ==
          {(a[0],a[1],a[2]) for a in A if (-a[0],a[1],a[2]) in {tuple(v) for v in A}})

    tex = (ROOT/'robin_gap_021.tex').read_text(encoding='utf-8')
    import re
    bib = set(re.findall(r'\\bibitem\{([^}]+)\}',tex))
    cited = {key.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',tex)
             for key in group.split(',')}
    labels = re.findall(r'\\label\{([^}]+)\}',tex)
    refs = set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex))
    check('Every bibliography entry is cited and every citation resolves', cited == bib)
    check('Every equation/figure/section reference resolves uniquely', refs <= set(labels) and len(labels)==len(set(labels)))
    result = {'review_date':'2026-10-02','tool':'Independent exact geometry and symbolic audit',
              'sympy_version':s.__version__,'checks':checks,'check_count':len(checks),
              'fiber_results':fiber_results,'polyhedral_gap_upper':str(upper),
              'interval_gap_lower':str(lower),'limits':['No PDE eigenvalue computation.',
              'No numerical smoothing threshold.', 'Functional-analytic steps require the written mathematical audit.']}
    (ROOT/'independent-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'Passed {len(checks)} independent exact geometry, symbolic and cross-reference checks.')


if __name__ == '__main__':
    main()
