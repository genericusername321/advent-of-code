from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List, Union, Optional, Set, Tuple

import numpy as np

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


@dataclass
class Instruction:
    direction: str
    distance: int


class RopeSegment:
    def __init__(
        self,
        head_position: np.ndarray = np.array([0, 0]),
        tail_position: np.ndarray = np.array([0, 0]),
        next_segment: Optional[RopeSegment] = None,
        index: int = 0,
    ):
        self.head_position = head_position
        self.tail_position = tail_position
        self.visited_head_positions = {tuple(self.head_position.astype(int))}
        self.visited_tail_positions = {tuple(self.tail_position.astype(int))}
        self.next_segment = next_segment
        self.index = index

    def set_head_position(self, position: np.ndarray):
        self.head_position = position
        self.visited_head_positions.add(tuple(position.astype(int)))
        head_tail_delta = self.head_position - self.tail_position
        delta_x, delta_y = head_tail_delta
        # print(
        #     f"Updating head: {self.index}, head: {self.head_position}, tail: {self.tail_position}, delta: {head_tail_delta}"
        # )

        if abs(delta_x) > 1 or abs(delta_y) > 1:
            new_tail_position = self.head_position - np.fix(head_tail_delta / 2)
            self.set_tail_position(new_tail_position)

    def set_tail_position(self, position: np.ndarray):
        # print(f"Updating tail: {self.index}, tail: {self.tail_position}")
        self.tail_position = position
        self.visited_tail_positions.add(tuple(position.astype(int)))
        if self.next_segment:
            self.next_segment.set_head_position(self.tail_position)

    def process_instruction(self, direction):
        up = np.array([1, 0])
        left = np.array([0, -1])
        dirs = {
            "U": up,
            "D": -up,
            "L": left,
            "R": -left,
        }

        delta_position = dirs[direction]
        self.set_head_position(self.head_position + delta_position)


def read_input(problem_input: str) -> List[Instruction]:
    lines = problem_input.split("\n")
    instructions = []
    for line in lines:
        if not line:
            continue

        direction, distance = line.split()
        instructions.append(Instruction(direction, int(distance)))
    return instructions


def print_rope(rope_head: RopeSegment) -> None:
    location_mapping = {}
    current_segment = rope_head
    while current_segment:
        location_mapping[current_segment.index] = tuple(
            current_segment.head_position.astype(int)
        )
        current_segment = current_segment.next_segment

    locations = list(location_mapping.values())
    x_coordinates = [-t[0] for t in locations]
    y_coordinates = [t[1] for t in locations]
    min_x, max_x = min(x_coordinates), max(x_coordinates)
    min_y, max_y = min(y_coordinates), max(y_coordinates)

    x_size = max_x - min_x
    y_size = max_y - min_y

    m = np.zeros(shape=(x_size + 1, y_size + 1)) - 1
    for index, (x, y) in location_mapping.items():
        m[-x - min_x, y - min_y] = index

    m = m.astype(int).astype(str)
    m[m == "-1"] = "."
    for line in m:
        print("".join(line))


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        instructions = read_input(problem_input)
        rope = RopeSegment()
        for instruction in instructions:
            for _ in range(instruction.distance):
                rope.process_instruction(instruction.direction)

        return len(rope.visited_tail_positions)

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        instructions = read_input(problem_input)
        rope_head = RopeSegment(index=0)
        current_segment = rope_head
        for i in range(1, 9):
            new_segment = RopeSegment(index=i)
            current_segment.next_segment = new_segment
            current_segment = current_segment.next_segment

        rope_tail = current_segment

        for instruction in instructions:
            for _ in range(instruction.distance):
                rope_head.process_instruction(instruction.direction)

        return len(rope_tail.visited_tail_positions)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
