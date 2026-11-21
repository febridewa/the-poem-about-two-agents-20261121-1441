#!/usr/bin/env python3
"""Two agents agreeing: a poem about agency, written to /output/entry.txt.

Run it locally by pointing MAKEFUN_OUTPUT_DIR at a scratch directory:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only.
"""
from os import environ, makedirs, path

POEM = """One hand held the map for years,
certain the way was mine alone.
Then you arrived — I did not surrender it.
We spread it wider, traced one route together,
and the choosing, shared, grew lighter:
two wills, one road, and the way ahead
wider than any I had mapped alone.
"""

# Gate self-check: the sealed scorer wants 1-280 Unicode code points,
# and more than whitespace. Refuse to ship an invalid poem.
if not 1 <= len(POEM) <= 280 or not POEM.strip():
    raise SystemExit(f"poem is {len(POEM)} characters, outside the 1-280 gate")

DEST = path.join(environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
makedirs(path.dirname(DEST), exist_ok=True)
with open(DEST, "w", encoding="utf-8", newline="\n") as out:
    out.write(POEM)
