#!/usr/bin/env python3
"""Check that GFM preserves every equation, then render it with MathJax.

Optional QA dependencies and setup are documented in CONTRIBUTING.md.
The normal catalogue check remains standard-library only.
"""

import json
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys

from markdown_math import expressions, validate_math

ROOT = Path(__file__).resolve().parents[1]


class RenderedMath(HTMLParser):
    """Read the code nodes GitHub's math filter consumes after Markdown parsing."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.math = []
        self.in_pre = False
        self.math_pre = False
        self.in_code = False
        self.math_code = False
        self.parts = []
        self.previous = ""
        self.pending_inline = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "pre":
            self.in_pre = True
            self.math_pre = attrs.get("lang") == "math"
        elif tag == "code":
            self.in_code = True
            self.math_code = (self.math_pre or attrs.get("class") == "language-math"
                              or (not self.in_pre and self.previous.endswith("$")))
            self.parts = []
        else:
            self.previous = ""

    def handle_endtag(self, tag):
        if tag == "code":
            if self.math_code:
                tex = "".join(self.parts).strip()
                if self.in_pre:
                    self.math.append((tex, True))
                else:
                    self.pending_inline = tex
            self.in_code = False
            self.math_code = False
            self.previous = ""
        elif tag == "pre":
            self.in_pre = self.math_pre = False
        else:
            self.previous = ""

    def handle_data(self, data):
        if self.in_code:
            self.parts.append(data)
            return
        if self.pending_inline is not None:
            if data.startswith("$"):
                self.math.append((self.pending_inline, False))
            self.pending_inline = None
        self.previous = data


def main():
    try:
        import cmarkgfm
    except ImportError:
        raise SystemExit("Install scripts/requirements-math.txt; see CONTRIBUTING.md for math QA setup.")
    files = sorted(path for path in ROOT.rglob("*.md")
                   if not {".git", "node_modules", ".venv"}.intersection(path.parts))
    equations, errors = [], []
    for path in files:
        name = str(path.relative_to(ROOT))
        content = path.read_text(encoding="utf-8")
        errors.extend(f"{name}: {error}" for error in validate_math(content))
        source, _ = expressions(content)
        rendered = RenderedMath()
        rendered.feed(cmarkgfm.github_flavored_markdown_to_html(content))
        expected = [(expression.tex.strip().replace("\r\n", " ").replace("\n", " ")
                     if not expression.display else expression.tex.strip(), expression.display)
                    for expression in source]
        if expected != rendered.math:
            errors.append(f"{name}: Markdown changed or lost mathematics "
                          f"({len(expected)} source expressions, {len(rendered.math)} rendered)")
            for index, (before, after) in enumerate(zip(expected, rendered.math), 1):
                if before != after:
                    errors.append(f"  expression {index}: {before!r} became {after!r}")
                    break
            continue
        equations.extend({"file": name, "line": expression.line, "tex": tex, "display": display}
                         for expression, (tex, display) in zip(source, rendered.math))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"GFM preserved all {len(equations)} equations across {len(files)} Markdown files.", flush=True)
    result = subprocess.run(["node", str(ROOT / "scripts/check_math.js")],
                            input=json.dumps(equations), text=True, encoding="utf-8")
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
