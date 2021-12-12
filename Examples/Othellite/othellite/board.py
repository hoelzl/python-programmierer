from .position import Position
from .field import Field
from .player import Player
from abc import ABC, abstractmethod
from typing import overload, Iterable


class Board(ABC):
    NUM_ROWS = 8
    NUM_COLS = 8

    @overload
    def __getitem__(self, index: Position) -> Field:
        ...

    @overload
    def __getitem__(self, index: tuple[int, int]) -> Field:
        ...

    @abstractmethod
    def __getitem__(self, index):
        ...

    @overload
    def __setitem__(self, index: Position, value: Field) -> None:
        ...

    @overload
    def __setitem__(self, index: tuple[int, int], value: Field) -> None:
        ...

    @abstractmethod
    def __setitem__(self, key, value) -> None:
        ...

    @staticmethod
    def positions() -> Iterable[Position]:
        """
        Return an iterable over the board's position
        :return: An iterable that returns the positions, columns move fastest
        """
        return (
            Position(row=row, column=col)
            for row in range(Board.NUM_ROWS)
            for col in range(Board.NUM_COLS)
        )

    def initialize_center_fields(self) -> None:
        """
        Sets the center fields to their initial values.

        Does not change any other fields of the board.
        """
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def is_empty(self, pos: Position) -> bool:
        """
        Checks whether a position on the board is empty.

        :param pos: The position to check.
        :return: True if the position is empty, false otherwise.
        """
        return self[pos].is_empty

    def is_occupied(self, pos: Position) -> bool:
        """
        Checks whether a position on the board is occupied.

        :param pos: The position to check.
        :return: True if the position is occupied, false otherwise.
        """
        return self[pos].is_occupied

    @abstractmethod
    def is_valid_move(self, player: Player, pos: Position) -> bool:
        """
        Checks whether a move is valid.

        :param player: The player performing the move.
        :param pos:
        :return:
        """
        ...

    @abstractmethod
    def find_valid_moves(self, player: Player) -> set[Position]:
        """
        Computes all valid moves for a player.

        :param player: The player performing the move
        :return: The set of all positions on which player could place a disk
        """
        ...

    @abstractmethod
    def play_move(self, player: Player, pos: Position) -> None:
        """
        Places a disk at a given position, flips the captured disks.
        :param player: The player performing the move
        :param pos: The position on which the disk is placed
        """
        ...
