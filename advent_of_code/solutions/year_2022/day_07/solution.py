from __future__ import annotations

import re
from bisect import bisect_right
from dataclasses import dataclass
from pathlib import Path
from typing import Generator, List, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

# Probably should do this with state machine parser


@dataclass
class Directory:
    name: str
    total_file_size: int
    sub_directories: list[Directory]

    @property
    def size(self) -> int:
        sub_dir_size = sum(sd.size for sd in self.sub_directories)
        return self.total_file_size + sub_dir_size

    def list_subdir_sizes(self) -> List[int]:
        subdir_sizes = []
        for subdir in self.sub_directories:
            subdir_sizes.extend(subdir.list_subdir_sizes())
        subdir_sizes.append(self.size)

        return subdir_sizes


def parse_filesystem(terminal_output: List[str]) -> Directory:

    pattern = re.compile(r"(\d+)\w")

    def output_generator() -> Generator[str, None, None]:
        for line in terminal_output:
            yield line

    output = output_generator()

    def parse_directory(output):
        line = next(output)
        dir_name = line[5:].strip()
        dir = Directory(name=dir_name, total_file_size=0, sub_directories=[])

        while True:
            try:
                line = next(output)
                match = pattern.match(line)
                if match:
                    dir.total_file_size += int(match.group())
                elif line.startswith("$ cd .."):
                    return dir
                elif line.startswith("$ cd"):
                    sub_dir = parse_directory(output)
                    dir.sub_directories.append(sub_dir)
                else:
                    pass

            except StopIteration:
                return dir

    return parse_directory(output)


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        terminal_output = problem_input.split("\n")
        root_dir = parse_filesystem(terminal_output)
        subdir_sizes = root_dir.list_subdir_sizes()
        return sum([d for d in subdir_sizes if d <= 100000])

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        terminal_output = problem_input.split("\n")
        root_dir = parse_filesystem(terminal_output)

        max_bytes = 70000000
        required_bytes = 30000000
        occupied_bytes = root_dir.size
        bytes_to_delete = occupied_bytes - (max_bytes - required_bytes)

        subdir_sizes = root_dir.list_subdir_sizes()
        subdir_sizes.sort()
        index = bisect_right(subdir_sizes, bytes_to_delete)
        return subdir_sizes[index]


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
