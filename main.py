#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt.

The joke is fixed text -- deterministic, no randomness, no clock, no I/O
beyond the single output file. It runs in well under 60 seconds.
"""

import os

# The joke text is fixed on purpose: the entry must be byte-identical on every run.
JOKE = (
    "I typed 'meeting at 3' and autocorrect sent 'meatloaf at sea' "
    "to my whole team, who now think I run a catering boat."
)


# Entry point: resolve the output dir, then write the joke plus a newline.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
