from abc import ABC, abstractmethod
from typing import Union


class BaseSolution(ABC):
    """Interface definition for solution class"""

    @abstractmethod
    def solve_part_one(self, problem_input: str) -> Union[str, int]:
        return NotImplementedError

    @abstractmethod
    def solve_part_two(self, problem_input: str) -> Union[str, int]:
        return NotImplementedError
