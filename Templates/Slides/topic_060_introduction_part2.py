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
# <div style="text-align:center; font-size:200%;"><b>Einführung in Python: Grundlagen Teil 2</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Introduction to Python: Part 2</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% "slideshow": [markdown] {"incorrectly_encoded_metadata": "{\"slide_type\": \"slide\"}}", "lang": "de", "slideshow": {"slide_type": "slide"}}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Convertsion to strings
#
# Python offers two functions that can be used to convert any value into a string:
#
# - `repr` for a "program-like" representation (how the value could be generated in the program)
# - `str` for "user-friendly" rendering

# %% {"tags": ["code-along"]}
print(str("Hallo!"))

# %% {"tags": ["code-along"]}
print(repr("Hallo!"))

# %% "slideshow": [markdown] {"incorrectly_encoded_metadata": "{\"slide_type\": \"subslide\"}}", "lang": "de"}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %% [markdown] {"lang": "en"}
# For some data types, `str` and `repr` return the same string:

# %% {"tags": ["code-along"]}
print(str(["a", "b", "c"]))
print(repr(["a", "b", "c"]))


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Custom data types
#
# In Python, user-defined data types (classes) can be defined:

# %% {"tags": ["code-along"]}
class PointV0:
    pass


# %% [markdown] {"lang": "de"}
#
# Klassennamen werden in Pascal-Case (d.h. groß und mit Großbuchstaben zur
# Trennung von Namensbestandteilen) geschrieben, z.B. `MyVerySpecialClass`.

# %% [markdown] {"lang": "en"}
# Class names are in pascal case (i.e. capital letters seperate components of names), e.g. `MyVerySpecialClass`.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Instanzen von benutzerdefinierten Klassen werden erzeugt, indem man den
# Klassennamen als Funktion aufruft.  Manche der Python Operatoren und
# Funktionen können verwendet werden ohne, dass zusätzliche Implementierungsarbeit nötig ist:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Instances of custom classes are created by calling the class name as a function. Some of the build-in operators and
# Functions can be used without extra effort:

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
p1 = PointV0()
p1

# %% {"tags": ["code-along"]}
print(p1)

# %% {"tags": ["code-along"]}
p2 = PointV0()
p1 == p2

# %% {"tags": ["code-along"]}
# Fehler
# p1 < p2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %% [markdown] {"lang": "en"}
# Much like dictionaries can be assigned new entries, one can
# assign new *attributes* to user-defined data types, but the `.` notation is used instead of the indexing notation `[]`:

# %% {"tags": ["code-along"]}
# Möglich, aber nicht gut... / Possible but not good...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)


# %% {"tags": ["code-along"]}
# Error!
# p2.x

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Im Gegensatz zu Dictionaries werden Instanzen von Klassen typischerweise
# *nicht* nach der Erzeugung beliebige Attribute zugewiesen!
#
# Statt dessen sollen allen Instanzen die gleiche Form haben. Deswegen werden
# die Attribute eines Objekts bei seiner Konstruktion initialisiert. Das geht
# über die `__init__()` Methode. 
#
# Die `__init__()`-Methode hat immer
# (mindestens) einen Parameter, der per Konvention `self` heißt:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Unlike dictionaries, we typically *do not* create any *new* attributes for an instance after creation!
#
# Instead, all instances should have the same shape. We initialize all attributes of an object when it is constructed. This can be done with the `__init__()` method.
#
# The `__init__()` method always has (at least) one parameter, named `self` by convention:

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


# %% {"tags": ["code-along"]}
p1 = PointV1()
p2 = PointV1()
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)

# %% {"tags": ["code-along"]}
p1 == p2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Die Werte von Attributen können verändert werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The values ​​of attributes can be changed:

# %% {"tags": ["code-along"]}
p1.x = 1.0
p1.y = 2.0
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# In many cases, when constructing an object, we would like to specify the attributes of the instance. 
# This is made possible by passing additional arguments to the `__init__()` method.

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %% {"tags": ["code-along"]}
p1 = PointV2(2.0, 3.0)
p2 = PointV2(0.0, 0.0)
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Kraftfahrzeuge (Teil 1)"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_062_objects`
# - Section "Motor Vehicles (Part 1)"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Methoden
#
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf
# dem die Methode aufgerufen wird muss als erster Parameter angegeben werden.
#
# Per Konvention hat dieser Parameter den Namen `self`, wie bei der
# `__init__()`-Methode.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Methods
#
# Classes can contain methods. Unlike many other languages,
# Python doesn't have an implicit `this` parameter when defining a method; the object on
# which the method is called must be specified as the first parameter of the definition.
#
# By convention, this parameter is named `self`, as in the `__init__()` method.

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
class PointV3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
p = PointV3(2, 3)
print("x =", p.x)
print("y =", p.y)

# %% {"tags": ["code-along"]}
p.move(3, 5)
print("x =", p.x)
print("y =", p.y)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Kraftfahrzeuge (Teil 2)"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `lecture_045x_Workshop_Custom_Datatypes`
# - Section "Motor Vehicles (Part 2)"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Das Python-Objektmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## The Python object model
#
# Dunder methods can be used to make user-defined data types act more like the built-in ones:

# %% {"tags": ["code-along"]}
print(str(p1))
print(repr(p1))


# %% [markdown] {"lang": "de"}
# Durch Definition der Methode `__repr__(self)` kann der von `repr`
# zurückgegebene String für benutzerdefinierte Klassen angepasst werden: Der
# Funktionsaufruf `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und
# ruft diese auf, falls sie existiert.

# %% [markdown] {"lang": "en"}
# By defining the method `__repr__(self)`, the string returned by `repr` can be defined for custom classes: The
# call `repr(x)` checks if `x` has a method `__repr__` and calls it if it exists.

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
class PointV4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV4(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% {"tags": ["code-along"]}
p1 = PointV4(2, 5)
print(repr(p1))

# %% [markdown] {"delegiert": null, "incorrectly_encoded_metadata": "slideshow={\"slide_type\": \"subslide\"} Standardm\u00e4\u00dfig", "lang": "de"}
# Die Funktion `str` delegiert an `repr`, falls keine `__str__`-Methode definiert ist:
#

# %% [markdown] {"lang": "en"}
# The function `str` delegates to `repr` if no `__str__` method is defined:

# %% {"tags": ["code-along"]}
print(str(p1))


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Python offers many dunder methods: see the documentation of the 
# [Python data model](https://docs.python.org/3/reference/datamodel.html).

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
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


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(2, 4)

# %% {"tags": ["code-along"]}
p1 == p2

# %% {"tags": ["code-along"]}
p2 == p3

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
p3 = p1 + p2
p3

# %% {"tags": ["code-along"]}
p3 = p1 - Point(3, 2)
p3

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
print(p1)
print(p1 * 3)
print(3 * p1)

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
print(p2)
p2 += p1
p2


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Kraftfahrzeuge (Teil 3)"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `lecture_045x_Workshop_Custom_Datatypes`
# - Section "Motor Vehicles (Part 3)"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Es ist möglich eigene Typen zu definieren, die sich wie Listen verhalten:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# It is possible to define custom types that behave like lists:

# %% {"tags": ["code-along"]}
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


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
my_list_1 = MyBadList()
my_list_2 = MyBadList()
my_list_3 = MyBadList([1, 2, 3])
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
my_list_1.append("a")
my_list_1.append("b")
my_list_1.append("c")
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% {"tags": ["code-along"]}
print(len(my_list_1))
print(my_list_1[0])
# print(my_list_1[10])

# %% {"tags": ["code-along"]}
for elt in my_list_1:
    print(elt)

# %% {"tags": ["code-along"]}
my_list_1[1:]


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation
# und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html)
# beinhaltet weitere Möglichkeiten.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Dataclasses
#
# Definition of a class in which attributes are more visible, representation
# and equality are predefined, etc.
#
# The [documentation](https://docs.python.org/3/library/dataclasses.html)
# includes other options.

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
from dataclasses import dataclass


@dataclass
class DataPoint:
    x: float
    y: float


# %% {"tags": ["code-along"]}
dp = DataPoint(2, 3)
dp

# %% {"tags": ["code-along"]}
dp1 = DataPoint(1, 1)
dp2 = DataPoint(1, 1)
print(dp1 == dp2)
print(dp1 is dp2)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
@dataclass
class Point3D:
    x: float
    y: float
    z: float = 0.0

    # Non-destructive move!
    def move(self, dx=0.0, dy=0.0, dz=0.0):
        return Point3D(self.x + dx, self.y + dy, self.z + dz)


# %% {"tags": ["code-along"]}
p3d = Point3D(1.0, 2.0)
print(p3d)
print(p3d.move(dy=1.0, dz=5.0))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Dataclasses erzwingen, dass alle Default-Werte unveränderlich sind:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Dataclasses ensure that all default values are immutable:

# %% {"tags": ["code-along"]}
from dataclasses import dataclass, field

@dataclass
class DefaultDemo:
    # item: list = []
    items: list = field(default_factory=list)


# %% {"tags": ["code-along"]}
d1 = DefaultDemo()
d2 = DefaultDemo()

# %% {"tags": ["code-along"]}
d1.items.append(1234)
print(d1)
print(d2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Einkaufsliste"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - Notebook `workshop_062_objects`
# - "Shopping list" section

# %%
