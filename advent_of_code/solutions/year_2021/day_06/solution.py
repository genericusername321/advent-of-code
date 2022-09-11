"""
Advent of Code solution
   year: 2021
   day: 6
   date: 2022-09-11
"""

from collections import Counter
from itertools import accumulate
from typing import Iterator, List, Mapping, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def parse_problem_input(problem_input: str) -> Iterator[int]:
    return map(int, problem_input.split(","))


def compute_number_of_fish(num_days: int) -> List[int]:
    """Compute the number of fish spawned by a single lantern fish

    The initial lantern fish is assumed to be at counter 0 at day 0. For a
    fish with counter `c`, find the number of fish spawned at day n at
    `total_fish[num_days - c]`

    :param_n: The last day for which we need to calculate the number of fish
    :return: List of integers, denoting the total number of fish at day n
    """
    list_len = num_days + 1
    new_fish = [0] * list_len
    new_fish[0] = 1

    for i in range(1, list_len, 7):
        new_fish[i] = 1

    for i in range(1, list_len):
        f = new_fish[i]
        if f == 0:
            continue
        for j in range(i + 9, list_len, 7):
            new_fish[j] += f

    total_fish = list(accumulate(new_fish))
    return total_fish


def count_fish(num_fish: List[int], fish_counts: Mapping[int, int]) -> int:
    days = len(num_fish) - 1
    total = 0
    for days_left, count in fish_counts.items():
        total += count * num_fish[days - days_left]
    return total


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        days = 80
        num_fish = compute_number_of_fish(days)

        numbers = parse_problem_input(problem_input)
        fish_counts = Counter(numbers)
        return count_fish(num_fish, fish_counts)

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        days = 256
        num_fish = compute_number_of_fish(days)

        numbers = parse_problem_input(problem_input)
        fish_counts = Counter(numbers)

        return count_fish(num_fish, fish_counts)
