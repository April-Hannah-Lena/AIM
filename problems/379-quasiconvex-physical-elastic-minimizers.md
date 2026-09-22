# 379. Existence of elastic equilibria under quasiconvexity and infinite compression energy

**Area:** Nonlinear elasticity; variational equilibrium

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^3$ be bounded with Lipschitz boundary, $p>3$, and let $W:\mathbb R^{3\times3}\to[0,\infty]$ be finite and $C^1$ on $\mathrm{GL}^+(3)=\{F:\det F>0\}$, infinite otherwise. Assume $W(RF)=W(F)$ for $R\in SO(3)$, $W(F)\ge c|F|^p-C$, and $W(F_j)\to\infty$ whenever $\det F_j\downarrow0$. Assume quasiconvexity in the explicit sense
$$W(F)\le\int_{(0,1)^3}W(F+D\varphi(x))\,dx\quad\text{for every }F\text{ and }\varphi\in C_c^\infty((0,1)^3;\mathbb R^3).$$
For every prescribed trace $g$ for which the class
$$\mathcal A_g=\{y\in W^{1,p}(\Omega;\mathbb R^3):\operatorname{Tr}y=g,\ I(y):=\int_\Omega W(Dy)\,dx<\infty\}$$
is nonempty, must $I$ attain its infimum on $\mathcal A_g$? No polyconvexity, polynomial upper growth or additional global-injectivity constraint is assumed.

## Application

The determinant barrier prevents local collapse and orientation reversal in a solid. Resolving existence with quasiconvexity would extend equilibrium theory to a broader class of constitutive laws than those covered by polyconvexity.

## References

1. J. M. Ball, [*Some open problems in elasticity*](https://people.maths.ox.ac.uk/~ball/Articles%20in%20Conference%20Proceedings%20and%20Books/JMB%202002%20re%20Marsden%2060th.pdf), in *Geometry, Mechanics, and Dynamics*, Springer (2002), §2.2, Problem 1, equations (2.7), (2.10) and Theorem 2.1.
2. J. M. Ball, [*Convexity conditions and existence theorems in nonlinear elasticity*](https://doi.org/10.1007/BF00279992), Archive for Rational Mechanics and Analysis 63 (1977), 337–403, polyconvex existence theory.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using quasiconvex determinant-constrained elasticity, Ball Problem 1, and existence beyond polyconvexity. The stated $p>3$ case avoids cavitation but retains the physical infinite-energy determinant barrier. Standard quasiconvex existence theorems with a finite polynomial upper bound cannot cover that barrier. Polyconvex theorems and existence for special relaxed material energies do not prove the assertion for every $W$ here. No later general theorem or matching counterexample was located. This concerns existence of a minimizer, distinct from the repository's question about whether an existing minimizer satisfies force balance.
