# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# # RPG-Würfel
#
# In Rollenspielen werden Konflikte zwischen Spielern oft durch Würfeln
# entschieden. Dabei werden oft mehrere Würfel gleichzeitig verwendet. Außerdem
# werden nicht nur die bekannten 6-seitigen Würfel verwendet, sondern auch
# 4-seitige, 8-seitige, 20-seitige Würfel, etc.
#
# Die Anzahl und Art der Würfel wird dabei durch folgende Notation beschrieben:
#
# ```text
# <Anzahl der Würfel> d <Seiten pro Würfel>
# ```
#
# Zum Beispiel wird das Würfeln mit zwei 6-seitigen Würfeln als `2d6`
# beschrieben. Manchmal werden auch komplexere Formeln verwendet: 
# `3d20 + 2d6 - 4` bedeutet, dass gleichzeitig drei 20-seitige Würfel und zwei 6-seitige
# Würfel geworfen werden und die Gesamtsumme der Augenzahlen dann um 4
# verringert wird.
#
# In manchen Spielen wird das Werfen der niedrigsten oder höchsten Augenzahl
# besonders behandelt ("katastrophale Niederlage", "kritischer Erfolg").
#
# In den folgenden Aufgaben sollen Sie derartige RPG-Würfel in Python
# implementieren. Um Ihre Implementierung testen zu können empfiehlt es sich
# sie in einem IDE zu realisieren. 
#
# Schreiben Sie Tests für jede Funktionalität, die Sie implementieren.
# Wie können Sie beim Testen mit der Zufälligkeit beim Würfeln umgehen?
# Was sind Stärken bzw. Schwächen der von Ihnen gewählten Teststrategie?

# %% [markdown] lang="en"
# # RPG dice
#
# In roleplaying games, conflicts between players are often decided by rolling
# dice, often multiple dice at the same time. Furthermore games often use
# not only the well known 6-sided dice, but also 4-sided, 8-sided, 20-sided dice, etc.
#
# The number and type of dice is described by the following notation:
#
# ```text
# <number of dice> d <number of sides per die>
# ```
#
# For example, rolling two 6-sided dice is described as `2d6`.
# Sometimes more complex formulas are used: `3d20 + 2d6 - 4`
# means that three 20-sided dice and two 6-sided dice are rolled
# at the same time, and the total sum of numbers is then reduced by 4.
#
# In some games, rolling the lowest or highest number of dice is treated
# in a special way ("catastrophic failure", "critical success").
#
# In the following exercise your task is to implement RPG dice in Python.
# To simplify testing your implementation it might be advisable
# to implement it in an IDE, but it is also possible to write tests as
# assertions in a jupyter notebook. 
#
# Write tests for each functionality you implement. How can you deal with the
# randomness in dice rolling? What are the strengths and weaknesses of the strategy
# you have chosen to test?

# %% [markdown] lang="de"
# ## Generalisierte Würfel: Interface `Dice`
#
# Implementieren Sie eine abstrakte Klasse `Dice`, die das Würfeln mit
# beliebigen Würfeln beschreibt: Die Klasse soll folgende abstrakte Methoden
# anbieten:
#
# - `roll(): int` liefert das Ergebnis eines Wurfes mit den entsprechenden
#   Würfeln zurück.
#
# - properties `max_value: int` und `min_value: int` geben den kleinsten bzw.
#   größten Wert zurück, der mit den entsprechenden Würfeln geworfen werden
#   kann.
#
# Falls Sie Pytest verwenden:
# Schreiben Sie parametrische Pytest Tests, mit denen (indirekte) Instanzen
# von `Dice` getestet werden können.

# %% [markdown] lang="en"
# ## Generalized dice: Interface `Dice`
#
# Implement an abstract class `Dice` that describes rolling of
# arbitrary dice: The class should provide the following abstract methods:
#
# - `roll(): int` returns the result of a roll with the appropriate
#   dice.
#
# - properties `max_value: int` and `min_value: int` return the smallest and largest
#   value that can be rolled with the corresponding dice.
#   dice.
#
# If you are using Pytest:
# Write parametric Pytest tests to test (indirect) instances of `Dice`.

# %% tags=["solution"]
import random
from abc import ABC, abstractmethod
from typing import Tuple, Callable, Sequence, Union, Iterable


# %% tags=["solution"]
class Dice(ABC):
    """Roll with a combination of multiple dice."""

    @abstractmethod
    def roll(self) -> int:
        ...

    @property
    @abstractmethod
    def min_value(self) -> int:
        ...

    @property
    @abstractmethod
    def max_value(self) -> int:
        ...


# %% [markdown] lang="de"
# ## Klasse `ConstantDice`
#
# Implementieren Sie eine Klasse `ConstantDice`, die das Interface `Dice`
# implementiert und einen Würfel realisiert, der immer einen konstanten, bei der
# Instanziierung des Objekts festgelegten Wert würfelt.

# %% [markdown] lang="en"
# ## Class `ConstantDice`
#
# Implement a class `ConstantDice`, which implements the interface `Dice` and
# represents a die that always rolls a constant value. The result value is
# specified when the creating an instance of the class.

# %% lang="en" tags=["solution"]
class ConstantDice(Dice):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, ConstantDice):
            return self.value == other.value
        else:
            return False

    def roll(self) -> int:
        return self.value

    @property
    def min_value(self) -> int:
        return self.value

    @property
    def max_value(self) -> int:
        return self.value

# %% tags=["solution"]
dice = ConstantDice(3)
assert dice.min_value == 3
assert dice.max_value == 3
assert dice.roll() == 3


# %% [markdown] lang="de"
# ## Klasse `FairDice`
#
# Implementieren Sie eine Klasse `FairDice`, die das Interface `Dice`
# implementiert und einen der oben beschriebenen Würfe mit mehreren Würfeln
# einer beliebigen (aber für alle Würfel gleichen) Augenzahl realisiert. Z.B.
# sollen Würfe der Form `3d6` oder `4d17` durch Instanzen dieser Klasse
# darstellbar sein (obwohl es in der Realität keinen 17-seitigen (fairen)
# Würfel gibt).
#
# Wie können Sie beim Testen mit der Zufälligkeit beim Würfeln umgehen? Was
# sind Stärken bzw. Schwächen der gewählten Teststrategie?
#
# *Hinweis:* Die Funktionen `random.randint()` und `random.seed()` können 
# bei dieser Aufgabe hilfreich sein.

# %% [markdown] lang="en"
# ## Class `FairDice`
#
# Implement a class `FairDice` that implements the interface `Dice`and
# represents a single rolls with multiple dice all having the same (configurable)
# number of sides. For example, instances of the class `FairDice` should be
# able to simulate dice rolls of the form `3d6` or `4d17`
# (although in reality there is no 17-sided (fair) die).
#
# How can you deal with randomness in dice rolling when testing? What
# are strengths or weaknesses of the chosen testing strategy?
#
# *Hint:* Look at `random.randint()` and `random.seed()`.


# %% tags=["solution"]
class FairDice(Dice):
    def __init__(self, num_dice, num_sides):
        assert num_dice >= 1
        assert num_sides >= 2

        self.num_dice = num_dice
        self.num_sides = num_sides

    def __eq__(self, other):
        if isinstance(other, FairDice):
            return (self.num_dice == other.num_dice
                    and self.num_sides == other.num_sides)
        else:
            return False

    def roll(self) -> int:
        result = 0
        for _ in range(self.num_dice):
            result += random.randint(1, self.num_sides)
        return result

    @property
    def min_value(self) -> int:
        return self.num_dice

    @property
    def max_value(self) -> int:
        return self.num_sides * self.num_dice


# %% tags=["solution"]
dice = FairDice(2, 6)
assert dice.min_value == 2
assert dice.max_value == 12
random.seed(1)
assert dice.roll() == 7

# %% [markdown] lang="de"
# ## Klasse `SumDice`
#
# Implementieren Sie eine Klasse `SumDice`, die das Interface `Dice`
# implementiert und die Summe des Würfelns mit mehreren verschiedenen Würfeln
# (potentiell der Form `<m>d<n>`) repräsentiert.

# %% [markdown] lang="en"
# ## Class `SumDice`
#
# Implement a class `SumDice` which implements the interface `Dice` and
# represents the sum of the dice rolls with several different dice
# (potentially of the form `<m>d<n>`).


# %% tags=["solution"]
class SumDice(Dice):
    def __init__(self, dice: Iterable):
        assert dice
        self.dice = dice

    def __eq__(self, other):
        if isinstance(other, SumDice):
            return self.dice == other.dice
        else:
            return False

    def roll(self) -> int:
        return sum(d.roll() for d in self.dice)

    @property
    def min_value(self) -> int:
        return sum(d.min_value for d in self.dice)

    @property
    def max_value(self) -> int:
        return sum(d.max_value for d in self.dice)



# %% tags=["solution"]
dice = SumDice([ConstantDice(3), ConstantDice(2)])
assert dice.min_value == 5
assert dice.max_value == 5
assert dice.roll() == 5

# %% tags=["solution"]
dice = SumDice([ConstantDice(1), FairDice(2, 6)])
assert dice.min_value == 3
assert dice.max_value == 13
random.seed(1)
assert dice.roll() == 8

# %% [markdown] lang="de"
# ## Klasse `SimpleDie`
#
# Implementieren Sie eine Klasse `SimpleDie`, die das Interface `Dice`
# implementiert und das Würfeln mit einem Würfel beliebiger, bei der
# Instanziierung des Würfels festgelegten, Seitenzahl ermöglicht.

# %% [markdown] lang="en"
# ## Class `SimpleDie`
#
# Implement a class `SimpleDie`, which implements the interface `Dice`
# and represents a single roll of a die with an arbitrary number of sides
# (specified when the die is instantiated).


# %% tags=["solution"]
class SimpleDie(Dice):
    def __init__(self, num_sides):
        assert num_sides >= 2
        self.num_sides = num_sides

    def __eq__(self, other):
        if isinstance(other, SimpleDie):
            return self.num_sides == other.num_sides
        else:
            return False

    def roll(self) -> int:
        return random.randint(1, self.num_sides)

    @property
    def min_value(self) -> int:
        return 1

    @property
    def max_value(self) -> int:
        return self.num_sides


# %% tags=["solution"]
die = SimpleDie(6)
assert die.min_value == 1
assert die.max_value == 6
random.seed(1)
assert die.roll() == 2

# %% [markdown] lang="de"
# ## Klasse `MultipleRollDice`
#
# Implementieren Sie eine Klasse `MultipleRollDice`, die das Interface `Dice`
# implementiert und das wiederholte Würfeln mit einem (generalisierten)
# Würfel realisiert.
#
# Was ist die Beziehung zwischen `FairDice` und der Kombination aus
# `SimpleDie` und `MultipleRollDice`? Wie unterscheiden sich die beiden
# Implementierungsstrategien in ihrer Testbarkeit.

# %% [markdown] lang="en"
# ## Class `MultipleRollDice`
#
# Implement a class `MultipleRollDice` which implements the interface `Dice` 
# and represents rolling of a (generalized) dice a certain number of times.
# Both the die and the number of rolls should be specified when an
# instance is created.
#
# What is the relationship between `FairDice` and the combination of
# `SimpleDie` and `MultipleRollDice`? How do the two
# implementation strategies in their testability.


# %% tags=["solution"]
class MultipleRollDice(Dice):
    def __init__(self, rolls, dice):
        assert rolls >= 1
        assert dice
        self.rolls = rolls
        self.dice = dice

    def __eq__(self, other):
        if isinstance(other, MultipleRollDice):
            return self.rolls == other.rolls and self.dice == other.dice
        else:
            return False

    def roll(self) -> int:
        result = 0
        for _ in range(self.rolls):
            result += self.dice.roll()
        return result

    @property
    def min_value(self) -> int:
        return self.rolls * self.dice.min_value

    @property
    def max_value(self) -> int:
        return self.rolls * self.dice.max_value



# %% tags=["solution"]
dice = MultipleRollDice(2, SimpleDie(6))
assert dice.min_value == 2
assert dice.max_value == 12
random.seed(1)
assert dice.roll() == 7

# %% [markdown] lang="de"
# # Factory für RPG-Würfel
#
# Schreiben Sie eine Funktion `create_dice(configuration: str) -> Dice`,
# die eine Konfiguration von RPG-Würfeln als Argument bekommt und eine
# geeignete Konfiguration von Dice-Instanzen zurückgibt.  Zum Beispiel soll
# für "3d8 + 6" ein `SumDice` zurückgegeben werden, der einen `FairDice` (mit
# 3 8-seitigen Würfeln) und einen `ConstantDice` mit dem Wert 6 enthält.

# %% [markdown] lang="en"
# # Factory for RPG dice
#
# Write a function `create_dice(configuration: str) -> Dice`,
# which gets a configuration of RPG dice as argument and returns an
# suitable configuration of dice instances.  For example
# for "3d8 + 6" a `SumDice` should be returned, which contains a `FairDice` (with
# 3 8-sided dice) and a `ConstantDice` with the value 6.

# %%
