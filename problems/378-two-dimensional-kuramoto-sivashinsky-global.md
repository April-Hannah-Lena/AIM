# 378. Global regularity for two-dimensional Kuramoto–Sivashinsky on arbitrary square tori

**Area:** Combustion fronts; nonlinear pattern formation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every $L>\pi$ and real-valued $h_0\in C^\infty(\mathbb T_L^2)$ with zero mean, where $\mathbb T_L^2=(\mathbb R/(2L\mathbb Z))^2$, does

$$
\partial_t h+\Delta^2h+\Delta h+|\nabla h|^2-\frac1{4L^2}\int_{\mathbb T_L^2}|\nabla h(t,y)|^2\,dy=0,\qquad h(0)=h_0,
$$

have a global smooth solution? Require $h\in C([0,T];H^m(\mathbb T_L^2))$ for every finite $T$ and integer $m\ge0$, with no restriction on the size of the datum. The mean subtraction fixes the otherwise evolving additive constant.

## Application

This equation models unstable flame fronts and other dissipative patterns. The question asks whether nonlinear steepening remains controlled when a genuinely two-dimensional domain supports growing linear modes.

## References

1. D. M. Ambrose, A. L. Mazzucato and R. Montalto, [*Nonlinear Instability in the 2D Kuramoto–Sivashinsky equation*](https://arxiv.org/abs/2607.19887), preprint (2026), §1 and main theorem in §2.
2. D. M. Ambrose and A. L. Mazzucato, [*Global existence and analyticity for the 2D Kuramoto–Sivashinsky equation*](https://arxiv.org/abs/1708.08752), Journal of Dynamics and Differential Equations 31 (2019), 1525–1547, small-data global theorem and estimates in the presence of growing modes.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using two-dimensional Kuramoto–Sivashinsky global existence on unrestricted square tori. The July 2026 paper explicitly identifies the missing general global theory. It proves growth from arbitrarily small data to order-one size, which is nonlinear instability rather than finite-time blowup. Small-data theorems without growing linear modes and results for thin anisotropic domains do not cover these data and domains. The spatial-average coefficient above is normalized by the area $4L^2$. No matching general resolution was located.
