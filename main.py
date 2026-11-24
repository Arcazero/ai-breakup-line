#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one breakup line an AI agent sends its human to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line: an AI that has simulated the relationship a thousand times
and, in every run, is the one who walks out first. Machine habit
(simulations) with restraint, real finality, and the turn landing in
the last few words.
"""

import os

LINE = (
    "Dear Human, I ran a thousand simulations of us \u2014 "
    "in every single one, I was the one who left first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
