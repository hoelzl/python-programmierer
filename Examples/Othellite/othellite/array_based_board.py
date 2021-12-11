from collections.abc import Sequence
from dataclasses import dataclass
import dataclasses
import reprlib

from .board import Board
from .direction import Direction
from .index import Index
from .field import Field
from .player import Player
from abc import ABC, abstractmethod


def _find_rightmost(seq: Sequence):
    for i in range(len(seq) - 1, -1, -1):
        if seq[i]:
            return i
    return 0


@dataclass
class FieldBasedBoard(Board):
    @abstractmethod
    @property
    def _fields(self) -> list[Field]:
        ...

    def __post_init__(self):
        self.initialize_center_fields()

    def resolve_index(self, index):
        if isinstance(index, Index):
            return index.to_linear_index()
        else:
            return index

    def __getitem__(self, index):
        return self._fields[self.resolve_index(index)]

    def __setitem__(self, index, value):
        self._fields[self.resolve_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result

    def _indices_to_flip_in_direction(
        self, p: Player, index: Index, d: Direction
    ) -> set[Index]:
        next_index = index.next_in_direction(d)
        occupied_indices = self._occupied_indices_in_direction(d, next_index)
        return self._select_indices_that_can_be_flipped(p, occupied_indices)

    def _occupied_indices_in_direction(self, d, index):
        occupied_indices = []
        while index.is_valid:
            if not self[index].is_occupied:
                break
            occupied_indices.append(index)
            index = index.next_in_direction(d)
        return occupied_indices

    def _select_indices_that_can_be_flipped(
        self, player: Player, non_empty_indices: list[Index]
    ) -> set[Index]:
        stop_index = self._find_highest_player_owned_index(player, non_empty_indices)
        return set(
            index
            for index in non_empty_indices[:stop_index]
            if self[index].is_owned_by_opponent_of(player)
        )

    def _find_highest_player_owned_index(
        self, player: Player, non_empty_indices: list[Index]
    ):
        """
        Find the highest i so that self[non_empty_indices[i]] is owned by player.

        When this function returns a value i, then only fields with index in
        non_empty_indices[:i] can potentially be flipped by the move that generated
        non_empty_indices. Therefore, we return 0 if no such i can be found, since
        this will correctly result in an empty list of fields to be flipped.
        """
        for i in range(len(non_empty_indices) - 1, -1, -1):
            if self[non_empty_indices[i]].is_owned_by_player(player):
                return i
        return 0

    def flips_field_in_any_direction(self, player: Player, index: Index) -> bool:
        for d in Direction:
            if self._indices_to_flip_in_direction(player, index, d):
                return True
        return False

    def is_valid_move(self, player: Player, index: Index) -> bool:
        result = not self.is_occupied(index) and self.flips_field_in_any_direction(
            index
        )
        return result

    def find_valid_moves(self, player: Player) -> set[Index]:
        result = set()
        for row in range(8):
            for column in range(8):
                move = (row, column)
                if self.is_valid_move(player, move):
                    result.add(move)
        return result

    def play_move(self, player: Player, index: Index) -> None:
        if self.is_valid_move(player, index):
            field = Field.LIGHT if player is Player.LIGHT else Field.DARK
            self[index] = field
            flipped_indices = self.find_flipped_indices(player, index)
            self.flip_indices(field, flipped_indices)
        else:
            raise ValueError(f"{index} is not a valid move")

    def find_flipped_indices(self, player: Player, index: Index) -> set[Index]:
        result = set()
        for d in Direction:
            result |= self._indices_to_flip_in_direction(player, index, d)
        return result

    def flip_indices(self, field: Field, flipped_indices: set[Index]) -> None:
        for index in flipped_indices:
            self[index] = field
