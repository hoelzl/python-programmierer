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
        # If we are passed a tuple, we convert it into a Position and back to a 2d
        # index to get error checking for out-of-bounds indices. Otherwise negative
        # indices would index from the end of the array. This keeps NumPy boards
        # consistent with boards that use linear indexing at the cost of a few
        # more memory allocations.
        if isinstance(pos, tuple):
            return Position(*pos).to_2d_index()
        elif isinstance(pos, Position):
            return pos.to_2d_index()
        else:
            return pos
