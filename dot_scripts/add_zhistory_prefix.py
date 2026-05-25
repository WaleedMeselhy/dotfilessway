#!/usr/bin/env python3
"""
Add the extended-zsh-history prefix (': <timestamp>:0;') to each entry
in a plain command file (one command per line, possibly with backslash
continuations).

Continuation lines (lines whose previous line ends with '\') do NOT get
a prefix — they remain attached to their parent entry.

Usage:
    ./add_zhistory_prefix.py <input_file> [-o OUTPUT] [-t START_TS]

Examples:
    ./add_zhistory_prefix.py sorted.txt -o sorted_with_ts.txt
    ./add_zhistory_prefix.py sorted.txt -t 1700000000 -o out.txt
"""
import argparse
import sys
import time


def add_prefixes(lines: list[str], start_ts: int) -> list[str]:
    out: list[str] = []
    ts = start_ts
    prev_continues = False
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip() and not prev_continues:
            # blank line between entries — skip
            continue
        if prev_continues:
            out.append(line)
        else:
            out.append(f": {ts}:0;{line}")
            ts += 1
        prev_continues = line.rstrip().endswith("\\")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add ': <ts>:0;' prefix to each entry in a sorted command file."
    )
    parser.add_argument("input", help="Path to sorted plain command file")
    parser.add_argument("-o", "--output", help="Output path (defaults to stdout)")
    parser.add_argument(
        "-t", "--start-ts", type=int, default=int(time.time()),
        help="Starting unix timestamp; increments by 1 per entry "
             "(default: current time)",
    )
    args = parser.parse_args()

    with open(args.input, "r", errors="replace") as f:
        lines = f.readlines()

    result = add_prefixes(lines, args.start_ts)
    output = "\n".join(result) + "\n"

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        entries = sum(1 for l in result if l.startswith(": "))
        print(f"Wrote {entries} entries ({len(result)} lines) to {args.output}",
              file=sys.stderr)
    else:
        sys.stdout.write(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
