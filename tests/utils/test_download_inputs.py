"""
Tests for advent_of_code.utils.download_inputs module
"""
from pathlib import Path

import pytest
from advent_of_code.config import PACKAGE_ROOT
from advent_of_code.utils.download_inputs import create_destination_path


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


def test_create_destination_path(test_directory):

    # Arrange
    year = 2021
    day = 10

    # Act
    solution_dir = create_destination_path(year, day, test_directory)

    # Assert
    print(solution_dir.name)
