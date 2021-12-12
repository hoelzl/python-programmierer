import pytest

from othellite.board import Board
from othellite.field import Field
from othellite.numpy_board import NumPyBoard
from board_test import AbstractBoardTests, setup_board_for_tests


@pytest.fixture
def board():
    result = NumPyBoard()
    setup_board_for_tests(result)
    return result


class TestNumPyBoard(AbstractBoardTests):
    pass
