from pathlib import Path
from advent_of_code.aoc.utils.package_utils import (
    create_day_package,
    create_year_package,
)
from advent_of_code.config import SOLUTION_FILE_NAME


def create_solution_package_dir(year: int, day: int, solutions_dir: Path) -> Path:
    """Create path to solution package"""

    year_package = create_year_package(year)
    day_package = create_day_package(day)

    solution_directory = solutions_dir / year_package / day_package
    if not solution_directory.exists():
        solution_directory.mkdir(parents=True)

    return solution_directory


def create_problem_input_path(year: int, day: int, solutions_dir: Path) -> Path:
    """Create path to store the problem input"""

    solution_directory = create_solution_package_dir(year, day, solutions_dir)
    return solution_directory / "problem_input.txt"


def create_solution_path(year: int, day: int, solutions_dir: Path) -> Path:
    """Create path to store solution.py file"""

    solution_directory = create_solution_package_dir(year, day, solutions_dir)
    solution_path = solution_directory / SOLUTION_FILE_NAME
    return solution_path
