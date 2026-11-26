#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song,
a single line under 200 characters, to entry.txt in the output dir.
Deterministic, no network, no dependencies.
"""

import os

BAND_LINE = (
    "The Smoke Detectors — hit single 'Low Battery Chirp (3AM Remix)' "
    "is one beep every sixty seconds, all night, forever."
)


def main() -> None:
    line = BAND_LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) < 200, f"entry must be 1-199 chars, got {len(line)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read it back: the grader counts exactly what is on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "round-trip mismatch"
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
