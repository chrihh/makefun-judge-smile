"""Write one line about a small good thing that happened today.

The bounty is "Make the Judge Smile": a single line, at most 200
characters, about a small good thing that happened today. The line
here is built from its two halves so the telling keeps its shape:

1. a small failure to start the day -- the generator coughing twice
   and giving up -- answered by a quiet, unasked-for kindness: the
   neighbour running an extension cord over the fence; and
2. the turn after the em dash -- the tea stays hot, and so does a
   truce about his mango tree that the cord quietly renews.

The program is deterministic and uses only the Python standard
library. It writes the assembled line to /output/entry.txt as
UTF-8, with no trailing newline, so the file is exactly the line
itself: 165 characters, inside the 1-200 gate, and one line only.
"""

import os

# The two halves of the line, in the order they are told. Joined
# with a single space they form the entry exactly; the em dash at
# the start of the second half carries the pause before the turn.
HALVES = (
    "The generator coughed twice, gave up, and the neighbour "
    "silently ran an extension cord over the fence",
    "— my tea stayed hot, and so did our truce about his mango tree.",
)

MAX_CHARACTERS = 200


def build_line() -> str:
    """Assemble the entry line and check it against the gate."""
    line = " ".join(HALVES)
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARACTERS:
        raise ValueError("entry line is over 200 characters")
    return line


def main() -> None:
    line = build_line()
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
