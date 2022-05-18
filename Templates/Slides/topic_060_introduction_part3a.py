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
# <div style="text-align:center; font-size:200%;"><b>Einführung in Python: Grundlagen Teil 3</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Introduction to Python: Part 3</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% "slideshow": [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Conversion to strings
#
# Python offers two functions that can be used to convert any value into a string:
#
# - `repr` for a "program-like" representation (how the value could be generated in the program)
# - `str` for "user-friendly" rendering

# %% {"tags": ["code-along"]}
print(str("Hallo!"))

# %% {"tags": ["code-along"]}
print(repr("Hallo!"))

# %% "slideshow": [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
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


# %% tags=["code-along"]
def print_point(name, p):
    print(f"{name}: x = {p.x}, y = {p.y}")


# %% {"tags": ["code-along"]}
p1 = PointV1()
p2 = PointV1()
print_point("p1", p1)
print_point("p2", p2)

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
print_point("p1", p1)
print_point("p2", p2)


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
print_point("p1", p1)
print_point("p2", p2)


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
# Klassen können Methoden enthalten. Methoden sind Funktionen, die
# "zu einem Objekt gehören". Wir werden im Abschnitt zu Vererbung sehen,
# welche Möglichkeiten sich dadurch bieten.
#
# Methoden werden mit der "Dot-Notation" aufgerufen: `my_object.method()`.
#
# Die Syntax von Methodendefinitionen entspricht Funktionsdefinitionen,
# steht aber im Rumpf einer Klassendefinition.
#
# Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf
# dem die Methode aufgerufen wird muss als erster Parameter angegeben werden.
# Per Konvention hat dieser Parameter den Namen `self`, wie bei der
# `__init__()`-Methode.
#
# Die Definition einer Methode, die mit `my_object.method()` aufgerufen
# werden kann erfolgt also folgendermaßen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Methods
#
# Classes can contain methods. Methods are functions that "belong to an object".
# We will see capabilities of methods that go beyond those of functions in the
# section on inheritance.
#
# Methods are called using "dot-notation": `my_object.method()`.
#
# Syntactically a method definion looks like a function definition, but nested
# inside the body of a class definition.
#
# Unlike many other languages, Python doesn't have an implicit `this` parameter
# when defining a method; the object on which the method is called must be
# specified as the first parameter of the definition. By convention, this
# parameter is named `self`, as in the `__init__()` method.
#
# The definition of a method that can be called with `my_object.method()` is thus
# as follows:

# %% {"slideshow": {"slide_type": "subslide"}}
class MyClass:
    def method(self):
        print(F"Called method on {self}")


# %%
my_object = MyClass()
my_object.method()


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# Wir können eine Methode zum Verschieben eines Punktes zu unserer `Point` Klasse hinzufügen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# We can add a method to move a point to our `Point` class:

# %% {"slideshow": {"slide_type": "-"}, "tags": ["code-along"]}
class PointV3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
p = PointV3(2, 3)
print_point("p", p)

# %% {"tags": ["code-along"]}
p.move(3, 5)
print_point("p", p)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Kraftfahrzeuge (Teil 2)"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_062_objects`
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


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
p1 = PointV4(2, 5)
print(repr(p1))

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
# Entsprechend kann eine `__str__()` Methode definiert werden, die von `str()`
# verwendet wird. Die Funktion `str()` delegiert an `__repr__()`, falls keine
# `__str__()`-Methode definiert ist:
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
#
# Similarly, if a `__str__()` method is defined it will be used by the `str()`
# function. However, the function `str()` delegates to `__repr__()` if no
# `__str__` method is defined:

# %% {"tags": ["code-along"]}
print(str(p1))

# %% tags=["code-along"]
print(p1)


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
        return f"Point({self.x!r}, {self.y!r})"

    def __eq__(self, rhs: object) -> bool:
        if isinstance(rhs, Point):
            return self.x == rhs.x and self.y == rhs.y
        return False

    def __add__(self, rhs):
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Point(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return Point(rhs * self.x, rhs * self.y)

    def __rmul__(self, lhs):
        return Point(lhs * self.x, lhs * self.y)

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
# - Notebook `workshop_062_objects`
# - Abschnitt "Kraftfahrzeuge (Teil 3)"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_062_objects`
# - Section "Motor Vehicles (Part 3)"

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


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
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

    def move(self, dx=0.0, dy=0.0, dz=0.0):
        self.x += dx
        self.y += dy
        self.z += dz


# %% {"tags": ["code-along"]}
p3d = Point3D(1.0, 2.0)
p3d

# %% {"tags": ["code-along"]}
p3d.move(dy=1.0, dz=5.0)
p3d

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Dataclasses erzwingen, dass Default-Werte unveränderlich sind (zumindest für einige Typen...):

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Dataclasses ensure that default values are immutable (at least for some types...):

# %% {"tags": ["code-along"]}
from dataclasses import dataclass, field


# %% {"tags": ["code-along"]}
@dataclass
class DefaultDemo:
    # items: list = []
    items: list = field(default_factory=list)


# %% {"tags": ["code-along"]}
d1 = DefaultDemo()
d2 = DefaultDemo()

# %% {"tags": ["code-along"]}
d1.items.append(1234)
print(d1)
print(d2)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# Der Test auf unveränderliche Defaults funktioniert aber nur für einige Typen aus der Standardbibliothek, nicht für benutzerdefinierte Typen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# However, the test for immutable defaults only works for some types from the standard library, not for user-defined types:

# %% {"tags": ["code-along"]}
@dataclass
class BadDefault:
    point: Point3D = Point3D(0.0, 0.0)


# %% {"tags": ["code-along"]}
bd1 = BadDefault()
bd2 = BadDefault()
bd1, bd2

# %% {"tags": ["code-along"]}
bd1.point.move(1.0, 2.0)
bd1, bd2


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
# Es ist möglich, koplexere Initialisierungen vorzunehmen:
#
# - Die `__post_init__()` Methode kann Code zur Initialisierung von Objekten
#   enthalten, der nach der generierten `__init__()` Methode ausgeführt wird.
# - Der Typ `InitVar[T]` deklariert, dass ein Klassen-Attribut als Argument an
#   `__post_init__()` übergeben und nicht als Instanz-Attribut verwendet wird.
# - Das Keyword-Argument `init=False` für `field()` bewirkt, dass ein Attribut
#   nicht in der generierten `__init__()` Methode initialisiert wird.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
#
# It is possible to perform more complex initializations:
#
# - The `__post_init__()` method can contain code that is executed after the
#   generated `__init__()` method has been executed.
# - The type `InitVar[T]` declasres that a class attribute serves as an argument
#   for the `__post_init__()` method and not as an attribute for the instance.
# - The keyword argument `init=False` for `field()` causes the corresponding
#   attribute to not be initialized in the generated `__init__()` method.

# %% {"tags": ["code-along"]}
from dataclasses import dataclass, field, InitVar

# %% {"tags": ["code-along"]}
@dataclass
class DependentInit:
    x: InitVar[float] = 0.0
    y: InitVar[float] = 0.0
    z: InitVar[float] = 0.0
    point: Point3D = field(init=False)
        
    def __post_init__(self, x, y, z):
        self.point = Point3D(x, y, z)

# %% {"tags": ["code-along"]}
bd1 = DependentInit()
bd2 = DependentInit(1.0, 2.0, 3.0)
bd1, bd2

# %% {"tags": ["code-along"]}
bd1.point.move(3.0, 5.0)
bd1, bd2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - Notebook `workshop_062_objects`
# - Abschnitt "Einkaufsliste"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - Notebook `workshop_062_objects`
# - Section "Shopping list"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# Es ist möglich einen Klasse zu definieren, deren Instanzen sich wie Listen verhalten. Um die Implementierung zu vereinfachen delegieren wir die Verwaltung der Elemente an eine Liste, die als Attribut gespeichert ist. Diese Form der Komposition findet man häufig in der objektorientierten Programmierung.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# It is possible to define a custom type whose instances behave like lists. To simplify the implementation we delegate the handling of the elements to a list that is stored as an attribute. This kind of composition is found very frequently in object oriented programming.

# %% {"tags": ["code-along"]}
class MyBadList:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def __getitem__(self, n):
        if isinstance(n, slice):
            return MyBadList(self.elements[n])
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


# %%
