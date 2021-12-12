import pytest

from othellite.board import Board
from othellite.field import Field
from othellite.list_board import ListBoard
from board_test import AbstractBoardTests, setup_board_for_tests


@pytest.fixture
def board():
    result = ListBoard()
    setup_board_for_tests(result)
    return result


class TestListBoard(AbstractBoardTests):
    pass
