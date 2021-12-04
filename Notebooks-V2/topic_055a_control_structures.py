# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

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

# %%

# %%

# %%

# %% [markdown]
#
#  ## Struktur einer `if`-Anweisung (vollständig):
#
#  ```python
#  if <Bedingung 1>:
#      Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
#  elif <Bedingung 2>:
#      Rumpf, der ausgeführt wird, wenn Bedingung 2 wahr ist
#  ...
#  else:
#      Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
#  ```
#  - Nur das `if` und der erste Rumpf sind notwendig
#  - Falls ein `elif` oder ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein

# %% [markdown]
#
#  ## Extra Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Positiv/Negativ"
#

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

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
#  Die Reihenfolge der `if`- und `elif`-Zweige ist wichtig:

# %%

# %%

# %%

# %% [markdown]
#
#  ## Return aus einem `if`-Statement
#
#  Die Zweige eines `if`-Statements können `return` Anweisungen enthalten um
#  einen Wert aus einer Funktion zurückzugeben:

# %%

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

# %%

# %%

# %% [markdown]
#
#  ## Beispiel: Konvertierung von Temperaturen
#
#  Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur in
#  Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius zurückgibt.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
#  Wir können eine Meldung ausgeben, wenn der Benutzer nichts eingibt (und die
#  Ausgabe etwas schöner gestalten):

# %%

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Umrechnung in Meilen"
#

# %%

# %%

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

# %%

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Ratespiele"
#
