from __future__ import annotations
import re
from pathlib import Path
from typing import List, Tuple, Union, Optional

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

Point = Tuple[int, int]
Interval = Tuple[int, int]


def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    merged_intervals = []
    for interval in sorted(intervals):
        if not merged_intervals:
            merged_intervals.append(interval)
            continue

        prev_interval_begin, prev_interval_end = merged_intervals[-1]
        next_interval_begin, next_interval_end = interval

        if next_interval_begin > prev_interval_end + 1:
            # Next interval is disjoint from previous interval
            merged_intervals.append(interval)
        else:
            # Next interval is not disjoint from previous interval
            if next_interval_end > prev_interval_end:
                merged_intervals.pop()
                merged_intervals.append((prev_interval_begin, next_interval_end))

    return merged_intervals


def manhattan_distance(p1: Point, p2: Point) -> int:
    a, b = p1
    c, d = p2
    return abs(c - a) + abs(d - b)


class Sensor:
    def __init__(self, position: Point, nearest_beacon: Point):
        self.position = position
        self.nearest_beacon = nearest_beacon
        self.distance = manhattan_distance(position, nearest_beacon)

    def compute_exclusion_zone(self, y: int) -> Optional[Tuple[int, int]]:
        """Compute excluded x-values for a given y-value

        :return: Tuple indicating excluded range
        """
        sensor_x, sensor_y = self.position
        d = self.distance - abs(y - sensor_y)
        if d < 0:
            return None

        return sensor_x - d, sensor_x + d


def parse_input(problem_input: str) -> List[Sensor]:
    pattern = re.compile(r"-?[\d]+")

    sensors = []
    for line in problem_input.split("\n"):
        if not line:
            continue

        a, b, c, d = tuple(map(int, pattern.findall(line)))
        sensors.append(Sensor((a, b), (c, d)))
    return sensors


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        sensors = parse_input(problem_input)

        # For each sensor find range of x
        y = 2000000
        intervals = []
        for s in sensors:
            interval = s.compute_exclusion_zone(y)
            if interval:
                intervals.append(interval)

        merged_intervals = merge_intervals(intervals)
        total = 0
        for a, b in merged_intervals:
            total += b - a
        return total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        sensors = parse_input(problem_input)

        y_range = 4000000
        x_range = 4000000
        for y in range(y_range + 1):
            intervals = []
            for s in sensors:
                interval = s.compute_exclusion_zone(y)
                if interval:
                    intervals.append(interval)

            merged_intervals = merge_intervals(intervals)
            for _, iv_end in merged_intervals:
                if -1 <= iv_end < x_range:
                    return 4000000 * (iv_end + 1) + y

        return -1


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
