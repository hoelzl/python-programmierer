from .index import Index
from .field import Field
from .player import Player
from abc import ABC, abstractmethod
from typing import overload


class Board(ABC):
    NUM_ROWS = 8
    NUM_COLS = 8

    @overload
    def __getitem__(self, index: Index) -> Field:
        ...

    @overload
    def __getitem__(self, index: tuple[int, int]) -> Field:
        ...

    @abstractmethod
    def __getitem__(self, index):
        ...

    @overload
    def __setitem__(self, index: Index, value: Field) -> None:
        ...

    @overload
    def __setitem__(self, index: tuple[int, int], value: Field) -> None:
        ...

    @abstractmethod
    def __setitem__(self, key, value) -> None:
        ...

    def initialize_center_fields(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def is_occupied(self, index: Index):
        return self[index].is_occupied

    @abstractmethod
    def is_valid_move(self, player: Player, index: Index) -> bool:
        ...

    @abstractmethod
    def find_valid_moves(self, player: Player) -> set[Index]:
        ...

    @abstractmethod
    def play_move(self, player: Player, index: Index) -> None:
        ...

    @abstractmethod
    def find_flipped_indices(self, player: Player, index: Index) -> set[Index]:
        ...

    @abstractmethod
    def flip_indices(self, field: Field, flipped_indices: set[Index]) -> None:
        ...
