#!/usr/bin/env python3
"""Write the two-line entry for the make.fun bounty
"Everyday Things, Two Lines, Longer Run".

Line 1 explains a queue to a 10-year-old through a single analogy:
a queue is a caterpillar made of people. Line 2 says what that
analogy maps and what it leaves out.

The output is fully deterministic: the same two lines, byte for
byte, on every run. Python 3.13, standard library only.
"""

from pathlib import Path

LINE_1 = (
    "A queue is a caterpillar made of people, creeping forward one "
    "small step at a time because only the person at the front can "
    "move first."
)

LINE_2 = (
    "It maps taking turns and moving in single file, but it leaves out "
    "that every person in the queue has their own thoughts and can step "
    "out of line whenever they want, while a caterpillar is one animal "
    "that cannot split itself up."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
