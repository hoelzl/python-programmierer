# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Benutzerdefinierte Datentypen<br/><br/>
# Mit Exkursen in Ausnahmebehandlung, Dateien und Context Manager</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %%
print(str("Hallo!"))

# %%
print(repr("Hallo!"))

# %% [markdown] slideshow={"slide_type": "subslide"}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
print(str(["a", "b", "c"]))
print(repr(["a", "b", "c"]))


# %% [markdown] slideshow={"slide_type": "slide"}
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden:

# %%
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

# %% slideshow={"slide_type": "subslide"}
p1 = PointV0()
p1

# %%
print(p1)

# %%
p2 = PointV0()
p1 == p2

# %%
# p1 < p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %%
# Möglich, aber nicht gut...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)

# %%
# Fehler!
# p2.y

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Im Gegensatz zu Dictionaries werden Instanzen von Klassen typischerweise
# *nicht* nach der Erzeugung beliebige Attribute zugewiesen!
#
# Statt dessen sollen allen Instanzen die gleiche Form haben. Deswegen werden
# die Attribute eines Objekts bei seiner Konstruktion initialisiert. Das geht
# über die `__init__()` Methode. Die `__init__()`-Methode hat immer
# (mindestens) einen Parameter, der per Konvention `self` heißt:

# %% slideshow={"slide_type": "subslide"}
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

# %%
p1 = PointV1()
p2 = PointV1()
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Die Werte von Attributen können verändert werden:

# %%
p1.x = 1.0
p1.y = 2.0
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] slideshow={"slide_type": "subslide"}
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %% slideshow={"slide_type": "subslide"}
class PointV2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


# %%
p1 = PointV2(x=2.0, y=3.0)
p2 = PointV2(y=2.1)
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)
p1


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
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

# %% slideshow={"slide_type": "subslide"}
class PointV3:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
    
    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy

# %% slideshow={"slide_type": "subslide"}
p = PointV3(2.0, 3.0)
print(p.x, p.y)

# %%
p.move(2.0, 5.0)
print(p.x, p.y)

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

# %%
print(str(p))
print(repr(p))


# %% [markdown]
# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# %% slideshow={"slide_type": "subslide"}
class PointV4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointV4({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, PointV4):
            return self.x == other.x and self.y == other.y
        return False

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p1 = PointV4(2, 5)
print(repr(p1))
print(str(p1))

# %%
p2 = PointV4(2, 5)
p3 = PointV4(3, 7)

# %%
p1 == p2

# %%
p1 is p2

# %%
p1 == p3

# %%
p1 == 123

# %% [markdown] slideshow={"slide_type": "subslide"}
# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
#

# %%
print(str(p1))


# %% [markdown] slideshow={"slide_type": "subslide"}
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# %% slideshow={"slide_type": "subslide"}
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

    # Double dispatch
    def __mul__(self, other):
        print("Called __mul__()")
        return Point(other * self.x, other * self.y)
    
    def __rmul__(self, other):
        print("Called __rmul__()")
        return Point(other * self.x, other * self.y)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"}
p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(2, 4)
p1, p2, p3

# %%
p1 == p2

# %%
p2 == p3

# %% slideshow={"slide_type": "subslide"}
p3 = p1 + p2
p3

# %%
p3 = p1 - Point(3, 2)
p3

# %% slideshow={"slide_type": "subslide"}
print(p1)
print(p1 * 3)
print(3 * p1)

# %% slideshow={"slide_type": "subslide"}
print(p2)
p2 += p1
p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Es ist möglich eigene Typen zu definieren, die sich wie Listen verhalten:

# %%
class MyBadList:
    def __init__(self, elements = None):
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


# %% slideshow={"slide_type": "subslide"}
my_list_1 = MyBadList()
my_list_2 = MyBadList()
my_list_3 = MyBadList([1, 2, 3])
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% slideshow={"slide_type": "subslide"}
my_list_1.append("a")
my_list_1.append("b")
my_list_1.append("c")
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %%
print(len(my_list_1))
print(my_list_1[0])
# print(my_list_1[10])

# %%
for elt in my_list_1:
    print(elt)

# %%
my_list_1[1:]

# %% [markdown]
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation
# und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html)
# beinhaltet weitere Möglichkeiten.

# %%
from dataclasses import dataclass

@dataclass
class DataPoint:
    x: float = 0.0
    y: float = 0.0


# %%
dp = DataPoint(2, 3)
dp

# %%
dp1 = DataPoint(1, 1)
dp2 = DataPoint(1, 1)
print(dp1 == dp2)
print(dp1 is dp2)


# %%
@dataclass
class Point3D:
    x: float
    y: float
    z: float = 0.0

    # Non-destructive move!
    def move(self, dx=0.0, dy=0.0, dz=0.0):
        return Point3D(self.x + dx, self.y + dy, self.z + dz)


# %%
p3d = Point3D(1.0, 2.0)
print(p3d)
print(p3d.move(dy=1.0, dz=5.0))

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Dataclasses erzwingen, dass alle Default-Werte unveränderlich sind:

# %%
from dataclasses import dataclass, field

@dataclass
class DefaultDemo:
    # item: list = []
    items: list = field(default_factory=list)

# %%
d1 = DefaultDemo()
d2 = DefaultDemo()

# %%
d1.items.append(1234)
print(d1)
print(d2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Einkaufsliste"

# %%
