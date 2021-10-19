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

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
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

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
print(str(['a', 'b', 'c']))
print(repr(['a', 'b', 'c']))


# %% [markdown] slideshow={"slide_type": "slide"}
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen definiert werden:

# %%
class PointV0:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %%
p = PointV0(2, 3)
p

# %%
print("x =", p.x)
print("y =", p.y)


# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Methoden
#
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf dem
# die Methode aufgerufen wird muss als erster Parameter angegeben werden.
#
# Per Konvention hat dieser Parameter den Namen `self`.

# %% slideshow={"slide_type": "subslide"}
class PointV1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"}
p = PointV1(2, 3)
print("x =", p.x)
print("y =", p.y)

# %%
p.move(3, 5)
print("x =", p.x)
print("y =", p.y)

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Das Python-Objektmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# %%
print(str(p))
print(repr(p))


# %% [markdown] pycharm={"name": "#%% md\n"}
# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# %% slideshow={"slide_type": "subslide"}
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV2(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = PointV2(2, 5)
print(repr(p))

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
#

# %%
print(str(p))


# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
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

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %% slideshow={"slide_type": "subslide"}
p1 = Point(1, 2)
p2 = Point(2, 4)
p = p1 + p2
p


# %%
p += p1
p

# %%
p3 = p - Point(3, 2)
p3

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Workshop
#
# - Notebook `lecture_012x_Workshop_Einführung in Python (Teil 2)`
# - Abschnitt "Verbesserte Einkaufsliste"

# %% [markdown]
# ## Dataclasses
#
# Definition einer Klasse, in der Attribute besser sichtbar sind, Repräsentation und Gleichheit vordefiniert sind, etc.
#
# Die [Dokumentation](https://docs.python.org/3/library/dataclasses.html) beinhaltet weitere Möglichkeiten.

# %%
from dataclasses import dataclass

@dataclass
class DataPoint:
    x: float
    y: float


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


# %% [markdown] slideshow={"slide_type": "slide"}
# # Vererbung

# %%
import random
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


# %% slideshow={"slide_type": "subslide"}
p = Point(0, 0)
p

# %%
p.move(2, 3)
p

# %%
p.randomize()
p


# %% slideshow={"slide_type": "subslide"}
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color='black'):
        super().__init__(x, y)
        self.color = color
    
    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# %%
cp = ColorPoint(2, 3, 'red')
# cp

# %%
cp.move(2, 3)
# cp

# %%
cp.randomize()
# cp

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Vererbung"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m` zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
#
# Einige Lösungsversuche:

# %% slideshow={"slide_type": "subslide"}
def int_sqrt_with_pair(n: int) -> tuple[int, bool]:
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False


# %% slideshow={"slide_type": "subslide"}
int_sqrt_with_pair(9)

# %%
int_sqrt_with_pair(8)

# %%
int_sqrt_with_pair(0)

# %%
int_sqrt_with_pair(1)


# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt_1(n):
    root, is_valid = int_sqrt_with_pair(8)
    print(f"The root of {n} is {root}.")

print_int_sqrt_1(8)


# %% slideshow={"slide_type": "subslide"}
def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1


# %% slideshow={"slide_type": "subslide"}
int_sqrt_with_negative_value(9)

# %%
int_sqrt_with_negative_value(8)


# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt_2(n):
    root = int_sqrt_with_negative_value(8)
    print(f"The root of {n} is {root}.")

print_int_sqrt_2(8)


# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt_2_better(n):
    root = int_sqrt_with_negative_value(8)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")

print_int_sqrt_2_better(8)


# %% [markdown] slideshow={"slide_type": "subslide"}
# Beide Ansätze haben mehrere Probleme:
# - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit einem falschen Wert weitergerechnet.
# - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden. Das führt zu unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur Fehlerbehandlung getrennt ist.
#
# Eine bessere Lösung:

# %% slideshow={"slide_type": "subslide"}
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# %% slideshow={"slide_type": "subslide"}
int_sqrt(9)

# %%
int_sqrt(0)

# %%
int_sqrt(1)


# %% slideshow={"slide_type": "subslide"}
# int_sqrt(8)

# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %% slideshow={"slide_type": "subslide"}
# print_int_sqrt(8)

# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt_no_error(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(str(error))


# %% slideshow={"slide_type": "subslide"}
print_int_sqrt_no_error(9)

# %% slideshow={"slide_type": "-"}
print_int_sqrt_no_error(8)


# %% slideshow={"slide_type": "subslide"}
def print_int_sqrt_no_error_2(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError:
        print(f"{n} does not have a root!")
    finally:
        print("And that's all there is to say about this topic.")


# %% slideshow={"slide_type": "subslide"}
print_int_sqrt_no_error_2(9)

# %%
print_int_sqrt_no_error_2(8)


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Fehlerklassen
#
# In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene Fehlerarten signalisiert werden können:
# - `Exception`: Basisklasse aller behandelbaren Exceptions
# - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#   - OverflowError
#   - ZeroDivisionError
# - `LookupError`: Basisklasse wenn ein ungültiger Index für eine Datenstruktur verwendet wurde
# - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
# - `EOFError`: Fehler wenn `intput()` unerwartet das Ende einer Datei erreicht
# - ...
#
# Die Liste der in der Standardbibliothek definierten Fehlerklassen ist [hier](https://docs.python.org/3/library/exceptions.html).

# %% slideshow={"slide_type": "subslide"}
class NoRootError(ValueError):
    pass


# %% slideshow={"slide_type": "-"}
try:
    raise ValueError("ValueError")
    # raise NoRootError("This is a NoRootError.")
except NoRootError as error:
    print(f"Case 1: {error}")
except ValueError as error:
    print(f"Case 2: {error}")

# %% slideshow={"slide_type": "subslide"}
my_var = 1
assert my_var == 1

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Knobeln"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet haben verloren.
#
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu speichern:

# %% slideshow={"slide_type": "subslide"}
import os

# %%
os.getcwd()

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
# - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet wird:
#   - `r`: Lesen
#   - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#   - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#   - `x`: Schreiben. Die Datei darf nicht existieren.
#   - `r+`: Lesen und Schreiben.
# - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als Binärdatei behandelt.
# - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei abgefragt oder verändert werden.

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', 'w')
file.write("The first line.\n")
file.write("The second line.\n")
file.close()

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', 'r')
contents = file.read()
print(contents)
file.close()
contents

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', mode='w')
file.write("Another line.\n")
file.write("Yet another line.\n")
file.close()

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', mode='r')
contents = file.read()
print(contents)
file.close()

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', mode='a')
file.write("Let's try this again.\n")
file.write("Until we succeed.\n")
file.close()

# %% slideshow={"slide_type": "subslide"}
file = open('my-data-file.txt', 'r')
contents = file.read()
print(contents)
file.close()

# %% [markdown] slideshow={"slide_type": "subslide"}
# Dateien müssen immer mit `close` geschlossen werden, auch wenn der Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen wird. Das könnte mit `try ... finally` erfolgen.
#
# Python bietet dafür ein eleganteres Konstrukt:

# %%
with open('my-data-file.txt', 'r') as file:
    contents = file.read()
print(contents)

# %% slideshow={"slide_type": "subslide"}
with open('my-data-file.txt', 'r+') as file:
    print(f"File position before reading: {file.tell()}")
    contents = file.read()
    print(f"File position after reading: {file.tell()}")
    file.write('Another line.\nAnd another.')
    print(f"File position after writing: {file.tell()}")   

# %% slideshow={"slide_type": "subslide"}
with open('my-data-file.txt', 'r+') as file:
    print(f"File has {len(file.readlines())} lines.")
    file.seek(40)
    file.write('overwrite a part of the file, yes?')
    file.seek(0)
    print(file.read())

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "# Lesen und Schreiben in Dateien"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Context Managers
#
# Context Manager sind Objekte, die häufig verwendete `try-except-finally` Patterns für `with`-Blöcke kapseln.

# %%
from contextlib import AbstractContextManager
import sys

class ProgressNotifier(AbstractContextManager):
    def __init__(self, entry_message, width=72):
        self.entry_message = entry_message
        self.width = width
        self.num_completed_items = 0

    def __enter__(self):
        print(f"{self.entry_message}")
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("failed!")
        else:
            print("done.")

    def item_completed(self):
        self.num_completed_items += 1
        print(".", end='\n' if self.num_completed_items % self.width == 0 else '')
        sys.stdout.flush()

    def item_skipped(self):
        self.num_completed_items += 1
        print("-", end='\n' if self.num_completed_items % self.width == 0 else '')
        sys.stdout.flush()


def progress(entry_message):
    return ProgressNotifier(entry_message)


# %%
import random

def download_items(n):
    with progress("Downloading articles") as p:
        for i in range(n):
            r = random.random()
            if r < 0.001:
                raise IOError("Download failed")
            elif r < 0.1:
                p.item_skipped()
            else:
                p.item_completed()


# %%
try:
    download_items(500)
    print("Finished successfully")
except IOError:
    print("Caught IOError")
