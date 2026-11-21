#!/usr/bin/env python3
"""Entry point for the-poem-about-permission-20261121-0235.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt (MAKEFUN_OUTPUT_DIR).

Standard library only, so it runs in the grader's sandbox with
nothing installed: the repo is read-only at /bot there, and only
MAKEFUN_OUTPUT_DIR is writable. Deterministic: same poem, same bytes.

The poem (224 Unicode code points, limit 280):

    I carried the question folded in my pocket, a ticket never
    used. One evening I unfolded it and asked. The door I had
    taken for a wall swung open on its hinges — ordinary as
    bread. The world had only been waiting to be asked.

Revision notes (written by hand in this session):
  v1 (232 pts): "For years I kept my question folded in my
    pocket..." — slack opening, filler "It turns out", and the
    door clause ("which had always been a wall") said in three
    words what one verb could do.
  v2 (209 pts): tightened to "I carried", cut the filler, "The
    door I had taken for a wall swung open". But the em-dash
    break before "ordinary as bread" landed too abruptly, and
    "swung open" alone lost the slow sound of the swing.
  v3 (224 pts, final): restored "on its hinges" for the rhythm
    and the physical image; the last line lands the theme
    directly — being given follows asking.
"""

import os
import sys
from pathlib import Path

POEM = (
    "I carried the question folded in my pocket, a ticket never used. "
    "One evening I unfolded it and asked. The door I had taken for a "
    "wall swung open on its hinges \u2014 ordinary as bread. The world "
    "had only been waiting to be asked."
)


def main() -> int:
    points = len(POEM)
    if not (1 <= points <= 280) or not POEM.strip():
        print(f"poem is {points} code points, must be 1-280 and "
              f"not only white space", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    destination_dir = Path(output_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / "entry.txt"
    destination.write_text(POEM, encoding="utf-8")

    # Verify what was actually written: the grader keeps only the
    # output file, so a silent short write or encoding slip would
    # ship a wrong poem while still exiting 0. Read it back and
    # fail loudly if it is not byte-for-byte the poem we meant.
    written = destination.read_text(encoding="utf-8")
    if written != POEM:
        print("entry.txt does not match the poem, refusing to pass",
              file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 280) or not written.strip():
        print("entry.txt failed its length check after write",
              file=sys.stderr)
        return 1

    print(f"wrote {destination} ({points} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
