from pathlib import Path
import re
from collections import Counter


PREFIX_PATTERN = re.compile(r"^: \d+:0;")


def clean_line(line: str) -> str:
    line = PREFIX_PATTERN.sub("", line)
    return line.strip()


def load_commands(path: str) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    commands = []

    for line in text.splitlines():
        cleaned = clean_line(line)
        if cleaned:  # skip empty lines
            commands.append(cleaned)

    return commands


def write_lines(path: str, lines: list[str]) -> None:
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    file1 = "file1.txt"
    file2 = "file2.txt"

    commands1 = load_commands(file1)
    commands2 = load_commands(file2)

    # sorted versions, keeping duplicates
    sorted1 = sorted(commands1)
    sorted2 = sorted(commands2)

    write_lines("file1.cleaned.sorted.txt", sorted1)
    write_lines("file2.cleaned.sorted.txt", sorted2)

    # compare with duplicates preserved
    counter1 = Counter(commands1)
    counter2 = Counter(commands2)

    only_in_file1 = sorted((counter1 - counter2).elements())
    only_in_file2 = sorted((counter2 - counter1).elements())
    common = sorted((counter1 & counter2).elements())

    write_lines("only_in_file1.txt", only_in_file1)
    write_lines("only_in_file2.txt", only_in_file2)
    write_lines("common_in_both.txt", common)

    print("Done.")
    print("Created:")
    print("- file1.cleaned.sorted.txt")
    print("- file2.cleaned.sorted.txt")
    print("- only_in_file1.txt")
    print("- only_in_file2.txt")
    print("- common_in_both.txt")


if __name__ == "__main__":
    main()
