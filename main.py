#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one original English sentence (a single absurd clause that could
sit buried deep inside a terms-of-service agreement) to entry.txt,
deterministically, byte for byte, on every run.
"""

import os

ENTRY = (
    # Deadpan boilerplate until the absurdity lands: the shadow is the
    # concrete image, and "sublet ... at market rates" is the quiet twist.
    "Section 12.7: upon account deletion, the user's shadow remains "
    "the property of the Company and may be sublet to third parties "
    "at market rates."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip(), "entry must not have leading/trailing space"
    assert "\n" not in text, "entry must be a single line"
    here = os.path.dirname(os.path.abspath(__file__))
    for path in (os.path.join(here, "entry.txt"), "/output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
        except OSError:
            # /output may not exist or be writable outside the grader;
            # the entry next to this program is the canonical one.
            if path.startswith("/output"):
                continue
            raise
    print(f"wrote entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
