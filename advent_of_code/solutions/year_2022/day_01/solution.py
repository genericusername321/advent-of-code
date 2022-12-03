from typing import List, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def read_input(problem_input: str) -> List[List[int]]:
    inventory_lists = problem_input.split("\n\n")
    return [list(map(int, lis.split())) for lis in inventory_lists]


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        inventory_lists = read_input(problem_input)
        return max(map(sum, inventory_lists))

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        inventory_lists = read_input(problem_input)
        calories = sorted(list(map(sum, inventory_lists)), reverse=True)
        return sum(calories[:3])
