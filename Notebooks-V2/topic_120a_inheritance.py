# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Objektorientierung Teil 2
#
# - Wir haben im vorherigen Kapitel Klassen kennengelernt, einen der grundlegenden Baustein der objektorientierten Programmierung
# - In diesem Kapitel werden wir Vererbung betrachten.
#
# ## Vererbung
#

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

# %%

# %%

# %%

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

# %%

# %%

# %% [markdown]
#
#  # Workshop
#
#  Siehe `070x-Workshop RPG-Würfel` bis `Factory für RPG-Würfel`.

# %% [markdown]
#
#  ## Attribute von Klassen

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
# Method Resolution Order:


# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
#  ## Zugriff auf Attribute
#
#  Python ermöglicht es uns als Programmierer, an mehreren Stellen in den Zugriff auf Attribute einzugreifen und das Verhalten zu modifizieren.

# %% [markdown]
#
#  ## Attribute von Klassen
#
#  Beim Zugriff auf `C.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Key in `C.__dict__` ist:
#    - `v = C.__dict__['name']`
#    - Falls `v` ein Deskriptor ist (i.e., `type(v).__get__` definiert ist:
#      - Resultat ist `type(v).__get__(v, None, C)`
#    - Falls `v` kein Deskriptor ist:
#      - Resultat ist `v`
#  - Falls `name` kein Key in `C.__dict__` ist:
#    - Die Baisklassen von `C` werden in Method Resolution Order durchlaufen und
#      diese Verfahren wird für jede Klasse ausgeführt

# %% [markdown]
#
#  ## Attribute von Instanzen
#
#  Beim Zugriff auf `object.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Overriding Descriptor `v` in `C` oder einer der
#    Basisklassen von `C` ist (`type(v)` hat Methoden `__get__()` und
#    `__set__()`:
#    - Das Resultat ist `type(v).__get__(v, object, C)`
#  - Andernfalls, falls `name` ein Schlüssel in `object.__dict__` ist:
#    - Das Resultat ist `object.__dict__['name']`
#  - Andernfalls delegiert `object.name` die Suche an die Klasse, wie oben
#    beschrieben
#    - Falls dadurch ein Deskriptor `v` gefunden wird, so ist das Ergebnis
#      `type(v).__get__(v, object, C)`
#    - Wenn ein Wert `v` gefunden wird, der kein Deskriptor ist, dann wird `v`
#      zurückgegeben
#  - Wenn kein Wert gefunden wird und `C.__getattr__` definiert ist, dann wird
#    `C.__getattr__(object, 'name')` aufgerufen um den Wert zu erhalten
#  - Andernfalls wird eine `AttributeError` Exception ausgelöst
#
#  Dieser Prozess kann durch die `__getattribute__` Methode überschrieben werden.

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

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

# %%

# %%
