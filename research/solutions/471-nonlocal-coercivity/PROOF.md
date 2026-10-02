# Directional moment bounds do not imply fractional coercivity

**Target:** Problem 471 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete counterexample, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Construction, estimates, source comparison and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Counterexample and ellipticity constants

Take $`n=2`$, $`s=1/2`$, $`\Lambda=4`$ and $`\lambda=1`$. Write $`x=(t,y)`$ and $`z=(r,w)`$. Define

```math
K(x,z)=\frac{\mathbf1_{\{tr>0\}}}{|x-z|^3}\qquad(x\ne z),
```

and set the kernel to zero on the diagonal. Its values when either first coordinate vanishes are immaterial. This is a nonnegative measurable symmetric kernel. Interactions across the line $`t=0`$ have been removed.

For every $`x`$ away from that line and every $`R>0`$,

```math
R\int_{B_{2R}(x)\setminus B_R(x)}K(x,z)\,dz
\le R\,2\pi\int_R^{2R}\rho^{-2}\,d\rho=\pi<4.
```

For $`t>0`$ all increments with positive first coordinate remain in the same half-plane; for $`t<0`$ use the opposite hemisphere. For every unit vector $`e`$, the integral of $`|e\cdot\theta|^2`$ over either such semicircle is $`\pi/2`$. Therefore

```math
R^{-1}\int_{B_{4R}(x)\setminus B_R(x)}
|e\cdot(x-z)|^2K(x,z)\,dz
\ge R^{-1}\frac\pi2\int_R^{4R}1\,d\rho
=\frac{3\pi}{2}>1.
```

Both assumptions hold with fixed constants, for almost every base point and every radius and direction.

## Smooth test functions

Choose $`0\le\chi\le1`$ in $`C_c^\infty(\mathbb R)`$, equal to one on $`[-1,1]`$ and supported in $`[-2,2]`$. Choose a smooth nondecreasing function $`\phi`$ equal to zero on $`(-\infty,0]`$ and one on $`[1,\infty)`$. Choose $`0\le b\le1`$ in $`C_c^\infty(\mathbb R)`$ equal to one on $`[-1,1]`$. For $`0<\varepsilon<1/8`$ set

```math
a_\varepsilon(t)=\chi(t)\phi(t/\varepsilon),
\qquad v_\varepsilon(t,y)=a_\varepsilon(t)b(y).
```

These are smooth compactly supported functions on the whole plane, including across $`t=0`$, and vanish in the negative half-plane.

For an interval $`J`$, denote the unnormalized one-dimensional seminorm by

```math
[f]_{1/2,J}^2=\int_J\int_J\frac{|f(t)-f(r)|^2}{|t-r|^2}\,dt\,dr.
```

The quantity $`[\phi]_{1/2,(0,\infty)}`$ is finite even though $`\phi`$ is not square-integrable on the half-line. Indeed, on $`(0,1)^2`$ its Lipschitz constant bounds the difference quotient. Both arguments above one give zero. The remaining contribution is

```math
2\int_0^1(1-\phi(r))^2\int_1^\infty(t-r)^{-2}\,dt\,dr
=2\int_0^1\frac{(1-\phi(r))^2}{1-r}\,dr<\infty,
```

since $`|1-\phi(r)|\le C(1-r)`$. Critical scaling and the product difference inequality consequently give

```math
[a_\varepsilon]_{1/2,(0,\infty)}^2
\le2[\chi]_{1/2,(0,\infty)}^2
+2\|\chi\|_\infty^2[\phi(\cdot/\varepsilon)]_{1/2,(0,\infty)}^2
=2[\chi]_{1/2,(0,\infty)}^2
+2\|\chi\|_\infty^2[\phi]_{1/2,(0,\infty)}^2.
```

Also $`\|a_\varepsilon\|_2\le\|\chi\|_2`$ uniformly.

## The kernel energy stays bounded

Only pairs in the positive half-plane contribute. Use

```math
|a(t)b(y)-a(r)b(w)|^2
\le2|a(t)-a(r)|^2|b(y)|^2
+2|a(r)|^2|b(y)-b(w)|^2
```

and the elementary integral

```math
\int_{\mathbb R}(h^2+q^2)^{-3/2}\,dq=\frac2{h^2}\qquad(h\ne0).
```

Tonelli's theorem, and enlargement of a half-line to the whole line in the second term, yield

```math
\begin{aligned}
\iint|v_\varepsilon(x)-v_\varepsilon(z)|^2K(x,z)\,dx\,dz
&\le4\|b\|_2^2[a_\varepsilon]_{1/2,(0,\infty)}^2
+4\|a_\varepsilon\|_2^2[b]_{1/2,\mathbb R}^2\\
&\le C,
\end{aligned}
```

where $`C`$ does not depend on $`\varepsilon`$.

## The full fractional energy diverges

In the full energy restrict to pairs satisfying

```math
2\varepsilon<t<1/4,\quad -1/2<y<1/2,
\quad -t<r<0,\quad y-t<w<y+t.
```

Here $`v_\varepsilon(t,y)=1`$ and $`v_\varepsilon(r,w)=0`$. Moreover $`|x-z|^2\le5t^2`$, and the allowed $`(r,w)`$ rectangle has area $`2t^2`$. Thus

```math
\iint\frac{|v_\varepsilon(x)-v_\varepsilon(z)|^2}{|x-z|^3}\,dx\,dz
\ge\frac2{5^{3/2}}\int_{2\varepsilon}^{1/4}\frac{dt}{t}
=\frac2{5^{3/2}}\log\frac1{8\varepsilon}\longrightarrow\infty.
```

The ratio of kernel energy to full fractional energy tends to zero for a single admissible kernel and fixed ellipticity constants. No positive coercivity constant of the proposed kind exists. This disproves the universal assertion in problem 471.

## Target comparison and audit

The example uses a measurable kernel, not a singular measure, and the test functions are smooth on all of $`\mathbb R^2`$. The null set of base points on the dividing line is permitted by the statement. The moment lower bound is uniform over every direction, not just the coordinate directions. The construction exploits the distinction between symmetry under exchange of endpoints and evenness of increments at a fixed base point: the former is required and holds; the latter is not assumed.

The source is Fernández-Real and Ros-Oton, [Integro-Differential Elliptic Equations](https://arxiv.org/pdf/2411.12455), §2.8.1, conditions (2.8.2)–(2.8.3) and the coercivity question following Open Question 2.1. The proof addresses the exact symmetric quadratic-form target in the pinned repository statement. It does not purport to settle a different pointwise nondivergence-form question with even increment kernels. All constants, smoothness claims, seminorm bounds and the divergent lower bound are established analytically above; no floating-point evidence is used. Independent mathematical review remains outstanding.
