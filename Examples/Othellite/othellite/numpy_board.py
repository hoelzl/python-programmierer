from .field_based_board import FieldBasedBoard
from dataclasses import dataclass
import dataclasses
import numpy as np

from .board import Board
from .field import Field
from .position import Position


@dataclass()
class NumPyBoard(FieldBasedBoard):
    _fields: np.ndarray = dataclasses.field(
        default_factory=lambda: np.array(
            [[Field.EMPTY] * Board.NUM_COLS] * Board.NUM_ROWS
        )
    )

    def resolve_position(self, pos):
        # We convert to Position and back to 2d index if we are passed a tuple
        # get error checking for negative indices. This makes NumPy boards consistent
        # with boards that use linear indexing.
        if isinstance(pos, tuple):
            return Position(*pos).to_2d_index()
        elif isinstance(pos, Position):
            return pos.to_2d_index()
        else:
            return pos
