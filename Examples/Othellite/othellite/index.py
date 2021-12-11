from dataclasses import dataclass
from typing import Protocol
from abc import abstractmethod


class DirectionProtocol(Protocol):
    @property
    @abstractmethod
    def value(self) -> tuple[int, int]:
        ...


@dataclass(frozen=True, slots=True)
class Index:
    row: int
    column: int

    @property
    def is_valid(self) -> bool:
        return 0 <= self.row < 8 and 0 <= self.column < 8

    def next_in_direction(self, direction: DirectionProtocol) -> "Index":
        assert self.is_valid
        d_row, d_column = direction.value
        return Index(self.row + d_row, self.column + d_column)

    def to_linear_index(self) -> int:
        """
        Compute the corresponding linear index (based on an 8x8 grid).

        We assume the usual conventions for multidimensional indexing, i.e., the first
        index is the row, the second index the column. In other words, this function
        should return the same value as
        `numpy.ravel_multi_index((self.row, self.column), (8, 8))`.
        """
        return self.row * 8 + self.column

    def to_2d_index(self) -> tuple[int, int]:
        return self.row, self.column
