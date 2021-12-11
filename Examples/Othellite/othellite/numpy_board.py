from .array_based_board import FieldBasedBoard
from dataclasses import dataclass
import dataclasses
import numpy as np

from .board import Board
from .field import Field
from .index import Index


@dataclass()
class NumPyBoard(FieldBasedBoard):
    _fields: np.ndarray = dataclasses.field(
        default_factory=lambda: np.array(
            [[Field.EMPTY] * Board.NUM_COLS] * Board.NUM_ROWS
        )
    )

    def resolve_index(self, index):
        if isinstance(index, Index):
            return index.to_2d_index()
        else:
            return index
