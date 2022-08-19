from pathlib import Path

import requests
from config import PACKAGE_ROOT, SOLUTION_DIR
from advent_of_code.utils.package_helpers import create_day_package, create_year_package


def create_destination_path(year: int, day: int, solutions_dir: Path) -> Path:
    """Create path to store the problem input."""

    year_package = create_year_package(year)
    day_package = create_day_package(day)
    solution_directory = solutions_dir / year_package / day_package
    solution_directory.mkdir(parents=True, exist_ok=True)
    return solution_directory / "problem_input.txt"


def save_problem_input(path, problem_input: bytes) -> None:

    with path.open("wb") as fh:
        fh.write(problem_input)


def get_session_cookie() -> dict[str, str]:
    """Read the session cookie stored in the .session file"""

    session_file_path = PACKAGE_ROOT / ".session"
    with session_file_path.open() as fh:
        session_value = fh.read()

    return {"session": session_value}


def download_problem_input(year: int, day: int) -> bytes:
    """Download problem input and return its contents in bytes"""

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = get_session_cookie()
    response: requests.Response = requests.get(url, cookies=session)
    response.raise_for_status()
    return response.content


def get_problem_input(
    year: int,
    day: int,
    solutions_dir: Path = SOLUTION_DIR,
) -> None:
    """Download and write the problem input to its solution directory"""

    problem_input = download_problem_input(year, day)
    destination_path = create_destination_path(year, day, solutions_dir)
    save_problem_input(destination_path, problem_input)
