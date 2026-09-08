# Problem 001 — Pólya's eigenvalue inequalities

- Source: [`problems/001-polya-eigenvalue-bound.md`](../../../problems/001-polya-eigenvalue-bound.md)
- Area: Spectral geometry
- Programme status: research
- Attempts completed: 1

## Target

For every bounded connected Lipschitz domain \(\Omega\subset\mathbb R^d\), \(d\ge2\), prove or disprove, for every \(k\ge1\),
\[
 \mu_k(\Omega)\le4\pi^2\left(\frac{k}{\omega_d|\Omega|}\right)^{2/d}
 \le\lambda_k(\Omega).
\]

## 1. VERIFIED RESULTS

### Full chain at \(k=1,2\)

Let \(P_k(V)=4\pi^2(k/(\omega_dV))^{2/d}\) and let \(B_v\) be a ball of volume \(v\). The recorded ball theorem, together with Faber--Krahn, Hong--Krahn--Szegő, Szegő--Weinberger, and Bucur--Henrot's sharp \(\mu_2\) theorem, gives
\[
\begin{aligned}
 \lambda_1(\Omega)&\ge\lambda_1(B_V)\ge P_1(V),\\
 \lambda_2(\Omega)&\ge\lambda_1(B_{V/2})\ge P_1(V/2)=P_2(V),\\
 \mu_1(\Omega)&\le\mu_1(B_V)\le P_1(V),\\
 \mu_2(\Omega)&\le\mu_1(B_{V/2})\le P_1(V/2)=P_2(V).
\end{aligned}
\]
Bucur--Henrot's theorem uses \(0=\mu_0\le\mu_1\le\mu_2\le\cdots\) and applies to bounded Lipschitz domains.

### Nodal-count criterion and Dirichlet low-index band

Write \(\nu=d/2-1\), let \(j_{\nu,1}\) be the first positive zero of \(J_\nu\), and set
\[
 \beta_d=\frac{j_{\nu,1}^{\,d}\omega_d^2}{(2\pi)^d}.
\]
If a \(\lambda_k\)-eigenfunction has \(r\) nodal domains, nodal-domain Faber--Krahn gives
\[
 \lambda_k(\Omega)\ge j_{\nu,1}^2
 \left(\frac{r\omega_d}{|\Omega|}\right)^{2/d}.
\]
Hence the Dirichlet Pólya bound holds whenever \(k\le r\beta_d\). Every eigenfunction above the simple ground state changes sign, so \(r\ge2\); consequently
\[
 P_k(|\Omega|)\le\lambda_k(\Omega)
 \quad(2\le k\le\lfloor2\beta_d\rfloor).
\]
The ball \(k=1\) theorem implies \(\beta_d\ge1\). Exact examples:

- \(d=2\): \(2\beta_2=j_{0,1}^2/2\in(2,3)\), so this gives exactly \(k\le2\).
- \(d=3\): \(2\beta_3=4\pi^2/9\in(4,5)\), so the Dirichlet inequality holds for every \(k\le4\).

### Equal-ball generalization is false

The stronger putative inequality \(\lambda_k(\Omega)\ge\lambda_1(B_{|\Omega|/k})\) fails for \((d,k)=(2,3)\). On the unit disk, the trial space
\[
 \operatorname{span}\{1-r^2,\ r(1-r^2)\cos\theta,\ r(1-r^2)\sin\theta\}
\]
has maximal Rayleigh quotient \(16\), so \(\lambda_3(D)\le16\). Meanwhile a disk of area \(\pi/3\) has ground eigenvalue \(3j_{0,1}^2>12\sqrt2>16\), using the exact Rayleigh sum \(\sum_{n\ge1}j_{0,n}^{-4}=1/32\).

Full derivation: [`attempts/2026-09-08_0825_sol.md`](attempts/2026-09-08_0825_sol.md).

## 2. PROMISING BUT UNPROVED CLAIMS

- A \(\lambda_3\)-specific stability argument may exclude the two-equal-ball degeneration that makes Hong--Krahn--Szegő sharp. It must use the third min--max dimension; there is no uniform connected-domain improvement of the \(\lambda_2\) inequality because thin-neck dumbbells approach equality.
- Bucur--Henrot's two-center construction suggests testing a three-center family for \(\mu_3\), but simultaneous orthogonality and the required mass-displacement inequality have not been established.

## 3. COMPUTATIONAL EVIDENCE

None. Attempt 1 used exact variational calculations and an exact Bessel-zero Rayleigh sum.

## 4. FAILED / EXHAUSTED ROUTES

- Do not try to extend the \(k=2\) proof by asserting that \(k\) equal balls minimize \(\lambda_k\). The unit disk polynomial trial space above rigorously disproves this already at \(k=3\).
- Do not replace the nodal count by \(k\) in the nodal lemma: Courant supplies \(r\le k\), not \(r\ge k\).
- A uniform positive stability gap for \(\lambda_2\) over connected domains is impossible because connected thin-neck approximations to two equal balls approach the sharp constant.

## 5. CURRENT BOTTLENECK

The first untreated full-chain index is \(k=3\). The Neumann side needs a new arbitrary-domain bound for \(\mu_3\). The first uncovered Dirichlet case is planar \(k=3\): nodal Faber--Krahn gives only \(\lambda_3|\Omega|\ge2\pi j_{0,1}^2<12\pi\).

## 6. NEXT HIGH-VALUE ATTACKS

1. Write the exact three-center Weinberger/Bucur--Henrot trial family for \(\mu_3\), including orthogonality to constants and the first two Neumann eigenfunctions; isolate the topological center-selection problem from the radial mass-displacement estimate.
2. For planar \(\lambda_3\), derive a quantitative dichotomy: either a \(\lambda_3\)-eigenfunction has three nodal domains (then the nodal criterion closes the bound) or the two-dimensional spectral subspace below \(\lambda_3\) forces a stability gap above the two-ball \(\lambda_2\) constant.
3. Use certified Bessel-zero bounds to tabulate \(\lfloor2\beta_d\rfloor\) only if this helps choose the first uncovered Dirichlet index in higher dimensions.
