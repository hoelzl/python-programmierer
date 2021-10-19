# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
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
# <h1 style="text-align:center;">Python: Kontrollstrukturen</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% slideshow={"slide_type": "subslide"}
# Ohne Angabe der Namensräume, siehe nächste Folie
a = 1
def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)
f(2)
print(a)
# print(x)

# %% slideshow={"slide_type": "subslide"}
a = 1                   # Globaler Namespace
def f(x):               # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1           # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)            # Greift auf a aus dem Namespace von f zu
f(2)
print(a)                # Greift auf a aus dem globalen Namespace zu
# print(x)              # Fehler: x ist im Namespace von f

# %% slideshow={"slide_type": "subslide"}
a = 1
def f2():
    global a
    a = 4
    print(a)
f2()
print(a)
a = 5
print(a)


# %% slideshow={"slide_type": "subslide"}
# ## Vermeiden von langwierigen Berechnungen in Notebooks:

# %%
def slow_computation():
    import time
    ## Increase this before demonstration!
    time.sleep(0.1)

# %%
"slow_value" in globals()

# %%
slow_value = slow_computation()

# %%
"slow_value" in globals()

# %% slideshow={"slide_type": "subslide"}
del slow_value

# %%
"slow_value" in globals()

# %% slideshow={"slide_type": "subslide"}
if "slow_value" not in globals():
    slow_value = slow_computation()

# %%
if "slow_value" not in globals():
    slow_value = slow_computation()

# %% [markdown]
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


# %% [markdown] slideshow={"slide_type": "skip"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Gerade Zahl"
#

# %% [markdown] slideshow={"slide_type": slideshow={"slide_type": "subslide"}
# ## Mehrere Zweige
#
# - Wir wollen ein Spiel schreiben, in dem der Spieler eine Zahl zwischen 1 und
#   100 erraten muss.
# - Nachdem er geraten hat, bekommt er die Information, ob seine Zahl zu hoch,
#   zu niedrig oder richtig war angezeigt.
# - Später wollen wir dem Spieler mehrere Versuche erlauben.

# %% slideshow={"slide_type": "subslide"}
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        print("Die geratene Zahl ist zu klein!")
    elif geratene_zahl > lösung:
        print("Die geratene Zahl ist zu groß!")
    else:
        print("Sie haben gewonnen!")


# %% slideshow={"slide_type": "subslide"}
klassifiziere_zahl(10, 12)

# %%
klassifiziere_zahl(14, 12)

# %%
klassifiziere_zahl(12, 12)


# %% [markdown] slideshow={"slide_type": "skip"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Positiv/Negativ"
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Struktur einer `if`-Anweisung:
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Bessere Klassifizierung
#
# Wir wollem dem Spieler etwas mehr Information geben, wie nahe er an der richtigen Lösung ist:
#
# - Die geratene Zahl ist viel zu klein/zu groß wenn der Unterschied größer als 10 ist

# %% slideshow={"slide_type": "subslide"}
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


# %% slideshow={"slide_type": "subslide"}
klassifiziere_zahl_2(1, 12)

# %%
klassifiziere_zahl_2(10, 12)

# %%
klassifiziere_zahl_2(14, 12)

# %%
klassifiziere_zahl_2(24, 12)

# %%
klassifiziere_zahl_2(12, 12)


# %% [markdown] slideshow={"slide_type": "subslide"}
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

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Signum"
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# # Benutzereingaben
#
# - Die Funktion `input()` erlaubt es dem Benutzer einen Text einzugeben.
# - Optional kann sie einen Eingabeprompt ausgeben.
# - Die Funktion gibt den vom Benutzer eingegebenen Text als String zurück.

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beispiel: Konvertierung von Temperaturen
#
# Wir wollen eine Anwendung schreiben, die den Benutzer nach einer Temperatur in Fahrenheit fragt und die entsprechende Temperatur in Grad Celsius zurückgibt.

# %% slideshow={"slide_type": "fragment"}
def konvertiere_fahrenheit_nach_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# %%
konvertiere_fahrenheit_nach_celsius(32)

# %%
konvertiere_fahrenheit_nach_celsius(90)

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen"
#

# %% slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
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

# %% slideshow={"slide_type": "subslide"}
if -1:
    print("-1 ist wahr")
elif 0:
    print("0 ist wahr")
else:
    print("Alles ist falsch")

# %% slideshow={"slide_type": "-"}
if 0:
    print("0 ist wahr")
else:
    print("0 ist falsch")

# %% slideshow={"slide_type": "subslide"}
if '':
    print("'' ist wahr")
else:
    print("'' falsch")

# %%
if print("Hallo"):
    print("None ist wahr")
else:
    print("None ist falsch")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Umrechnung in Meilen mit Truthiness"
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Kino-Preis"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # While-Schleifen
#
# Manchmal wollen wir einen Teil eines Programms immer wieder ausführen:
#
# - Zahlenraten bis die richtige Zahl gefunden wurde
# - Physik-Simulation bis das Ergebnis genau genug ist
# - Verarbeitung von Benutzereingaben in interaktiven Programmen
#
# Wenn wir die Anzahl der Wiederholungen nicht von vornherein wissen, verwenden wir dafür in der Regel eine While-Schleife.

# %% slideshow={"slide_type": "subslide"}
number = 0
while number < 3:
    print(f"Durchlauf {number}")
    number += 1 # <==


# %% slideshow={"slide_type": "subslide"}
def führe_ein_experiment_aus(versuch_nr):
    """Führt ein Experiment aus
    Gibt True zurück wenn das Experiment erfolgreich war, andernfalls False.
    """
    print(f"Versuch Nr. {versuch_nr} gestartet...", end='')
    from random import random
    if random() > 0.8:
        print("Erfolg!")
        return True
    else:
        print("Fehlschlag.")
        return False


# %% slideshow={"slide_type": "subslide"}
versuch_nr = 0

while not führe_ein_experiment_aus(versuch_nr):
    versuch_nr += 1

print("Wir haben einen erfolgreichen Versuch ausgeführt.")

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Beenden von Schleifen
#
# Manchmal ist es leichter, die Abbruchbedingung einer Schleife im Rumpf zu
# bestimmen, statt am Anfang. Mit der Anweisung `break` kann man eine Schleife
# vorzeitig beenden:

# %%
i = 1
while i < 10:
    print(i)
    if i % 3 == 0:
        break
    i += 1
print("Nach der Schleife:", i)


# %% slideshow={"slide_type": "subslide"}
def annoy_user():
    while True:
        text = input("Say hi! ")
        if text.lower() == "hi":
            break
        else:
            print("You chose", text)


# %%
# annoy_user()

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_020x_Workshop_Kontrollstrukturen`
# - Abschnitt "Ratespiele"
#
