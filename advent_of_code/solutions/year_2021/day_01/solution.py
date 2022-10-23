from typing import List, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        parsed_input = Solution.prepare_input(problem_input)

        count = 0
        previous = float("inf")
        for depth in parsed_input:
            if depth > previous:
                count += 1

            previous = depth

        return count

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        parsed_input = Solution.prepare_input(problem_input)

        count = 0
        window_length = 3
        current_window = sum(parsed_input[:window_length])
        for index in range(window_length, len(parsed_input)):
            new_window = (
                current_window
                - parsed_input[index - window_length]
                + parsed_input[index]
            )
            if new_window > current_window:
                count += 1
            current_window = new_window

        return count

    @staticmethod
    def prepare_input(problem_input: str) -> List[int]:

        return list(map(int, problem_input.split()))
