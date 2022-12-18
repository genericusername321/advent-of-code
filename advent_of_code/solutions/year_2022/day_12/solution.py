from collections import deque
from pathlib import Path
from typing import Callable, Optional, Union

import numpy as np
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution


def parse_input(problem_input: str) -> np.ndarray:
    lines = problem_input.split()
    map_height, map_width = len(lines), len(lines[0])
    return np.fromiter("".join(lines), dtype="U1").reshape(map_height, map_width)


def BFS(
    graph: np.ndarray,
    starting_point: tuple,
    starting_point_height: str,
    end_point_value: str,
    end_point_height: str,
    condition: Callable,
) -> Optional[int]:

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    graph[starting_point] = starting_point_height

    visited = np.zeros(graph.shape)
    visited[starting_point] = 1

    depth = 0
    queue = deque()
    queue.append((starting_point, depth))

    while queue:
        (x, y), depth = queue.popleft()
        current_height = graph[x, y]
        for dx, dy in directions:
            new_position = (x + dx, y + dy)
            next_height = graph[new_position]

            if next_height == end_point_value and condition(
                end_point_height, current_height
            ):
                return depth + 1

            if condition(next_height, current_height) and not visited[new_position]:
                visited[new_position] = 1
                queue.append((new_position, depth + 1))


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int, None]:
        height_map = parse_input(problem_input)
        height_map = np.pad(height_map, [[1, 1], [1, 1]], constant_values="~")
        starting_point = tuple(map(int, np.where(height_map == "S")))

        nsteps = BFS(
            graph=height_map,
            starting_point=starting_point,
            starting_point_height="a",
            end_point_value="E",
            end_point_height="z",
            condition=lambda x, y: ord(x) - ord(y) <= 1,
        )
        return nsteps

    def solve_part_two(self, problem_input: str) -> Union[str, int, None]:
        height_map = parse_input(problem_input)
        height_map = np.pad(height_map, [[1, 1], [1, 1]], constant_values="A")
        height_map[np.where(height_map == "S")] = "a"

        return BFS(
            graph=height_map,
            starting_point=tuple(map(int, np.where(height_map == "E"))),
            starting_point_height="z",
            end_point_value="a",
            end_point_height="a",
            condition=lambda x, y: ord(x) - ord(y) >= -1,
        )


if __name__ == "__main__":
    input_file = Path(__file__).parent / "problem_input.txt"

    solution = Solution()
    res = solution.solve_part_one(input_file.read_text())
    print(res)

    res = solution.solve_part_two(input_file.read_text())
    print(res)
