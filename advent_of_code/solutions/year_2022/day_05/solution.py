import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


@dataclass
class Instruction:
    """Moving instruction representing number of crates to move, the
    source and the destination.
    """

    number: int
    source: int
    destination: int


def parse_crates(crates: str) -> Dict[int, list]:
    """Parse the initial crate configuration to a dictionary.

    :param crates: Initial stack of crates
    :return: Dict containing the crates in each stack. The top of the stack is
             at the end of the deque
    """

    stacks: Dict[int, list] = defaultdict(list)
    pattern = re.compile(r"[A-Z]")
    for line in crates.split("\n"):
        matches = pattern.finditer(line)
        for match in matches:
            position = match.start() // 4 + 1
            crate = match.group()
            stacks[position].append(crate)

    for _, stack in stacks.items():
        stack.reverse()

    return stacks


def parse_procedure(procedure: str) -> List[Instruction]:
    """Parse the moving instructions

    :param procedure: Instruction input
    :return: List of instructions
    """

    instruction_list = []
    pattern = re.compile(r"move (\d+) from (\d) to (\d)")
    for line in procedure.split("\n"):
        match = pattern.search(line)
        if match:
            number, source, destination = tuple(map(int, match.groups()))
            instruction_list.append(Instruction(number, source, destination))

    return instruction_list


def find_top_crates(stacks: Dict[int, list]):
    """List the top crates of the stacks

    :param crates: stack of crates
    :return: string with the concatenated crates at the top of the stacks
    """

    result = ""
    stack_indices = sorted(list(stacks.keys()))
    for index in stack_indices:
        result += stacks[index][-1]

    return result


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        crate_map, procedure = problem_input.split("\n\n")
        stacks = parse_crates(crate_map)
        instruction_list = parse_procedure(procedure)

        for instruction in instruction_list:
            number = instruction.number
            source_stack = stacks[instruction.source]
            destination_stack = stacks[instruction.destination]

            for _ in range(number):
                crate = source_stack.pop()
                destination_stack.append(crate)

        return find_top_crates(stacks)

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        crate_map, procedure = problem_input.split("\n\n")
        stacks = parse_crates(crate_map)
        instruction_list = parse_procedure(procedure)

        for instruction in instruction_list:
            number = instruction.number
            source_stack = stacks[instruction.source]
            destination_stack = stacks[instruction.destination]

            staying_crates = source_stack[:-number]
            moving_crates = source_stack[-number:]
            stacks[instruction.source] = staying_crates
            destination_stack.extend(moving_crates)

            print(instruction)
            for i in range(1, 10):
                print(f"{i}: ", stacks[i])

        return find_top_crates(stacks)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
