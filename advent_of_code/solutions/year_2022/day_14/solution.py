from pathlib import Path
from typing import List, Tuple, Union

import numpy as np
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def get_direction(x: int) -> int:
    if x > 0:
        return 1

    if x < 0:
        return -1

    if x == 0:
        return 0

    raise ValueError("x must be an integer")


Point = Tuple[int, int]
Segment = Tuple[Point, Point]


def parse_input(puzzle_input: str) -> List[Segment]:
    lines = puzzle_input.split("\n")
    segments = []
    for line in lines:
        if not line:
            continue

        segment = line.split(" -> ")
        segment = list(map(lambda x: tuple(map(int, x.split(","))), segment))
        for start, end in zip(segment, segment[1:]):
            segments.append((start, end))
    return segments


class ReservoirSimulation:
    def __init__(self, segments: List[Segment]):
        self.starting_point = (500, 0)
        self.count = 0
        self.reservoir_map = np.zeros(shape=(1000, 200))
        self.max_depth = 0

        for segment in segments:
            (a, b), (c, d) = segment
            self.max_depth = max(self.max_depth, b, d)
            dx = get_direction(c - a)
            dy = get_direction(d - b)
            self.reservoir_map[a, b] = 1
            x, y = a, b
            while x != c or y != d:
                x = x + dx
                y = y + dy
                self.reservoir_map[x, y] = 1

        # Add floor
        floor_depth = self.max_depth + 2
        self.reservoir_map[:, floor_depth] = 1

    def drop_sand(self) -> int:
        """Simulate dropping a particle of sand.

        :return: Integer representing the depth at which the particle comes to rest
        """
        x, y = self.starting_point
        while True:
            if not self.reservoir_map[(x, y + 1)]:
                y += 1
            elif not self.reservoir_map[(x - 1, y + 1)]:
                x -= 1
                y += 1
            elif not self.reservoir_map[(x + 1, y + 1)]:
                x += 1
                y += 1
            else:
                # Particle comes to rest
                self.reservoir_map[(x, y)] = 1
                self.count += 1
                return y

    def simulate_part_1(self):
        while self.drop_sand() < self.max_depth:
            pass
        return self.count

    def simulate_part_2(self):
        while self.reservoir_map[500, 0] == 0:
            self.drop_sand()

        return self.count


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        segments = parse_input(problem_input)
        reservoir_map = ReservoirSimulation(segments)
        return reservoir_map.simulate_part_1() - 1

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        segments = parse_input(problem_input)
        reservoir = ReservoirSimulation(segments)
        return reservoir.simulate_part_2()


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
