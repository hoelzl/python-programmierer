#!/usr/bin/env python
# coding: utf-8

# %% [markdown]
#
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Kontrollstrukturen<br/><br/>
# Mit Exkursen in Vererbung, Ausnahmebehandlung und Dateien</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown]
#
# # Namensräume
#
# Variablen und Funktionsnamen existieren in einem *Namensraum (Namespace)*.
#
# - Globale Variablen und Funktionsnamen sind im globalen Namensraum.
# - Mit `import` importierte Namen existieren im importierten Namensraum.
# - Namen, die innerhalb einer Funktion definiert werden sind im Namensraum dieser Funktion.
#     - Parameter
#     - lokale Variablen
#
# Der Namensraum einer Funktion "verschwindet" am Ende des Rumpfs.

# %%
# Ohne Angabe der Namensräume, siehe nächste Folie
a = 1


def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)


f(2)
print(a)
# print(x)

# %%
a = 1  # Globaler Namespace


def f(x):  # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1  # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)  # Greift auf a aus dem Namespace von f zu


f(2)
print(a)  # Greift auf a aus dem globalen Namespace zu
# print(x)              # Fehler: x ist im Namespace von f

# %%
a = 1


def f2():
    global a
    a = 4
    print(a)


f2()
print(a)
a = 5
print(a)

# %% [markdown]
#
# # `if`-Anweisung
#
# Wiederholung:

# %%
def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")
    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")
    print("Wir wünschen Ihnen alles Gute.")


# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Gerade Zahl"
#

# %% [markdown]
#
# ## Mehrere Zweige
#
# - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und 100 erraten muss.
# - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch, zu niedrig oder richtig war angezeigt.
# - Später wollen wir dem Spieler mehrere Versuche erlauben.

# %%
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl(10, 12)

# %%
klassifiziere_zahl(14, 12)

# %%
klassifiziere_zahl(12, 12)

# %% [markdown]
#
# ## Struktur einer `if`-Anweisung (vollständig):
#
# ```python
# if <Bedingung 1>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# elif <Bedingung 2>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 2 wahr ist
# ...
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Positiv/Negativ"
#

# %% [markdown]
#
# ### Bessere Klassifizierung
#
# Wir wollem dem Spieler etwas mehr Information geben, wie nahe er an der
# richtigen Lösung ist:
#
# - Die geratene Zahl ist viel zu klein/zu groß wenn der Unterschied größer als
#   10 ist

# %%
def klassifiziere_zahl_2(geratene_zahl, lösung):
    if geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl_2(1, 12)

# %%
klassifiziere_zahl_2(10, 12)

# %%
klassifiziere_zahl_2(14, 12)

# %%
klassifiziere_zahl_2(24, 12)

# %%
klassifiziere_zahl_2(12, 12)

# %% [markdown]
#
# Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# %%
def klassifiziere_zahl_3(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl < lösung - 10:
        print("Die geratene Zahl ist viel zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    elif geratene_zahl > lösung + 10:
        print("Die geratene Zahl ist viel zu groß!")
    else:
        print("Sie haben gewonnen!")


# %%
klassifiziere_zahl_3(1, 12)

# %%
klassifiziere_zahl_3(100, 12)

# %% [markdown]
#
# ## Return aus einem `if`-Statement
#
# Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um einen Wert aus einer Funktion zurückzugeben:

# %%
def ist_große_zahl(zahl):
    if zahl > 10:
        return True
    else:
        return False


# %% [markdown]
#
# Es können auch mehrere Werte aus einem `if`-Statement zurückgegeben werden:

# %%
def klassifiziere_zahl_4(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        return False, "Die geratene Zahl ist zu klein!"
    elif geratene_zahl > lösung:
        return False, "Die geratene Zahl ist zu groß!"
    else:
        return True, "Sie haben gewonnen!"


# %%
gewonnen, text = klassifiziere_zahl_4(1, 10)
print(gewonnen)
print(text)

# %%
gewonnen, text = klassifiziere_zahl_4(15, 10)
print(gewonnen)
print(text)

# %%
gewonnen, text = klassifiziere_zahl_4(10, 10)
print(gewonnen)
print(text)

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Signum"
#

# %% [markdown]
#
# # Benutzereingaben
#
# - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
# - Optional kann sie einen Eingabeprompt ausgeben.
# - Die Funktion gibt den vom Benutzer eingegebenen Text als String zurück.

# %%
# input("What is your name? ")

# %%
def query_name():
    name = input("What is your name? ")
    print(f"You entered {name}")


# %%
# query_name()

# %% [markdown]
#
# ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius zurückgibt.

# %%
def konvertiere_fahrenheit_nach_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# %%
konvertiere_fahrenheit_nach_celsius(32)

# %%
konvertiere_fahrenheit_nach_celsius(90)

# %%
def temperaturkonverter_1():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
    print(f"{fahrenheit}F sind {celsius}°C")


# %%
float("1.23")

# %%
# temperaturkonverter_1()

# %%
def temperaturkonverter_2():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{fahrenheit}F sind {celsius}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %%
# temperaturkonverter_2()

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen"
#

# %%
def temperaturkonverter_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit:
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{fahrenheit}F sind {celsius}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %%
# temperaturkonverter_3()

# %% [markdown]
#
# # Wahrheitswerte: Truthiness
#
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen, nicht nur Boole'sche Werte.
#
# Folgende Werte gelten als *nicht wahr*
#
# - `None` und `False`
# - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
# - Leere Strings, Sequences und Collections: ``
#
# Alle anderen Werte gelten als wahr.

# %%
if -1:
    print("-1 ist wahr")
elif 0:
    print("0 ist wahr")
else:
    print("Alles ist falsch")

# %%
if 0:
    print("0 ist wahr")
else:
    print("0 ist falsch")

# %%
if "":
    print("'' ist wahr")
else:
    print("'' falsch")

# %%
if print("Hallo"):
    print("None ist wahr")
else:
    print("None ist falsch")

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen mit Truthiness"
#

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Kino-Preis"
#

# %% [markdown]
#
# ## Hinweis: Umwandeln eines Strings in Kleinbuchstaben

# %%
text = "Das ist ein Text"
print(text.lower())
print(text)

# %%
"Das ist ein Text".upper()

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Shout"
#

# %% [markdown]
#
# # While-Schleifen
#
# Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
# - Zahlenraten bis die richtige Zahl gefunden wurde
# - Physik-Simulation bis das Ergebnis genau genug ist
# - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
# Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen, verwenden wir dafür in der Regel eine While-Schleife.

# %%
number = 0
while number < 3:
    print(f"Durchlauf {number}")
    number += 1  # <==

# %%
def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print(f"Versuch Nr. {versuch_nr} gestartet...", end="")
    from random import random

    if random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False


# %%
versuch_nr = 0

while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1

print("Wir haben einen erfolgreichen Versuch ausgeführt.")

# %% [markdown]
#
# ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine Schleife vorzeitig beenden:

# %%
i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)

# %%
def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# %%
# annoy_user()

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Ratespiele"
#

# # Vererbung

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
cp

# %%
cp.move(2, 3)
cp

# %%
cp.randomize()
cp

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Vererbung"
#

# %% [markdown]
#
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m` zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
#
# Einige Lösungsversuche:

# %%
def int_sqrt_with_pair(n: int) -> Tuple[int, bool]:
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False


# %%

# %%
int_sqrt_with_pair(9)

# %%
int_sqrt_with_pair(8)

# %%
int_sqrt_with_pair(0)

# %%
int_sqrt_with_pair(1)

# %%
def print_int_sqrt_1(n):
    root, is_valid = int_sqrt_with_pair(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_1(8)

# %%
def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1


# %%
int_sqrt_with_negative_value(9)

# %%
int_sqrt_with_negative_value(8)

# %%
def print_int_sqrt_2(n):
    root = int_sqrt_with_negative_value(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_2(8)

# %%
def print_int_sqrt_2_better(n):
    root = int_sqrt_with_negative_value(8)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")


print_int_sqrt_2_better(8)

# %% [markdown]
#
# Beide Ansätze haben mehrere Probleme:
# - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit
#   einem falschen Wert weitergerechnet.
# - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über
#   mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden. Das führt zu
#   unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur
#   Fehlerbehandlung getrennt ist.
#
# Eine bessere Lösung:

# %%
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# %%
int_sqrt(9)

# %%
int_sqrt(0)

# %%
int_sqrt(1)

# %%
# int_sqrt(8)

# %%
def print_int_sqrt(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %%
# print_int_sqrt(8)

# %%
def print_int_sqrt_no_error(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(str(error))


# %%
print_int_sqrt_no_error(9)

# %%
print_int_sqrt_no_error(8)

# %%
def print_int_sqrt_no_error_2(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError:
        print(f"{n} does not have a root!")
    finally:
        print("And that's all there is to say about this topic.")


# %%
print_int_sqrt_no_error_2(9)

# %%
print_int_sqrt_no_error_2(8)

# %% [markdown]
#
# ## Fehlerklassen
#
# In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene
# Fehlerarten signalisiert werden können:
# - `Exception`: Basisklasse aller behandelbaren Exceptions
# - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#   - OverflowError
#   - ZeroDivisionError
# - `LookupError`: Basisklasse wenn ein ungültiger Index für eine Datenstruktur
#   verwendet wurde
# - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
# - `EOFError`: Fehler wenn `intput()` unerwartet das Ende einer Datei erreicht
# - ...
#
# Die Liste der in der Standardbibliothek definierten Fehlerklassen ist
# [hier](https://docs.python.org/3/library/exceptions.html).

# %%
class NoRootError(ValueError):
    pass


# %%
try:
    raise ValueError("ValueError")
    # raise NoRootError("This is a NoRootError.")
except NoRootError as error:
    print(f"Case 1: {error}")
except ValueError as error:
    print(f"Case 2: {error}")

# %%
my_var = 1
assert my_var == 1

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "Knobeln"
#

# %% [markdown]
#
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet haben verloren.
#
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu speichern:

# %%
import os

# %%
os.getcwd()

# %% [markdown]
#
# - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
# - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet
#   wird:
#   - `r`: Lesen
#   - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#   - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#   - `x`: Schreiben. Die Datei darf nicht existieren.
#   - `r+`: Lesen und Schreiben.
# - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als
#   Binärdatei behandelt.
# - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei
#   abgefragt oder verändert werden.

# %%
file = open("my-data-file.txt", "w")
file.write("The first line.\n")
file.write("The second line.\n")
file.close()

# %%
file = open("my-data-file.txt", "r")
contents = file.read()
print(contents)
file.close()
contents

# %%
file = open("my-data-file.txt", mode="w")
file.write("Another line.\n")
file.write("Yet another line.\n")
file.close()

# %%
file = open("my-data-file.txt", mode="r")
contents = file.read()
print(contents)
file.close()

# %%
file = open("my-data-file.txt", mode="a")
file.write("Let's try this again.\n")
file.write("Until we succeed.\n")
file.close()

# %%
file = open("my-data-file.txt", "r")
contents = file.read()
print(contents)
file.close()

# %% [markdown]
#
# Dateien müssen immer mit `close` geschlossen werden, auch wenn der
# Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen
# wird. Das könnte mit `try ... finally` erfolgen.
#
# Python bietet dafür ein eleganteres Konstrukt:

# %%
with open("my-data-file.txt", "r") as file:
    contents = file.read()
print(contents)

# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File position before reading: {file.tell()}")
    contents = file.read()
    print(f"File position after reading: {file.tell()}")
    file.write("Another line.\nAnd another.")
    print(f"File position after writing: {file.tell()}")

# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File has {len(file.readlines())} lines.")
    file.seek(40)
    file.write("overwrite a part of the file, yes?")
    file.seek(0)
    print(file.read())

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "# Lesen und Schreiben in Dateien"
#

# %% [markdown]
#
# # Context Managers
#
# Context Manager sind Objekte, die häufig verwendete `try-except-finally`
# Patterns für `with`-Blöcke kapseln.

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
        print(".", end="\n" if self.num_completed_items % self.width == 0 else "")
        sys.stdout.flush()

    def item_skipped(self):
        self.num_completed_items += 1
        print("-", end="\n" if self.num_completed_items % self.width == 0 else "")
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

# %%
