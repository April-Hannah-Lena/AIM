"""Locate mathematics while leaving Markdown code examples untouched."""

from dataclasses import dataclass
import re
import textwrap


@dataclass
class Expression:
    tex: str
    display: bool
    start: int
    end: int
    line: int
    syntax: str


TOKEN = re.compile(
    r"(?P<fence>^[ ]{0,3}(?P<marker>`{3,}|~{3,})(?P<info>[^\n]*)\n)"
    r"|(?P<comment><!--)"
    r"|(?P<code>(?<!\\)`+)"
    r"|(?P<dollar>(?<!\\)\$\$?)"
    r"|(?P<legacy>(?<!\\)\\[\[(])", re.MULTILINE)


def expressions(content):
    """Return math spans and delimiter errors, including legacy unprotected math."""
    found, errors = [], []
    position = 0
    while match := TOKEN.search(content, position):
        start, end = match.span()
        line = content.count("\n", 0, start) + 1
        if match["comment"]:
            close = content.find("-->", end)
            position = len(content) if close < 0 else close + 3
            continue
        if match["fence"]:
            marker = match["marker"]
            closing = re.compile(r"^[ ]{0,3}" + re.escape(marker[0]) +
                                 "{" + str(len(marker)) + r",}[ \t]*(?:\n|\Z)", re.MULTILINE)
            close = closing.search(content, end)
            if close is None:
                errors.append(f"line {line}: unclosed code fence")
                break
            if match["info"].strip() == "math":
                found.append(Expression(textwrap.dedent(content[end:close.start()]).strip(),
                                        True, start, close.end(), line, "fence"))
            position = close.end()
            continue
        if match["code"]:
            closing = re.compile(r"(?<!`)" + re.escape(match["code"]) + r"(?!`)")
            close = closing.search(content, end)
            position = close.end() if close else end
            continue
        if match["dollar"]:
            delimiter = match["dollar"]
            display = delimiter == "$$"
            syntax = "dollars"
            if not display and content[end:end + 1] == "`":
                end += 1
                closing = re.compile(r"`\$")
                syntax = "inline-code"
            else:
                closing = re.compile(r"(?<!\\)" + re.escape(delimiter))
        else:
            display = match["legacy"] == r"\["
            closing = re.compile(r"(?<!\\)" + re.escape(r"\]" if display else r"\)"))
            syntax = "legacy"
        close = closing.search(content, end)
        if close is None:
            errors.append(f"line {line}: unclosed math delimiter")
            break
        found.append(Expression(content[end:close.start()], display, start,
                                close.end(), line, syntax))
        position = close.end()
    return found, errors


def validate_math(content):
    found, errors = expressions(content)
    for expression in found:
        if expression.syntax not in ("fence", "inline-code"):
            errors.append(f"line {expression.line}: protect math with a math code fence "
                          "or dollar-backtick inline delimiters")
        if re.search(r"(?<!\\)\\operatorname\b", expression.tex):
            errors.append(f"line {expression.line}: unsupported operator-name macro")
    return errors
