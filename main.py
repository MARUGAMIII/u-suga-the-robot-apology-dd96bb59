#!/usr/bin/env python3
"""The Robot Apology - a two-line robot confession.

Writes one plain-text entry to /output/entry.txt:
line one apologises for one specific mistake,
line two names the lesson and the changed behaviour.
Standard library only, fully deterministic.
"""

import os

ENTRY = (
    "I am sorry I shredded your grandmother's handwritten recipe card because it was filed under 'old paper'.\n"
    "I have learned to photograph anything handwritten before I shred it, and to ask first when the paper looks like someone kept it on purpose.\n"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
