# A counterexample to fractional logarithmic convexity with rotating drift

**Target:** Problem 405 at repository revision `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete counterexample, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex, at the repository user's request. The argument and the hypothesis audit below are by the same AI agent. No independent or human verification is claimed.

## Result

The estimate in problem 405 is false. There is a smooth, real, uniformly elliptic operator of exactly the prescribed form on the unit disk and a nonzero real initial datum whose solution has zero final value at time one.

The mechanism is a complex zero of the fractional evolution multiplier. Intersections of finite-dimensional fractional trajectories through such zeros are already known; the contribution here is their realization by the particular scalar, real-coefficient, Dirichlet PDE in the target.

## 1. A nonreal zero of the half-order multiplier

Define the entire functions

```math
\mathop{\mathrm{erf}}(z)=\frac{2}{\sqrt\pi}\int_0^z e^{-w^2}\,dw,
\qquad \mathop{\mathrm{erfc}}(z)=1-\mathop{\mathrm{erf}}(z),
\qquad E_{1/2}(z)=\sum_{k=0}^\infty\frac{z^k}{\Gamma(1+k/2)}.
```

There is a nonreal zero of $`\mathop{\mathrm{erfc}}`$. Here is an existence argument requiring no numerical approximation. The entire function $`\mathop{\mathrm{erf}}`$ is nonconstant and odd. If it omitted the value one, oddness would force it also to omit minus one, contradicting Little Picard's theorem. On the real axis its values are strictly between minus one and one, by the Gaussian integral. Its points with value one are therefore nonreal.

The identity

```math
E_{1/2}(z)=e^{z^2}\mathop{\mathrm{erfc}}(-z)
```

can also be checked without special-function asymptotics: both sides equal one at zero and solve $`F'(z)=2zF(z)+2/\sqrt\pi`$, as follows by differentiation and the Gamma recurrence. Choose a nonreal zero $`\zeta=a+ib`$ of $`E_{1/2}`$, taking its conjugate if necessary so that $`b>0`$.

In particular, $`E_{1/2}(\zeta)=0`$. Every such zero is simple, since the displayed differential equation gives $`E_{1/2}'(\zeta)=2/\sqrt\pi`$.

## 2. Real scalar elliptic realization

Let $`\Omega=\{x\in\mathbb R^2:|x|<1\}`$ and let $`j=j_{1,1}>0`$ be the first positive zero of the Bessel function $`J_1`$. In polar coordinates put

```math
\psi(r,\vartheta)=J_1(jr)e^{i\vartheta}.
```

This is smooth on the closed disk, including its center: the power series for $`J_1(jr)/r`$ is a power series in $`r^2`$, and $`\psi=(x_1+ix_2)J_1(jr)/r`$. The Bessel equation gives

```math
\Delta\psi=-j^2\psi,\qquad \partial_\vartheta\psi=i\psi,
\qquad \psi|_{\partial\Omega}=0.
```

Set

```math
A(x)=I_2,\qquad B(x)=b(-x_2,x_1),\qquad p(x)=j^2+a,
\qquad L=\Delta+B\cdot\nabla+p.
```

All coefficients are real and smooth, and $`A`$ is symmetric and uniformly positive definite. Since $`B\cdot\nabla=b\partial_\vartheta`$, we have $`L\psi=\zeta\psi`$. This drift genuinely falls outside the gradient class: $`\partial_1B_2-\partial_2B_1=2b\ne0`$.

## 3. The solution and the contradiction

Take $`\alpha=1/2`$, $`T=1`$, and define the real-valued function

```math
u(t,x)=\mathop{\mathrm{Re}}\bigl(E_{1/2}(\zeta\sqrt t)\psi(x)\bigr),
\qquad u_0=\mathop{\mathrm{Re}}\psi.
```

The scalar series satisfies

```math
D_t^{1/2}E_{1/2}(\zeta\sqrt t)
=\zeta E_{1/2}(\zeta\sqrt t),\qquad E_{1/2}(0)=1.
```

Indeed, apply $`D_t^{1/2}t^\beta=\Gamma(\beta+1)t^{\beta-1/2}/\Gamma(\beta+1/2)`$ to each term with $`\beta=k/2>0`$; the constant term has zero Caputo derivative. On bounded time intervals the resulting series converges, and the original derivative is integrable at zero, so termwise integration in the Caputo formula is justified. It follows that $`D_t^{1/2}u=Lu`$, with the prescribed homogeneous Dirichlet boundary values and initial datum. In particular this is a mild solution continuous into $`L^2(\Omega)`$ at zero; it is smooth in space and for positive time.

The two real modes $`J_1(jr)\cos\vartheta`$ and $`J_1(jr)\sin\vartheta`$ are orthogonal and have the same positive norm $`c`$. Therefore

```math
\|u(t)\|_{L^2(\Omega)}=c\,|E_{1/2}(\zeta\sqrt t)|,
\qquad \|u_0\|_{L^2(\Omega)}=c>0,
\qquad u(1)=0.
```

Continuity and $`E_{1/2}(0)=1`$ ensure $`\|u(t)\|>0`$ for all sufficiently small positive $`t`$. At each such time the asserted estimate, for any finite $`C`$, would imply

```math
0<\|u(t)\|\le C\|u_0\|^{1-t}\|u(1)\|^t=0,
```

a contradiction. This resolves the universal statement negatively. No numerical approximation to the zero is used in the proof.

## Hypothesis and dependency audit

| Target requirement | Verification |
| --- | --- |
| Dimension at least two; bounded smooth domain | The unit disk in dimension two. A universal claim is refuted by one allowed dimension. |
| Smooth real coefficients and symmetric uniform ellipticity | Constant identity diffusion; linear real drift; constant real potential. |
| Fractional order strictly between zero and one | Exactly one half. |
| Arbitrary real potential is permitted | The choice $`p=j^2+a`$ uses this freedom. No sign restriction is silently discarded. |
| Real $`L^2`$ initial datum | The nonzero smooth cosine mode. |
| Caputo derivative based at zero | Verified directly from the defining series. No time shift or semigroup rule is used. |
| Constant may depend on all fixed PDE data | Even a data-dependent finite constant cannot bound a positive norm by zero. |
| Boundary condition | $`J_1(j)=0`$ holds for all times. |

Standard dependencies are Little Picard's theorem, the Gaussian integral, elementary Bessel-function facts, and the Gamma integral for the Caputo derivative of a power. The counterexample does not resolve variants imposing a dissipativity or potential-sign condition absent from this entry. It does not claim failure of forward uniqueness: a zero state at a later time does not erase the earlier Caputo memory.

## Sources and scope of review

- S.-E. Chorfi, [Logarithmic convexity of evolution equations and application to inverse problems](https://arxiv.org/html/2506.19954v1), §5, question 2. The source asks about removing the gradient-drift hypothesis. The repository fixes the precise quantified statement used here.
- S.-E. Chorfi, L. Maniar and M. Yamamoto, [Logarithmic convexity of non-symmetric time-fractional diffusion equations](https://arxiv.org/abs/2404.14046), also published with [DOI 10.1002/mma.10421](https://doi.org/10.1002/mma.10421). Its gradient-drift theorem is not contradicted by this example.
- NIST DLMF, [§7.13(ii)](https://dlmf.nist.gov/7.13#ii), independently records the nonreal complementary-error-function zeros; [§10.21(i)](https://dlmf.nist.gov/10.21#i) records positive Bessel zeros.
- A. Deshpande, V. Daftardar-Gejji and P. Vellaisamy, [Analysis of intersections of trajectories of linear systems](https://arxiv.org/abs/1808.02253), gives prior finite-dimensional fractional-trajectory intersection results. The underlying zero-multiplier mechanism is not claimed as new.

The originating AI checked the exact target, real-valuedness, boundary regularity, eigenvalue signs, the derivative convention, and the terminal-zero implication. Independent assessment of the complete argument is outstanding.
