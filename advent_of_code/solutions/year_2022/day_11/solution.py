from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

Operation = Callable[[int], int]


@dataclass
class Monkey:
    items: List[int]
    operation: Operation
    test_value: int
    true_target: int
    false_target: int
    number_inspected: int = 0

    @classmethod
    def from_string(cls, input: str) -> Monkey:
        def parse_number(line: str):
            match = re.search(r"(\d+)", line)
            if match:
                return int(match.group())
            else:
                raise ValueError("Line does not contain numbers")

        def parse_expression(line: str):
            pattern = r"[a-z\d]+ [+*] [a-z\d]+"
            match = re.search(pattern, line)
            if match:
                return match.group()
            else:
                raise ValueError("Line does not contain expression")

        lines = input.split("\n")
        return cls(
            items=list(map(int, re.findall(r"(\d+)", lines[1]))),
            operation=eval("lambda old:" + parse_expression(lines[2])),
            test_value=parse_number(lines[3]),
            true_target=parse_number(lines[4]),
            false_target=parse_number(lines[5]),
        )

    def play(self, worry_divider: int, worry_mod: int):
        """Inspect and throw all of the items the monkey currently has

        :param worry_divider: The number to divide worry number by after each
        inspection
        :param worry_mod: Perform modulo operation after each inspection
        :yield: tuple indicating the monkey the item will be thrown to
        """
        while self.items:
            self.number_inspected += 1
            inspected_item = self.items.pop()
            worry_level = (self.operation(inspected_item) // worry_divider) % worry_mod
            if worry_level % self.test_value == 0:
                yield (self.true_target, worry_level)
            else:
                yield (self.false_target, worry_level)

    def receive_item(self, item):
        self.items.append(item)


class KeepAway:
    def __init__(self, monkeys: List[Monkey], divider: int):
        self.monkeys = monkeys
        self.worry_divider = divider
        self.worry_mod = self.compute_worry_mod()

    def compute_worry_mod(self):
        mod = 1
        for monkey in self.monkeys:
            mod *= monkey.test_value
        return mod

    def play_round(self):
        for monkey in self.monkeys:
            for target, item in monkey.play(self.worry_divider, self.worry_mod):
                self.monkeys[target].receive_item(item)

    @property
    def monkey_business(self):
        numbers_inspected = sorted(
            [m.number_inspected for m in self.monkeys], reverse=True
        )
        first, second, *_ = numbers_inspected
        return first * second


def parse_input(problem_input: str) -> List[Monkey]:

    monkey_inputs = problem_input.split("\n\n")
    monkeys = []
    for m in monkey_inputs:
        monkeys.append(Monkey.from_string(m))
    return monkeys


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        monkeys = parse_input(problem_input)
        game = KeepAway(monkeys, divider=3)
        number_of_rounds = 20

        for _ in range(number_of_rounds):
            game.play_round()

        return game.monkey_business

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        monkeys = parse_input(problem_input)
        game = KeepAway(monkeys, divider=1)
        number_of_rounds = 10000

        for _ in range(number_of_rounds):
            game.play_round()

        return game.monkey_business


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
