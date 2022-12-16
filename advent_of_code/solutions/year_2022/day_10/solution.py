from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

import numpy as np
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

NOOP = "noop"
ADDX = "addx"


@dataclass
class Instruction:
    operation: str
    value: Optional[int] = None


def parse_input(problem_input: str) -> List[Instruction]:
    instructions = []
    for line in problem_input.split("\n"):
        if not line:
            continue

        if line == NOOP:
            instructions.append(Instruction(line))
        else:
            operation, value = line.split()
            instructions.append(Instruction(operation, int(value)))
    return instructions


class Process:

    cycle_cost = {
        NOOP: 1,
        ADDX: 2,
    }

    def __init__(self, instruction_list: List[Instruction]):
        self.instructions = instruction_list
        self.cycle_number = 0
        self.x = 1
        self.signal_strengths = []

    def process(self):
        for instruction in self.instructions:
            if instruction.operation == NOOP:
                self.cycle_number += self.cycle_cost[instruction.operation]
                yield self.x
            elif instruction.operation == ADDX:
                for _ in range(self.cycle_cost[instruction.operation]):
                    self.cycle_number += 1
                    yield self.x

                self.x += instruction.value
            else:
                # Probably should be InvalidInstructionError
                raise ValueError("Operation must be one of `{NOOP}` or `{ADDX}`")


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        instructions = parse_input(problem_input)
        process = Process(instructions)
        total = 0
        for cycle_number, val in enumerate(process.process(), start=1):
            if (cycle_number - 20) % 40 == 0:
                total += val * (cycle_number)
        return total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        instructions = parse_input(problem_input)
        process = Process(instructions)

        pixels = []
        for cycle_number, x in enumerate(process.process()):
            write_location = cycle_number % 40
            if abs(write_location - x) <= 1:
                pixels.append("#")
            else:
                pixels.append(".")

        picture = np.array(pixels).reshape(6, 40)
        result = "\n"
        for row in picture:
            result += "".join(row)
            result += "\n"
        return result


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
