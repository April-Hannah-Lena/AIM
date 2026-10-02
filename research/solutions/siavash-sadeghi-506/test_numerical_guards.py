"""Cheap regression probes for final AIM506 scipy_direct guards."""
import importlib.util
import math
from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location(
    "aim506_final", ROOT / "verify_numerical.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
checks = 0


def reject(results, message):
    global checks
    with patch.object(module, "quad", side_effect=results):
        try:
            module.scipy_direct(1.0, 0.5)
        except ArithmeticError as error:
            if message not in str(error):
                raise AssertionError(f"Unexpected rejection: {error}") from error
        else:
            raise AssertionError(f"Invalid numerical results accepted: {results}")
    checks += 1


for bad in (float("nan"), math.inf, -math.inf):
    for index in range(4):
        values = [1.0, 0.01, 1.0, 0.01]
        values[index] = bad
        reject([(values[0], values[1]), (values[2], values[3])], "Non-finite")
for index in (1, 3):
    values = [1.0, 0.01, 1.0, 0.01]
    values[index] = -0.01
    reject([(values[0], values[1]), (values[2], values[3])], "Negative quadrature")
for bad in (0.0, -1.0):
    for index in (0, 2):
        values = [1.0, 0.01, 1.0, 0.01]
        values[index] = bad
        reject([(values[0], values[1]), (values[2], values[3])], "Nonpositive")
reject([(1e308, 0.0), (1e-308, 0.0)], "Non-finite numerical log")
reject([(1e-308, 1e308), (1e-308, 0.0)], "Non-finite numerical log")

with patch.object(module, "quad", side_effect=[(2.0, 0.01), (4.0, 0.02)]):
    result = module.scipy_direct(1.0, 0.5)
    if result != (math.log(0.5), 0.01):
        raise AssertionError(f"Valid finite calculation changed: {result}")
checks += 1
print(f"PASS: {checks} focused scipy_direct regression cases")
print("Covered nonfinite integrals/error estimates, negative errors, nonpositive")
print("integrals, computed overflow, and an unchanged valid finite control.")
