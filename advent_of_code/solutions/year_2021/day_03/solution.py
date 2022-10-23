from typing import Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class NumberList:
    def __init__(self, problem_input: str):

        self._numbers = [(line) for line in problem_input.split() if line]
        self._ndigits = len(self._numbers[0])

    def _length(self):
        return len(self._numbers)

    def _compute_bit_sum(self, index: int) -> int:

        bit_sum = 0
        for num in self._numbers:
            if num[index] == "1":
                bit_sum += 1

        return bit_sum

    def _compute_most_common_bit(self, index: int) -> int:

        bit_sum = self._compute_bit_sum(index)
        return str(int(bit_sum >= self._length() / 2))

    def _compute_least_common_bit(self, index: int) -> int:

        most_common_bit = self._compute_most_common_bit(index)
        if most_common_bit == "1":
            return "0"
        else:
            return "1"

    def compute_gamma_rate(self) -> int:

        gamma = ""
        for i in range(self._ndigits):
            most_common_bit = self._compute_most_common_bit(i)
            gamma += most_common_bit

        return int(gamma, 2)

    def compute_epsilon_rate(self) -> int:

        gamma_rate = self.compute_gamma_rate()
        return 2 ** (self._ndigits) - gamma_rate - 1

    def compute_oxygen_generator_rating(self) -> int:

        index = 0
        while len(self._numbers) > 1:
            most_common_bit = self._compute_most_common_bit(index)
            self._filter(index, most_common_bit)
            index += 1

        return int(self._numbers[0], 2)

    def compute_co2_scrubber_rating(self) -> int:

        index = 0
        while len(self._numbers) > 1:
            least_common_bit = self._compute_least_common_bit(index)
            self._filter(index, least_common_bit)
            index += 1

        return int(self._numbers[0], 2)

    def _filter(self, index: int, value: str) -> None:

        self._numbers = [num for num in self._numbers if num[index] == value]


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        number_list = NumberList(problem_input)
        gamma = number_list.compute_gamma_rate()
        epsilon = number_list.compute_epsilon_rate()

        print(gamma, epsilon)
        return gamma * epsilon

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        number_list_oxygen = NumberList(problem_input)
        oxygen_generator_rating = number_list_oxygen.compute_oxygen_generator_rating()

        number_list_co2 = NumberList(problem_input)
        co2_scrubber_rating = number_list_co2.compute_co2_scrubber_rating()

        print(oxygen_generator_rating, co2_scrubber_rating)
        return oxygen_generator_rating * co2_scrubber_rating
