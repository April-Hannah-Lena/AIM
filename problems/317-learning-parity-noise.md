# 317. Classical hardness of learning parity with noise

**Area:** Statistical learning and average-case computational complexity

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-17

## Problem statement

Fix a noise probability $0<\eta<1/2$, independent of the dimension $n$. Draw a secret $s$ uniformly from $\mathbb F_2^n$, where $\mathbb F_2=\{0,1\}$ with arithmetic modulo two. An algorithm receives $q(n)$ independent examples

$$
(a_i,b_i),\qquad a_i\sim\operatorname{Unif}(\mathbb F_2^n),\qquad
b_i=\langle a_i,s\rangle+e_i\pmod2,
$$

where the $e_i$ are independent Bernoulli$(\eta)$ bits, independent of $s$ and of all $a_i$.

Prove or refute the classical search-LPN hardness conjecture: for every such fixed $\eta$, every polynomial-time computable, polynomially bounded sample count $q:\mathbb N\to\mathbb N$, and every uniform randomized algorithm $A$ running in time polynomial in $n$, the success probability

$$
p_{A,q,\eta}(n)=\Pr\!\left[A\bigl(n,(a_i,b_i)_{i=1}^{q(n)}\bigr)=s\right]
$$

is negligible in $n$. Here negligible means that for every $c>0$ there is $n_0$ such that $p_{A,q,\eta}(n)\le n^{-c}$ for every $n\ge n_0$. Probability includes the algorithm's randomness. The algorithm and sample-count function are fixed before taking $n\to\infty$ and may depend on the fixed noise rate.

Time includes reading the examples and computing any preprocessing; no advice depending on the randomly drawn example matrix is supplied. The data are ordinary classical random examples, not chosen queries or coherent quantum examples. This asserts a computational barrier for recovering a hidden parity, not an information-theoretic impossibility.

## Applied significance

This is a basic test case for learning a discrete signal from independently corrupted labels. The conjectured gap between statistical identifiability and efficient recovery also underlies security arguments for lightweight authentication and other cryptographic constructions. Those security conclusions remain conditional on the relevant LPN assumption.

## References

1. Krzysztof Pietrzak, *Cryptography from Learning Parity with Noise*, SOFSEM 2012, LNCS 7147, 99–114, [published text](https://wiki.epfl.ch/edicpublic/documents/Candidacy%20exam/Cryptography_from_learning_parity_with_noise.pdf), §1 Definition 1, Lemma 1 and footnote 7.
2. Yu Bai, Chi Jin and Tiancheng Yu, *Near-Optimal Reinforcement Learning with Self-Play*, NeurIPS 2020, [published paper](https://proceedings.neurips.cc/paper_files/paper/2020/file/172ef5a94b4dd0aa120c6878fc29f70c-Paper.pdf), §5 Conjecture 7.
3. Divesh Aggarwal, Rishav Gupta, Hai Hoang Nguyen, Kel Zin Tan and Prashant Nalini Vasudevan, *Towards Worst-case Hardness for Low-Noise LPN*, [arXiv:2606.05834v1](https://arxiv.org/html/2606.05834v1), June 4, 2026 preprint, §1, Theorem 3.1 and Corollary 4.1.
4. Hayata Yamasaki, Natsuto Isogai and Mio Murao, *Advantage of quantum machine learning from general computational advantages*, npj Quantum Information 12 (2026), article 125, [published article](https://www.nature.com/articles/s41534-026-01279-y), noisy-label discussion around Eqs. (22)–(23).

## Status review

Pietrzak specifies the average-case search assumption, and the independently authored Bai–Jin–Yu paper states polynomial-time LPN hardness as a conjecture. The July 2026 Yamasaki–Isogai–Murao discussion still identifies efficient Search-LPN as unresolved. Its exhaustive search is polynomial in an external size $N$ because the secret dimension is only $O(\log N)$; it is exponential in that dimension.

Aggarwal et al. derive hardness from additional worst-case assumptions rather than proving unconditional hardness. The May 2026 [hardness-amplification paper](https://arxiv.org/html/2605.10056v2), Theorem 4.1 and Corollary 3, likewise assumes an LPN solver at transformed parameters; it supplies a reduction, not an unconditional lower bound. Noise can be added to transfer hardness to larger noise rates, but this does not remove those assumptions. BKW gives a subexponential algorithm using subexponentially many examples; polynomial-sample algorithms discussed in the cited surveys also remain superpolynomial. Statistical-query lower bounds restrict the algorithm class.

The September 17 searches also checked recent balanced-code preprocessing and sparse-XOR algorithms. Their full theorem statements change the advice or example distribution and do not settle this dense, uniform, fixed-noise question. The [evidence ledger](../research/expansion-2026-09/candidates/learning-parity-noise.json) records these comparisons, version checks, duplicate screening and access limits. Search/decision formulations are treated as one problem family, not separate additions.

A clearly separated adversarial self-pass passed on September 17. Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration.
