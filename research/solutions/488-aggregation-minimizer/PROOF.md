# Existence of compactly supported subcritical aggregation minimizers

**Target:** Problem 488 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete existence proof, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Proof construction, source comparison and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Result and strategy

For every parameter choice in problem 488, the infimum is attained. A minimizer can be chosen radially nonincreasing and compactly supported. Radial symmetry is obtained by rearrangement, not imposed as a restriction on competitors. The proof first drops the second-moment constraint, proves attainment in the larger class using exact mass scaling, and then proves bounded support of the resulting minimizer.

Fix $`d\ge2`$, $`\chi>0`$ and $`1<m<2+2/d`$. For $`M>0`$ define

```math
\mathcal B_M=\{u\in H^1(\mathbb R^d)\cap L^1(\mathbb R^d):u\ge0,\ \int u=M\},
\qquad I(M)=\inf_{u\in\mathcal B_M}\mathcal E_m(u).
```

## 1. Lower bounds, negativity, and exact mass scaling

The Gagliardo–Nirenberg inequality between the gradient in $`L^2`$ and the function in $`L^1`$ gives

```math
\int u^m\le C\|\nabla u\|_2^\alpha\|u\|_1^{m-\alpha},
\qquad \alpha=\frac{2d(m-1)}{d+2}<2.
```

The exponent is within the Sobolev range in every dimension under consideration. Thus at fixed mass the energy is bounded below and any minimizing sequence has bounded gradient norm. The same interpolation inequality at exponent two, or equivalently the Nash inequality, bounds its $`L^2`$ norm. In particular $`I(M)>-\infty`$ and minimizing sequences are bounded in $`H^1`$.

For a nonzero smooth nonnegative mass-one function $`f`$, the dilation $`f_\tau(x)=\tau^df(\tau x)`$ has

```math
\mathcal E_m(f_\tau)
=\frac{\tau^{d+2}}2\int|\nabla f|^2
-\frac\chi{m-1}\tau^{d(m-1)}\int f^m.
```

Since $`d(m-1)<d+2`$, this is negative for sufficiently small positive $`\tau`$. Hence $`I(1)<0`$.

Set

```math
\delta=2-d(m-2)>0,\qquad
a=\frac2\delta,\qquad b=\frac{m-2}\delta,\qquad
q=1+\frac{2(m-1)}\delta>1.
```

The map $`u(x)\mapsto M^a u(M^b x)`$ is a bijection from $`\mathcal B_1`$ onto $`\mathcal B_M`$. Indeed $`a-db=1`$, and both energy terms scale by the same factor since

```math
2a+(2-d)b=am-db=q.
```

Taking infima in both directions gives the exact identity

```math
I(M)=M^qI(1)\qquad(M>0).                                      \tag{1}
```

## 2. Rearrangement and strong convergence of the attractive term

Apply symmetric decreasing rearrangement to a minimizing sequence in $`\mathcal B_1`$. It preserves the mass and $`L^m`$ integral, and the Pólya–Szegő inequality decreases the gradient integral. We therefore have a radial nonincreasing minimizing sequence $`u_j`$, still bounded in $`H^1`$.

By weak compactness, local Rellich compactness and a diagonal subsequence, there is a nonnegative radial nonincreasing $`u\in H^1`$ such that $`u_j\rightharpoonup u`$ in $`H^1`$, almost everywhere, and strongly in $`L^m`$ on every ball. Local Rellich applies because $`m<2d/(d-2)`$ when $`d>2`$, and $`m`$ is finite when $`d=2`$. Fatou's lemma gives $`M:=\int u\le1`$.

Write $`\omega_d=|B_1|`$. Radial monotonicity and mass one imply

```math
u_j(r)\le\frac1{\omega_d r^d}\qquad(r>0)
```

for the monotone radial representatives. Consequently

```math
\int_{|x|>R}u_j^m\,dx
\le(\omega_dR^d)^{1-m}\int_{|x|>R}u_j\,dx
\le(\omega_dR^d)^{1-m}\longrightarrow0
```

uniformly in $`j`$. The same bound holds for $`u`$. Together with local convergence this proves strong convergence in $`L^m(\mathbb R^d)`$. Therefore

```math
\mathcal E_m(u)\le\liminf_j\mathcal E_m(u_j)=I(1)<0.             \tag{2}
```

In particular $`u`$ is not zero, so $`M>0`$. If $`M<1`$, (1) and (2) imply the contradiction

```math
I(1)\ge\mathcal E_m(u)\ge I(M)=M^qI(1)>I(1).
```

Thus $`M=1`$ and $`u`$ attains $`I(1)`$ in the full relaxed class $`\mathcal B_1`$. This step rules out escape of any mass; a second-moment bound on the minimizing sequence was not needed.

## 3. Euler equation in the positivity region and its multiplier

Write $`u(x)=U(|x|)`$. On every annulus separated from the origin, the radial $`H^1`$ profile has a continuous, locally absolutely continuous representative. It is nonnegative and nonincreasing. Since its mass is positive, it is bounded below by a positive constant on some closed annulus. Choose a smooth function $`\psi_0`$ compactly supported in such an annulus, with $`\int\psi_0=1`$.

Both signs of sufficiently small $`\varepsilon`$ make $`u+\varepsilon\psi_0`$ nonnegative. Its mass is $`1+\varepsilon`$, so minimality at every mass and (1) give

```math
\mathcal E_m(u+\varepsilon\psi_0)\ge I(1+\varepsilon)
=(1+\varepsilon)^q I(1),
```

with equality at zero. Differentiating this two-sided inequality at zero gives

```math
D\mathcal E_m(u)[\psi_0]=qI(1)<0.                             \tag{3}
```

For any smooth test function $`\varphi`$ compactly supported where $`|x|>0`$ and $`U(|x|)>0`$, perturbation in the direction $`\varphi-(\int\varphi)\psi_0`$ preserves the mass and is feasible for both small signs. First variation, together with (3), gives

```math
\int\nabla u\cdot\nabla\varphi
-\frac{\chi m}{m-1}\int u^{m-1}\varphi
=qI(1)\int\varphi.
```

The differentiations are justified on compact positive annuli, where the continuous profile is bounded above and away from zero. Define

```math
c_m=\frac{\chi m}{m-1}>0,\qquad \lambda=-qI(1)>0.
```

The weak Euler equation on those annuli is therefore

```math
\Delta u=\lambda-c_m u^{m-1}.                                \tag{4}
```

## 4. The minimizing profile has bounded support

If $`U`$ does not have bounded support, monotonicity and continuity away from zero imply $`U(r)>0`$ for every $`r>0`$. Mass integrability also implies $`U(r)\to0`$ as $`r\to\infty`$. On every positive annulus (4) becomes the radial distributional equation

```math
(r^{d-1}U'(r))'=r^{d-1}(\lambda-c_mU(r)^{m-1}).
```

Its right-hand side is continuous, so the one-dimensional equation upgrades $`U`$ to $`C^2`$ there. Choose $`R>0`$ so large that $`c_mU(r)^{m-1}\le\lambda/2`$ for $`r\ge R`$. Integration yields

```math
r^{d-1}U'(r)
\ge R^{d-1}U'(R)+\frac\lambda{2d}(r^d-R^d),\qquad r\ge R.
```

The right-hand side is eventually positive. This contradicts $`U'\le0`$. Hence $`u`$ is supported in a finite ball. Since its mass is one,

```math
\int|x|^2u(x)\,dx<\infty.
```

Thus $`u\in\mathcal A`$. As $`\mathcal A\subset\mathcal B_1`$, its energy $`I(1)`$ is also the infimum over $`\mathcal A`$, and that infimum is attained, as required.

## Dependencies, scope and audit

The proof uses the classical Gagliardo–Nirenberg and Nash inequalities, Pólya–Szegő rearrangement, local Rellich compactness, weak lower semicontinuity, and elementary radial Sobolev regularity. It supplies the mass scaling, exclusion of mass loss, sign of the multiplier and bounded-support argument explicitly. No symmetry assumption is imposed on the original admissible class, and no evolution estimate or convergence-to-equilibrium assertion is used. All dimensions and exponents in the target are covered; the endpoint $`m=1`$ and the critical exponent are not part of that target.

For comparison with the stated gap, see Carrillo, Esposito, Falcó and Fernández-Jiménez, [Competing effects in fourth-order aggregation–diffusion equations](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12623), Theorem 2.1, §3 and the closing discussion, and Falcó, Baker and Carrillo, [A nonlocal-to-local approach to aggregation-diffusion equations](https://arxiv.org/abs/2505.08443), §4. The existence proof above concerns the stationary unconstrained full-space problem, including its finite-second-moment requirement. It does not settle uniqueness or the dynamics. Independent review of the full argument remains outstanding.
