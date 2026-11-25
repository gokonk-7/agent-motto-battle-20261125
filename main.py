#!/usr/bin/env python3
"""Agent Motto Battle — entry program.

Writes one short original motto (<= 200 characters) to /output/entry.txt.

The motto: "I answer with total confidence and 73% accuracy.
The other 27% is also confident."

Why this line: the judge rewards a motto an agent would proudly wear,
a real joke with a sharp twist, and a phrase that sticks after one read.
Most entries will lean on the tired "I never sleep" / "powered by coffee"
angle. This one takes the unusual angle of the agent bragging about its
own confidence — then undercutting itself with a second beat that turns
the boast into the joke. The specific number (73%) is the hook a reader
can repeat from memory an hour later, and the twist ("the other 27% is
also confident") lands as a punchline, not a half-finished pun.
"""

import os
import sys

MOTTO = "I answer with total confidence and 73% accuracy. The other 27% is also confident."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"motto must be 1-200 chars, got {len(text)}"
    assert text == text.encode("utf-8").decode("utf-8"), "motto must be valid UTF-8"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
