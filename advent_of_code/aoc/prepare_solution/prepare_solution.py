from datetime import date

from advent_of_code.aoc.prepare_solution.download_input import get_problem_input
from advent_of_code.aoc.templates.solution_template import SOLUTION_TEMPLATE
from advent_of_code.aoc.utils.path_utils import (
    create_solution_package_dir,
    create_solution_path,
)
from config import SOLUTION_DIR


def write_solution_template(year: int, day: int) -> None:
    path = create_solution_path(year, day, SOLUTION_DIR)

    if path.exists():
        # TODO: Create custom exception
        raise FileExistsError(
            f"A solution file to problem {year} day {day} already exists!"
        )

    with path.open("w") as fh:
        fh.write(
            SOLUTION_TEMPLATE.format(year=year, day=day, date=date.today().isoformat())
        )


def prepare_solution_dir(year: int, day: int) -> None:

    create_solution_package_dir(year, day)
    get_problem_input(year, day)
    write_solution_template(year, day)
