# Independent audit of concurrent Sol's low-index and disk claims

Verdict: the stated disk obstruction and the Dirichlet low-index band are correct. They are classical consequences and do not resolve Pólya. In particular the disk obstruction rejects a stronger Faber--Krahn-style extrapolation, not Pólya itself.

## Disk trial calculation

On the unit disk, take `f0=1-r^2`, `f1=r(1-r^2)cos(theta)`, and `f2=r(1-r^2)sin(theta)`. They are linearly independent elements of `H_0^1`. Their mass and Dirichlet-energy matrices are respectively

\[
M=\pi\operatorname{diag}(1/3,1/24,1/24),\qquad
K=\pi\operatorname{diag}(2,2/3,2/3).
\]

All off-diagonal entries vanish by angular orthogonality. The generalized Rayleigh quotients are exactly `6,16,16`; thus every vector in their three-dimensional span has quotient at most `16`, and min--max gives `lambda_3(disk)<=16`. Checking individual quotients alone would not have sufficed without the two orthogonalities.

The canonical product and power series of `J0` give

\[
J_0(z)=\prod_{j\ge1}(1-z^2/j_{0,j}^2)
=1-z^2/4+z^4/64+O(z^6).
\]

Comparing the `z^4` logarithmic coefficient yields `sum j_(0,j)^(-4)=1/32`. The positive contribution of all zeros after the first makes `j_(0,1)^4>32` strict. Consequently

\[
\lambda_3(\mathbb D)\le16<12\sqrt2<3j_{0,1}^2
=3\lambda_1(\mathbb D).
\]

The middle strict inequality follows by squaring positive quantities: `256<288`. Thus `lambda_k>=k lambda_1` fails for this actual smooth planar domain at `k=3`. Pólya asks only `lambda_3>=12` on this disk; no contradiction to that conjecture has been obtained.

Analytic Bessel dependencies are recorded in NIST DLMF: [canonical product, equation 10.21.15](https://dlmf.nist.gov/10.21.E15) and [power series, equation 10.2.2](https://dlmf.nist.gov/10.2.E2). The exact arithmetic script checks both matrices independently using Cartesian polynomial moments.

## Nodal estimate and regularity scope

Put `j=j_(d/2-1,1)`, `V=|Omega|`, and

\[
\beta_d=\frac{j^d\omega_d^2}{(2\pi)^d}.
\]

For an eigenfunction with eigenvalue `lambda_k` and `r` nodal domains, the usual nodal-restriction lemma and Faber--Krahn give

\[
\lambda_k\ge j^2\left(\frac{r\omega_d}{V}\right)^{2/d}.
\]

Indeed each nodal restriction has Rayleigh quotient `lambda_k`; its nodal domain therefore has volume at least `omega_d (j^2/lambda_k)^(d/2)`. Sum this over all `r` disjoint nodal domains. Comparing powers gives Pólya whenever `k<=r beta_d`.

One must **not** assert that nodal domains are Lipschitz. The standard restriction lemma is a Sobolev statement: zero extension of the restriction belongs to `H_0^1(Omega)` and has the corresponding restricted gradient. Faber--Krahn is used in its finite-measure open-set or support-measure form, which does not require Lipschitz nodal boundaries. A treatment using only the Lipschitz-domain formulation of Faber--Krahn would leave a regularity gap here.

The universal low-index band does not need arbitrary nodal-domain regularity at all. Take a real second eigenfunction `u`, orthogonal to the strictly positive first eigenfunction (the ambient domain is connected). Both `u_+` and `u_-` are nonzero and lie in `H_0^1(Omega)`. Test the weak eigenvalue equation with these positive/negative parts to obtain their Rayleigh quotients `lambda_2`. Their disjoint support volumes sum to at most `V`; one is at most `V/2`. The support-measure form of Faber--Krahn, proved by symmetric rearrangement of that Sobolev function extended by zero, gives

\[
\lambda_2\ge j^2(2\omega_d/V)^{2/d}.
\]

For every `k>=2`, use `lambda_k>=lambda_2`. This proves the Dirichlet Pólya inequality for `2<=k<=floor(2 beta_d)`, with `k=1` supplied by Faber--Krahn. This is the Hong--Krahn--Szegő route and avoids claiming extra smoothness for any nodal component.

In dimension three, `j_(1/2,1)=pi` and `omega_3=4*pi/3`, so

\[
\beta_3=2\pi^2/9,\qquad 2\beta_3=4\pi^2/9.
\]

The classical rational bounds `3<pi<22/7` give `4<2 beta_3<1936/441<5`. Therefore the universal Dirichlet band is `k=1,2,3,4` in dimension three. These statements provide no Neumann conclusion without a separate argument.

The companion script is `concurrent_sol_audit_2026-09-08.py`; its output is saved as `concurrent_sol_audit_2026-09-08.json`.
