# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Objektorientierung Teil 2: Vererbung</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Object orientation part 2: Inheritance</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  # Objektorientierung Teil 2
#
#  - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
#  - In diesem Kapitel werden wir Vererbung betrachten.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Object Orientation Part 2
#
#  - In the previous lesson we got to know classes, one of the basic building blocks of object-oriented programming
#  - In this chapter we will consider inheritance.

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#  ## Vererbung

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Inheritance

# %%
import random
from typing import Tuple


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 4)
        self.y = random.gauss(3, 2)


# %%
p = Point(0, 0)
p

# %%
assert p.x == 0.0
assert p.y == 0.0

# %%
p.move(2, 3)
p

# %%
assert p.x == 2.0
assert p.y == 3.0

# %%
p.randomize()
p


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# Wie können wir farbige Punkte einführen, ohne die komplette Funktionalität von `Point` neu implementieren zu müssen?

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# How can we introduce colored points without having to re-implement the entire functionality of `Point`?

# %% {"tags": ["code-along"]}
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# %% {"tags": ["code-along"]}
cp = ColorPoint(2, 3, "red")
# cp


# %% {"tags": ["code-along"]}
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "red"

# %% {"tags": ["code-along"]}
cp.move(2, 3)
# cp


# %% {"tags": ["code-along"]}
assert cp.x == 4.0
assert cp.y == 6.0
assert cp.color == "red"

# %% {"tags": ["code-along"]}
cp.randomize()
# cp


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Abschnitt "Vererbung"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Section "Inheritance"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Abstrakte Klassen
#
# - Klassen von denen keine direkte Instanz erzeugt werden kann
# - Haben die Klasse `abc.ABC` als Basisklasse
#     - (Eigentlich ist eine Metaklasse verantwortlich für das Verhalten)
# - Erlauben die Verwendung des `@abstractmethod` Dekorators um abstrakte Methoden zu definieren
#     - Der Rumpf einer abstrakten Methode ist oft `...`
# - Abstrakte Klassen, die nur abstrakte Methoden haben nennt man Interfaces
#     - Interfaces beschreiben Anforderungen an ihre Unterklassen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Abstract classes
#
# - Classes that cannot have direct instances
# - Have `abc.ABC` as base class
#     - (a metaclass is actually responsible for their behavior)
# - Allow use of the `@abstractmethod` decorator to define abstract methods
#     - Often the body of an abstract method is written as `...`
# - Abstract classes that have only abstract methods are called Interfaces
#     - Interfaces describe requirements placed on subclasses

# %% {"tags": ["code-along"]}
...

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
from abc import ABC, abstractmethod

class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        ...


# %% {"tags": ["code-along"]}
class MyClass(MyBase):
    def my_method(self):
        super().my_method()
        print("my_method()")


# %% {"tags": ["code-along"]}
mc = MyClass()
mc.my_method()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - Abstrakte Methoden können eine Implementierung haben
# - Klassen, die von einer abstrakten Klasse erben aber nicht alle abstrakten Methoden überschreiben sind selber abstrakt.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - Abstract methods can provide an implementation
# - Classes that inherit from an abstract class but do not override all abstract methods are themselves abstract.

# %% {"tags": ["code-along"]}
from abc import ABC, abstractmethod

class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("Hi!")


# %% {"tags": ["code-along"]}
class MyClass(MyBase):
    pass


# %% {"tags": ["code-along"]}
# mc = MyClass()


# %% {"tags": ["code-along"]}
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")


# %% {"tags": ["code-along"]}
yc = YourClass()
yc.my_method()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# # Workshop
#
# Siehe `workshop_950_rpg_dice` bis `Factory für RPG-Würfel`.


# %% [markdown] {"lang": "en"}
# # Workshop
#
# See `workshop_950_rpg_dice` to `Factory for RPG Cubes`.

# %% [markdown] {"lang": "de"}
# ## RPG-Würfel
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

# %% [markdown] {"lang": "en"}
# ## RPG dice
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

# %% [markdown] {"lang": "de"}
# # Protokolle
#
# Durch Protokolle unterstützt Python strukturelles Subtyping, bei dem Subtyp-Beziehungen aus der Struktur der Klassen erschlossen werden (im Gegensatz zum nominalen Subtyping bei dem die Beziehungen explizit deklariert werden müssen).

# %% [markdown] {"lang": "en"}
# # Protocols
#
# With protocols Python supports structural subtyping, i.e., the derivation of subtype relationships from the structure of classes (in contrast to nominal subtyping where the relationships have to be decalared via inheritance).

# %% {"tags": ["code-along"]}
from typing import Protocol, runtime_checkable, SupportsInt


# %% {"tags": ["code-along"]}
class MyNumber:
    def __int__(self):
        return 0


# %% {"tags": ["code-along"]}
my_number = MyNumber()
int(my_number)

# %% {"tags": ["code-along"]}
isinstance(MyNumber, SupportsInt)


# %% {"tags": ["code-along"]}
@runtime_checkable
class SupportsCastSpell(Protocol):
    def cast_spell(self, name):
        ...


# %% {"tags": ["code-along"]}
@runtime_checkable
class SupportsHit(Protocol):
    def hit(self, who, how):
        ...


# %% {"tags": ["code-along"]}
class Mage:
    def __init__(self, name="The Mage"):
        self.name = name
    def cast_spell(self, spell):
        print(f"{self.name} casts a {spell} spell.")


# %% {"tags": ["code-along"]}
class Fighter:
    @property
    def name(self):
        return "The Fighter"
    def hit(self, opponent, weapon):
        print(f"{self.name} attacks {opponent} with {weapon}.")


# %% {"tags": ["code-along"]}
class Bard:
    def __init__(self, name="The Bard"):
        self.name = name


# %% {"tags": ["code-along"]}
p1 = Mage()
p2 = Fighter()
p3 = Bard()

# %% {"tags": ["code-along"]}
isinstance(p1, SupportsCastSpell)

# %% {"tags": ["code-along"]}
isinstance(p2, SupportsCastSpell)

# %% {"tags": ["code-along"]}
isinstance(p3, SupportsCastSpell)

# %% {"tags": ["code-along"]}
isinstance(p1, SupportsHit)

# %% {"tags": ["code-along"]}
isinstance(p2, SupportsHit)

# %% {"tags": ["code-along"]}
isinstance(p3, SupportsHit)


# %% {"tags": ["code-along"]}
@runtime_checkable
class HasName(Protocol):
    @property
    def name(self):
        ...


# %% {"tags": ["code-along"]}
isinstance(p1, HasName)

# %% {"tags": ["code-along"]}
isinstance(p2, HasName)

# %% {"tags": ["code-along"]}
isinstance(p3, HasName)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Abschnitt "Vererbung"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Section "Inheritance"

# %% [markdown] {"lang": "de"}
# ## Single Dispatch Funktionen
#
# Single Dispatch Funktionen erlauben die definition von "Methoden" außerhalb von Klassen, d.h., man kann Funktionen definieren, die polymorph in ihrem ersten Argument sind.
#
# Dieser Mechanismus erlaubt die flexible Erweiterung von bereits existierenden Klassen.

# %% [markdown] {"lang": "en"}
# ## Single dispatch functions
#
# Single dispatch functions allow "methods" to be defined outside of classes, i.e. one can define functions that are polymorphic in their first argument.
#
# This mechanism allows the flexible extension of already existing classes.

# %% {"tags": ["code-along"]}
from functools import singledispatch


# %% {"tags": ["code-along"]}
@singledispatch
def attack(player: HasName, opponent):
    print(f"{player.name} just stares at the carnage.")


# %% {"tags": ["code-along"]}
@attack.register
def _(player: Mage, opponent):
    player.cast_spell("fireball")


# %% {"tags": ["code-along"]}
@attack.register
def _(player: Fighter, opponent):
    player.hit(opponent, "sword")


# %% {"tags": ["code-along"]}
attack(p1, "The Baddie")

# %% {"tags": ["code-along"]}
attack(p2, "The Baddie")

# %% {"tags": ["code-along"]}
attack(p3, "The Baddie")

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# ## Mehrfachvererbung


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Multiple inheritance

# %%
class A:
    """Superclass of everything"""
    def __init__(self, arg_a="arg_a", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(A, {arg_a})")
    
    def f(self):
        print(f"f(A) on {self!r}")

    def g(self):
        print(f"g(A) on {self!r}")


# %%
class B(A):
    def __init__(self, arg_b="arg_b", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(B, {arg_b})")

    def f(self):
        print(f"f(B) on {self!r}")
        super().f()

    def g(self):
        print(f"g(B) on {self!r}")
        A.g(self)


# %%
class C(A):
    def __init__(self, arg_c="arg_c", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(C, {arg_c})")
    
    def f(self):
        print(f"f(C) on {self!r}")
        super().f()

    def g(self):
        print(f"g(C) on {self!r}")
        A.g(self)


# %%
class D(B, C):
    def __init__(self, arg_d="arg_d", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(D, {arg_d})")
    
    def f(self):
        print(f"f(D) on {self!r}")
        super().f()

    def g(self):
        print(f"g(D) on {self!r}")
        B.g(self)
        C.g(self)


# %% {"tags": ["code-along"]}
d = D()
d.f()

# %% {"tags": ["code-along"]}
d.g()

# %% {"tags": ["code-along"]}
type(d).mro()

# %%
