#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint - make.fun bounty entry.

Writes one micro-confession in exactly two parts - a "To:" line naming
who it was meant for and the unsent message itself, one line exactly as
typed, with no explanation after it - to entry.txt in the output
directory (the file the make.fun harness grades).

The confession text lives in ENTRY below and is returned unchanged by
get_entry(). main() only resolves the output directory (from
MAKEFUN_OUTPUT_DIR, defaulting to /output) and hands it to
write_entry(), so the text itself is never transformed on the way out.
"""

import os

ENTRY = "To: my first boss\nI still type the thank-you I never sent you \u2014 you saw the kid in me before I believed in him, and pride kept my thumb off send while you were still there to hear it."

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
