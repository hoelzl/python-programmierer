# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# %%

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Kontrollstrukturen") }}

# %% [markdown]
#
#  # `if`-Anweisung
#
#  Wiederholung:

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
#  ## Extra Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Gerade Zahl"

# %% [markdown]
#
#  ## Mehrere Zweige
#
#  - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#    100 erraten muss.
#  - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#    zu niedrig oder richtig war angezeigt.
#  - Später wollen wir dem Spieler mehrere Versuche erlauben.

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
#  ## Extra Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Positiv/Negativ"
#

# %% [markdown]
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
#  - Nur das `if` und der erste Rumpf sind notwendig
#  - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein

# %% [markdown]
#
#  ### Bessere Klassifizierung
#
#  Wir wollem dem Spieler etwas mehr Information geben, wie nahe er an der
#  richtigen Lösung ist:
#
#  - Die geratene Zahl ist viel zu klein/zu groß wenn der Unterschied größer als
#    10 ist

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
#  Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

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
#  ## Return aus einem `if`-Statement
#
#  Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um
#  einen Wert aus einer Funktion zurückzugeben:

# %%
def ist_große_zahl(zahl):
    if zahl > 10:
        return True
    else:
        return False



# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Signum"
#

# %% [markdown]
#
#  # Benutzereingaben
#
#  - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
#  - Optional kann sie einen Eingabeprompt ausgeben.
#  - Die Funktion gibt den vom Benutzer eingegebenen Text als String zurück.

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
#  ## Beispiel: Konvertierung von Temperaturen
#
#  Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur in
#  Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius zurückgibt.

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

# %% [markdown]
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):

# %%
def temperaturkonverter_2():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit != "":
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")


# %%
# temperaturkonverter_2()

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Umrechnung in Meilen"
#

# %%
def temperaturkonverter_3():
    fahrenheit = input("Bitte geben Sie die Temperatur in Fahrenheit ein: ")
    if fahrenheit:
        celsius = konvertiere_fahrenheit_nach_celsius(float(fahrenheit))
        print(f"{float(fahrenheit):.1f}F sind {celsius:.1f}°C")
    else:
        print("Bitte geben Sie eine gültige Temperatur ein.")

# %%
# temperaturkonverter_3()


# %% [markdown]
#
#  # Wahrheitswerte: Truthiness
#
#  Die `if`-Anweisung kann als Argument beliebige Python-Werte bekommen, nicht nur Boole'sche Werte.
#
#  Folgende Werte gelten als *nicht wahr*
#
#  - `None` und `False`
#  - `0` und `0.0` (und Null-Werte von anderen Zahlentypen)
#  - Leere Strings, Sequences und Collections: ``
#
#  Alle anderen Werte gelten als wahr.

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
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Umrechnung in Meilen mit Truthiness"
#

# %% [markdown]
#
#  ## Extra Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Kino-Preis"
#

# %% [markdown]
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
#  ## Beenden von Schleifen
#
#  Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine Schleife vorzeitig beenden:

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
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Ratespiele"
#
