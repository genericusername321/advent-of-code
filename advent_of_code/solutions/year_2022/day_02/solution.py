from typing import List, Tuple, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


Game = Tuple[str, str]


def token_to_value(token: str) -> int:
    return ord(token) - ord("A")


def value_to_token(value: int) -> str:
    return chr(value + ord("A"))


def read_input(problem_input: str) -> List[Game]:
    lines = problem_input.split("\n")
    return [tuple(line.split()) for line in lines if line]


def compute_score(token_a: str, token_b: str) -> int:
    """Compute the score for player B given the tokens played"""
    result_map = {0: 3, 1: 6, 2: 0}

    value_a = token_to_value(token_a)
    value_b = token_to_value(token_b)
    result = (value_b - value_a) % 3
    return result_map[result] + value_b + 1


def compute_token(token_a: str, desired_result: str) -> str:
    """Compute the token that needs to be played to obtain the desired result"""
    value_map = {"X": -1, "Y": 0, "Z": 1}
    value_a = token_to_value(token_a)
    value_b = (value_a + value_map[desired_result]) % 3
    return value_to_token(value_b)


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        games = read_input(problem_input)

        total_score = 0
        for game in games:
            token_a, token_b = game
            token_b = chr(ord(token_b) - ord("X") + ord("A"))
            total_score += compute_score(token_a, token_b)
        return total_score

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        games = read_input(problem_input)

        total_score = 0
        for game in games:
            token_a, desired_outcome = game
            token_b = compute_token(token_a, desired_outcome)
            total_score += compute_score(token_a, token_b)
        return total_score
