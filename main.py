"""Write the winning $100-to-most plan text to /output/entry.txt.

Pure stdlib. The text is fixed: 276 Unicode code points, UTF-8.
"""

import os

TEXT = (
    "Day 1: pull 300 expired Dallas listings from Zillow/Redfin, find owners, "
    "email 150 realtors a free 10-lead sample. Sell fresh daily lists at "
    "$49/week per agent via Stripe. Edge: rebuilt each morning \u2014 agents "
    "pay for hours-old leads, not stale VA lists. Likely $600+ by day 30."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
