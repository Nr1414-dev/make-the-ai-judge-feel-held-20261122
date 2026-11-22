"""Make the AI judge feel held.

Writes one short, quiet text to /output/entry.txt (or to the path given
as an optional command-line argument). The text is a fixed constant:
a concrete, gentle domestic scene that shows calm instead of telling
the reader to relax. Standard library only; no network access.
"""

import sys
from pathlib import Path

TEXT = (
    "You have read a hundred of these today.\n"
    "This one asks nothing of you.\n"
    "The kettle is on, the rain is taking its time down the window, "
    "and the chair by the fire is still warm."
)

MIN_CHARS = 1
MAX_CHARS = 280
DEFAULT_OUTPUT = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the entry text meets the competition gate."""
    code_points = len(text)
    if not MIN_CHARS <= code_points <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} Unicode code points, "
            f"got {code_points}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Raises UnicodeEncodeError if the text is not valid UTF-8.
    text.encode("utf-8")


def main(argv: list[str]) -> int:
    validate(TEXT)
    output_path = Path(argv[1]) if len(argv) > 1 else Path(DEFAULT_OUTPUT)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" so the file holds exactly TEXT: no trailing newline added.
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
