import os

from aoc_2022 import day1


def test_part_a(capsys):
    day1.main(
        [
            "-i",
            os.path.abspath(
                os.path.join(__file__, os.pardir, os.pardir, "inputs", "1a.txt"),
            ),
        ],
    )
    captured = capsys.readouterr()
    assert captured.out.strip() == "Most calories: 71506"


def test_part_b(capsys):
    day1.main(
        [
            "-i",
            os.path.abspath(
                os.path.join(__file__, os.pardir, os.pardir, "inputs", "1a.txt"),
            ),
            "-n", "3",
        ],
    )
    captured = capsys.readouterr()
    assert captured.out.strip() == "Most calories: 209603"