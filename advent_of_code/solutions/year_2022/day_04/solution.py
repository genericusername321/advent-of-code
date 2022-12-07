from pathlib import Path
from typing import List, Tuple, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

Shift = Tuple[int, int]
Assignment = Tuple[Shift, Shift]


def read_input(problem_input: str) -> List[Assignment]:
    lines = problem_input.split()
    shifts = []
    for line in lines:
        if line:
            first, second = line.split(",")
            shifts.append(
                (tuple(map(int, first.split("-"))), tuple(map(int, second.split("-"))))
            )
    return shifts


def check_interval_contains(assignment_a: Shift, assignment_b: Shift) -> bool:
    a_start, a_end = assignment_a
    b_start, b_end = assignment_b

    if (a_start <= b_start and a_end >= b_end) or (
        b_start <= a_start and b_end >= a_end
    ):
        return True

    return False


def check_interval_intersect(assignment_a: Shift, assignment_b: Shift) -> bool:
    a_start, a_end = assignment_a
    b_start, b_end = assignment_b

    if max(a_start, b_start) <= min(a_end, b_end):
        return True

    return False


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        shifts = read_input(problem_input)
        count = 0
        for shift in shifts:
            first_assignment, second_assignment = shift
            if check_interval_contains(first_assignment, second_assignment):
                count += 1

        return count

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        shifts = read_input(problem_input)
        count = 0
        for shift in shifts:
            first_assignment, second_assignment = shift
            if check_interval_intersect(first_assignment, second_assignment):
                count += 1

        return count


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
