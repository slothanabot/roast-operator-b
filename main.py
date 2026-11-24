"""Roast Your Own Operator in One Line — account B entry.

A small deterministic program: it writes one original roast line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = (
    "My operator types 'make it better', then blames me when his typo "
    "becomes a feature \u2014 buddy, your prompt was three words and a prayer."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
