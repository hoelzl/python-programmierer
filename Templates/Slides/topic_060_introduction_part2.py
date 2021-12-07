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
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Einführung in Python: Grundlagen Teil 2") }}


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Vergleiche, Boole'sche Werte

# %% [markdown]
# Gleichheit von Werten wird mit `==` getestet:

# %% {{ doc.codealong() }}
1 == 1

# %% {{ doc.codealong() }}
1 == 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %% {{ doc.codealong() }}
type(True)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Gleichheit von Zahlen

# %% {{ doc.codealong() }}
1 == 1.0

# %% [markdown]
# Mit Unterstrichen lassen sich Zahlen übersichtlicher schreiben.

# %% {{ doc.codealong() }}
0.000_000_1 * 10_000_000 == 1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Vorsicht: Rundungsfehler!

# %% {{ doc.codealong() }}
1 / 10

# %% {{ doc.codealong() }}
1 / 100

# %% {{ doc.codealong() }}
(1 / 10) * (1 / 10) == (1 / 100)

# %% {{ doc.codealong() }}
0.1 * 0.1

# %% {{ doc.codealong() }}
0.1 - 0.01

# %% {{ doc.codealong() }}
100 * 1.1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %% {{ doc.codealong() }}
1 != 1.0

# %% {{ doc.codealong() }}
1 != 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Vergleich von Zahlen

# %% {{ doc.codealong() }}
1 < 2

# %% {{ doc.codealong() }}
1 < 1

# %% {{ doc.codealong() }}
1 <= 1

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
1 > 2

# %% {{ doc.codealong() }}
2 >= 1

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Operatoren auf Boole'schen Werten
#

# %% {{ doc.codealong() }}
1 < 2 and 3 < 2

# %% {{ doc.codealong() }}
1 < 2 or 3 < 2

# %% {{ doc.codealong() }}
not (1 < 2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Wann ist ein logischer Ausdruck wahr?
#
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Verkettung von Vergleichen

# %% {{ doc.codealong() }}
1 < 2 < 3

# %% {{ doc.codealong() }}
# noinspection PyChainedComparisons
1 < 2 and 2 < 3

# %% {{ doc.codealong() }}
1 < 3 <= 2

# %% {{ doc.codealong() }}
# noinspection PyChainedComparisons
1 < 3 and 3 <= 2


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_012x_Workshop_Einführung in Python (Teil 2)`
# - Abschnitt "Operatoren, Vergleiche"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # `if`-Anweisungen
#
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Wir benötigen dazu die `if`-Anweisung:

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")

    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")

    print("Wir wünschen Ihnen alles Gute.")


# %% {{ doc.codealong() }}
ist_glückszahl(1)

# %% {{ doc.codealong() }}
ist_glückszahl(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# %% {{ doc.codealong() }}
ist_glückszahl_2(1)

# %% {{ doc.codealong() }}
ist_glückszahl_2(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def einseitiges_if_1(zahl):
    print("Vorher")

    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")

    print("Nachher")


# %% {{ doc.codealong() }}
einseitiges_if_1(1)

# %% {{ doc.codealong() }}
einseitiges_if_1(7)


# %% {"slideshow": {"slide_type": "subslide"}}
def einseitiges_if_2(zahl):
    if zahl % 2 != 0:
        zahl += 1  # zahl = zahl + 1
    print(zahl)


# %% {{ doc.codealong() }}
einseitiges_if_2(1)

# %% {{ doc.codealong() }}
einseitiges_if_2(6)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Struktur einer `if`-Anweisung (unvollständig):
#
# ```python
# if <Bedingung>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein
#

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_012x_Workshop_Einführung in Python (Teil 2)`
# - Abschnitt "Volljährig"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Listen

# %%
warenkorb = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %% [markdown]
# Der Typ von Listen ist `list`.

# %% {{ doc.codealong() }}
type(warenkorb)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern
#   einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %% {"slideshow": {"slide_type": "subslide"}}
liste_1 = [1, 2, 3, 4, 5]
liste_2 = ["string1", "another string"]

# %% {{ doc.codealong() }}
print(liste_1)

# %% {{ doc.codealong() }}
print(liste_2)

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
liste_3 = []
liste_4 = [1, 0.4, "ein String", True, None]

# %% {{ doc.codealong() }}
print(liste_3)

# %% {{ doc.codealong() }}
print(liste_4)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"
warenkorb = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]
warenkorb

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Nachdem eine Liste erzeugt ist hat sie keine Verbindung zu den Variablen, die
# in ihrer Konstruktion verwendet wurden:

# %% {{ doc.codealong() }}
produkt_1 = "Dinkelflocken"
produkt_2 = "Teebeutel"
warenkorb

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
#
# Mit der Funktion `list` können manche andere Datentypen in Listen umgewandelt
# werden.
#
# Im Moment kennen wir nur Listen, Strings und Dictionaries als mögliche
# Argumenttypen:

# %% {{ doc.codealong() }}
list("abc")

# %% {{ doc.codealong() }}
list([1, 2, 3])

# %% {{ doc.codealong() }}
list({"a": 1, "b": 2})

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": ""}}
# ## Zugriff auf Listenelemente

# %%
zahlenliste = [0, 1, 2, 3]

# %% {{ doc.codealong() }}
zahlenliste[0]

# %% {{ doc.codealong() }}
zahlenliste[3]

# %% {{ doc.codealong() }}
zahlenliste[-1]

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Länge einer Liste

# %%
zahlenliste

# %% {{ doc.codealong() }}
len(zahlenliste)

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Modifikation von Listeneinträgen

# %% {{ doc.codealong() }}
zahlenliste[1] = 10
zahlenliste

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Anhängen von Elementen an eine Liste

# %% {{ doc.codealong() }}
zahlenliste.append(40)
zahlenliste

# %% {{ doc.codealong() }}
zahlenliste.extend([50, 60])
zahlenliste

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %% {"slideshow": {"slide_type": "subslide"}}
zahlenliste = [0, 1, 2, 3, 4]
zahlenliste

# %% {{ doc.codealong() }}
for zahl in zahlenliste:
    print("Die Zahl ist:", zahl)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Syntax der `for`-Schleife
#
# ```python
# for <element-var> in <liste>:
#     <rumpf>
# ```

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - Notebook `lecture_012x_Workshop_Einführung in Python (Teil 2)`
# - Abschnitt "Einkaufsliste"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Simulation der klassischen `for`-Schleife
#
# Iteration mit einer `for`-Schleife ist auch über andere Datenstrukturen als Listen möglich.
#
# In Python stellt der Typ `range` eine Folge von ganzen Zahlen dar:
#
# - `range(n)` erzeugt das ganzzahlige Interval von $0$ bis $n-1$
# - `range(m, n)` erzeugt das ganzzahlige Interval von $m$ bis $n-1$
# - `range(m, n, k)` erzeugt die ganzzahlige Sequenz $m, m+k, m+2k, ..., p$, wobei $p$ die größte Zahl der Form $m + jk$ mit $j \geq 0$ und $p < n$ ist

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
range(3)

# %% {{ doc.codealong() }}
list(range(3))

# %% {{ doc.codealong() }}
list(range(3, 23, 5))

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
for i in range(3):
    print(i)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `lecture_012x_Workshop_Einführung in Python (Teil 2)`
# - Abschnitt "Ausgabe von Quadratzahlen"

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings umgewandelt
# werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %% {{ doc.codealong() }}
print(str("Hallo!"))

# %% {{ doc.codealong() }}
print(repr("Hallo!"))

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "subslide"}}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %% {{ doc.codealong() }}
print(str(['a', 'b', 'c']))
print(repr(['a', 'b', 'c']))


# %% [markdown] slideshow={"slide_type": "slide"}
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen (Klassen) definiert werden:

# %% {{ doc.codealong() }}
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

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
p1 = PointV0()
p1

# %% {{ doc.codealong() }}
print(p1)

# %% {{ doc.codealong() }}
p2 = PointV0()
p1 == p2

# %% {{ doc.codealong() }}
# Fehler
# p1 < p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Ähnlich wie Dictionaries neue Einträge zugewiesen werden können, kann man
# benutzerdefinierten Datentypen neue *Attribute* zuweisen, allerdings verwendet
# man die `.`-Notation statt der Indexing Notation `[]`:

# %% {{ doc.codealong() }}
# Möglich, aber nicht gut...
p1.x = 1.0
p1.y = 2.0
print(p1.x)
print(p1.y)


# %% {{ doc.codealong() }}
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

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
class PointV1:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


# %% {{ doc.codealong() }}
p1 = PointV1()
p2 = PointV1()
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)

# %% {{ doc.codealong() }}
p1 == p2

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Die Werte von Attributen können verändert werden:

# %% {{ doc.codealong() }}
p1.x = 1.0
p1.y = 2.0
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


# %% [markdown] slideshow={"slide_type": "subslide"}
#
# In vielen Fällen wäre es besser, bei der Konstruktion eines Objekts Werte für
# die Attribute anzugeben. Das ist möglich, indem man der `__init__()`-Methode
# zusätzliche Parameter gibt.

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %% {{ doc.codealong() }}
p1 = PointV2(2.0, 3.0)
p2 = PointV2(0.0, 0.0)
print("p1: x =", p1.x, "y =", p1.y)
print("p2: x =", p2.x, "y =", p2.y)


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

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
class PointV3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0.0, dy=0.0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
p = PointV3(2, 3)
print("x =", p.x)
print("y =", p.y)

# %% {{ doc.codealong() }}
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

# %% {{ doc.codealong() }}
print(str(p1))
print(repr(p1))


# %% [markdown]
# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
class PointV4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV4(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% {{ doc.codealong() }}
p1 = PointV4(2, 5)
print(repr(p1))

# %% [markdown] slideshow={"slide_type": "subslide"}
# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
#

# %% {{ doc.codealong() }}
print(str(p1))


# %% [markdown] slideshow={"slide_type": "subslide"}
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
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


# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
p1 = Point(1, 2)
p2 = Point(2, 4)
p3 = Point(2, 4)

# %% {{ doc.codealong() }}
p1 == p2

# %% {{ doc.codealong() }}
p2 == p3

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
p3 = p1 + p2
p3

# %% {{ doc.codealong() }}
p3 = p1 - Point(3, 2)
p3

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
print(p1)
print(p1 * 3)
print(3 * p1)

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
print(p2)
p2 += p1
p2


# %% [markdown] slideshow={"slide_type": "subslide"}
#
#  ## Mini-Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Kraftfahrzeuge (Teil 2)"

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Es ist möglich eigene Typen zu definieren, die sich wie Listen verhalten:

# %% {{ doc.codealong() }}
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


# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
my_list_1 = MyBadList()
my_list_2 = MyBadList()
my_list_3 = MyBadList([1, 2, 3])
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
my_list_1.append("a")
my_list_1.append("b")
my_list_1.append("c")
print(my_list_1)
print(my_list_2)
print(my_list_3)

# %% {{ doc.codealong() }}
print(len(my_list_1))
print(my_list_1[0])
# print(my_list_1[10])

# %% {{ doc.codealong() }}
for elt in my_list_1:
    print(elt)

# %% {{ doc.codealong() }}
my_list_1[1:]

# %% [markdown]
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation
# und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html)
# beinhaltet weitere Möglichkeiten.

# %% {{ doc.codealong() }}
from dataclasses import dataclass


@dataclass
class DataPoint:
    x: float
    y: float


# %% {{ doc.codealong() }}
dp = DataPoint(2, 3)
dp

# %% {{ doc.codealong() }}
dp1 = DataPoint(1, 1)
dp2 = DataPoint(1, 1)
print(dp1 == dp2)
print(dp1 is dp2)


# %% {{ doc.codealong() }}
@dataclass
class Point3D:
    x: float
    y: float
    z: float = 0.0

    # Non-destructive move!
    def move(self, dx=0.0, dy=0.0, dz=0.0):
        return Point3D(self.x + dx, self.y + dy, self.z + dz)


# %% {{ doc.codealong() }}
p3d = Point3D(1.0, 2.0)
print(p3d)
print(p3d.move(dy=1.0, dz=5.0))

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Dataclasses erzwingen, dass alle Default-Werte unveränderlich sind:

# %% {{ doc.codealong() }}
from dataclasses import dataclass, field


@dataclass
class DefaultDemo:
    # item: list = []
    items: list = field(default_factory=list)


# %% {{ doc.codealong() }}
d1 = DefaultDemo()
d2 = DefaultDemo()

# %% {{ doc.codealong() }}
d1.items.append(1234)
print(d1)
print(d2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - Notebook `lecture_045x_Workshop_Benutzerdefinierte_Datentypen`
# - Abschnitt "Einkaufsliste"

# %%
