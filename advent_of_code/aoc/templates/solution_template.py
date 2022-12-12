SOLUTION_TEMPLATE = """
from pathlib import Path
from typing import Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        pass

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        pass


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
"""
