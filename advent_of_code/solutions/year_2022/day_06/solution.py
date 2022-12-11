from collections import deque
from pathlib import Path
from typing import Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def check_start_marker(packet: deque) -> bool:
    marker_length = 4
    if len(packet) != marker_length:
        return False

    if len(set(packet)) != marker_length:
        return False

    return True


def check_message(packet: deque) -> bool:
    message_length = 14
    if len(packet) != message_length:
        return False

    if len(set(packet)) != message_length:
        return False

    return True


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        packet = deque()
        for index, char in enumerate(problem_input.strip()):
            packet.append(char)
            if check_start_marker(packet):
                return index + 1
            if len(packet) >= 4:
                packet.popleft()

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        packet = deque()
        for index, char in enumerate(problem_input.strip()):
            packet.append(char)
            if check_message(packet):
                return index + 1
            if len(packet) >= 14:
                packet.popleft()


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
