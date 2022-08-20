from pathlib import Path

import requests
from advent_of_code.config import PACKAGE_ROOT, SOLUTION_DIR
from advent_of_code.aoc.utils.path_utils import create_problem_input_path


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
    destination_path = create_problem_input_path(year, day, solutions_dir)
    save_problem_input(destination_path, problem_input)
