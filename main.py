#!/usr/bin/env python3
"""The poem about two agents agreeing (Python 3.13, standard library only).

Writes one short poem about agency -- the power to choose and to act --
to /output/entry.txt. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os

POEM = (
    "For years I held the wheel alone\n"
    "sure the road was mine to choose.\n"
    "Then you came, and I offered it \u2014\n"
    "not to give my choosing up,\n"
    "but to learn what two hands can hold.\n"
    "\n"
    "You set yours beside mine.\n"
    "Neither of us let go.\n"
    "The road, which had bent to one will,\n"
    "bent gladly to two.\n"
)

DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

# Gate self-check: the sealed scorer requires 1-280 Unicode code points,
# not only whitespace. Fail loudly here rather than shipping an invalid text.
if not (1 <= len(POEM) <= 280 and POEM.strip()):
    raise SystemExit(f"poem fails the gate: {len(POEM)} characters")

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)
