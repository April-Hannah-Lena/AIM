# Exact synthetic-spectrum obstruction and a positive-order cutoff theorem

Independent mathematical audit, 2026-09-08.

**Scope.** These are abstract nondecreasing positive sequences, not spectra of constructed domains. They show that the listed averaged inequalities and two Weyl terms, by themselves, do not imply the pointwise Pólya inequality. No geometric counterexample or spectral-realizability assertion is made.

Normalize the two-dimensional Weyl coefficient to one. Write

```math
N(E)=\#\{j:b_j\le E\},\qquad
R_s(E)=\sum_j(E-b_j)_+^s\quad(s>0).
```

The target averaged inequality is
$`R_s(E)\le E^{s+1}/(s+1)`$ for all $`E\ge0`$.
Counting conventions at eigenvalues do not affect any integral below. All sums are locally finite.

## 1. The concrete block and its elementary order-one certificate

Put $`a_j=j+\lceil\sqrt j\rceil`$ for $`j\ge1`$, and

```math
b_j=\begin{cases}399/4,&90\le j\le100,\\a_j,&\text{otherwise.}\end{cases}
```

The only changed block is exactly the set of $`j\le100`$ for which
$`a_j>399/4`$. Since $`a_{89}=99<399/4<a_{101}=112`$, the new sequence is nondecreasing. But $`b_{100}=399/4<100`$, so its pointwise normalized Pólya bound fails.

For $`x\ge0`$, monotonicity of $`(x-u)_+`$ gives
$`\sum_{j\ge1}(x-j)_+\le\int_0^\infty(x-u)_+\,du=x^2/2`$.
Because $`a_j\ge j+1`$,

```math
R_{1,a}(E)\le\tfrac12(E-1)_+^2.
```

The total downward displacement is exactly

```math
\Delta=\sum_{j=90}^{100}(j+10-399/4)=231/4.
```

The function $`x\mapsto(E-x)_+`$ is 1-Lipschitz, so the change in
$`R_1`$ is at most $`\Delta`$, and is zero for $`E\le399/4`$.
For $`E\ge399/4`$,

```math
\tfrac12E^2-\tfrac12(E-1)^2=E-\tfrac12
\ge397/4>231/4.
```

Consequently $`R_{1,b}(E)\le E^2/2`$ for every energy. This is an all-energy analytic certificate, not a sampled calculation.

## 2. A localized counting-deficit lemma

Let $`K>\varepsilon>0`$, $`q=K-\varepsilon`$, and let a sequence satisfy

1. $`N(x)\le x`$ outside $`[q,K)`$;
2. $`N(x)-x\le\varepsilon`$ on $`[q,K)`$;
3. $`x-N(x)\ge M>0`$ on $`[q-L,q)`$, where $`0<L\le q`$.

For any $`0<s\le1`$, the sharp bound holds at every energy if

```math
M\big((1+L/\varepsilon)^s-1\big)\ge\varepsilon.\tag{2.1}
```

**Proof.** The layer-cake identity is

```math
R_s(E)-\frac{E^{s+1}}{s+1}
=s\int_0^E(N(x)-x)(E-x)^{s-1}\,dx.
```

For $`E\le q`$, the integrand has no positive part. For $`E>q`$, set
$`\delta=E-q>0`$. Discarding other nonpositive contributions bounds the
right side above by

```math
\varepsilon A(\delta)-M B(\delta),\qquad
A(\delta)=\delta^s-(\delta-\varepsilon)_+^s,\quad
B(\delta)=(\delta+L)^s-\delta^s.
```

The ratio $`A/B`$ reaches its maximum at $`\delta=\varepsilon`$, where it equals

```math
\frac{1}{(1+L/\varepsilon)^s-1}.
```

For $`0<\delta\le\varepsilon`$, this follows by writing the ratio as
$`((1+L/\delta)^s-1)^{-1}`$, an increasing function. For
$`\delta>\varepsilon`$, write $`A`$ and $`B`$ as integrals of
$`f(t)=s t^{s-1}`$ over $`[\delta-\varepsilon,\delta]`$ and
$`[\delta,\delta+L]`$. Their logarithmic derivatives are weighted averages
of $`f'(t)/f(t)=(s-1)/t`$. This function is nondecreasing in $`t`$, so
$`A'/A\le B'/B`$, and $`A/B`$ is nonincreasing. This also covers $`s=1`$,
when the ratio is constant on that range. Continuity supplies the endpoint.
Condition (2.1) now proves the assertion. ∎

## 3. The same 100-level block satisfies every order s >= 1/128

For the sequence in Section 1,

```math
N_b(x)=\begin{cases}N_a(x),&x<q,\\\max\{100,N_a(x)\},&x\ge q.\end{cases}
```

Thus $`N_b(x)\le x`$ outside $`[q,100)`$, and the excess in that interval
is at most $`1/4`$. On $`[199/4,399/4)`$, let $`n=N_a(x)`$. Since
$`a_{42}=49\le199/4`$, one has $`n\ge42`$; hence

```math
x-n\ge a_n-n=\lceil\sqrt n\rceil\ge7.
```

Apply the lemma with $`\varepsilon=1/4`$, $`L=50`$, and $`M=7`$.
At $`s=1/128`$, its sufficient condition is exactly

```math
201^{1/128}\ge29/28
\quad\Longleftrightarrow\quad
29^{128}\le201\,28^{128},
```

an integer inequality verified by the companion script. Therefore

```math
R_{1/128,b}(E)\le\frac{128}{129}E^{129/128}\qquad(E\ge0).
```

For every $`\sigma>s`$, Tonelli's theorem and the beta integral give

```math
R_\sigma(E)=
\frac{\Gamma(\sigma+1)}{\Gamma(s+1)\Gamma(\sigma-s)}
\int_0^E R_s(u)(E-u)^{\sigma-s-1}\,du.
```

Inserting the order-$`s`$ bound gives
$`R_\sigma(E)\le E^{\sigma+1}/(\sigma+1)`$. Thus the single explicit block
satisfies all sharp Riesz bounds for **every $`\sigma\ge1/128`$**.

The heat bound follows from the same nonnegative integral identity:

```math
\sum_j e^{-t b_j}
=\frac{t^{s+1}}{\Gamma(s+1)}\int_0^\infty e^{-tE}R_s(E)\,dE
\le\frac1t\qquad(t>0).
```

## 4. Every prescribed positive lower cutoff is possible

Fix $`0<s\le1`$. Choose an integer

```math
K\ge\max\left\{4,\frac1{4(5^s-1)^2}\right\},
```

and set $`q=K-1/4`$,

```math
b_j=\begin{cases}\min\{a_j,q\},&j\le K,\\a_j,&j>K.\end{cases}
```

This is nondecreasing and $`b_K=q<K`$. As above, its counting function is
below $`x`$ except on $`[q,K)`$, with excess at most $`1/4`$.

For $`x\in[q-1,q)`$, let $`n=N_a(x)`$. If $`n\ge K/4`$, then
$`x-n\ge\sqrt n\ge\sqrt K/2`$. If $`n<K/4`$, including $`n=0`$, then

```math
x-n\ge3K/4-5/4\ge\sqrt K/2\qquad(K\ge4).
```

The localized lemma with $`L=1`$ and $`M=\sqrt K/2`$ gives the
order-$`s`$ bound. The beta identity gives every order $`\sigma\ge s`$,
and the heat estimate follows. A simpler sufficient choice is
$`K\ge\max\{4,1/(4s^2)\}`$, because $`5^s-1\ge s\log5>s`$.
For an arbitrary cutoff larger than one, use the construction for $`s=1`$.

This is substantially stronger than an exponentially large cutoff construction:
a polynomial-size $`K=O(s^{-2})`$ suffices.

## 5. Weyl terms and the unavoidable order-zero obstruction

For the baseline sequence,

```math
N_a(E)=E-\sqrt E+O(1).
```

Indeed, if $`n=N_a(E)`$, then
$`n+\sqrt n\le E<n+1+\lceil\sqrt{n+1}\rceil \le n+\sqrt{n+1}+2`$. This gives $`n=E+O(\sqrt E)`$, then
$`\sqrt n=\sqrt E+O(1)`$, and finally the displayed formula.
Only finitely many entries were changed, and the counting functions are exactly
equal once $`E`$ exceeds every changed old and new level. Thus the same
two-term law holds for each modified sequence.

The quantifier is essential: **for each fixed positive cutoff, there exists a
sequence** with all the bounds above that cutoff. A single sequence violating
Pólya cannot satisfy the sharp bound for every positive order. If
$`b_K<K`$, choose $`E\in(b_K,K)`$. As $`s\downarrow0`$, the locally finite
sum $`R_s(E)`$ tends to the strict counting function
$`\#\{j:b_j<E\}\ge K>E`$, whereas $`E^{s+1}/(s+1)\to E`$.
Thus some sufficiently small positive orders must fail.

The coefficient one of the negative second Weyl term has the disk's
isoperimetric-minimum value when the leading coefficient is normalized to one.
That numerical match does not provide realizability. These constructions also
do not establish any other constraints imposed on genuine Dirichlet spectra,
such as universal commutator inequalities or a full geometric heat expansion.

## 6. Reproduction

Run `python obstruction_referee_2026-09-08.py`. The script uses integer
arithmetic, `fractions.Fraction`, and `math.isqrt`; it verifies the exact block,
the all-energy order-one constants, the localized strip constants, and the
integer condition for order $`1/128`$. It writes
`obstruction_referee_2026-09-08.json`. It does not sample energies or claim to
mechanize the analytic arguments.

## 7. Independent adversarial audit of the separate square-tail construction

The note `spectral_attack_square_tail_obstruction_2026-09-08.md` was checked
independently after the preceding construction. **Verdict: its existential
abstract-sequence theorem is established, conditional only on its correctly
stated standard/external square-spectrum facts; no mathematical error was
found.** This is an audit within the same research invocation, not a second
separate senior-review run of a solution candidate.

The source of the positive-order boundary asymptotics was checked directly:
[Frank--Larson, version 3, Theorem 1.1, equation (5)](https://arxiv.org/html/2407.11808v3)
applies to bounded Lipschitz domains and every fixed positive Riesz order.
With area $`4\pi`$ and $`B=|\partial Q|/(4\pi)`$, its three boundary
coefficients are $`-2B/3`$, $`-8B/15`$, and $`-\pi B/4`$, at orders
$`1,2,1/2`$, respectively. These imply the claimed Yang margin
$`-4Bz^{5/2}/15+o(z^{5/2})`$.

The following potential failure points were checked explicitly.

- The lattice estimate $`b_j=j+O(\sqrt j)`$ is uniform on the entire
  moving block $`n\le j<n+m`$, since $`m=\lfloor n^{7/10}\rfloor=o(n)`$.
  Thus the mean is $`a=n+(m-1)/2+O(\sqrt n)`$, and all block deviations
  are $`O(m)`$.
- At $`z=a`$, deleting the old active block terms changes
  $`F(z)=3R_2(z)-2zR_1(z)`$ by $`O(nm^2)=O(n^{12/5})`$, smaller than
  its negative baseline term of order $`n^{5/2}`$. Only the fixed square's
  asymptotic expansion is evaluated along $`a=a_n\to\infty`$; there is no
  appeal to an expansion uniform in the modified spectra.
- On each new gap, the modified Yang functional is a quadratic whose
  leading coefficient is the number of active entries, hence is
  nonnegative. It lies below the chord between its nonpositive endpoint
  values. Above the block, preservation of the block sum gives exactly
  $`F_\nu-F_b=-3\sum(b_j-a)^2\le0`$. Multiplicities at endpoints
  contribute zero and do not spoil either argument.
- Jensen's inequality decreases every convex trace under replacement of a
  whole block by its mean. This preserves the heat upper bounds and Riesz
  upper bounds of orders at least one. Every partial sum inside the block
  increases because the mean of an initial segment of an ordered block is
  at most the mean of the whole block; other partial sums are unchanged.
- At $`E=b_{n+m-1}`$, normalized original block gaps differ uniformly from
  $`1-r/m`$ by $`o(1)`$. Uniform continuity of the square root validates
  the Riemann sum even where a gap vanishes. The gain coefficient
  $`1/\sqrt2-2/3`$ is positive because $`1/2>4/9`$. Its order is
  $`m^{3/2}\asymp n^{21/20}`$, exceeding the square's order-$`n`$
  half-Riesz boundary deficit.
- The mean is strictly below the last replaced index for large $`n`$,
  since $`\sqrt n=o(m)`$, giving the claimed pointwise violation.
  For each fixed block, eventual equality with the square spectrum is
  literal, so the boundary asymptotics survive. This last assertion takes
  the energy limit with the block fixed; it is not a uniform assertion
  over growing blocks.

The theorem's threshold remains existential; no explicit large integer has
been certified. It does not give a realizable Dirichlet spectrum, a domain
counterexample, or an obstruction to using further geometric constraints.
The conclusion about logical insufficiency is confined to the explicitly
listed scalar inequalities and asymptotic/tail data.
