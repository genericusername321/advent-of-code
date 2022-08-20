from pathlib import Path

import pytest
from advent_of_code.config import PACKAGE_ROOT
from advent_of_code.aoc.utils.path_utils import create_solution_package_dir


def recursive_rm(path: Path) -> None:
    """Remove all items in the directory at path"""

    if path.is_file():
        path.unlink()
        return

    for child in path.iterdir():
        recursive_rm(child)

    path.rmdir()


@pytest.fixture
def test_directory():

    test_dir = PACKAGE_ROOT / "tests" / ".testdir"
    yield test_dir
    recursive_rm(test_dir)


def test_create_solutions_package_dir(test_directory):

    # Arrange
    year = 2021
    day = 1
    solutions_dir = test_directory

    expected = solutions_dir / "year_2021" / "day_01"

    # Act
    actual = create_solution_package_dir(year, day, solutions_dir)

    # Assert
    assert actual == expected
