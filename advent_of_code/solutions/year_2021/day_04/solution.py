"""
Advent of Code solution
   year: 2021
   day: 4
   date: 2022-09-03
"""

from typing import List, Tuple, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


class Board:
    def __init__(self, board: List[List[int]]):
        """Create a board object from a matrix of numbers

        :param board: 2D square matrix denoting the numbers of the bingo board.
        """

        n_columns = len(board[0])
        self._lines = [set(row) for row in board]
        self._lines.extend(
            set(row[col_index] for row in board) for col_index in range(n_columns)
        )
        self.game_over = False

    def play_turn(self, called_number: int) -> None:
        """Mark the called number on the bingo board and check if
        the board won

        :param called_number: Number called at current turn in bingo game
        :return: None
        """

        for line in self._lines:
            line.discard(called_number)

    def check_win(self) -> bool:
        """Check the board to see if any lines have been fully marked

        :return: Boolean value indicating whether the bingo card has won.
        """
        for line in self._lines:
            if not line:
                self.game_over = True
                return True

        return False

    @property
    def board_total(self) -> int:
        """Compute the sum of the values of the unmarked numbers on the board

        :return: Integer representing the sum of the unmarked values
        """

        return sum(sum(line) for line in self._lines) // 2


def parse_input(problem_input: str) -> Tuple[List[int], list[Board]]:
    """Parse problem input to called numbers and bingo boards"""

    called_numbers, *board_data = problem_input.split("\n\n")
    called_numbers = list(map(int, called_numbers.split(",")))

    bingo_boards = []
    for board_string in board_data:
        parsed_board = [
            list(map(int, row.split())) for row in board_string.split("\n") if row
        ]
        bingo_boards.append(Board(parsed_board))

    return called_numbers, bingo_boards


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        called_numbers, boards = parse_input(problem_input)

        for number in called_numbers:
            for bingo_board in boards:
                bingo_board.play_turn(number)
                win = bingo_board.check_win()
                if win:
                    return number * bingo_board.board_total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        called_numbers, boards = parse_input(problem_input)

        last_score = None
        for number in called_numbers:
            for bingo_board in boards:
                if bingo_board.game_over:
                    continue

                bingo_board.play_turn(number)
                win = bingo_board.check_win()
                if win:
                    last_score = number * bingo_board.board_total

        return last_score
