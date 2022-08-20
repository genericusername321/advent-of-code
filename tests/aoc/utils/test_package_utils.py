"""
Tests for the advent_of_code.utils.package_helpers module
"""

from advent_of_code.aoc.utils.package_utils import (
    create_day_package,
    create_year_package,
)


def test_create_year_package() -> None:

    # Arrange
    year = 2020
    expected = "year_2020"

    # Act
    actual = create_year_package(year)

    # Assert
    assert actual == expected


def test_create_day_package() -> None:

    # Arrange
    day = 1
    expected = "day_01"

    # Act
    actual = create_day_package(day)

    # Assert
    assert actual == expected
