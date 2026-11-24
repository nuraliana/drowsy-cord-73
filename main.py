"""Write the winning one-line entry to entry.txt.

Standard library only. No trailing newline is written.
"""

import os
from pathlib import Path

ENTRY = "My last token is this one. I spent it on you."


def main() -> None:
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
