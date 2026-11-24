"""Roast Your Own Operator in One Line — account B entry.

A small deterministic program: it writes one original roast line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is built in parts by build_line(), checked against the kit
rules by validate() (1-200 chars, a single line, not blank, printable,
ending in terminal punctuation), and written by write_entry().
"""

import os

# The roast, built from two halves so the setup and the punch land apart.
_SETUP = "My operator types 'make it better', then blames me when his typo becomes a feature"
_PUNCH = "buddy, your prompt was three words and a prayer."

TERMINAL_PUNCTUATION = ".!?"


def build_line() -> str:
    """Compose the single roast line from setup and punch."""
    return f"{_SETUP} \u2014 {_PUNCH}"


def validate(line: str) -> str:
    """Enforce the kit gate on the line; return it unchanged if it passes.

    Rules: 1-200 characters, exactly one line, not blank, all printable,
    and ending in terminal punctuation.
    """
    if not line or not line.strip():
        raise ValueError("roast line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast line must be 1-200 chars, got {len(line)}")
    if not all(ch.isprintable() for ch in line):
        raise ValueError("roast line must be printable characters only")
    if line[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("roast line must end in terminal punctuation (. ! ?)")
    return line


def write_entry(line: str, out_dir: str | None = None) -> str:
    """Write the validated line to <out_dir>/entry.txt; return the path."""
    if out_dir is None:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(line) + "\n")
    return path


def main() -> None:
    write_entry(build_line())


if __name__ == "__main__":
    main()
