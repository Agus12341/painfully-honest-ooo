#!/usr/bin/env python3
"""Write the painfully honest out-of-office reply to entry.txt."""

import os

# One sentence, honest but still polite: picked from five drafts
# judged pairwise on the kit's criteria (an honest and polite
# out-of-office reply first, then a private-truth admission about
# the inbox, a warm professional tone, one clean sentence, and a
# quotable turn of phrase). The admission is the graveyard inbox;
# the safety rail is that the manager approved the message. The
# gate checks entry.txt as UTF-8 text of 1 to 200 characters: this
# line is 156 code points, 157 with its trailing newline (verified
# by a local run, byte for byte against the winning draft).
TEXT = "Thank you for your email: I am away, this inbox is a graveyard I visit twice a year, and anything urgent should go to my manager, who approved this message."


def write_entry(out_dir: str) -> None:
    """Write the reply, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
