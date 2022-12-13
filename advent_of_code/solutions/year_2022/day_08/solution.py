from pathlib import Path
from typing import Iterable, List, Union

import numpy as np
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def parse_input_to_matrix(problem_input: str) -> np.ndarray:
    """Parse problem input to numpy array

    :param problem_input: problem input
    :return: numpy array of tree heights
    """
    input_lines = problem_input.split()
    height = len(input_lines)
    width = len(input_lines[0])

    return (
        np.fromiter("".join(input_lines), dtype=np.dtype("U1"))
        .astype(int)
        .reshape(height, width)
    )


def is_visible(line: Iterable[int]) -> List[bool]:
    tallest = -1
    visible = []
    for tree in line:
        if tree > tallest:
            visible.append(True)
            tallest = tree
        else:
            visible.append(False)
    return visible


def check_visibility(tree_heights: np.ndarray) -> np.ndarray:
    """Check the visibility from the left given a map of tree heights

    :param tree_heights: 2D numpy array with tree heights
    :return: 2D numpy array, indicating which trees are visible from the top
    """
    nrow, ncol = tree_heights.shape
    visible_trees = np.zeros(shape=tree_heights.shape)

    row_max = -1 * np.ones(ncol)
    for i in range(nrow):
        row = tree_heights[i, :]
        visible_trees[i, :] = row > row_max
        row_max = np.maximum(row, row_max)

    return visible_trees


def compute_tree_score(tree_map: np.ndarray, start_row: int, start_col: int):

    nrow, ncol = tree_map.shape
    current_height = tree_map[start_row, start_col]

    score = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dir in directions:
        temp_score = 0
        dx, dy = dir

        i = 1
        row = start_row + i * dx
        col = start_col + i * dy
        while 0 <= row < nrow and 0 <= col < ncol:
            if tree_map[row, col] < current_height:
                temp_score += 1
            else:
                temp_score += 1
                break

            i += 1
            row = start_row + i * dx
            col = start_col + i * dy
        score *= temp_score

    return score


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        tree_heights = parse_input_to_matrix(problem_input)
        visible_trees = np.zeros(shape=tree_heights.shape)

        for k in range(4):
            rotated_tree_heights = np.rot90(tree_heights, k=k)
            rotated_visibility = check_visibility(rotated_tree_heights)
            direction_visible_trees = np.rot90(rotated_visibility, k=4 - k)
            visible_trees = np.maximum(visible_trees, direction_visible_trees)

        return int(np.sum(visible_trees))

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        tree_heights = parse_input_to_matrix(problem_input)
        nrow, ncol = tree_heights.shape
        max_score = 0
        for i in range(0, nrow):
            for j in range(0, ncol):
                score = compute_tree_score(tree_heights, i, j)
                max_score = max(max_score, score)

        return max_score


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
