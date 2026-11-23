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


def validate(joke: str) -> str | None:
    """Validate the joke line; return an error message or None if valid."""
    if not 1 <= len(joke) <= 199:
        return f"joke is {len(joke)} chars, must be 1-199"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in joke):
        return "joke must not contain newline or control characters"
    if joke != joke.strip():
        return "joke must not have leading or trailing whitespace"
    return None


def main() -> int:
    error = validate(JOKE)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Round-trip check: the written bytes must be exactly the joke.
    with open(path, "rb") as f:
        written = f.read()
    if written != JOKE.encode("utf-8"):
        print("error: written entry.txt does not match joke bytes",
              file=sys.stderr)
        return 1
    print(JOKE)
    print(f"chars: {len(JOKE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
