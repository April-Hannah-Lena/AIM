# Exact obstruction to desmoothing, including Yang's inequality

Research note, 2026-09-08. These are statements about an **abstract spectral sequence** and a separate exact product reduction. No Euclidean-domain counterexample, proof of Pólya's conjecture, or claim of novelty is asserted.

## 1. A certified abstract sequence

Work in planar Weyl units: the putative area is `4*pi`, the Weyl count is `E`, and the sharp order-gamma Riesz bound is `E^(gamma+1)/(gamma+1)`.

Let

```math
n=262144,\quad m=1024,\quad
a=n+(m+1)/2=262656.5,
```

and define an increasing sequence, with multiplicities, by

```math
\nu_j=\begin{cases}
a,&n\le j\le n+m-1,\\
j+1,&\text{otherwise},
\end{cases}\qquad j=1,2,\ldots.
```

This replaces a finite block of the baseline sequence `b_j=j+1` by its arithmetic mean. The first `n-1` entries and the infinite tail remain unchanged.

### Theorem

The sequence has all of the following properties:

1. `nu_j/j -> 1` (indeed `nu_j=j+1` eventually).
2. For every `t>0`, `sum exp(-t nu_j) <= 1/t`.
3. For every real `gamma>=1` and every `E>=0`,

   ```math
   \sum_j(E-\nu_j)_+^\gamma\le E^{\gamma+1}/(\gamma+1).
   ```

4. For every integer `k>=1`, `sum_{j<=k}nu_j >= k^2/2`.
5. Yang's planar first universal inequality holds at **every** energy:

   ```math
   F_\nu(z):=\sum_{\nu_j<z}(z-\nu_j)(z-3\nu_j)\le0
   \qquad(z\ge0).
   ```

   Equivalently, `sum (z-nu_j)_+^2 <= 2 sum nu_j (z-nu_j)_+`.
6. Pólya counting fails: at `E0=a+1/4`,

   ```math
   N_\nu(E_0)=n+m-1=263167>E_0=262656.75.
   ```

7. The sharp half-Riesz inequality fails at `E=n+m=263168`:

   ```math
   \sum_j(E-\nu_j)_+^{1/2}>\frac23E^{3/2}.
   ```

### Proof of properties 1--4

For every nonnegative, decreasing convex function `f`, Jensen's inequality on the replaced block gives

```math
\sum_j f(\nu_j)\le\sum_j f(j+1)
\le\int_0^\infty f(x)\,dx.
```

The second inequality follows interval by interval from monotonicity. Apply this to `f(x)=exp(-t x)` and `f(x)=(E-x)_+^gamma`, `gamma>=1`. The infinite sums converge or are finite in the cases used. This proves 2--3. A mean replacement raises every partial sum ending inside the block, leaves the full block sum fixed, and otherwise leaves the partial sums unchanged. Thus

```math
\sum_{j=1}^k\nu_j\ge\sum_{j=1}^k(j+1)=k(k+3)/2\ge k^2/2.
```

The finite nature of the modification proves 1.

### Proof of Yang's inequality, including the two new gaps

For the baseline sequence, with `k` active terms,

```math
F_b(z)=kz^2-4z\sum_{j=1}^k(j+1)+3\sum_{j=1}^k(j+1)^2.
```

At the right endpoint `z=k+2`,

```math
F_b(k+2)=-3k(k+1)/2\le0.
```

The value at the left endpoint is nonpositive as well, since that endpoint is the previous right endpoint and its newly entering summand is zero. Convexity of the quadratic on each spectral gap proves `F_b(z)<=0` for every `z`.

Below `z=n` the modified and baseline sequences coincide. At the new plateau `z=a`, exactly `n-1` terms contribute and direct summation gives

```math
\frac{F_\nu(a)}{n-1}
=\frac{(m-3)^2}{4}-\frac{3n+2}{2}.
```

This is nonpositive if `(m-3)^2 <= 6n+4`; our integers satisfy this strictly. Consequently the quadratic is nonpositive throughout the first new gap `[n,a]`.

Write `b=n+m+1` for the next eigenvalue after the plateau. At `z=b` all original and replacement block entries contribute. The block sum is unchanged and its sum of squares decreases by

```math
V_m=\sum_{i=1}^m\left(i-\frac{m+1}{2}\right)^2
=\frac{m(m^2-1)}{12}.
```

Therefore `F_nu(b)=F_b(b)-3V_m<=0`. Convexity proves the inequality throughout the second new gap `[a,b]`. For every `z>=b`, the same identity `F_nu(z)=F_b(z)-3V_m` holds, proving the complete, infinite statement. Values at eigenvalues cause no difficulty because their summands vanish.

### Exact certificate for the half-Riesz violation

Set `E=n+m`. The baseline half-Riesz sum is

```math
R_b(E)=\sum_{h=1}^{E-2}\sqrt h
\ge\frac23(E-2)^{3/2}.
```

Thus its deficit from `(2/3)E^(3/2)` is less than `2 sqrt(E)`. The mean replacement increases this sum by

```math
\Delta=m\sqrt{(m-1)/2}-\sum_{h=0}^{m-1}\sqrt h
\ge m\sqrt{(m-1)/2}-\frac23m^{3/2}.
```

Here `sqrt(m)=32`, `(2261/100)^2 < (m-1)/2`, and `E<514^2`. Consequently

```math
\Delta>
1024\frac{2261}{100}-\frac{65536}{3}
=\frac{98048}{75}>1028>2\sqrt E.
```

Every comparison in this certificate is rational after squaring the two positive square-root bounds. This proves property 7 without computing a large sum or using floating point. Property 6 is immediate from the plateau's multiplicity.

### What this excludes, and what it does not

Even Weyl asymptotics, all sharp heat and order-`gamma>=1` Riesz bounds, Li--Yau, and the full planar Yang inequality **together** do not imply either Pólya counting or the half-Riesz inequality. Additional information tied to Euclidean domains is required.

This sequence is not asserted to be a Dirichlet spectrum. Its eventual form has no negative square-root boundary term in the count; it is therefore not an obstruction to arguments explicitly using such additional boundary information. The note establishes only the stated logical non-implication. The standard role of Yang's inequalities and transform relations is documented, for example, by Harrell--Hermi, *On Riesz Means of Eigenvalues*, https://arxiv.org/abs/0712.4088 . The construction and its proof above are self-contained.

## 2. Exact cylinder equivalence and finite transfer threshold

Let `Omega` be an actual bounded Lipschitz domain in `R^d`, `V=|Omega|`, and `I_L=(0,L)`. Put

```math
C_q=\frac{\omega_q}{(2\pi)^q},\qquad
R_{1/2}^{D/N}(E)=\sum_j(E-\lambda_j^{D/N})_+^{1/2}.
```

Use the inclusive Dirichlet count `N_D^le(E)=#{lambda_j<=E}` and the strict Neumann count `N_N^lt(E)=#{mu_j<E}`, including the zero Neumann eigenvalue. These conventions give the desired Pólya eigenvalue statements by continuity in energy.

Separation of variables gives exactly

```math
N_{\Omega\times I_L}^{D,\le}(E)
=\sum_{\lambda_j\le E}
\left\lfloor\frac L\pi\sqrt{E-\lambda_j}\right\rfloor,
```

```math
N_{\Omega\times I_L}^{N,<}(E)
=\sum_{\mu_j<E}
\left\lceil\frac L\pi\sqrt{E-\mu_j}\right\rceil.
```

The strict Neumann restriction `mu_j<E` is essential: a zero residual energy contributes no eigenvalue. In particular,

```math
0\le\frac L\pi R_{1/2}^D(E)-N_{\Omega\times I_L}^{D,\le}(E)
\le N_\Omega^{D,\le}(E),
```

```math
0\le N_{\Omega\times I_L}^{N,<}(E)-\frac L\pi R_{1/2}^N(E)
\le N_\Omega^{N,<}(E).
```

For each fixed `E`, the quantities on the right are finite and independent of `L`. Dividing by `L` and taking `L` to infinity is therefore justified by this explicit error bound, with no uniform-in-energy limit claimed.

It follows that the following statements are equivalent, separately for each boundary condition:

* Pólya holds for `Omega x I_L` for **every** length `L>0` and every energy.
* The sharp half-Riesz inequality holds for `Omega` at every energy, namely

  ```math
  R_{1/2}^D(E)\le \pi C_{d+1}V E^{(d+1)/2},
  \quad\text{or}\quad
  R_{1/2}^N(E)\ge \pi C_{d+1}V E^{(d+1)/2}.
  ```

Here

```math
\pi C_{d+1}=
\frac{\Gamma(3/2)}{(4\pi)^{d/2}\Gamma((d+3)/2)}
=L_{1/2,d}^{\rm cl},
```

so these are precisely the semiclassical constants. The reverse implication uses the floor/ceiling sign directly; the forward implication uses the displayed controlled limit.

There is also a quantitative finite transfer. If an actual domain violates its half-Riesz inequality at `E` by `delta>0`, in the relevant direction, then its cylinder violates Pólya at the same energy for every

```math
L>\pi N_\Omega(E)/\delta,
```

using the relevant base counting convention. This follows by bounding the floor/ceiling rounding error by the base count. It is conditional on a violation for an **actual** domain; the abstract sequence in Section 1 supplies no such domain.

The reduction identifies a smaller, exact bottleneck: establish geometric half-Riesz information for the one-dimensional-cylinder route. Sharp order-one Riesz bounds, even supplemented by Yang, do not suffice by Section 1. The reduction is elementary and no novelty claim is made; compare Laptev's dimension-lifting framework and He--Wang, *Pólya's conjecture for thin products*, https://arxiv.org/abs/2402.12093 .


A stronger, noneffective construction preserving an actual square spectral tail is proved in `spectral_attack_square_tail_obstruction_2026-09-08.md`.
