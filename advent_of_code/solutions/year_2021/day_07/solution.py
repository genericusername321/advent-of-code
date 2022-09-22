"""
Advent of Code solution
   year: 2021
   day: 7
   date: 2022-09-22
"""

from math import ceil, floor
from statistics import median
from typing import List, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        def compute_cost(optimal_location: int, crabs: List[int]) -> int:
            return int(sum(abs(optimal_location - crab) for crab in crabs))

        crab_locations = Solution.parse_problem_input(problem_input)
        median_value = median(crab_locations)
        fuel_cost = compute_cost(median_value, crab_locations)
        return fuel_cost

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        def compute_cost(optimal_location: int, crabs: List[int]) -> int:
            total = 0
            for crab in crabs:
                n = abs(optimal_location - crab)
                total += n * (n + 1) / 2
            return int(total)

        crab_locations = Solution.parse_problem_input(problem_input)
        mean_value = sum(crab_locations) / len(crab_locations)
        value_a = floor(mean_value)
        cost_a = compute_cost(value_a, crab_locations)

        value_b = ceil(mean_value)
        cost_b = compute_cost(value_b, crab_locations)
        return min(cost_a, cost_b)

    @staticmethod
    def parse_problem_input(problem_input: str) -> List[str]:
        """Parse the problem input"""
        return list(map(int, problem_input.split(",")))
