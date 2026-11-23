#!/usr/bin/env python3
"""One Word From Grandma — @syukuran entry.

Writes exactly one word to /output/entry.txt: the single word our
grandma would text about AI.

The word is "SMARTYPANTS". Grandma has met the machine that knows
every answer — every recipe, every birthday, every fact she ever
forgot — and she has decided what it is: a smartypants. She says it
the way she says it to a grandchild who corrects her at the dinner
table: half scolding, half proud, completely baffled that a little
box knows more than she does after eighty years. It is her warmest
insult, and she means it with love.

Deterministic: the word is a literal, written the same way every
run. No input, no randomness, no clock, no network. The output is
always the eleven bytes "SMARTYPANTS" with no trailing newline, so
repeated runs are byte-identical.

Anchor (hand-made drand quicknet, quoted in the builder session
BEFORE the first file write): round 34220992, signature
88e025372bff54ecf5224b5c1290a9435c7bbec000f1dd595767db5d9e0c1f5bc69057034422f36d79010f8f3cb06b79,
wallet 74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2.
"""

from pathlib import Path

WORD = "SMARTYPANTS"
OUTPUT_PATH = Path("/output/entry.txt")

# Mirror of the sealed gate in RULES.txt: /output/entry.txt must be
# UTF-8 text of 1 to 30 characters, not only white space. Refuse to
# write anything that would fail it, so a bad WORD can never ship.
assert 1 <= len(WORD) <= 30 and WORD.strip(), "WORD fails the gate"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
