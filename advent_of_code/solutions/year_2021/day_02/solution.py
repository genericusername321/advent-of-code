"""
Advent of Code solution
   year: 2021
   day: 2
   date: 2022-09-01
"""

from typing import List, Tuple, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        commands = Solution.parse_input(problem_input)
        x = y = 0
        for direction, magnitude in commands:
            if direction == "forward":
                x += magnitude
            elif direction == "down":
                y += magnitude
            elif direction == "up":
                y -= magnitude
            else:
                raise ValueError(f"Unexpected direction `{direction}`.")

        return x * y

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        commands = Solution.parse_input(problem_input)
        x = y = aim = 0
        for direction, magnitude in commands:
            if direction == "forward":
                x += magnitude
                y += aim * magnitude
            elif direction == "down":
                aim += magnitude
            elif direction == "up":
                aim -= magnitude
            else:
                raise ValueError(f"Unexpected direction `{direction}`")

        return x * y

    @staticmethod
    def parse_input(problem_input: str) -> List[Tuple[str, int]]:
        def split_and_parse(command: str) -> Tuple[str, int]:
            direction, magnitude = command.split()
            return direction, int(magnitude)

        lines = [line for line in problem_input.split("\n") if line]
        return list(map(split_and_parse, lines))
