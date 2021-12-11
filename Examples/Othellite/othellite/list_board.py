from .array_based_board import FieldBasedBoard
from dataclasses import dataclass
import dataclasses
import numpy as np

from .board import Board
from .field import Field
from .index import Index


@dataclass()
class ListBoard(FieldBasedBoard):
    _fields: list[Field] = dataclasses.field(default_factory=lambda: [Field.EMPTY] * 64)

    def resolve_index(self, index):
        if isinstance(index, Index):
            return index.to_2d_index()
        else:
            return index
