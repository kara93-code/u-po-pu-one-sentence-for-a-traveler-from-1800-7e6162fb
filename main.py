"""One sentence for a traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to someone who has just stepped out of the year 1800, using only
words and pictures that person could already know: a post office, a
library, a letter, a book, the sea. No word coined after their time.
"""

import os
import stat

SENTENCE = (
    "Picture a post office and library as wide as the world, where a letter "
    "you send reaches a friend across the sea in a blink, and a thousand "
    "books lie open on your desk."
)

# Words coined after 1800 that must never appear in the sentence.
BANNED_WORDS = (
    "internet",
    "computer",
    "website",
    "email",
    "online",
    "digital",
    "screen",
    "wireless",
    "server",
    "data",
    "telegraph",
    "telephone",
)


def check_sentence(text):
    """Check the sentence against the contest gate and the judge brief."""
    if not text or not text.strip():
        raise ValueError("sentence is empty")
    if len(text) > 200:
        raise ValueError("sentence is %d characters, over the 200 limit" % len(text))
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError("sentence uses a word coined after 1800: %s" % word)
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "  " in text or text != text.strip():
        raise ValueError("sentence has stray spacing")
    # The picture must carry both halves of the internet: sending word
    # to people far away, and reading what others have written.
    if "letter" not in lowered or "book" not in lowered:
        raise ValueError("sentence must show both sending and reading")
    return True


def output_path():
    """Resolve where entry.txt goes: the harness dir, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the sentence with a plain open() and mode 0644."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return path


def main():
    check_sentence(SENTENCE)
    path = write_entry(SENTENCE, output_path())
    print("wrote %s (%d characters)" % (path, len(SENTENCE)))


if __name__ == "__main__":
    main()
