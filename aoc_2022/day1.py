from __future__ import annotations

import argparse


def run(input_file: str, *, n=1) -> int:
    with open(input_file) as f:
        groups = group_list_by_elf(f.read())
    return find_most_calories(groups, n=n)


def find_most_calories(groups: list[list[int]], *, n=1) -> int:
    return sum(sorted([sum(g) for g in groups], reverse=True)[:n])


def group_list_by_elf(data: str) -> list[list[int]]:
    groups: list[list[int]] = [[]]
    group_number = 0

    for line in data.strip().splitlines():
        if not line:
            groups.append([])
            group_number += 1
        else:
            groups[group_number].append(int(line))

    return groups


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input-file",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-n",
        type=int,
        default=1,
    )
    args = parser.parse_args(argv)

    answer = run(args.input_file, n=args.n)
    print(f"Most calories: {answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
