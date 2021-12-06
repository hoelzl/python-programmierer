# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# %%

# j2 import 'macros.j2' as doc
# %% [markdown] {"incorrectly_encoded_metadata": "{{ doc.slide() }}"}
# {{ doc.header (Objektorientierung Teil 2: Vererbung) }}


# %% [markdown]
#
#  # Objektorientierung Teil 2
#
#  - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
#  - In diesem Kapitel werden wir Vererbung betrachten.

# %% [markdown]
#  ## Vererbung

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
p.move(2, 3)
p


# %%
p.randomize()
p


# %%
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])



# %%
cp = ColorPoint(2, 3, "red")
# cp


# %%
cp.move(2, 3)
# cp


# %%
cp.randomize()
# cp


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Vererbung"
#

# %% [markdown]
#
#  ## Abstrakte Klassen
#
#  - Die Klasse `abc.ABC` als Basisklasse
#  - (Eigentlich ist eine Metaklasse verantwortlich)
#  - `@abstractmethod` Dekorator

# %%
from abc import ABC, abstractmethod


class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("HI!")



# %%
class MyClass(MyBase):
    pass


# mc = MyClass()


# %%
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")


yc = YourClass()
yc.my_method()

# %% [markdown]
#
#  # Workshop
#
#  Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.


# %% [markdown]
# ## Mehrfachvererbung


# %%
class A:
    """Superclass of everything"""

    def f(self):
        print(f"f(A) on {self!r}")

    def g(self):
        print(f"g(A) on {self!r}")



# %%
class B(A):
    def f(self):
        print(f"f(B) on {self!r}")
        super().f()

    def g(self):
        print(f"g(B) on {self!r}")
        A.g(self)



# %%
class C(A):
    def f(self):
        print(f"f(C) on {self!r}")
        super().f()

    def g(self):
        print(f"g(C) on {self!r}")
        A.g(self)



# %%
class D(B, C):
    def f(self):
        print(f"f(D) on {self!r}")
        super().f()

    def g(self):
        print(f"g(D) on {self!r}")
        B.g(self)
        C.g(self)



# %%
d = D()
d.f()


# %%
d.g()

