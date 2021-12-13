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
# {{ doc.header("Einführung in Python: Grundlagen Teil 2") }}


# %% [markdown] "slideshow": {"slide_type": "slide"}}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %% tags=["code-along"]
print(str("Hallo!"))

# %% tags=["code-along"]
print(repr("Hallo!"))

# %% [markdown] "slideshow": {"slide_type": "subslide"}}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %% tags=["code-along"]
print(str(["a", "b", "c"]))
print(repr(["a", "b", "c"]))


# %% [markdown] slideshow={"slide_type": "slide"}
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden:

# %% tags=["code-along"]
class PointV0:
    pass


# %% [markdown]
#
# Klassennamen werden in Pascal-Case (d.h. groß und mit Großbuchstaben zur
# Trennung von Namensbestandteilen) geschrieben, z.B. `MyVerySpecialClass`.

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Instanzen von benutzerdefinierten Klassen werden erzeugt, indem man den
# Klassennamen als Funktion aufruft.  Manche der Python Operatoren und
# Funktionen können verwendet werden:

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
p1 = PointV0()
p1

# %% tags=["code-along"]
print(p1)

# %% tags=["code-along"]
p2 = PointV0()
p1 == p2

# %% tags=["code-along"]
# Fehler
# p1 < p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %% tags=["code-along"]
# Möglich, aber nicht gut...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)


# %% tags=["code-along"]
# Fehler!
# p2.x

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Im Gegensatz zu Dictionaries werden Instanzen von Klassen typischerweise
# *nicht* nach der Erzeugung beliebige Attribute zugewiesen!
#
# Statt dessen sollen allen Instanzen die gleiche Form haben. Deswegen werden
# die Attribute eines Objekts bei seiner Konstruktion initialisiert. Das geht
# über die `__init__()` Methode. Die `__init__()`-Methode hat immer
# (mindestens) einen Parameter, der per Konvention `self` heißt:

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


# %% tags=["code-along"]
p1 = PointV1()
p2 = PointV1()
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)

# %% tags=["code-along"]
p1 == p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Die Werte von Attributen können verändert werden:

# %% tags=["code-along"]
p1.x = 1.0
p1.y = 2.0
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] slideshow={"slide_type": "subslide"}
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %% tags=["code-along"]
p1 = PointV2(2.0, 3.0)
p2 = PointV2(0.0, 0.0)
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Kraftfahrzeuge (Teil 1)"


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Methoden
#
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf
# dem die Methode aufgerufen wird muss als erster Parameter angegeben werden.
#
# Per Konvention hat dieser Parameter den Namen `self`, wie bei der
# `__init__()`-Methode.

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
class PointV3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
p = PointV3(2, 3)
print("x =", p.x)
print("y =", p.y)

# %% tags=["code-along"]
p.move(3, 5)
print("x =", p.x)
print("y =", p.y)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Kraftfahrzeuge (Teil 2)"


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Das Python-Objektmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# %% tags=["code-along"]
print(str(p1))
print(repr(p1))


# %% [markdown]
# Durch Definition der Methode `__repr__(self)` kann der von `repr`
# zurückgegebene String für benutzerdefinierte Klassen angepasst werden: Der
# Funktionsaufruf `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und
# ruft diese auf, falls sie existiert.

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
class PointV4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV4(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% tags=["code-along"]
p1 = PointV4(2, 5)
print(repr(p1))

# %% [markdown] slideshow={"slide_type": "subslide"} Standardmäßig delegiert
# die Funktion `str` an `repr`, falls keine `__str__`-Methode definiert ist:
#

# %% tags=["code-along"]
print(str(p1))


# %% [markdown] slideshow={"slide_type": "subslide"}
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(" + repr(self.x) + ", " + repr(self.y) + ")"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Point):
            return self.x == o.x and self.y == o.x
        return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(other * self.x, other * self.y)

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(2, 4)

# %% tags=["code-along"]
p1 == p2

# %% tags=["code-along"]
p2 == p3

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
p3 = p1 + p2
p3

# %% tags=["code-along"]
p3 = p1 - Point(3, 2)
p3

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
print(p1)
print(p1 * 3)
print(3 * p1)

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
print(p2)
p2 += p1
p2


# %% [markdown] slideshow={"slide_type": "subslide"}
#
#  ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Kraftfahrzeuge (Teil 3)"


# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Es ist möglich eigene Typen zu definieren, die sich wie Listen verhalten:

# %% tags=["code-along"]
class MyBadList:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def __getitem__(self, n):
        return self.elements[n]

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return f"MyBadList({self.elements!r})"

    def append(self, element):
        self.elements.append(element)


# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
my_list_1 = MyBadList()
my_list_2 = MyBadList()
my_list_3 = MyBadList([1, 2, 3])
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% slideshow={"slide_type": "subslide"} tags=["code-along"]
my_list_1.append("a")
my_list_1.append("b")
my_list_1.append("c")
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% tags=["code-along"]
print(len(my_list_1))
print(my_list_1[0])
# print(my_list_1[10])

# %% tags=["code-along"]
for elt in my_list_1:
    print(elt)

# %% tags=["code-along"]
my_list_1[1:]


# %% [markdown]
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation
# und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html)
# beinhaltet weitere Möglichkeiten.

# %% tags=["code-along"]
from dataclasses import dataclass


@dataclass
class DataPoint:
    x: float
    y: float


# %% tags=["code-along"]
dp = DataPoint(2, 3)
dp

# %% tags=["code-along"]
dp1 = DataPoint(1, 1)
dp2 = DataPoint(1, 1)
print(dp1 == dp2)
print(dp1 is dp2)


# %% tags=["code-along"]
@dataclass
class Point3D:
    x: float
    y: float
    z: float = 0.0

    # Non-destructive move!
    def move(self, dx=0.0, dy=0.0, dz=0.0):
        return Point3D(self.x + dx, self.y + dy, self.z + dz)


# %% tags=["code-along"]
p3d = Point3D(1.0, 2.0)
print(p3d)
print(p3d.move(dy=1.0, dz=5.0))

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Dataclasses erzwingen, dass alle Default-Werte unveränderlich sind:

# %% tags=["code-along"]
from dataclasses import dataclass, field


@dataclass
class DefaultDemo:
    # item: list = []
    items: list = field(default_factory=list)


# %% tags=["code-along"]
d1 = DefaultDemo()
d2 = DefaultDemo()

# %% tags=["code-along"]
d1.items.append(1234)
print(d1)
print(d2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Einkaufsliste"

# %%
