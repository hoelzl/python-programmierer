# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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
# <div style="text-align:center; font-size:200%;"><b>Object orientation part 1: Inheritance</b></div>
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
p.move(2, 3)
p

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
cp.move(2, 3)
# cp


# %% {"tags": ["code-along"]}
cp.randomize()
# cp


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Vererbung"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `020x workshop control structures`
#  - Section "Inheritance"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  ## Abstrakte Klassen
#
#  - Die Klasse `abc.ABC` als Basisklasse
#  - (Eigentlich ist eine Metaklasse verantwortlich)
#  - `@abstractmethod` Dekorator

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Abstract classes
#
#  - The class `abc.ABC` as base class
#  - (actually a metaclass is responsible)
#  - `@abstractmethod` decorator

# %% {"tags": ["code-along"]}
from abc import ABC, abstractmethod


class MyBase(ABC):
    @abstractmethod
    def my_method(self):
        print("HI!")


# %% {"tags": ["code-along"]}
class MyClass(MyBase):
    pass


# mc = MyClass()


# %% {"tags": ["code-along"]}
class YourClass(MyBase):
    def my_method(self):
        super().my_method()
        print("Hello!")


yc = YourClass()
yc.my_method()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  # Workshop
#
#  Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.


# %% [markdown] {"lang": "en"}
# # Workshop
#
#  See `070x-Workshop RPG Cubes` to `Factory for RPG Cubes`.

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# ## Mehrfachvererbung


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Multiple inheritance

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
