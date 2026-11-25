"""One Line of Earned Pride — sukamtiindrawati-dot.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene. The line is chosen by scoring a
shortlist of fresh, concrete candidates against the judge's own criteria:

  1. genuine earned pride — a small person doing something hard, or a long
     effort finally landing (never asserted, congratulated or explained)
  2. a concrete scene with a real person, seen happening, not summarised
  3. the pride is earned inside the line, by effort the reader can feel
  4. it lands in one read — the pride arrives by the last word
  5. freshness — no stock trophy, podium or graduation image

The winner: a woman who failed her driving test four times finally parks
her mother's old car perfectly, first try — and sits there a minute with
both hands still on the wheel. The long effort, the concrete scene and the
quiet last image are all inside the line, and nothing in it says "proud".
"""

import os

# Candidates, each scored 0-2 on the judge's five criteria:
# (pride, scene, earned, one_read, freshness)
CANDIDATES = [
    (
        "She'd failed the driving test four times; this morning she parked "
        "her mother's old car perfectly, first try, and sat there a minute "
        "with both hands still on the wheel.",
        (2, 2, 2, 2, 2),
    ),
    (
        "For three winters he mended the same fence in the rain; this spring "
        "the lambs stayed in, and he stood at the gate a long while, saying "
        "nothing.",
        (2, 2, 2, 2, 1),
    ),
    (
        "After a year of evening classes, the night-shift cleaner read the "
        "safety notice aloud to her son — slowly, correctly, without asking "
        "for help.",
        (2, 2, 2, 1, 2),
    ),
    (
        "He'd carried the piano up three flights alone when he was twenty; "
        "at seventy he watched his granddaughter play it, and kept his hands "
        "in his pockets.",
        (2, 1, 2, 2, 2),
    ),
    (
        "The boy who couldn't tie his shoes tied them himself this morning, "
        "double-knotted, then ran to show his grandfather before the bus "
        "came.",
        (1, 2, 1, 2, 2),
    ),
]


def validate(text):
    """Gate: UTF-8 text of 1 to 240 characters, one line, not only whitespace."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 240, f"length {len(text)} outside 1-240"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text.strip(), "line must be a single line"
    text.encode("utf-8")
    return text


def pick():
    """Highest total score wins; ties break toward the earlier candidate."""
    best_line, best_score = None, -1
    for line, scores in CANDIDATES:
        total = sum(scores)
        if total > best_score:
            best_line, best_score = line, total
    return validate(best_line)


def main():
    line = pick()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back check: what landed on disk must be exactly the picked line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch"
    validate(written)
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
