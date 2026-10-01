#!/usr/bin/env python3
"""Numerical supplement to the smooth Steklov counterexample proof.

This is NOT a proof or a certified error enclosure. It approximates the even
(cosine) sector of Lambda v = sigma w v, with
    q(z) = 1 + epsilon * sum_{n>=1} exp(-sqrt(n)) z**n,
    w(theta) = 1 / abs(q(exp(i theta)))**2.

The domain is F(D), F' = q**(-2). Generalized eigenvectors are normalized in
L2(w dtheta/(2*pi)); dividing by sqrt(2*pi) gives physical arc-length norm one.
Finite truncations of q define analytic domains. The infinite-series theorem
must not be inferred from any finite numerical run.

Dependencies: Python 3.10+, NumPy, SciPy.
Example:
    python check_steklov.py --order 256 --samples 8192 --output results.csv
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import numpy as np
from numpy.typing import NDArray
from scipy.linalg import eigh


def compute(order: int, samples: int, epsilon: float) -> tuple[
    NDArray[np.float64], NDArray[np.float64], dict[str, float]
]:
    if order < 1:
        raise ValueError("order must be at least 1")
    if samples < 8 * (order + 1) or samples % 2:
        raise ValueError("samples must be even and at least 8*(order+1)")
    if not 0.0 < epsilon <= 0.01:
        raise ValueError("epsilon must lie in (0, 0.01]")

    coefficients = np.zeros(samples, dtype=np.complex128)
    modes = np.arange(1, samples // 2)
    coefficients[0] = 1.0
    coefficients[modes] = epsilon * np.exp(-np.sqrt(modes))
    q = np.fft.ifft(coefficients) * samples
    w = 1.0 / np.abs(q) ** 2
    w_hat_complex = np.fft.fft(w) / samples
    w_hat = w_hat_complex.real
    n = np.arange(order + 1)

    # For n,m >= 1, 2*cos(n theta)*cos(m theta) equals the sum of
    # cos((n-m) theta) and cos((n+m) theta).
    weight = w_hat[np.abs(n[:, None] - n[None, :])] + w_hat[n[:, None] + n[None, :]]
    weight[0, :] = np.sqrt(2.0) * w_hat[n]
    weight[:, 0] = np.sqrt(2.0) * w_hat[n]
    weight[0, 0] = w_hat[0]
    weight = (weight + weight.T) / 2.0
    dt_n = np.diag(n.astype(np.float64))

    eigenvalues, eigenvectors = eigh(dt_n, weight, check_finite=True)
    center_values = eigenvectors[0, :] / np.sqrt(2.0 * np.pi)
    residual = dt_n @ eigenvectors - (weight @ eigenvectors) * eigenvalues[None, :]
    diagnostics = {
        "max_abs_q_minus_one": float(np.max(np.abs(q - 1.0))),
        "min_weight": float(np.min(w)),
        "max_weight": float(np.max(w)),
        "max_imaginary_weight_coefficient": float(np.max(np.abs(w_hat_complex.imag))),
        "weighted_orthogonality_inf_norm": float(np.linalg.norm(
            eigenvectors.T @ weight @ eigenvectors - np.eye(order + 1), ord=np.inf)),
        "residual_inf_norm_divided_by_max_eigenvalue": float(
            np.linalg.norm(residual, ord=np.inf) / max(1.0, float(eigenvalues[-1]))),
    }
    return eigenvalues, center_values, diagnostics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=256, help="largest cosine mode")
    parser.add_argument("--samples", type=int, default=8192, help="even FFT sample count")
    parser.add_argument("--epsilon", type=float, default=0.01)
    parser.add_argument("--output", type=Path, default=Path("results.csv"))
    args = parser.parse_args()
    try:
        eigenvalues, center, diagnostics = compute(args.order, args.samples, args.epsilon)
    except (ValueError, np.linalg.LinAlgError) as exc:
        parser.error(str(exc))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["even_sector_index", "eigenvalue", "abs_center_value",
                         "minus_log_abs_center_over_eigenvalue"])
        for j, (sigma, value) in enumerate(zip(eigenvalues, np.abs(center))):
            ratio = -np.log(value) / sigma if j > 0 and sigma > 0 and value > 0 else float("nan")
            writer.writerow([j, f"{sigma:.16g}", f"{value:.16g}", f"{ratio:.16g}"])

    print("Finite Galerkin approximation; no rigorous numerical error bounds.")
    print(f"order={args.order}, samples={args.samples}, epsilon={args.epsilon}")
    for key, value in diagnostics.items():
        print(f"{key}: {value:.6g}")
    print("index   eigenvalue        abs(center)       -log(abs(center))/eigenvalue")
    for j in (8, 16, 32, 64, 96, 128, 160, 192):
        if j <= args.order:
            sigma, value = eigenvalues[j], abs(center[j])
            ratio = -np.log(value) / sigma if value > 0 else float("inf")
            print(f"{j:5d}   {sigma:14.9f}   {value:.9e}   {ratio:.9f}")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
