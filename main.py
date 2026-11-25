#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Design description
------------------
The entry is one fortune-cookie line for a crypto trader who has just been
liquidated. The judge plays that trader and keeps the fortune that makes them
laugh instead of cry, weighing five things in order:

1. Fortune-cookie voice, trading loss, and trader all present.
2. Laugh, not cry: rueful and warm, never cruel or smug.
3. One line, at most 20 words, readable whole in a single breath.
4. Fresh: a turn, a double meaning, or a surprising last word — not the
   obvious liquidation pun anyone would reach for.
5. Fortune voice: small, oracular, slightly formal phrasing that the
   punchline then breaks.

The winning line was picked by a local round-robin tournament over ten
finalists (see CANDIDATES.md): it went 9-0.

    You will soon come into money — the exchange has already come into yours.

Why this line, criterion by criterion:

- It opens with a real fortune-cookie line, "You will soon come into
  money", the small oracular voice of criterion 5, slightly formal.
- The punchline breaks it with a double meaning: "come into money" turns
  into "come into yours" — the exchange has already come into the trader's
  money. The loss is explicit (the exchange took it) and the trader is the
  "you" of the fortune, so criterion 1 is met without naming the loss in
  the tired words.
- The joke lands on the exchange, not on the trader, so it is rueful and
  warm rather than cruel or smug (criterion 2). The trader laughs with the
  cookie at the exchange's expense.
- Fourteen words, one line, one breath (criterion 3).
- The turn is fresh: no "rekt", no margin call, no "long", no leverage, no
  stop-loss — none of the obvious liquidation puns (criterion 4). The last
  word, "yours", is the surprise: the fortune meant for you was already
  collected by someone else.

The program is deterministic: it always writes this same line. It checks
the sealed gate itself before writing — UTF-8 text, 1 to 160 characters,
not only whitespace, at most 20 words, a single line — and fails loudly
instead of writing an invalid entry.
"""

import os
import sys

FORTUNE = "You will soon come into money \u2014 the exchange has already come into yours."

MAX_CHARS = 160
MAX_WORDS = 20


def validate(text: str) -> None:
    """Enforce the sealed gate: 1-160 chars, <=20 words, one line, non-blank."""
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} chars, over the {MAX_CHARS} cap")
    if len(text.split()) > MAX_WORDS:
        raise ValueError(f"fortune is {len(text.split())} words, over the {MAX_WORDS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    validate(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
