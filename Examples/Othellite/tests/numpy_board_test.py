import pytest

from othellite.numpy_board import NumPyBoard
from board_test import AbstractBoardTests, setup_board_for_tests


@pytest.fixture
def initial_board():
    return NumPyBoard()


@pytest.fixture
def board():
    result = NumPyBoard()
    setup_board_for_tests(result)
    return result


class TestNumPyBoard(AbstractBoardTests):
    pass
