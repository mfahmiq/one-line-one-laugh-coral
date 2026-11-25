"""One Line, One Laugh — make.fun entry.

Writes the single entry line byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line (chosen after brainstorming several candidates against the
judge brief — surprise turn, economy, freshness, clean rhythm):
a sweet setup (telling a houseplant you love it), the plant dying
anyway, and the punchline reframing the death as a deadpan corporate
"performance review". No stock joke, no setup longer than the
punchline needs.
"""

import os

ENTRY = (
    "I told my houseplant I loved it and it died anyway \u2014 "
    "the most honest performance review I've ever received."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write byte-for-byte, UTF-8, no trailing newline: the line is
    # the whole entry, exactly as in entry.txt.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
