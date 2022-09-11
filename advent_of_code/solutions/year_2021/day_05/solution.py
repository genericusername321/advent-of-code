"""
Advent of Code solution
   year: 2021
   day: 5
   date: 2022-09-11
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from typing import Generator, List, Tuple, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

PointType = Tuple[int, int]
LineType = Tuple[PointType, PointType]


@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)


def sign(x: int) -> int:
    if x >= 0:
        return 1
    elif x < 0:
        return -1
    else:
        return ValueError


@dataclass
class Line:
    start: Point
    end: Point

    def is_horizontal(self):
        return self.start.x == self.end.x

    def is_vertical(self):
        return self.start.y == self.end.y

    def generate_coordinates(self) -> Generator[Tuple[int, int]]:
        delta = self.end - self.start
        step_x = sign(delta.x)
        step_y = sign(delta.y)
        range_x = range(self.start.x, self.end.x + step_x, step_x)
        range_y = range(self.start.y, self.end.y + step_y, step_y)

        if self.is_horizontal() or self.is_vertical():
            for x, y in product(range_x, range_y):
                yield (x, y)
        else:
            for x, y in zip(range_x, range_y):
                yield (x, y)


def parse_problem_input(problem_input: str) -> List[Line]:
    def parse_point(input_pair: str) -> Point:
        return Point(*map(int, input_pair.split(",")))

    floor_map = []
    for line in problem_input.split("\n"):
        if not line:
            continue

        vent_start, vent_end = line.split(" -> ")
        start_point = parse_point(vent_start)
        end_point = parse_point(vent_end)
        floor_map.append(Line(start_point, end_point))

    return floor_map


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        height_map = defaultdict(int)
        floor_map = parse_problem_input(problem_input)

        for line in floor_map:
            if line.is_horizontal() or line.is_vertical():
                for coords in line.generate_coordinates():
                    height_map[coords] += 1

        heights = height_map.values()
        return len([h for h in heights if h >= 2])

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        height_map = defaultdict(int)
        floor_map = parse_problem_input(problem_input)

        for line in floor_map:
            for coords in line.generate_coordinates():
                height_map[coords] += 1

        heights = height_map.values()
        return len([h for h in heights if h >= 2])
