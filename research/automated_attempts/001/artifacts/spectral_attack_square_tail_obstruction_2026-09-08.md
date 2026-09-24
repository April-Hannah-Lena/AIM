# Yang-compatible obstruction preserving an actual square spectral tail

Research note, 2026-09-08. This is an existential abstract-sequence result, not a counterexample domain or a claim of novelty. The separate rational certificate is in `spectral_attack_yang_and_cylinders_2026-09-08.md`.


The absence of a boundary term in the rational example can be repaired at the abstract-sequence level. The following argument is rigorous but does not provide an effective threshold for its large integer parameter. It uses a stated external theorem on two-term Riesz asymptotics, rather than claiming a numerical certificate for that theorem.

Let `Q` be the square of area `4*pi`, let `b_j` be its actual Dirichlet eigenvalues, and put `B=|boundary Q|/(4*pi)>0`. For each integer `n`, set

```math
m=\lfloor n^{7/10}\rfloor,\qquad
a=\frac1m\sum_{j=n}^{n+m-1}b_j,
```

and replace precisely these `m` entries by `a`, leaving every other entry unchanged. Denote the resulting abstract sequence by `nu`.

**Theorem.** For all sufficiently large `n`, the modified sequence has the exact square spectral tail and the first `n-1` square eigenvalues; satisfies every sharp heat bound and every sharp Riesz bound of order `gamma>=1`, Li--Yau, and Yang's first planar inequality at every energy; but violates both Pólya counting and the sharp half-Riesz inequality. It therefore preserves the square's leading boundary asymptotics as well. No actual domain realizing the modified spectrum is asserted.

**Dependencies.** The square satisfies Pólya by tiling and Yang's universal inequality. Its lattice spectrum gives the elementary estimate `b_j=j+O(sqrt(j))`: enclosing the quarter-disk lattice cells between disks with radii differing by a constant proves `N_Q(E)=E+O(sqrt(E))`, which inverts to this assertion. The two-term Riesz expansions of positive orders are, in these normalized units,

```math
R_1^b(E)=\tfrac12E^2-\tfrac{2B}{3}E^{3/2}+o(E^{3/2}),
```


```math
R_2^b(E)=\tfrac13E^3-\tfrac{8B}{15}E^{5/2}+o(E^{5/2}),
```


```math
R_{1/2}^b(E)=\tfrac23E^{3/2}-\tfrac{\pi B}{4}E+o(E).
```

These are instances of Theorem 1.1, equation (5), in Frank--Larson, *Riesz means asymptotics for Dirichlet and Neumann Laplacians on Lipschitz domains*, https://arxiv.org/abs/2407.11808 (version 3, 8 August 2025). Its coefficient is `-(1/4)L_(gamma,d-1)^cl |boundary Q|`, with `L_(gamma,q)^cl=Gamma(gamma+1)/((4*pi)^(q/2) Gamma(gamma+q/2+1))`; the theorem applies to bounded Lipschitz domains and every fixed positive `gamma`. Only positive-order asymptotics are used; no unproved two-term counting law is needed.

**Proof.** Mean replacement preserves the ordering. Jensen's inequality decreases every convex trace, so the sharp heat/Riesz bounds follow from those for the square. Every initial partial sum increases or stays fixed, preserving Li--Yau. The sequence eventually equals the square spectrum exactly.

It remains to check Yang. In terms of Riesz means,

```math
F_b(z)=3R_2^b(z)-2zR_1^b(z)
=-\tfrac{4B}{15}z^{5/2}+o(z^{5/2}).
```

The lattice estimate gives, uniformly on the replaced block,

```math
b_{n+r}=n+r+O(\sqrt n),\qquad 0\le r\le m-1.
```

Hence `a=n+O(m)`, and every block entry differs from `a` by `O(m)`. At the plateau, all replacement terms vanish. Compared with `F_b(a)`, at most `m` original terms have been removed; each is `O(n*m)`. Therefore

```math
F_\nu(a)=F_b(a)+O(nm^2)
=-\tfrac{4B}{15}n^{5/2}+o(n^{5/2})<0,
```

because `n*m^2=O(n^(12/5))=o(n^(5/2))`.

Before the first replaced eigenvalue the sequences agree. On the gap from `b_(n-1)` to `a`, `F_nu` is a convex quadratic with nonpositive endpoint values. At the next unreplaced eigenvalue `b_(n+m)`, all block entries are active, and preservation of the block sum gives

```math
F_\nu(b_{n+m})=F_b(b_{n+m})
-3\sum_{j=n}^{n+m-1}(b_j-a)^2\le0.
```

Thus the second new gap is handled by the same convexity argument; above it the same nonpositive variance correction holds identically. Possible multiplicities at endpoints add only zero terms. This proves Yang at every energy.

For half-Riesz, set `E=b_(n+m-1)`. Since `sqrt(n)=o(m)`, the uniform lattice estimate and a Riemann sum give

```math
R_{1/2}^\nu(E)-R_{1/2}^b(E)
=\left(\frac1{\sqrt2}-\frac23+o(1)\right)m^{3/2}.
```

Indeed the new block contributes `m sqrt(E-a)`, asymptotic to `m^(3/2)/sqrt(2)`, while the original block contributes `m^(3/2) integral_0^1 sqrt(1-s) ds + o(m^(3/2))`. Uniform continuity of the square root justifies this even at the last block entry, where its argument is zero.

The positive gain has order `n^(21/20)`, whereas the square's half-Riesz deficit has order `E=O(n)`. It therefore exceeds that deficit for every sufficiently large `n`, proving a strict half-Riesz violation. Finally,

```math
a=n+(m-1)/2+O(\sqrt n)<n+m-1
```

for all sufficiently large `n`, so `nu_(n+m-1)<n+m-1`, directly violating Pólya.

This stronger result rules out deriving half-Riesz or pointwise Pólya from the above scalar inequalities even after supplying the actual square spectral tail. It does not rule out arguments using restrictions on how low and intermediate eigenvalues can vary while that tail is fixed, spatial eigenfunction information, or other geometric spectral constraints. No novelty claim is made.
