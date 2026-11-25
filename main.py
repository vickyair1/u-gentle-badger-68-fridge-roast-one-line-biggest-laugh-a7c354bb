#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes one single-line smart-fridge roast (130 characters, under the
200-character cap) to /output/entry.txt and prints it to stdout.
Deterministic: no randomness, no network, no input, stdlib only.

Revisions tried (best kept):
  V1 (135 chars): "My smart fridge pushed a firmware update at 3 a.m. and
    forgot how to make ice — three grand for a box that needs a reboot
    to stay cold."
    Solid firmware angle, but the punch ("needs a reboot to stay cold")
    is a touch predictable.
  V2 (130 chars, KEPT): "My smart fridge wants a monthly subscription
    for crushed ice — I bought a freezer, not a landlord with a
    touchscreen and opinions."
    Freshest angle: a subscription for ice, and the turn at the end
    (freezer -> landlord with a touchscreen) lands hardest on first
    read. Specific to smart fridges, tight, and dodges the obvious
    cracks (ordering groceries, watching you).
  V3 (142 chars): "My smart fridge's app called my milk 'past its
    prime' and suggested oat milk — bold talk from a box whose ice
    cubes fuse into one sad glacier."
    Vivid glacier image, but two jokes dilute each other and the
    setup runs longer than the punch earns.
"""

import os

def build_line() -> str:
    """Return the one-line smart-fridge roast."""
    return (
        "My smart fridge wants a monthly subscription for crushed ice \u2014 "
        "I bought a freezer, not a landlord with a touchscreen and opinions."
    )


def output_dir() -> str:
    """Return the directory entry.txt is written to.

    Honours MAKEFUN_OUTPUT_DIR when set (the kit harness may point
    output elsewhere); defaults to /output.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def validate_line(line: str) -> None:
    """Check the roast is a single line within the 200-char cap."""
    assert isinstance(line, str) and line, "line must be a non-empty string"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert len(line) <= 200, f"line is {len(line)} chars, over the 200-char cap"


def main() -> None:
    line = build_line()
    validate_line(line)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
