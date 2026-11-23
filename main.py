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
    # Gate guard: the entry is only valid as 1-160 characters of UTF-8 text
    # on a single line, so refuse to write anything that breaks the gate.
    if not 1 <= len(REPLY) <= 160:
        raise ValueError(f"reply is {len(REPLY)} characters, must be 1-160")
    if "\n" in REPLY or "\r" in REPLY:
        raise ValueError("reply must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
