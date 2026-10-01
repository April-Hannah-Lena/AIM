"""Regression tests for nonfinite numerical results; no large matrix solves."""
from contextlib import ExitStack, redirect_stdout
import io
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import verify_numerics as verifier


def valid_spectral(s, v, lam):
    """Cheap valid controls let each test reach its chosen failure path."""
    if not isinstance(lam, str):
        return verifier.mp.mpf("-0.5")
    s, v = verifier.mp.mpf(s), verifier.mp.mpf(v)
    if lam == "chi2":
        return -s*(s-v)/(verifier.mp.sqrt(v)*(2*s-v)**verifier.mp.mpf("1.5"))
    return v*((1+s+v)**verifier.mp.mpf("-1.5")-(1+2*v)**verifier.mp.mpf("-1.5"))


class NumericalGuardTests(unittest.TestCase):
    def valid_controls(self):
        stack = ExitStack()
        stack.enter_context(patch.object(verifier, "spectral_integral", valid_spectral))
        stack.enter_context(patch.object(verifier, "nystrom_integral", lambda *args: -0.5))
        stack.enter_context(patch.object(verifier, "prefix_stress_test", lambda: (363810, -0.1)))
        stack.enter_context(redirect_stdout(io.StringIO()))
        return stack

    def test_invalid_integral_values(self):
        # 30 cases: six calculation paths, each with five invalid values.
        with self.valid_controls():
            for value in (float("nan"), float("inf"), -float("inf"), 0.0, 1.0):
                for location in ("spectral", "n256", "n512", "n2048", "chi2", "mmd"):
                    with self.subTest(location=location, value=value):
                        def spectral(s, v, lam):
                            if (location == "spectral" and not isinstance(lam, str)) or location == lam:
                                return verifier.mp.mpf(value)
                            return valid_spectral(s, v, lam)

                        def nystrom(s, v, lam, nodes):
                            return value if location == f"n{nodes}" else -0.5

                        with patch.object(verifier, "spectral_integral", spectral), patch.object(
                                verifier, "nystrom_integral", nystrom):
                            with self.assertRaisesRegex(AssertionError, "Nonfinite or nonnegative"):
                                verifier.main(None)

    def test_nonfinite_errors(self):
        # Six cases: inject errors separately from their input-value guards.
        with self.valid_controls():
            for value in (float("nan"), float("inf"), -float("inf")):
                for fail_at, label in ((0, "Nystrom comparison error"), (12, "Endpoint mismatch")):
                    with self.subTest(path=label, value=value):
                        calls = [0]

                        def faulty_abs(value_in):
                            index = calls[0]
                            calls[0] += 1
                            return value if index == fail_at else abs(value_in)

                        with patch.object(verifier, "abs", faulty_abs, create=True):
                            with self.assertRaisesRegex(AssertionError, label):
                                verifier.main(None)

    def test_nonfinite_prefixes(self):
        # Three cases in the real prefix loop, without any quadrature calls.
        original_zeros_like = verifier.np.zeros_like
        for value in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                with patch.object(verifier.np, "zeros_like",
                                  lambda array: original_zeros_like(array) + value):
                    with verifier.np.errstate(invalid="ignore"):
                        with self.assertRaisesRegex(AssertionError, "Nonfinite or nonnegative prefix"):
                            verifier.prefix_stress_test()

    def test_strict_json(self):
        # Three cases: strict JSON remains a final guard for report fields.
        with self.valid_controls(), TemporaryDirectory() as directory:
            for value in (float("nan"), float("inf"), -float("inf")):
                with self.subTest(value=value):
                    with patch.object(verifier, "prefix_stress_test", lambda: (363810, value)):
                        with self.assertRaises(ValueError):
                            verifier.main(Path(directory) / "invalid.json")


if __name__ == "__main__":
    unittest.main()
