from collections import deque
from typing import List, Union
from advent_of_code.aoc.prepare_solution.base_solution import BaseSolution

Matrix = List[List[int]]


def parse_input(problem_input: str) -> Matrix:
    lines = problem_input.split("\n")
    heights = [list(map(int, list(line))) for line in lines if line]

    # Pad the sides of the height map with 0s
    width = len(heights[0])
    pad = [[9] * width]
    heights = pad + heights + pad
    heights = [[9] + row + [9] for row in heights]
    return heights


class Solution(BaseSolution):
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        height_map = parse_input(problem_input)

        # Find the sum of the local minima
        total = 0
        height, width = len(height_map), len(height_map[0])
        for row in range(1, height - 1):
            for col in range(1, width - 1):
                current = height_map[row][col]
                if (
                    current < height_map[row - 1][col]
                    and current < height_map[row][col - 1]
                    and current < height_map[row + 1][col]
                    and current < height_map[row][col + 1]
                ):
                    total += current + 1
        return total

    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        height_map = parse_input(problem_input)

        # Create map of visited locations
        # Locations of height 9 are not part of any basin, so mark those as visited
        height, width = len(height_map), len(height_map[0])
        visited = [[0] * width for _ in range(height)]
        for row in range(height):
            for col in range(width):
                if height_map[row][col] == 9:
                    visited[row][col] = 2

        # Use DFS to find the components and their respective size
        def dfs(start_row: int, start_col: int) -> int:
            if visited[start_row][start_col] == 2:
                return 0

            size = 0
            stack = deque()
            stack.append((start_row, start_col))

            while stack:
                row, col = stack.pop()
                size += 1
                visited[row][col] = 2

                directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for dy, dx in directions:
                    new_row = row + dy
                    new_col = col + dx
                    if visited[new_row][new_col] == 0:
                        stack.append((new_row, new_col))
                        visited[new_row][new_col] = 1

            return size

        # We can be assured that this approach is correct, for every location of height
        # 8 or lower is part of exactly one basin
        component_size = []
        for row in range(1, height - 1):
            for col in range(1, width - 1):
                component_size.append(dfs(row, col))

        component_size.sort(reverse=True)
        return component_size[0] * component_size[1] * component_size[2]
