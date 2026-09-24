# Pólya Cartesian-product closure certificate

For `C_d=(4*pi)^(-d/2)/Gamma(d/2+1)`, assume a bounded domain `Omega subset R^d` satisfies one of

```math
N_D^{\le}(E)\le C_d|\Omega|E^{d/2},\qquad
N_N^{<}(E)\ge C_d|\Omega|E^{d/2}.
```

Layer-cake implies for every `gamma>0`, on the same side,

```math
R_\gamma(E)\ \lessgtr\
\frac{\Gamma(\gamma+1)}{(4\pi)^{d/2}\Gamma(\gamma+d/2+1)}
|\Omega|E^{\gamma+d/2}.                                \tag{C1}
```

For factors of dimensions `a,b`, tensorization and the factor-2 counting bound give

```math
N_{1\times2}(E)\ \lessgtr\ C_b|\Omega_2|R_{b/2}^{(1)}(E). \tag{C2}
```

Applying (C1) to factor 1 and using

```math
C_b\frac{\Gamma(b/2+1)}{(4\pi)^{a/2}\Gamma((a+b)/2+1)}
=C_{a+b}                                                \tag{C3}
```

proves the corresponding Pólya inequality on `Omega_1 times Omega_2`. Here `less-than` is Dirichlet and `greater-than` is Neumann; the Neumann Riesz sum includes `mu_0=0`.

Hence the two-sided conjecture is closed under finite Cartesian products. In particular, known ball cases plus the exact interval counts prove both sides for all finite products of Euclidean balls and intervals.

For `gamma=1/2`, the exact Abel identity

```math
R_{1/2}^D(E)-L_{1/2,d}^{cl}|\Omega|E^{(d+1)/2}
=\frac12\int_0^E\frac{N_D^{\le}(t)-C_d|\Omega|t^{d/2}}{\sqrt{E-t}}dt
```

shows that a half-Riesz excess `delta` forces a counting excess at least `delta/sqrt(E)` at some lower energy. The Neumann reverse statement is identical. Thus a half-Riesz violation cannot occur on a Pólya-valid base.
