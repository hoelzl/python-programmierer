# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Case Study: Othellite") }}


# %%
from collections import Sequence
from enum import Enum
from dataclasses import dataclass, field
import reprlib
from typing import Union
from random import sample

try:
    import numpy as np
except ModuleNotFoundError:
    print("NumPy not found, some (minor) examples may not work")


# %% [markdown]
#
# # Othellite
#
# Im Folgenden wollen wir eine vereinfachte Variante des Spiels Reversi (auch
# unter dem Handelsnamen Othello bekannt) implementieren. Das Spiel wird auf
# einem Brett mit 8x8 Feldern gespielt, auf die Spieler schwarze oder
# weiße Spielsteine legen können. Die genauen Regeln sind
# [im Wikipedia Artikel](https://de.wikipedia.org/wiki/Othello_(Spiel))
# beschrieben.

# %% [markdown]
#
# Wir definieren eine Enumeration, die den Zustand eines einzelnen Feldes auf
# dem Brett beschreibt:

# %% tags=["code-along"]
class Field(Enum):
    EMPTY = "\N{Open Box}"
    LIGHT = "\N{Medium White Circle}"
    DARK = "\N{Medium Black Circle}"


# %%
print("Fields:           ", list(Field))
print("Empty field:      ", Field.DARK)
print("Light field:      ", Field.LIGHT)
print("Dark field:       ", Field.DARK)
print("Light field value:", Field.LIGHT.value)
print("Light field name: ", Field.LIGHT.name)


# %% [markdown]
#
# ## Micro-Workshop
#
# Definieren Sie eine Funktion `is_occupied(f: Field) -> bool`,
# die genau dann `True` zurückgibt, wenn `field` nicht leer ist.


# %%
def is_occupied(f: Field) -> bool:
    return f is not Field.EMPTY


# %%
assert is_occupied(Field.DARK)
assert is_occupied(Field.LIGHT)
assert not is_occupied(Field.EMPTY)


# %% [markdown]
#
# ## Micro-Workshop
#
# Definieren Sie eine Enumeration `Player`, die analog zu `Field` die beiden
# Spieler beschreibt. Drucken Sie ähnlich wie für `Field` die möglichen Werte
# sowie Value und Namen für einen Enum-Wert aus.


# %% tags=["code-along"]
class Player(Enum):
    LIGHT = 0
    DARK = 1


# %% tags=["code-along"]
print("Players:           ", list(Player))
print("Light player:      ", Player.LIGHT)
print("Dark player:       ", Player.DARK)
print("Light player value:", Player.LIGHT.value)
print("Light player name: ", Player.LIGHT.name)


# %% [markdown]
#
# ## Micro-Workshop
#
# Definieren Sie eine Funktion
# `is_field_owned_by_opponent(p: Player, f: Field) -> bool`,
# die genau dann `True` zurückgibt, wenn der Spielstein auf Feld `f` dem
# Gegner gehört, d.h., wenn `f` belegt ist und der Stein auf `f` nicht die
# gleiche Farbe hat wie der Spieler.
#
# Überprüfen Sie, dass Ihre Implementierung die angegebenen Assertions erfüllt.
#
# Implementieren Sie eine entsprechende Methode `is_field_owned_by_player()`.

# %% tags=["code-along"]
def is_field_owned_by_opponent(p: Player, f: Field) -> bool:
    if p is Player.DARK:
        return f is Field.LIGHT
    else:
        return f is Field.DARK


# %%
assert is_field_owned_by_opponent(Player.LIGHT, Field.DARK)
assert is_field_owned_by_opponent(Player.DARK, Field.LIGHT)
assert not is_field_owned_by_opponent(Player.DARK, Field.DARK)
assert not is_field_owned_by_opponent(Player.DARK, Field.EMPTY)
assert not is_field_owned_by_opponent(Player.LIGHT, Field.LIGHT)
assert not is_field_owned_by_opponent(Player.LIGHT, Field.EMPTY)


# %% tags=["code-along"]
def is_field_owned_by_player(p: Player, f: Field) -> bool:
    if p is Player.DARK:
        return f is Field.DARK
    else:
        return f is Field.LIGHT


# %%
assert is_field_owned_by_player(Player.LIGHT, Field.LIGHT)
assert is_field_owned_by_player(Player.DARK, Field.DARK)
assert not is_field_owned_by_player(Player.DARK, Field.LIGHT)
assert not is_field_owned_by_player(Player.DARK, Field.EMPTY)
assert not is_field_owned_by_player(Player.LIGHT, Field.DARK)
assert not is_field_owned_by_player(Player.LIGHT, Field.EMPTY)


# %% [markdown]
#
# Wir wollen auf die einzelnen Felder eines 8x8 Spielfelds mittels eines
# zweidimensionalen Index-Werts zugreifen: `board[0, 0]` steht für das linke
# obere Feld, `board[0, 1]` für das Feld rechts daneben, usw.
#
# Das ist einfach, wenn wir ein zweidimensionales Array als zugrunde liegende
# Datenstruktur verwenden können, z.B. das `ndarray` von NumPy. In diesem Fall
# delegieren wir einfach `__getitem__()` und `__setitem__()` an die
# entsprechenden Methoden des NumPy Arrays.
#
# Die mittleren 4 Felder des Spielfelds initialisieren wir mit diagonal
# angeordneten Steinen.
#
# <!--
# We want to be able to access the individual fields of the 8x8 board using
# a 2-dimensional index notation: `board[0, 0]` for the field in the upper
# left corner, `board[0, 1]` for the field to the right of the upper left
# corner, etc.
#
# This is easy when using a two-dimensional array, such as NumPy's `ndarray`.
# We simply need to delegate the `__getitem__()` and `__setitem__()` methods
# to the NumPy array:
# -->

# %% tags=["code-along"]
@dataclass()
class NumPyBoard:
    _fields: np.array = field(default_factory=lambda: np.array([[Field.EMPTY] * 8] * 8))

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, item) -> Union[Field, np.ndarray]:
        return self._fields[item]

    def __setitem__(self, key, value) -> None:
        self._fields[key] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row_index in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row_index, col].value) + "|"
            prefix = "\n|"
        return result


# %% tags=["code-along"]
npb = NumPyBoard()
npb[0, 0] = Field.DARK
npb[0, 1] = Field.LIGHT
print(npb)

# %% [markdown]
#
# Dadurch, dass der Index an das NumPy Array weitergereicht wird, stehen auch
# mächtigere Zugriffsvarianten, wie z.B. Slicing zur Verfügung:

# %%
npb[0, 2:] = Field.DARK
npb[1:3, 1:3] = Field.LIGHT
print(npb)


# %%
# ## Mini-Workshop Compute Linear Index
#
# Wenn wir eine Python Liste als Speicher für das Spielfeld verwenden wollen,
# müssen wir die Umrechnung von zweidimensionalen Index-Werten in einen
# eindimensionalen Index selber vornehmen.
#
# Das geht indem wir für eine Position `(r, c)` den Wert `r * 8 + c` berechnen.
# Für den Fall, dass einer der Indices nicht `>= 0` und `< 8` ist soll eine
# geeignete Exception ausgelöst werden.
#
# Implementieren Sie eine Funktion `compute_linear_index()` die diese Aufgabe
# übernimmt.


# %% tags=["code-along"]
def compute_linear_index(index):
    """
    Compute the linear index for the given (possibly complex) index.

    If `index` is already a linear index or sliced it is returned unchanged.
    If it is a pair of numbers, each between 0 and 7, the corresponding
    linear index into an 8x8 grid is computed, using the usual conventions
    for multidimensional indexing, i.e., the first index is the row, the
    second index the column.

    (For a real application this function should probably be extended to
    convert 2-dimensional slices into 1-dimensional slices as well, but that
    is too complex for this example.)

    :param index: A linear index, a pair of indices or a linear slice
    :return: A linear index or slice
    """
    try:
        row, column = index
        if 0 <= row <= 7:
            raise ValueError(f"Row index {row} out of range.")
        if 0 <= column <= 7:
            raise ValueError("Column index out of range.")
        return row * 8 + column
    except TypeError:
        return index


# %% [markdown]
#
# ## Mini-Workshop
#
# Implementieren Sie eine Klasse `Board`, die ein 8x8 Othellite Brett
# repräsentiert, das den Zustand des Bretts in einer Liste speichert.
# Sie können sich bei der Implementierung an der Klasse `NumPyBoard`
# orientieren, und `compute_linear_index` zur Berechnung von Index-Werten
# verwenden.


# %% tags=["code-along"]
@dataclass(repr=False)
class Board:
    _fields: list[Field] = field(default_factory=lambda: [Field.EMPTY] * 64)

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, index) -> Field:
        return self._fields[compute_linear_index(index)]

    def __setitem__(self, index, value):
        self._fields[compute_linear_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result


# %% tags=["code-along"]
board = Board()
board[0, 0] = Field.DARK
board[0, 2] = Field.DARK
board[0, 1] = Field.LIGHT
print(str(board))
board[:3]


# %% [markdown]
#
# Wir definieren eine weitere Enumeration für "Himmelsrichtungen". Die
# Schlüssel der Enumeration sollen Abkürzungen für die Kompassrichtungen (N,
# NE, E, ...) sein. Als Wert soll jeweils der zur Bewegung in diese Richtung
# benötigte "Offset" verwendet werden:
#
# - `(-1, 0)` für eine Bewegung in Richtung Norden,
# - `(0, 1)` für eine Bewegung in Richtung Osten,
# - `(1, 0)` für eine Bewegung in Richtung Süden,
# - `(0, -1)` für eine Bewegung in Richtung Westen,
# - `(-1, 1)` für eine Bewegung in Richtung Nord-Osten,
# - `(1, 1)` für eine Bewegung in Richtung Süd-Osten,
# - `(-1, -1)` für eine Bewegung in Richtung Nord-Westen,
# - `(1, -1` für eine Bewegung in Richtung Süd-Westen.
#
# <!--
# We define yet another enumeration, this time for directions.
# The keys of this enumeration should be the compass directions (N, NE, E, ...),
# the values should be the (x, y) offset to move to this field in a
# right-handed coordinate system, i.e.,
# - `(-1, 0)` for moving north,
# - `(0, 1)` for moving east,
# - `(1, 0)` for moving south,
# - `(0, -1)` for moving west,
# - `(-1, 1)` for moving north-east,
# - `(1, 1)` for moving south-east,
# - `(-1, -1)` for moving north-west,
# - `(1, -1` for moving south-west.
# -->

# %% [markdown]
#
# ## Micro-Workshop
#
# Definieren Sie eine Enumeration `Directions`, wie gerade beschrieben.

# %% tags=["code-along"]
class DirectionV0(Enum):
    N = (-1, 0)
    NE = (-1, 1)
    E = (0, 1)
    SE = (1, 1)
    S = (1, 0)
    SW = (1, -1)
    W = (0, -1)
    NW = (-1, -1)


# %% [markdown]
# Es ist bei Enumerationen möglich, mehrere Schlüssel für den gleichen Wert
# zu definieren (also gewissermaßen Synonyme anzugeben).


class Synonyms(Enum):
    DRINK = 0
    BEVERAGE = 0
    FOOD = 1
    BIG = 2
    LARGE = 2
    SMALL = 3


# %%
print(Synonyms.DRINK is Synonyms.BEVERAGE)
print(Synonyms.DRINK is not Synonyms.FOOD)
print(Synonyms.BIG is Synonyms.LARGE)
print(Synonyms.BIG is not Synonyms.SMALL)


# %% [markdown]
#
# Erweitern Sie die Enumeration `Directions` so, dass auch die vollständigen
# Namen der Kompassrichtungen (`NORTH`, `NORTH_EAST`, ...) verwendet werden
# können.


# %% tags=["code-along"]
class Direction(Enum):
    # Abbreviated names
    N = (-1, 0)
    NE = (-1, 1)
    E = (0, 1)
    SE = (1, 1)
    S = (1, 0)
    SW = (1, -1)
    W = (0, -1)
    NW = (-1, -1)
    # Full names as aliases
    NORTH = (-1, 0)
    NORTH_EAST = (-1, 1)
    EAST = (0, 1)
    SOUTH_EAST = (1, 1)
    SOUTH = (1, 0)
    SOUTH_WEST = (1, -1)
    WEST = (0, -1)
    NORTH_WEST = (-1, -1)


# %% [markdown]
#
# ## Micro-Workshop
#
# Überprüfen Sie, dass die Abkürzungen und die vollständigen Name die
# gleichen Werte repräsentieren.
# <!--
# Ensure that the abbreviated names and the full names denote the
# same values.
# -->

# %% tags=["code-along"]
assert Direction.N is Direction.NORTH
assert Direction.NE is Direction.NORTH_EAST
assert Direction.E is Direction.EAST
assert Direction.SE is Direction.SOUTH_EAST
assert Direction.S is Direction.SOUTH
assert Direction.SW is Direction.SOUTH_WEST
assert Direction.W is Direction.WEST
assert Direction.NW is Direction.NORTH_WEST

# %% tags=["code-along"]
print("Direction[0:3]: ", list(Direction)[:3])
print("Direction values:", [d.value for d in Direction])
print("Direction names: ", [d.name for d in Direction])

# %%
Index = tuple[int, int]


# %% [markdown]
#
# Micro-Workshop
#
# Schreiben Sie eine Funktion `is_valid_index(index: Index) -> bool`,
# die genau dann `True` zurückgibt, wenn `index` ein gültiger Index für
# ein Othellite Brett ist, andernfalls `False`. Überprüfen Sie, ob Ihre
# Implementierung die Assertions erfüllt

# %% tags=["code-along"]
def is_valid_index(index: Index) -> bool:
    row, column = index
    return 0 <= row < 8 and 0 <= column < 8


# %%
assert is_valid_index((0, 7))
assert not is_valid_index((8, 1))
assert not is_valid_index((1, 8))
assert not is_valid_index((6, -1))
assert not is_valid_index((-2, 4))


# %% [markdown]
# ## Micro-Workshop
#
# Schreiben Sie eine Funktion
# `assert_valid_index(index: Index) -> None:`, die eine Exception vom
# Typ `IndexError` mit einer geeigneten Fehlermeldung auslöst, wenn `index`
# kein gültiger Index für ein Othellite-Brett ist. Überprüfen Sie, dass die
# Funktion für korrekte Argumente keinen Exception auslöst, dass sie aber für
# verschiedene Fehlerfälle eine Exception auslöst.


# %% tags=["code-along"]
def assert_valid_index(index: Index) -> None:
    def assert_component_in_range(value: int, component: str):
        if value < 0 or value >= 8:
            raise IndexError(f"{component} component of index {index} out or range.")

    x, y = index
    assert_component_in_range(x, "First")
    assert_component_in_range(y, "Second")


# %% tags=["code-along"]
assert_valid_index((2, 0))

# %% tags=["code-along"]
try:
    assert_valid_index((-1, 3))
except IndexError as err:
    print(err)

# %% tags=["code-along"]
try:
    assert_valid_index((1, 8))
except IndexError as err:
    print(err)


# %% [markdown]
#
# Schreiben Sie eine Funktion
# `next_index_in_direction(index: Index, direction: Direction)`,
# die zwei Werte zurückgibt, falls `index` ein gültiger Index ist:
# - den nächsten Index in Richtung `direction` und
# - `True` oder `False`, je nachdem ob der nächste Index gültig ist oder nicht.
# Falls `index` kein gültiger Index ist soll eine Exception vom Typ
# `IndexError` ausgelöst werden.
#
# *Hinweis:* Die Werte, die zu den Komponenten von `index` addiert werden
# müssen können Sie mittels `d_row, d_column = direction.value` berechnen.
#
# Überprüfen Sie, ob Ihre Implementierung die angegebenen Assertions erfüllt.


# %% tags=["code-along"]
def next_index_in_direction(index: Index, direction: Direction):
    assert_valid_index(index)
    row, column = index
    d_row, d_column = direction.value
    next_index = (row + d_row, column + d_column)
    return next_index, is_valid_index(next_index)


# %%
assert next_index_in_direction((0, 0), Direction.N) == ((-1, 0), False)
assert next_index_in_direction((0, 0), Direction.NE) == ((-1, 1), False)
assert next_index_in_direction((0, 0), Direction.E) == ((0, 1), True)
assert next_index_in_direction((0, 0), Direction.SE) == ((1, 1), True)
assert next_index_in_direction((0, 0), Direction.S) == ((1, 0), True)
assert next_index_in_direction((0, 0), Direction.SW) == ((1, -1), False)
assert next_index_in_direction((0, 0), Direction.W) == ((0, -1), False)
assert next_index_in_direction((0, 0), Direction.NW) == ((-1, -1), False)

# %%
assert next_index_in_direction((4, 5), Direction.N) == ((3, 5), True)
assert next_index_in_direction((4, 5), Direction.NE) == ((3, 6), True)
assert next_index_in_direction((4, 5), Direction.E) == ((4, 6), True)
assert next_index_in_direction((4, 5), Direction.SE) == ((5, 6), True)
assert next_index_in_direction((4, 5), Direction.S) == ((5, 5), True)
assert next_index_in_direction((4, 5), Direction.SW) == ((5, 4), True)
assert next_index_in_direction((4, 5), Direction.W) == ((4, 4), True)
assert next_index_in_direction((4, 5), Direction.NW) == ((3, 4), True)

# %%
assert next_index_in_direction((7, 7), Direction.N) == ((6, 7), True)
assert next_index_in_direction((7, 7), Direction.NE) == ((6, 8), False)
assert next_index_in_direction((7, 7), Direction.E) == ((7, 8), False)
assert next_index_in_direction((7, 7), Direction.SE) == ((8, 8), False)
assert next_index_in_direction((7, 7), Direction.S) == ((8, 7), False)
assert next_index_in_direction((7, 7), Direction.SW) == ((8, 6), False)
assert next_index_in_direction((7, 7), Direction.W) == ((7, 6), True)
assert next_index_in_direction((7, 7), Direction.NW) == ((6, 6), True)

# %%
try:
    next_index_in_direction((7, 8), Direction.S)
except IndexError as err:
    print(err)


# %% [markdown]
#
# Wir wollen unsere Klasse `Board` jetzt um eine Methode
#
# ```
# _fields_flipped_in_direction(self, p: Player, index: Index,
#                              d: Direction) -> set[Index]
# ```
#
# erweitern, die die Indizes aller Felder zurückgibt, die der Spieler ausgehend
# vom Feld `index` in Richtung `d` umdrehen kann.

# %% tags=["code-along"]
# This is very specific to the use in `Board`...
def _find_rightmost(seq: Sequence):
    for i in range(len(seq) - 1, -1, -1):
        if seq[i]:
            return i
    return 0


# %%
assert _find_rightmost([True, False, True, False]) == 2
assert _find_rightmost([False, False, False]) == 0


# %% tags=["code-along"]
@dataclass(repr=False)
class Board:
    _fields: list[Field] = field(default_factory=lambda: [Field.EMPTY] * 64)

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, index) -> Field:
        return self._fields[compute_linear_index(index)]

    def __setitem__(self, index, value):
        self._fields[compute_linear_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result

    def _indices_that_can_be_flipped(
        self, player: Player, occupied_indices: list[Index]
    ) -> set[Index]:
        is_self_owned_field = [
            is_field_owned_by_player(player, self[index]) for index in occupied_indices
        ]
        stop_index = _find_rightmost(is_self_owned_field)
        return set(
            index
            for index in occupied_indices[:stop_index]
            if is_field_owned_by_opponent(player, self[index])
        )

    def _indices_to_flip_in_direction(
        self, p: Player, index: Index, d: Direction
    ) -> set[Index]:
        next_index, is_valid = next_index_in_direction(index, d)
        occupied_indices = []
        while is_valid:
            if not is_occupied(self[next_index]):
                break
            occupied_indices.append(next_index)
            next_index, is_valid = next_index_in_direction(next_index, d)
        return self._indices_that_can_be_flipped(p, occupied_indices)


# %%
def assert_flips_direction(player, index, directions):
    board = Board()
    board[index] = Field.LIGHT if player == Player.LIGHT else Field.DARK
    print(f"Player {player} at {index} flips {directions}.")
    print(board)

    for d in set(Direction) - directions:
        # noinspection PyProtectedMember
        result = board._indices_to_flip_in_direction(player, index, d)
        assert result == set(), f"Fields flipped in {d} are not empty."

    for d in directions:
        # noinspection PyProtectedMember
        result = board._indices_to_flip_in_direction(player, index, d)
        assert result != set(), f"Fields flipped in {d} are empty."


# %%
assert_flips_direction(Player.LIGHT, (0, 0), set())
assert_flips_direction(Player.LIGHT, (2, 3), {Direction.S})
assert_flips_direction(Player.LIGHT, (3, 2), {Direction.E})
assert_flips_direction(Player.LIGHT, (4, 5), {Direction.W})
assert_flips_direction(Player.LIGHT, (5, 2), set())
assert_flips_direction(Player.LIGHT, (5, 3), set())
assert_flips_direction(Player.LIGHT, (5, 4), {Direction.N})
assert_flips_direction(Player.LIGHT, (6, 4), set())

# %%
assert_flips_direction(Player.DARK, (0, 0), set())
assert_flips_direction(Player.DARK, (2, 4), {Direction.S})
assert_flips_direction(Player.DARK, (3, 5), {Direction.W})
assert_flips_direction(Player.DARK, (4, 2), {Direction.E})
assert_flips_direction(Player.DARK, (5, 2), set())
assert_flips_direction(Player.DARK, (5, 3), {Direction.N})
assert_flips_direction(Player.DARK, (5, 4), set())
assert_flips_direction(Player.DARK, (6, 4), set())


# %% [markdown]
#
# ## Mini-Workshop
#
# Erweitern Sie die Klasse `Board` um eine Methode
# `is_valid_move(self, player: Player, index: Index) -> bool`
# die genau dann `True` zurückgibt, wenn `index` eine gültiger Index für
# den nächsten Zug des Spielers `player` ist.
#
# Ein Index ist gültig, wenn
# - Er nicht schon besetzt ist,
# - Mindestens ein Stein des Gegenspielers durch den Zug umgedreht wird
#

# %% tags=["code-along"]
@dataclass(repr=False)
class Board:
    _fields: list[Field] = field(default_factory=lambda: [Field.EMPTY] * 64)

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, index) -> Field:
        return self._fields[compute_linear_index(index)]

    def __setitem__(self, index, value):
        self._fields[compute_linear_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result

    def _indices_that_can_be_flipped(
        self, player: Player, occupied_indices: list[Index]
    ) -> set[Index]:
        is_self_owned_field = [
            is_field_owned_by_player(player, self[index]) for index in occupied_indices
        ]
        stop_index = _find_rightmost(is_self_owned_field)
        return set(
            index
            for index in occupied_indices[:stop_index]
            if is_field_owned_by_opponent(player, self[index])
        )

    def _indices_to_flip_in_direction(
        self, p: Player, index: Index, d: Direction
    ) -> set[Index]:
        next_index, is_valid = next_index_in_direction(index, d)
        occupied_indices = []
        while is_valid:
            if not is_occupied(self[next_index]):
                break
            occupied_indices.append(next_index)
            next_index, is_valid = next_index_in_direction(next_index, d)
        return self._indices_that_can_be_flipped(p, occupied_indices)

    def is_valid_move(self, player: Player, index: Index) -> bool:
        if is_occupied(self[index]):
            return False
        for d in Direction:
            if self._indices_to_flip_in_direction(player, index, d):
                return True
        return False


# %%
def assert_valid_moves(player, valid_indices):
    board = Board()
    for row in range(8):
        for col in range(8):
            index = (row, col)
            result = board.is_valid_move(player, index)
            if index in valid_indices:
                assert result, f"Index {index} should be valid."
            else:
                assert not result, f"Index {index} is valid?"


# %%
print(Board())

# %%
valid_moves_for_light_player = {(2, 3), (3, 2), (4, 5), (5, 4)}
assert_valid_moves(Player.LIGHT, valid_moves_for_light_player)

# %%
valid_move_for_dark_player = {(2, 4), (3, 5), (4, 2), (5, 3)}
assert_valid_moves(Player.DARK, valid_move_for_dark_player)


# %% [markdown]
#
# ## Mini-Workshop
#
# Erweitern Sie die Klasse `Board` um eine Methode
# `find_valid_moves(self, player: Player) -> set[Index]`,
# die alle für den Spieler `player` möglichen Züge zurückgibt.
#
# *Hinweis:* Das können Sie leicht mittels *Generate and Test* erreichen:
# Erzeugen Sie alle möglichen Züge und testen Sie dann für jeden Zug, ob
# er möglich ist.

# %% tags=["code-along"]
@dataclass(repr=False)
class Board:
    _fields: list[Field] = field(default_factory=lambda: [Field.EMPTY] * 64)

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, index) -> Field:
        return self._fields[compute_linear_index(index)]

    def __setitem__(self, index, value):
        self._fields[compute_linear_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result

    def _indices_that_can_be_flipped(
        self, player: Player, occupied_indices: list[Index]
    ) -> set[Index]:
        is_self_owned_field = [
            is_field_owned_by_player(player, self[index]) for index in occupied_indices
        ]
        stop_index = _find_rightmost(is_self_owned_field)
        return set(
            index
            for index in occupied_indices[:stop_index]
            if is_field_owned_by_opponent(player, self[index])
        )

    def _indices_to_flip_in_direction(
        self, p: Player, index: Index, d: Direction
    ) -> set[Index]:
        next_index, is_valid = next_index_in_direction(index, d)
        occupied_indices = []
        while is_valid:
            if not is_occupied(self[next_index]):
                break
            occupied_indices.append(next_index)
            next_index, is_valid = next_index_in_direction(next_index, d)
        return self._indices_that_can_be_flipped(p, occupied_indices)

    def is_valid_move(self, player: Player, index: Index) -> bool:
        if is_occupied(self[index]):
            return False
        for d in Direction:
            if self._indices_to_flip_in_direction(player, index, d):
                return True
        return False

    def find_valid_moves(self, player: Player) -> set[Index]:
        result = set()
        for row in range(8):
            for column in range(8):
                move = (row, column)
                if self.is_valid_move(player, move):
                    result.add(move)
        return result


# %%
board = Board()
assert board.find_valid_moves(Player.LIGHT) == valid_moves_for_light_player
assert board.find_valid_moves(Player.DARK) == valid_move_for_dark_player


# %% [markdown]
#
# ## Mini-Workshop
#
# Schreiben Sie eine Methode
# `play_move(self, player: Player, index: Index) -> None`,
# die den Zug von `player` auf das Feld `index` ausführt.
# Falls der Zug ungültig ist, soll eine Exception ausgelöst werden.
# Falls der Zug gültig ist, sollen alle Felder, die durch den Zug
# umgedreht werden von dieser Methode auf den korrekten Wert gesetzt werden.
#
# Schreiben Sie dazu geeignete Hilfsmethoden, damit `play_move` nicht zu
# viele Verantwortlichkeiten hat.


# %% tags=["code-along"]
@dataclass(repr=False)
class Board:
    _fields: list[Field] = field(default_factory=lambda: [Field.EMPTY] * 64)

    def __post_init__(self):
        self[3, 3] = Field.DARK
        self[3, 4] = Field.LIGHT
        self[4, 3] = Field.LIGHT
        self[4, 4] = Field.DARK

    def __getitem__(self, index) -> Field:
        return self._fields[compute_linear_index(index)]

    def __setitem__(self, index, value):
        self._fields[compute_linear_index(index)] = value

    def __iter__(self):
        return iter(self._fields)

    def __repr__(self) -> str:
        name = type(self).__name__
        return f"{name}({reprlib.repr(self._fields)})"

    def __str__(self) -> str:
        result = ""
        prefix = "|"
        for row in range(8):
            result += prefix
            for col in range(8):
                result += str(self[row, col].value) + "|"
            prefix = "\n|"
        return result

    def _indices_that_can_be_flipped(
        self, player: Player, occupied_indices: list[Index]
    ) -> set[Index]:
        is_self_owned_field = [
            is_field_owned_by_player(player, self[index]) for index in occupied_indices
        ]
        stop_index = _find_rightmost(is_self_owned_field)
        return set(
            index
            for index in occupied_indices[:stop_index]
            if is_field_owned_by_opponent(player, self[index])
        )

    def _indices_to_flip_in_direction(
        self, p: Player, index: Index, d: Direction
    ) -> set[Index]:
        next_index, is_valid = next_index_in_direction(index, d)
        occupied_indices = []
        while is_valid:
            if not is_occupied(self[next_index]):
                break
            occupied_indices.append(next_index)
            next_index, is_valid = next_index_in_direction(next_index, d)
        return self._indices_that_can_be_flipped(p, occupied_indices)

    def is_valid_move(self, player: Player, index: Index) -> bool:
        if is_occupied(self[index]):
            return False
        for d in Direction:
            if self._indices_to_flip_in_direction(player, index, d):
                return True
        return False

    def find_valid_moves(self, player: Player) -> set[Index]:
        result = set()
        for row in range(8):
            for column in range(8):
                move = (row, column)
                if self.is_valid_move(player, move):
                    result.add(move)
        return result

    def play_move(self, player: Player, index: Index) -> None:
        if self.is_valid_move(player, index):
            field = Field.LIGHT if player is Player.LIGHT else Field.DARK
            self[index] = field
            flipped_indices = self.find_flipped_indices(player, index)
            self.flip_indices(field, flipped_indices)
        else:
            raise ValueError(f"{index} is not a valid move")

    def find_flipped_indices(self, player: Player, index: Index) -> set[Index]:
        result = set()
        for d in Direction:
            result |= self._indices_to_flip_in_direction(player, index, d)
        return result

    def flip_indices(self, field: Field, flipped_indices: set[Index]) -> None:
        for index in flipped_indices:
            self[index] = field


# %%
def play_some_random_moves(n: int = 10):
    board = Board()
    player = Player.DARK
    for _ in range(n):
        print(board)
        moves = board.find_valid_moves(player)
        if moves:
            move = sample(list(moves), 1)[0]
            print(f"Player {player} plays {move}.")
            board.play_move(player, move)
        else:
            print(f"{player} has no more valid moves.")
        player = Player.LIGHT if player == Player.DARK else Player.DARK
    print(board)


# %%
play_some_random_moves()
