from pathlib import Path
from typing import List, Tuple, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

Rucksack = Tuple[str, str]


def read_input(problem_input: str) -> List[Rucksack]:

    lines = problem_input.split()
    rucksacks = []
    for line in lines:
        length = len(line)
        first_compartment = line[: length // 2]
        second_compartment = line[(length // 2) :]
        rucksacks.append((first_compartment, second_compartment))

    return rucksacks


def compute_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord("A") + 27
    elif item.islower():
        return ord(item) - ord("a") + 1
    else:
        raise ValueError


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        rucksacks = read_input(problem_input)
        total_priority = 0
        for rucksack in rucksacks:
            first_compartment, second_compartment = rucksack
            intersection = set.intersection(
                set(first_compartment), set(second_compartment)
            )
            common_item = "".join(intersection)
            total_priority += compute_priority(common_item)

        return total_priority

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        lines = problem_input.split()
        total_priority = 0
        for index in range(0, len(lines), 3):
            group: List[str] = lines[index : index + 3]
            common = set.intersection(*list(map(set, group)))
            badge = "".join(common)
            total_priority += compute_priority(badge)

        return total_priority


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
