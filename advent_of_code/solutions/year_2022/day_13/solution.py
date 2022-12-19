from __future__ import annotations
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
from typing import Any, List, Optional, Tuple, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


@dataclass
class Packet:
    data: list

    def __lt__(self, other: Packet) -> int:
        """Compare whether lhs packet is smaller than rhs packet

        :param lhs: lhs packet
        :param rhs: rhs packet
        :return: True if lhs < rhs, None if inconclusive
        """

        lhs = self.data
        rhs = other.data

        def try_listify(object: Any) -> Union[Any, List[Any]]:
            if isinstance(object, list):
                return object

            return [object]

        for item_left, item_right in zip_longest(lhs, rhs):
            if item_left is None:
                return True

            if item_right is None:
                return False

            if isinstance(item_right, int) and isinstance(item_left, int):
                if item_left == item_right:
                    continue
                if item_left < item_right:
                    return True
                else:
                    return False

            # Both items are lists
            left_sub_packet = Packet(try_listify(item_left))
            right_sub_packet = Packet(try_listify(item_right))
            sub_packet_result = left_sub_packet.__lt__(right_sub_packet)
            if sub_packet_result == 2:
                continue
            else:
                return sub_packet_result

        return 2


def parse_input_to_pairs(problem_input: str) -> List[Tuple[list, list]]:
    packet_pairs = []
    packets = problem_input.strip().split("\n\n")
    for pair in packets:
        packet_pairs.append(tuple(map(eval, pair.split("\n"))))
    return packet_pairs


def parse_input_to_list(problem_input: str) -> List[Packet]:
    problem_input = problem_input.replace("\n\n", "\n")
    packets = problem_input.split()
    return list(map(lambda x: Packet(eval(x)), packets))


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        packet_pairs = parse_input_to_pairs(problem_input)
        total = 0
        for index, (lhs, rhs) in enumerate(packet_pairs, start=1):
            if Packet(lhs).__lt__(Packet(rhs)):
                total += index

        return total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        divider_packet_2 = Packet([[2]])
        divider_packet_6 = Packet([[6]])

        packets = parse_input_to_list(problem_input)
        packets.append(divider_packet_2)
        packets.append(divider_packet_6)
        sorted_packets = sorted(packets)
        two_index = sorted_packets.index(divider_packet_2) + 1
        six_index = sorted_packets.index(divider_packet_6) + 1
        return two_index * six_index


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
