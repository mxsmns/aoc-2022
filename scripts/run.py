#!/usr/bin/env bash
from aoc_2022 import day1
import os


def main() -> int:
    print(day1.run(os.path.join(_input_folder(), "1a.txt")))
    return 0


def _input_folder() -> str:
    return os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "inputs"))

if __name__ == "__main__":
    raise SystemExit(main())