from abc import ABC, abstractmethod
from othellite.board import Board
from othellite.field import Field


def setup_board_for_tests(board):
    for pos in [(0, 0), (0, 2), (1, 1)]:
        board[pos] = Field.DARK
    for pos in [(0, 1), (0, 3)]:
        board[pos] = Field.LIGHT


# noinspection PyMethodMayBeStatic
class AbstractBoardTests:
    def test_indexing_for_default_board(self, board: Board):
        assert board[0, 0] == Field.DARK
