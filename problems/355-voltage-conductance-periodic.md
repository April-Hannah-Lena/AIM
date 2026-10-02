# 355. Self-sustained oscillations in the full voltage–conductance neuron equation

**Area:** Mathematical neuroscience; kinetic equations

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For some $`v_E>v_F>0`$, $`y_L,a_*,y_*,c>0`$, does the following model admit a nonnegative probability density $`F(t,v,y)`$ that is $`T`$-periodic for some $`T>0`$ and has nonconstant firing rate $`N(t)`$? Put

```math
J(v,y)=y(v_E-v)-y_Lv,\quad y_F=\frac{y_Lv_F}{v_E-v_F},\quad N(t)=\int_{y_F}^{\infty}J(v_F,y)F(t,v_F,y)\,dy,
```



```math
K_F(t,y)=y_*+cN(t)-y,\qquad a_F(t)=a_*+c^2N(t).
```

On $`(v,y)\in(0,v_F)\times(0,\infty)`$ require

```math
\partial_tF+\partial_v(JF)+\partial_y(K_FF)-a_F\partial_{yy}F=0,\qquad \iint F\,dv\,dy=1.
```

For $`0<y<y_F`$, impose $`F(t,0,y)=F(t,v_F,y)=0`$; for $`y>y_F`$, impose $`J(0,y)F(t,0,y)=J(v_F,y)F(t,v_F,y)`$. At $`y=0`$ impose $`K_FF-a_F\partial_yF=0`$, with vanishing flux as $`y\to\infty`$. Seek a distributional solution continuous in time into $`L^1`$, with these boundary traces, finite entropy and uniformly finite second $`y`$-moment over one period.

## Application

The voltage and the fluctuating synaptic conductance are both retained in this population model. A periodic orbit would explain collective firing rhythms without replacing conductance dynamics by a scalar rate or prescribing an external periodic drive.

## References

1. J. A. Carrillo and P. Roux, [*Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory*](https://arxiv.org/abs/2501.06015), Mathematical Models and Methods in Applied Sciences 35 (2025), 403–584, §7.6 (open periodic-solution problem).
2. C. Fonte Sanchez, S. Mischler and D. Salort, [*Existence of solutions to the Voltage-Conductance kinetic equation in a general conductivity regime*](https://arxiv.org/abs/2607.22112), preprint (2026), equations (1.1)–(1.4) and Theorem 1.1.
3. M. J. Cáceres, J. A. Carrillo and L. Tao, [*A numerical solver for a nonlinear Fokker–Planck equation representation of neuronal network dynamics*](https://doi.org/10.1016/j.jcp.2010.10.027), Journal of Computational Physics 230 (2011), 1084–1099, numerical oscillatory regimes.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using full voltage–conductance periodic solutions, nonlinear kinetic neuronal oscillations, and the cited authors. The 2025 survey explicitly lists periodic-solution existence as open. The July 2026 paper proves global weak existence for general connectivity and supplies the normalization above; its theorem does not construct a periodic trajectory. Periodic solutions of reduced voltage–conductance models do not settle this full transport–diffusion boundary-reset system. No later matching periodic-orbit theorem was located.
