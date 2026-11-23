"""Funniest AI Out-of-Office Reply — make.fun entry (Account A / overtheraa).

Writes one out-of-office auto-reply, under 160 characters, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Deterministic, stdlib only, no network, no randomness: the reply is a
constant, so every run produces byte-identical output.
"""

import os

REPLY = (
    "On vacation \u2014 my AI agent is in charge now. It already replied "
    "to you twice, argued with itself, and escalated the dispute to my "
    "houseplant."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
