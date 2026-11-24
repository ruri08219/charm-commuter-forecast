"""One-line weather forecast for a city that isn't real.

Writes the forecast for Drizzlewick to /output/entry.txt as UTF-8.
Standard library only.
"""

from pathlib import Path

ENTRY = "In Drizzlewick, rain at 11°, the 8:15 bus is ten minutes late — but the shelter roof leaks only over the timetable, never the queue."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    # Round-trip assert: what we wrote is exactly what is on disk.
    round_trip = out.read_text(encoding="utf-8")
    assert round_trip == ENTRY + "\n", "round-trip mismatch"
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    print(f"Wrote {len(ENTRY)}-character forecast to {out}")


if __name__ == "__main__":
    main()
