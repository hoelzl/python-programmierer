from abc import ABC, abstractmethod

import pytest

from othellite.board import Board
from othellite.field import Field
from othellite.player import Player
from othellite.position import Position


def setup_board_for_tests(board) -> None:
    """
    Initialize a board so that
    - all fields in [0, :4] are not empty,
    - some fields in the range [:5, :5] are not empty, some are, and
    - all fields in [5:, 5:] are empty.

    :param board: The board to initialize.
    """
    for pos in [(0, 0), (1, 1)]:
        board[pos] = Field.DARK
    for pos in [(0, 1), (0, 2), (0, 3)]:
        board[pos] = Field.LIGHT


# noinspection PyMethodMayBeStatic
class AbstractBoardTests:
    def test_2d_indexing_with_tuples(self, board: Board):
        assert board[0, 0] == Field.DARK
        assert board[0, 1] == Field.LIGHT
        assert board[0, 2] == Field.LIGHT
        assert board[0, 3] == Field.LIGHT
        assert board[0, 4] == Field.EMPTY
        assert board[1, 0] == Field.EMPTY
        assert board[1, 1] == Field.DARK
        assert board[1, 2] == Field.EMPTY

        for pos in [(-1, 3), (6, -1), (2, 8), (8, 7)]:
            with pytest.raises(ValueError):
                board[pos]

    def test_2d_indexing_with_positions(self, board: Board):
        # Swap the light and dark fields, since the default setup method uses
        # tuple-based indexing.
        for pos in [(0, 0), (1, 1)]:
            board[Position(*pos)] = Field.LIGHT
        for pos in [(0, 1), (0, 2), (0, 3)]:
            board[Position(*pos)] = Field.DARK

        assert board[0, 0] == Field.LIGHT
        assert board[0, 1] == Field.DARK
        assert board[0, 2] == Field.DARK
        assert board[0, 3] == Field.DARK
        assert board[0, 4] == Field.EMPTY
        assert board[1, 0] == Field.EMPTY
        assert board[1, 1] == Field.LIGHT
        assert board[1, 2] == Field.EMPTY

        for pos in [(-1, 3), (6, -1), (2, 8), (8, 7)]:
            with pytest.raises(ValueError):
                board[Position(*pos)]

    def test_conversion_to_string(self, board: Board):
        assert str(board) == (
            "|⚫|⚪|⚪|⚪|␣|␣|␣|␣|\n"
            "|␣|⚫|␣|␣|␣|␣|␣|␣|\n"
            "|␣|␣|␣|␣|␣|␣|␣|␣|\n"
            "|␣|␣|␣|⚫|⚪|␣|␣|␣|\n"
            "|␣|␣|␣|⚪|⚫|␣|␣|␣|\n"
            "|␣|␣|␣|␣|␣|␣|␣|␣|\n"
            "|␣|␣|␣|␣|␣|␣|␣|␣|\n"
            "|␣|␣|␣|␣|␣|␣|␣|␣|"
        )

    def test_is_empty(self, board: Board):
        assert board[6, 6].is_empty
        assert not board[0, 0].is_empty

    def test_is_occupied(self, board: Board):
        assert board[0, 0].is_occupied
        assert not board[6, 6].is_occupied

    def test_is_valid_move_against_initial_board(self, initial_board: Board):
        def assert_valid_moves(player, valid_positions):
            for pos in initial_board.positions():
                result = initial_board.is_valid_move(player, pos)
                if pos.to_2d_index() in valid_positions:
                    assert result, f"Move {pos} should be valid."
                else:
                    assert not result, f"Move {pos} should not be valid."

        light_moves = {(2, 3), (3, 2), (4, 5), (5, 4)}
        dark_moves = {(2, 4), (3, 5), (4, 2), (5, 3)}

        assert_valid_moves(Player.LIGHT, light_moves)
        assert_valid_moves(Player.DARK, dark_moves)

    def test_is_valid_move_against_border_pieces(self, board: Board):
        """
        Test whether the valid positions in the upper left corner of the board are
        recognized correctly. The board looks like this:

          0 |⚫|⚪|⚪|⚪|␣|
          1 |␣|⚫|␣|␣|␣|
          2 |␣|␣|␣|␣|␣|

          so the light player has moves (2, 0) and (2, 1), the dark player has move
          (0, 4).
        """

        # We remove some center pieces that might lead to valid moves against the
        # center.
        board[3, 3] = Field.EMPTY
        board[3, 4] = Field.EMPTY

        valid_moves = {
            (Player.LIGHT, Position(2, 0)),
            (Player.LIGHT, Position(2, 1)),
            (Player.DARK, Position(0, 4)),
        }

        all_positions = set(Position(row, col) for row in range(3) for col in range(5))
        invalid_light_moves = all_positions - {Position(2, 0), Position(2, 1)}
        invalid_dark_moves = all_positions - {Position(0, 4)}

        for player, pos in valid_moves:
            assert board.is_valid_move(player, pos)

        for pos in invalid_light_moves:
            assert not board.is_valid_move(Player.LIGHT, pos), f"Cannot play {pos}."

        for pos in invalid_dark_moves:
            assert not board.is_valid_move(Player.DARK, pos), f"Cannot play {pos}."

    def test_find_valid_moves_against_initial_board(self, initial_board: Board):
        light_moves = set(Position(*pos) for pos in {(2, 3), (3, 2), (4, 5), (5, 4)})
        dark_moves = set(Position(*pos) for pos in {(2, 4), (3, 5), (4, 2), (5, 3)})

        assert initial_board.find_valid_moves(Player.LIGHT) == light_moves
        assert initial_board.find_valid_moves(Player.DARK) == dark_moves

    def test_play_move_white_2_3_against_initial_board(self, initial_board: Board):
        # TODO: Implement a nice way to input boards in different configurations.
        # Otherwise these tests will be pretty unreadable.
        pass
