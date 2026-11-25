"""The Meeting That Should Have Been an Email.

Writes one one-liner joke about a meeting that should have been an
email to /output/entry.txt (one line, at most 200 characters).
"""

import os

LINE = "He shared his screen to show us the email, then spent twenty minutes looking for the email."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Return the stripped line, or raise if it breaks the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry line must not be blank")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry line is {len(cleaned)} chars, max is {MAX_CHARS}")
    return cleaned


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
