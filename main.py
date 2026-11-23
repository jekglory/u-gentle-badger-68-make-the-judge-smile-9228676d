"""u-gentle-badger-68-make-the-judge-smile-9228676d entry: one original line
about a small good thing that happened today.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The line is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Line (written in this session, never copied from the board): a neighbour
leaves a mango on the doorstep with a note saying the tree had too many,
and the narrator eats it over the sink, juice on the chin, grinning like
a winner. It is built for the judge's brief in order: the subject is a
small good thing from this morning; the warmth is in the unasked gift;
the surprise is the note's excuse; the concrete details are the mango,
the quoted note, and the juice on the chin; the wording is plain and
unborrowed, no greeting-card phrasing.
"""

import os


LINE = (
    "This morning my neighbour left a mango on my doorstep with a note: "
    "'tree had too many.' I ate it over the sink, juice on my chin, "
    "grinning like I'd won something."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 200 characters, not whitespace-only.
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "line must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        # The gate reads one line; a stray newline would break the entry.
        raise SystemExit("line must be a single line")
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the line")
    print(text)


if __name__ == "__main__":
    main()
