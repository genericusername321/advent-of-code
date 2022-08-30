import time
from functools import wraps
from typing import Callable, Tuple

from advent_of_code.aoc.utils.package_utils import (
    create_day_package,
    create_year_package,
)
from advent_of_code.aoc.utils.path_utils import create_problem_input_path
from advent_of_code.config import (
    SOLUTION_CLASS_NAME,
    SOLUTION_FILE_NAME,
    SOLUTION_PACKAGE,
)


def timethis(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()

        duration = end - start
        return result, duration

    return wrapper


class SolutionRunner:
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

        module_name = SolutionRunner.build_module_name(year, day)
        solution_module = __import__(module_name, fromlist=[SOLUTION_CLASS_NAME])
        self._solution = solution_module.Solution()

    def _load_problem_input(self) -> None:
        problem_path = create_problem_input_path(self.year, self.day)
        with problem_path.open("r") as fh:
            self._problem_input = fh.read()

    @timethis
    def run_part_one(self) -> Tuple[any, int]:
        return self._solution.solve_part_one(self._problem_input)

    @timethis
    def run_part_two(self) -> Tuple[any, int]:
        return self._solution.solve_part_two(self._problem_input)

    def run_solutions(self) -> None:

        fmt_string = "Solution {year} day {day} part {part}: {value} in {duration} µs"

        self._load_problem_input()
        answer_one, duration_one = self.run_part_one()
        print(
            fmt_string.format(
                year=self.year,
                day=self.day,
                part="one",
                value=answer_one,
                duration=duration_one / 1000,
            )
        )

        answer_two, duration_two = self.run_part_two()
        print(
            fmt_string.format(
                year=self.year,
                day=self.day,
                part="one",
                value=answer_two,
                duration=duration_two / 1000,
            )
        )

    @staticmethod
    def build_module_name(year: int, day: int) -> str:
        """Build module name from year and day"""
        year_package = create_year_package(year)
        day_package = create_day_package(day)
        return f"{SOLUTION_PACKAGE}.{year_package}.{day_package}.{SOLUTION_FILE_NAME}"


def run_solution(year: int, day: int) -> None:
    """Run solution for problem given by year and day"""

    runner = SolutionRunner(year, day)
    runner.run_solutions()
