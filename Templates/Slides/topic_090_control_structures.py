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
# <div style="text-align:center; font-size:200%;"><b>Kontrollstrukturen</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Control Structures</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  # `if`-Anweisung
#
#  Wiederholung:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # `if` statement
#
# Recall:

# %%
def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")
    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")
    print("Wir wünschen Ihnen alles Gute.")


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Extra Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Gerade Zahl"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Extra mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Even number section

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mehrere Zweige
#
#  - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#    100 erraten muss.
#  - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#    zu niedrig oder richtig war angezeigt.
#  - Später wollen wir dem Spieler mehrere Versuche erlauben.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Multiple branches
#
#  - We want to write a game in which the player has to guess a number between 1 and
#    100.
#  - After guessing, he gets the information whether his number is too high,
#    too low or correct.
#  - In a later iteration we want to give the player multiple tries.

# %%
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %% {"tags": ["code-along"]}
klassifiziere_zahl(10, 12)

# %% {"tags": ["code-along"]}
klassifiziere_zahl(14, 12)

# %% {"tags": ["code-along"]}
klassifiziere_zahl(12, 12)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Extra Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Positiv/Negativ"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Extra mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Section "Positive/Negative"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Struktur einer `if`-Anweisung (vollständig):
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
# - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende
#   Rumpf nicht leer sein

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Structure of an `if` statement (complete):
#
# ```python
# if <Bedingung 1>:
#     # Body that runs if condition 1 is true
# elif <Bedingung 2>:
#     # Body executed if condition 2 is true
# ...
# else:
#     # Body that is executed if none of the conditions are true
# ```
# - Only the `if` and the first body are necessary
# - If there is an `elif` or an `else`, the corresponding body may
#   not be empty

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ### Bessere Klassifizierung
#
#  Wir wollem dem Spieler etwas mehr Information geben, wie nahe er an der
#  richtigen Lösung ist:
#
#  - Die geratene Zahl ist viel zu klein/zu groß wenn der Unterschied größer als
#    10 ist

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Better classification
#
#  We want to give the player a bit more information about how close they are to the
#  correct solution:
#
#  - The guessed number is way too small/too big if the difference is bigger than
#    10

# %% {"slideshow": {"slide_type": "subslide"}}
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


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The order of the `if` and `elif` branches is important:

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


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Return aus einem `if`-Statement
#
#  Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um
#  einen Wert aus einer Funktion zurückzugeben:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Return from an `if` statement
#
#  The branches of an `if` statement can contain `return` statements to
#  return a value from the enclosing function:

# %% {"tags": ["code-along"]}
def ist_große_zahl(zahl):
    if zahl > 10:
        return True
    else:
        return False


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Signum"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - "Signum" section

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  # Benutzereingaben
#
#  - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
#  - Optional kann sie einen Eingabeprompt ausgeben.
#  - Die Funktion gibt den vom Benutzer eingegebenen Text als String zurück.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # User input
#
#  - The `input()` function allows the user to enter text.
#  - Optionally, it can output an input prompt.
#  - The function returns the text entered by the user as a string.

# %%
# input("What is your name? ")


# %% {"tags": ["code-along"]}
def query_name():
    name = input("What is your name? ")
    print(f"You entered {name}")


# %%
# query_name()

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur
# in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius
# zurückgibt.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Example: conversion of temperatures
#
# We want to write an application that will ask the user for a temperature
# in Fahrenheit and return the corresponding temperature in degrees Celsius.

# %% {"tags": ["code-along"]}
def konvertiere_fahrenheit_nach_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# %% {"tags": ["code-along"]}
konvertiere_fahrenheit_nach_celsius(32)

# %% {"tags": ["code-along"]}
konvertiere_fahrenheit_nach_celsius(90)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def temperaturkonverter_1():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
    print(f"{fahrenheit}F sind {celsius}°C")


# %% {"tags": ["code-along"]}
float("1.23")


# %% {"tags": ["code-along"]}
# temperaturkonverter_1()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# We can print a message if the user doesn't type anything (and
# make the output a little nicer):

# %% {"tags": ["code-along"]}
def temperaturkonverter_2():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %% {"tags": ["code-along"]}
# temperaturkonverter_2()

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Umrechnung in Meilen"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Section "Conversion to Miles"

# %% {"tags": ["code-along"]}
def temperaturkonverter_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit:
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %% {"tags": ["code-along"]}
# temperaturkonverter_3()


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  # Wahrheitswerte: Truthiness
#
# Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen,
# nicht nur Boole'sche Werte.
#
#  Folgende Werte gelten als *nicht wahr*
#
#  - `None` und `False`
#  - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
#  - Leere Strings, Sequences und Collections: ``
#
#  Alle anderen Werte gelten als wahr.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Truth Values: Truthiness
#
# The `if` statement can take any Python value as an argument,
# not just Boolean values.
#
#  The following values ​​are considered *not true*
#
#  - `None` and `False`
#  - `0` and `0.0` (and null values ​​of other number types)
#  - Empty strings, sequences and collections: ``
#
#  All other values ​​are considered true.

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Umrechnung in Meilen mit Truthiness"
#

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Section "Conversion to Miles with Truthiness"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Extra Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Kino-Preis"
#

# %% [markdown] {"lang": "en"}
# ## Extra mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Section "Cinema Price"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  # While-Schleifen
#
#  Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
#  - Zahlenraten bis die richtige Zahl gefunden wurde
#  - Physik-Simulation bis das Ergebnis genau genug ist
#  - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
#  Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen, verwenden wir dafür in der Regel eine While-Schleife.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # While loops
#
#  Sometimes we want to run a part of a program over and over again:
#
#  - Number of guesses until the right number is found
#  - Physics simulation until the result is accurate enough
#  - Processing of user input in interactive programs
#
#  When we don't know the number of iterations upfront, we typically use a while loop to do that.

# %% {"tags": ["code-along"]}
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
#
#  ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine
# Schleife vorzeitig beenden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Terminating loops
#
# Sometimes it's easier to determine whether to terminate a loop inside the body
# rather than in the loop condition. With the `break` statement you can
# exit a loop early:

# %%
i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)


# %% {"tags": ["code-along"]}
def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# %% {"tags": ["code-along"]}
# annoy_user()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Abschnitt "Ratespiele"
#

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - "Question games" section
