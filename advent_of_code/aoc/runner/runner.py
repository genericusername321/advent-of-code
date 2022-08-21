from advent_of_code.aoc.utils.package_utils import (
    create_year_package,
    create_day_package,
)
from advent_of_code.aoc.utils.path_utils import create_problem_input_path

from advent_of_code.config import (
    SOLUTION_CLASS_NAME,
    SOLUTION_PACKAGE,
    SOLUTION_FILE_NAME,
)


def build_module_name(year: int, day: int) -> str:
    year_package = create_year_package(year)
    day_package = create_day_package(day)
    return f"{SOLUTION_PACKAGE}.{year_package}.{day_package}.{SOLUTION_FILE_NAME}"


def load_problem_input(year: int, day: int) -> str:
    problem_path = create_problem_input_path(year, day)
    with problem_path.open("r") as fh:
        return fh.read()


def run_solution(year: int, day: int) -> None:
    """Run solution for problem given by year and day"""
    fmt_string = "Solution {year} day {day} part {part}: {value}"

    module_name = build_module_name(year, day)
    solution_module = __import__(module_name, fromlist=[SOLUTION_CLASS_NAME])
    solution = solution_module.Solution()

    problem_input = load_problem_input(year, day)

    # Run part 1 of solution
    answer_part_one = solution.solve_part_one(problem_input)
    print(fmt_string.format(year=year, day=day, part="one", value=answer_part_one))

    # Run part 2 of solution
    answer_part_two = solution.solve_part_two(problem_input)
    print(fmt_string.format(year=year, day=day, part="two", value=answer_part_two))
