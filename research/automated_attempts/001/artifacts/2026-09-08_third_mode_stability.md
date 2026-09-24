# Third-mode stability: a precise source-dependent exclusion strip

This addendum follows the concurrently committed Sol attempt 1. It does not prove the planar Pólya bound. It identifies an existing theorem behind the proposed stability route and derives the exact quantitative gap still to be closed.

## External premise and its direction

Alexis de Villeroché, [arXiv:2506.05870v3](https://arxiv.org/html/2506.05870v3), Theorem 1.1 (6 May 2026), controls the full Dirichlet spectrum of a fixed-volume open set by its second-eigenvalue deficit from two equal balls. In dimension two its exponent is `1/18`. The theorem statement and hypotheses were inspected; its full analytic proof was not independently reconstructed in this run. The consequence below explicitly depends on that theorem.

Theorem 1.2 improves the exponent to `1/2` only for the **positive part** of `lambda_k(Omega)-lambda_k(Theta)`. It cannot supply the lower bound needed here. Generic spectral stability near two balls is therefore an existing result, not the missing new lemma; the needed improvement is quantitative and in the lower direction.

## Derivation

Scale an actual planar domain to area `pi`. Let `D` be the unit disk and `Theta` the union of two disks of area `pi/2`. Put

```math
A=\lambda_2(\Theta)=2j_{0,1}^2<12,\qquad
B=\lambda_3(\Theta)=2\lambda_2(D)>12.
```

The first strict inequality follows from the non-eigenfunction trial `1-r^2`, of Rayleigh quotient 6. The second requires no numerical Bessel value: Hong–Krahn–Szegő gives `lambda_2(D)>=2j_{0,1}^2`, while the independently checked Rayleigh sum gives `j_{0,1}^2>4sqrt(2)`. Hence `B>=4j_{0,1}^2>16sqrt(2)>12`.

Assume a would-be violating domain has `lambda_3(Omega)<=12` (including equality only strengthens the exclusion). Then `A<=lambda_2(Omega)<=12`. Specializing the external theorem at `d=2,k=3` gives

```math
B-12\le B-\lambda_3(\Omega)
\le81C_2\,12^{17/18}(\lambda_2(\Omega)-A)^{1/18}.
```

Thus it must satisfy

```math
\lambda_2(\Omega)-A\ge
\eta:=\left(\frac{B-12}{81C_2\,12^{17/18}}\right)^{18}>0.
```

This excludes a genuine neighborhood of the two-ball degeneration for any counterexample, with no compactness or limiting-domain assumption added. The useful constant is presently unevaluated: this run did not obtain a validated numerical bound for `C_2`.

If `eta>12-A`, the whole possible interval is excluded; no such comparison has been proved. Otherwise the surviving interval is `[A+eta,12]`. Merely proving that `eta` is positive, or citing a thin-neck limit, does not settle that interval. At equality of a sufficient threshold, the distinction between a strict Pólya violation and equality should be handled directly rather than discarded.

For area `V`, apply the statement to normalized eigenvalues `(V/pi)*lambda_j(Omega)`.

## Next experiment in analysis

First seek explicit usable lower-side constants on this small normalized interval, or prove a sharper estimate only for `k=3` and `lambda_3<=12`. A global estimate for every spectral index may lose far more than this local problem requires. Audit the exponent and the direction of every cited stability inequality. This is a source-dependent research lead, not a newly verified numerical coverage theorem.
