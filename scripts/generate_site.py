"""Regenerate the public publication site from the checklist."""

from pathlib import Path


def main() -> None:
    checklist = Path("docs/publication_checklist.md").read_text(encoding="utf-8")
    print("parsed", len(checklist.splitlines()), "lines")


if __name__ == "__main__":
    main()
