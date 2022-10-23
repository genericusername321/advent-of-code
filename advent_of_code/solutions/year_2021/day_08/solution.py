from collections import defaultdict
from typing import Dict, List, Set, Union

from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def sort_string(s: str) -> str:
    return "".join(sorted(s))


class SegmentDisplayProblem:
    def __init__(self, signals: List[str], outputs: List[str]):
        # sort signals and outputs
        sorted_signals = list(map(sort_string, signals))
        sorted_outputs = list(map(sort_string, outputs))

        self.signals = sorted_signals
        self.outputs = sorted_outputs
        self._signal_to_display = {}
        self._display_to_signal = {}
        self._signals_by_length = defaultdict(set)

    def map_output_digits(self) -> List[str]:
        """Find values of display"""
        self._create_mapping()
        return [self._signal_to_display[output] for output in self.outputs]

    def _map_signal(self, signal: str, output: str):
        self._signal_to_display[signal] = output
        self._display_to_signal[output] = signal

    def _create_mapping(self) -> Dict[Set[str], int]:
        """Create a mapping from signals to the displayed value"""

        # First we map the signals with unique number of illuminated
        # segments to their output, i.e. 1, 4, 7 and 8.
        for signal in self.signals:
            if len(signal) == 2:
                self._map_signal(signal, "1")
            elif len(signal) == 3:
                self._map_signal(signal, "7")
            elif len(signal) == 4:
                self._map_signal(signal, "4")
            elif len(signal) == 7:
                self._map_signal(signal, "8")
            else:
                self._signals_by_length[len(signal)].add(signal)

        # Then we can find the signals that map to 0, 6 and 9, as these have
        # 6 segments each. Note that:
        #   - 9 contains 4 and 7
        #   - 0 contains 7
        #   - 6 contains neither 4 or 7
        for signal in self._signals_by_length[6]:
            signal_seven = self._display_to_signal["7"]
            signal_four = self._display_to_signal["4"]
            if set(signal_four).issubset(set(signal)):
                self._map_signal(signal, "9")
            elif set(signal_seven).issubset(set(signal)):
                self._map_signal(signal, "0")
            else:
                self._map_signal(signal, "6")

        # Finally map the signals that correspond to 2, 3 and 5.
        # Note that 7 is a subset of 3, and that 5 is a subset of 6
        for signal in self._signals_by_length[5]:
            signal_seven = self._display_to_signal["7"]
            signal_six = self._display_to_signal["6"]
            if set(signal_seven).issubset(set(signal)):
                self._map_signal(signal, "3")
            elif set(signal).issubset(set(signal_six)):
                self._map_signal(signal, "5")
            else:
                self._map_signal(signal, "2")


def parse_input(problem_input: str) -> List[SegmentDisplayProblem]:
    lines = problem_input.split("\n")
    problems = []
    for line in lines:
        if not line:
            continue
        signals, outputs = map(lambda x: x.split(), line.split(" | "))
        problems.append(SegmentDisplayProblem(signals, outputs))

    return problems


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        problems = parse_input(problem_input)

        total = 0
        for problem in problems:
            output_digits = problem.map_output_digits()
            for digit in output_digits:
                if digit in {"1", "4", "7", "8"}:
                    total += 1

        return total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        problems = parse_input(problem_input)

        total = 0
        for problem in problems:
            output_digits = problem.map_output_digits()
            display = int("".join(output_digits))
            total += display
        return total
