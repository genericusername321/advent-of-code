def create_year_package(year: int) -> str:
    """Create year package name from given day"""

    return f"year_{year}"


def create_day_package(day: int) -> str:
    """Create day package name from given day of advent-of-code calendar"""

    return f"day_{day:02}"
