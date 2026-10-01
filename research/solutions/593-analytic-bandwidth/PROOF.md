# Logarithmic bandwidth with all three global norm bounds

**Target:** Problem 593 at `aa776a01d7d48a79f93251af11fde9454b0aea95`; [unchanged statement](statement.md).

**Status:** Solution claimed — complete constructive proof, awaiting independent review.

**Prepared:** 2026-10-02 by OpenAI Codex. Construction, estimates, source comparison and self-review were performed by the same AI agent. No independent or human audit is claimed.

## Result and construction

The conjecture holds for every function in the statement, with constants depending on the function and its analytic neighborhood. The key is to let the compactly supported extension depend on the requested accuracy. A family of smooth cutoffs with controlled derivatives through order $`N`$, followed by a smooth Fourier cutoff at bandwidth proportional to $`N`$, gives error exponentially small in $`N`$. Uniform spatial support and amplitude separately enforce the Fourier norm bounds.

Fix the given holomorphic extension and $`M=\|f\|_{L^\infty([-1,1])}>0`$. By compactness and continuity, choose $`0<\delta<1`$ such that $`f`$ is holomorphic on a neighborhood of

```math
J=[-1-\delta,1+\delta],\qquad \sup_{x\in J}|f(x)|\le2M.
```

Choose $`R>0`$ so that all closed complex disks of radius $`R`$ centered in $`J`$ lie in that neighborhood. Compactness and Cauchy's inequalities supply $`B<\infty`$ with

```math
\sup_{x\in J}|f^{(j)}(x)|\le B R^{-j}j!\qquad(j\ge0).          \tag{1}
```

These constants are fixed independently of the approximation accuracy.

## 1. A cutoff family with derivatives controlled through order N

Fix a nonnegative $`\varphi\in C_c^\infty((-1,1))`$ of integral one, and put $`L_\varphi=\|\varphi'\|_1`$. For each integer $`N\ge2`$, let

```math
r_N=\frac{\delta}{4N},\qquad
\varphi_{r_N}(x)=r_N^{-1}\varphi(x/r_N),
\qquad
\eta_N=\mathbf1_{[-1-\delta/2,\,1+\delta/2]}*
\underbrace{\varphi_{r_N}*\cdots*\varphi_{r_N}}_{N\text{ factors}}.
```

Then $`\eta_N\in C_c^\infty(\mathbb R)`$, $`0\le\eta_N\le1`$, it equals one on $`[-1,1]`$, and its support lies in

```math
[-1-3\delta/4,1+3\delta/4]\subset J\subset[-2,2].
```

For $`0\le k\le N`$, distribute the $`k`$ derivatives onto $`k`$ distinct mollifier factors. Young's convolution inequality gives

```math
\|\eta_N^{(k)}\|_\infty
\le\|\varphi_{r_N}'\|_1^k
=\left(\frac{4L_\varphi N}{\delta}\right)^k
=(C_0N)^k,\qquad C_0=\frac{4L_\varphi}{\delta}.                \tag{2}
```

This estimate does not assert a uniform analytic bound at all derivative orders for one compactly supported cutoff. It uses a different cutoff for each $`N`$, and only orders through $`N`$ are needed.

Define $`F_N=f\eta_N`$ on $`J`$ and zero outside. Because the cutoff has support strictly inside $`J`$, this is a smooth compactly supported function on the whole line. Moreover

```math
F_N=f\text{ on }[-1,1],\qquad
\|F_N\|_\infty\le2M,\qquad
\mathop{\mathrm{supp}}\nolimits F_N\subset[-2,2].              \tag{3}
```

By Leibniz's rule, (1), (2), and $`j!\le N^j`$ for $`0\le j\le N`$,

```math
\begin{aligned}
\|F_N^{(N)}\|_1
&\le4B\sum_{j=0}^N\binom Nj R^{-j}j!(C_0N)^{N-j}\\
&\le4B(DN)^N,\qquad D=C_0+R^{-1}.                            \tag{4}
\end{aligned}
```

## 2. Smooth frequency truncation with exponential error

Fix $`0\le\theta\le1`$ in $`C_c^\infty((-1,1))`$ with $`\theta=1`$ on $`[-1/2,1/2]`$. Set

```math
A=2D,\qquad c_N=2AN,\qquad
\widehat g_N(\xi)=\theta(\xi/c_N)\widehat F_N(\xi),
```

using exactly the Fourier normalization of the target. Since $`\widehat g_N`$ is smooth and compactly supported, its inverse Fourier transform $`g_N`$ is Schwartz and has Fourier support in $`[-c_N,c_N]`$.

Integrating by parts $`N`$ times gives, for $`\xi\ne0`$,

```math
|\widehat F_N(\xi)|\le\frac{\|F_N^{(N)}\|_1}{2\pi|\xi|^N}.
```

The frequency multiplier equals one on $`[-AN,AN]`$. Fourier inversion and (4) therefore give a global error estimate

```math
\begin{aligned}
\|g_N-F_N\|_\infty
&\le\int_{|\xi|>AN}|\widehat F_N(\xi)|\,d\xi\\
&\le\frac{4B(DN)^N}{\pi(N-1)}(AN)^{1-N}\\
&=\frac{4BA}{\pi}\frac N{N-1}\left(\frac DA\right)^N\\
&\le\frac{8BA}{\pi}\,2^{-N}.                               \tag{5}
\end{aligned}
```

In particular the same estimate controls approximation to $`f`$ on the target interval.

## 3. All global bounds hold with the prescribed constant

From (3) and the Fourier convention,

```math
\|\widehat F_N\|_\infty
\le\frac{1}{2\pi}\int_{-2}^2 2M\,dx=\frac{4M}{\pi},
\qquad
\|\widehat F_N'\|_\infty
\le\frac{1}{2\pi}\int_{-2}^2|x|\,2M\,dx=\frac{4M}{\pi}.      \tag{6}
```

Choose $`N`$ large enough that $`c_N\ge\|\theta'\|_\infty`$ and the right side of (5) is at most $`\varepsilon M`$, where $`0<\varepsilon<1`$. Then

```math
\|g_N\|_\infty\le2M+\varepsilon M<3M<4M,
\qquad
\|\widehat g_N\|_\infty\le\frac{4M}{\pi}<4M.
```

The product rule and (6) also give

```math
\|\widehat g_N'\|_\infty
\le\frac{\|\theta'\|_\infty}{c_N}\|\widehat F_N\|_\infty
+\|\widehat F_N'\|_\infty
\le\frac{8M}{\pi}<4M.
```

Thus the global spatial bound and both global Fourier bounds required in the problem hold simultaneously.

## 4. Choosing N proves logarithmic bandwidth

Put $`K=\max\{1,8BA/(\pi M)\}`$ and choose a fixed integer $`N_0\ge2`$ with $`2AN_0\ge\|\theta'\|_\infty`$. For each $`\varepsilon\in(0,1)`$ take

```math
N(\varepsilon)=\max\left\{N_0,\left\lceil\log_2\frac K\varepsilon\right\rceil\right\}.
```

All previous requirements are met. Since $`N(\varepsilon)\le N_0+1+\log_2K+\log_2(1/\varepsilon)`$, there are finite $`C_f`$ and positive $`\varepsilon_f`$ such that

```math
c_f(\varepsilon)\le c_{N(\varepsilon)}=2AN(\varepsilon)
\le C_f\log(1/\varepsilon)
\qquad(0<\varepsilon<\varepsilon_f).
```

This proves the full assertion.

## Dependencies, target comparison and audit

The only analytic ingredients are Cauchy's derivative estimate, convolution with a nonnegative smooth mollifier, Young's convolution inequality, and Fourier inversion with integration by parts. The finite-order cutoff estimate is proved directly rather than imported as an additional approximation hypothesis. It allows arbitrary complex-valued $`f`$, and only analyticity in a neighborhood of the given finite interval is used.

The source is Chen, Serkh and Bremer, [On the adaptive Levin method](https://www.math.toronto.edu/~bremer/papers/levin.pdf), §2.3, Definition 1 and the conjecture following equation (42). The construction above checks every quantitative bound of the pinned statement, including the Schwartz condition, compact Fourier support and the derivative of the Fourier transform. In particular, local polynomial approximation alone is not being used to infer global norm control. The bounds are analytic and need no numerical certificate. Independent mathematical review remains outstanding.
