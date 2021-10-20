# -*- coding: utf-8 -*-
# %% [markdown]
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Vererbung und Ausnahmebehandlung</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Vererbung

# %%
import random
class Point:
    def __init__(self, x=0.0, y=0.0):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0.0, dy=0.0):
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
    def __init__(self, x=0.0, y=0.0, color='black'):
        super().__init__(x, y)
        self.color = color
    
#     def __repr__(self):
#         return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

#     def randomize(self):
#         super().randomize()
#         self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


# %%
cp = ColorPoint(2, 3, 'red')
cp, type(cp)

# %%
cp.move(2, 3)
# cp

# %%
cp.randomize()
# cp

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_048x_Workshop_Vererbung`
# - Abschnitt "Vererbung"


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
# ## Mini-Workshop
#
# - Notebook `lecture_048x_Workshop_Vererbung`
# - Abschnitt "Bank Account"

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


# %% [markdown] slideshow={"slide_type": "slide"}
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet
# haben verloren.
#
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu
# speichern:

# %% slideshow={"slide_type": "subslide"}
import os

# %%
os.getcwd()

# %% [markdown] slideshow={"slide_type": "subslide"}
#
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
#
# Dateien müssen immer mit `close` geschlossen werden, auch wenn der
# Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen
# wird. Das könnte mit `try ... finally` erfolgen.
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
# - Notebook `lecture_048x_Workshop_Vererbung`
# - Abschnitt "Lesen und Schreiben in Dateien"
#
