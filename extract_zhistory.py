#!/usr/bin/env python3
"""
Extract commands from an extended zsh history file and sort them.
 
Extended zsh history format: ": <timestamp>:<duration>;<command>"
Multi-line commands (continued with backslash) are kept as single entries.
 
Usage:
    ./extract_zhistory.py <input_file> [-u|--unique] [-o OUTPUT]
 
Examples:
    ./extract_zhistory.py ~/.zsh_history -o sorted.txt
    ./extract_zhistory.py ~/.zsh_history -u -o unique_sorted.txt
 
Compare two processed files:
    comm -23 a.txt b.txt   # only in A
    comm -13 a.txt b.txt   # only in B
    comm -12 a.txt b.txt   # in both
"""
import argparse
import re
import sys
 
 
def extract_commands(content: str) -> list[str]:
    """Split on the ': <digits>:<digits>;' marker, keeping multi-line commands intact."""
    pattern = re.compile(r'^: \d+:\d+;', re.MULTILINE)
    parts = pattern.split(content)
    # parts[0] is whatever preceded the first marker (usually empty)
    return [p.strip() for p in parts[1:] if p.strip()]
 
 
def main() -> int:
    parser = argparse.ArgumentParser(description="Extract and sort zsh history commands.")
    parser.add_argument("input", help="Path to zsh history file")
    parser.add_argument("-u", "--unique", action="store_true", help="Deduplicate commands")
    parser.add_argument("-o", "--output", help="Output path (defaults to stdout)")
    args = parser.parse_args()
 
    with open(args.input, "r", errors="replace") as f:
        content = f.read()
 
    commands = extract_commands(content)
    if args.unique:
        commands = sorted(set(commands))
    else:
        commands = sorted(commands)
 
    output = "\n".join(commands) + "\n"
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Wrote {len(commands)} commands to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(output)
 
    return 0
 
 
if __name__ == "__main__":
    sys.exit(main())
 
