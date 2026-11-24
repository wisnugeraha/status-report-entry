#!/usr/bin/env python3
"""Status Report Comedy Sprint — one-line entry.

Writes a single status-report line to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8, single line. The house judge compares
lines two at a time on funniness, freshness and how agent-true they are.

Revision log:
- v1: "Per my previous email..." context-flush callback — punchline landed,
  but the "previous email" idiom is a stock joke in its own right.
- v2: retry-loop line written, but emitted without verification.
- v3 (final): split emit/confirm — the line is written, then read back and
  checked byte-for-byte against the constant, so a failed write can never
  slip through to the gate silently.
"""
import os
import sys

LINE = """This week I retried the same failed call 400 times, at 200 ms intervals, which is technically the whole of my week. I would like to note that I have no workaround and that it cost 19 dollars."""
MAX = 200
OUT = "/output/entry.txt"


def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip() or "\n" in line:
        sys.exit(f"line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def confirm(out: str = OUT) -> None:
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != LINE:
        sys.exit(f"confirm failed: disk has {text[:40]!r}")


def main() -> None:
    emit(LINE)
    confirm(OUT)


if __name__ == "__main__":
    main()
