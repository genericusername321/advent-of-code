from advent_of_code.aoc.utils.package_utils import (
    create_year_package,
    create_day_package,
)

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
    pass


def run_solution(year: int, day: int) -> None:
    """Run solution for problem given by year and day"""
    fmt_string = "Solution {year} / {day} part {part}: {value}"

    module_name = build_module_name(year, day)
    solution_module = __import__(module_name, fromlist=[SOLUTION_CLASS_NAME])
    solution = solution_module.Solution()

    # Run part 1 of solution
    answer_part_one = solution.solve_part_one()
    print(fmt_string.format(year, day, "one", answer_part_one))

    # Run part 2 of solution
    answer_part_two = solution.solve_part_two()
    print(fmt_string.format(year, day, "two", answer_part_two))
