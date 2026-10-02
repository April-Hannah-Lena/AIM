#!/usr/bin/env python3
"""Reproduce supporting checks without changing the submitted proof packages.

Run from any directory with Python 3.12, numpy 2.3.5, scipy 1.17.0,
sympy 1.14.0 and mpmath 1.3.0. Logs are written alongside this file.
The computations corroborate the mathematical audit in README.md; they are
not a formal proof of any universal statement.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOLUTIONS = ROOT / "research" / "solutions"


def main() -> int:
    import numpy
    import scipy
    import sympy
    import mpmath

    versions = {"python": sys.version.split()[0], "numpy": numpy.__version__,
                "scipy": scipy.__version__, "sympy": sympy.__version__,
                "mpmath": mpmath.__version__}
    checks = []
    # Hash the committed Git blobs: Windows checkout newline conversion must
    # not invalidate a contributor's hash of the original file bytes.
    for manifest in sorted(SOLUTIONS.glob("*/SHA256SUMS*")):
        for line in manifest.read_text(encoding="utf-8").splitlines():
            expected, name = line.split(maxsplit=1)
            path = manifest.parent / name.lstrip("*")
            relative = path.relative_to(ROOT).as_posix()
            blob = subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=ROOT)
            actual = hashlib.sha256(blob).hexdigest()
            if actual != expected:
                raise RuntimeError(f"Submitted hash mismatch: {relative}")
            checks.append(relative)
    (HERE / "submitted_hashes.json").write_text(
        json.dumps({"method": "SHA-256 of committed original Git blobs",
                    "checked_files": checks, "passed": len(checks)}, indent=2) + "\n",
        encoding="utf-8")
    print(f"PASS: {len(checks)} submitted file hashes", flush=True)
    cases = [
        ("558-exact", "siavash-sadeghi-457-558", "verify_558.py", []),
        ("558-symbolic", "siavash-sadeghi-457-558", "symbolic_audit_558.py", []),
        ("506-exact", "siavash-sadeghi-506", "verify_exact.py",
         ["--output", str(HERE / "506-exact.json")]),
        ("560-exact", "siavash-sadeghi-560", "verify_exact.py",
         ["--json", str(HERE / "560-exact.json")]),
        ("024-numerical", "siavash-sadeghi-steklov-024", "check_steklov.py",
         ["--order", "256", "--samples", "8192", "--output", str(HERE / "024-numerical.csv")]),
        ("560-guards", "siavash-sadeghi-560", "test_verify_numerics.py", []),
        ("506-guards", "siavash-sadeghi-506", "test_numerical_guards.py", []),
        ("560-numerical", "siavash-sadeghi-560", "verify_numerics.py",
         ["--json", str(HERE / "560-numerical.json")]),
        ("506-numerical", "siavash-sadeghi-506", "verify_numerical.py",
         ["--output", str(HERE / "506-numerical.json")]),
    ]
    results = []
    for label, folder, script, arguments in cases:
        print(f"Running {label}", flush=True)
        command = [sys.executable, "-B", str(SOLUTIONS / folder / script), *arguments]
        result = subprocess.run(command, cwd=SOLUTIONS / folder,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, encoding="utf-8", errors="replace")
        (HERE / f"{label}.log").write_text(result.stdout, encoding="utf-8")
        results.append({"check": label, "exit_code": result.returncode,
                        "script": f"research/solutions/{folder}/{script}",
                        "arguments": [Path(a).name if a.startswith(str(HERE)) else a for a in arguments],
                        "log": f"{label}.log"})
        print(f"{label}: exit {result.returncode}", flush=True)
        if result.returncode:
            print(result.stdout, flush=True)
    report = {"checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "versions": versions, "results": results,
              "scope": "Reproduced supporting computations, not proof-assistant verification"}
    (HERE / "reproduction.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return int(any(row["exit_code"] for row in results))


if __name__ == "__main__":
    raise SystemExit(main())
