from enum import Enum
from .player import Player


class Field(Enum):
    EMPTY = "\N{Open Box}"
    LIGHT = "\N{Medium White Circle}"
    DARK = "\N{Medium Black Circle}"

    @staticmethod
    def for_player(player: Player):
        if player is Player.LIGHT:
            return Field.LIGHT
        else:
            return Field.DARK

    @property
    def is_empty(self) -> bool:
        return self is Field.EMPTY

    @property
    def is_occupied(self) -> bool:
        return not self.is_empty

    def is_owned_by_opponent_of(self, p: Player) -> bool:
        if p is Player.DARK:
            return self is Field.LIGHT
        else:
            return self is Field.DARK

    def is_owned_by_player(self, p: Player) -> bool:
        return self.is_occupied and not self.is_owned_by_opponent_of(p)
