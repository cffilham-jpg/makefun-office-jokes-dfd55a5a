#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes a single one-line office joke (1-199 characters) to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default: output/entry.txt).
Standard library only. Deterministic: the same joke every run.
"""

import os
import sys

JOKE = (
    "We hired a consultant to tell us our meetings are too long; "
    "he presented his findings in a three-hour meeting."
)


def main() -> int:
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(JOKE) <= 199:
        print(f"error: joke is {len(JOKE)} chars, must be 1-199",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)
    print(f"chars: {len(JOKE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
