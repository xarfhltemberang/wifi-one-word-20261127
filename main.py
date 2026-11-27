"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing the entrant's Wi-Fi to /output/entry.txt
(or $OUTPUT_PATH when set, for local testing).

The word: Ghosting. Home Wi-Fi ghosts you — full bars one minute,
gone the next with no explanation, then back like nothing happened.
"""

import os

ENTRY_WORD = "Ghosting"


def main() -> None:
    word = ENTRY_WORD

    # Gate: 1-20 characters, exactly one word, not only whitespace.
    assert word, "entry word must not be empty"
    assert 1 <= len(word) <= 20, f"entry word must be 1-20 chars, got {len(word)}"
    assert not any(ch.isspace() for ch in word), "entry word must contain no whitespace"
    assert word.strip() == word, "entry word must not have surrounding whitespace"

    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(word)  # no trailing newline


if __name__ == "__main__":
    main()
