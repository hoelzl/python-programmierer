# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
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

# %% [markdown] lang="de"
# # Einleitung
#
# Wie können Sie den String `Hello, world!` in Python darstellen?

# %% [markdown] lang="en"
# # Introduction
#
# How can you represent the string `Hello, world!` in Python?

# %% tags=["solution"]
"Hello, world!"

# %% [markdown] lang="de"
# Wie können Sie Ihren Namen als Text (String) in Python darstellen?

# %% [markdown] lang="en"
# How can you represent your name as text (string) in Python?

# %% tags=["solution"]
"Matthias"

# %% [markdown] lang="de"
# Wie können Sie den String `Hello, World!` auf dem Bildschirm ausgeben?

# %% [markdown] lang="en"
# How can you output the string `Hello, World!` to the screen?

# %% tags=["solution"]
print("Hello, World!")

# %% [markdown] lang="de"
# Wie können Sie Ihren Namen auf dem Bildschirm ausgeben?

# %% [markdown] lang="en"
# How can you output your name to the screen?

# %% tags=["solution"]
print("Matthias")

# %% [markdown] lang="de"
# Wie können Sie
#
# ```
# 130 g   Mehl
# 250 ml  Milch
# 1 EL    Vanillezucker
# 1 Prise Salz
# ```
#
# auf dem Bildschirm ausgeben?

# %% [markdown] lang="en"
# How can you output
#
# ```
# 130 grams of flour
# 250ml milk
# 1 tbsp vanilla sugar
# 1 pinch of salt
# ```
#
# to the screen?

# %% tags=["solution"]
print("130 g   Mehl")
print("250 ml  Milch")
print("1 EL    Vanillezucker")
print("1 Prise Salz")

# %% tags=["solution"]
# Alternativ:
print(
    """130 g   Mehl
250 ml  Milch
1 EL    Vanillezucker
1 Prise Salz"""
)

# %% tags=["solution"]
# Alternativ:
print("130 g   Mehl\n" "250 ml  Milch\n" "1 EL    Vanillezucker\n" "1 Prise Salz")

# %% [markdown] lang="de"
# # Zahlen und Mathematik
#
# Wie können Sie die Zahl `32` in Python darstellen?

# %% [markdown] lang="en"
# # Numbers and math
#
# How can you represent the number `32` in Python?

# %% tags=["solution"]
32

# %% [markdown] lang="de"
# Wie können Sie den Datentyp von `14` in Python feststellen?

# %% [markdown] lang="en"
# How can you determine the type of `14` in Python?

# %% tags=["solution"]
type(14)

# %% [markdown] lang="de"
# Wie können Sie den Datentyp von `14.0` in Python feststellen?

# %% [markdown] lang="en"
# How can you determine the type of `14.0` in Python?

# %% tags=["solution"]
type(14.0)

# %% [markdown] lang="de"
# Wie können Sieden Datentyp von `'14'` in Python feststellen?

# %% [markdown] lang="en"
# How can you determine the type of `'14'' in Python?

# %% tags=["solution"]
type("14")

# %% [markdown] lang="de"
# Was ist der Wert von `1 + 2 * 3`?

# %% [markdown] lang="en"
# What is the value of `1 + 2 * 3`?

# %% tags=["solution"]
1 + 2 * 3

# %% [markdown] lang="de"
# Was ist der Datentyp von `1 + 2 * 3` in Python?

# %% [markdown] lang="en"
# What is the type of `1 + 2 * 3` in Python?

# %% tags=["solution"]
type(1 + 2 * 3)

# %% [markdown] lang="de"
# Was ist der Wert von `4 / 2` in Python?

# %% [markdown] lang="en"
# What is the value of `4 / 2` in Python?

# %% tags=["solution"]
4 / 2

# %% [markdown] lang="de"
# Was ist der Datentyp von `4 / 2` in Python?

# %% [markdown] lang="en"
# What is the type of `4/2` in Python?

# %% tags=["solution"]
type(4 / 2)

# %% [markdown] lang="de"
# Was sind Wert und Datentyp von `1 + 1.0` in Python? Können Sie den Datentyp
# ohne Verwendung von `type` feststellen?

# %% [markdown] lang="en"
# What is the value and type of `1 + 1.0` in Python? Can you determine the data type
# without using `type`?

# %% tags=["solution"]
1 + 1.0  # Typ ist float, da Ausgabe Nachkommastellen hat

# %% [markdown] lang="de"
# # Piraten
#
# Der Legende nach wurde die Beute bei Piratenbanden gerecht durch alle Piraten
# geteilt. Falls sich die Beute sich nicht gerecht aufteilen ließ erhielt der
# Kapitän den überschüssigen Anteil.
#
# Wie viele Golddublonen erhält jeder Pirat einer 8-köpfigen Bande
# (7 Piraten + 1 Kapitän), wenn ein Schatz mit 1000 Golddublonen erbeutet wurde?
#
# (Verwenden Sie Variablen um die Berechnung klarer zu machen.)

# %% [markdown] lang="en"
# # Pirates
#
# According to legend, the booty in pirate gangs was divided fairly amongst all pirates. If the booty could not be shared fairly, the captain received the excess share.
#
# How many gold doubloons does each pirate in a gang of 8 (7 pirates + 1 captain) get
# when looting a treasure with 1000 gold doubloons?
#
# (Use variables to make the calculation clearer.)

# %% tags=["solution"]
anzahl_piraten = 8
beute_gesamt = 1000
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown] lang="de"
# Wie viele Golddublonen erhält der Kapitän extra?

# %% [markdown] lang="en"
# How many extra gold doubloons does the captain get?

# %% tags=["solution"]
# noinspection NonAsciiCharacters
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän

# %% [markdown] lang="de"
# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
#
# Wie verändert sich die Aufteilung der Beute?
#
# (Verwenden Sie Zuweisungen an die existierenden Variablen um das Problem zu
# lösen.)

# %% [markdown] lang="en"
# The pirate gang takes on 3 new pirate apprentices.
#
# How does the distribution of the loot change?
#
# (Use assignments to the existing variables to solve the problem.)

# %% tags=["solution"]
# anzahl_piraten += 3 # anzahl_piraten = anzahl_piraten + 3
anzahl_piraten = 11  # besser, falls die Zelle evtl. mehrmals ausgewertet wird
beute_pro_pirat = beute_gesamt // anzahl_piraten
beute_pro_pirat

# %% [markdown] lang="de"
# Wie viele Golddublonen erhält der Kapitän in diesem Fall zusätzlich?

# %% [markdown] lang="en"
# In this case, how many additional gold doubloons does the captain receive?

# %% tags=["solution"]
beute_kapitän = beute_gesamt % anzahl_piraten
beute_kapitän


# %% [markdown] lang="de"
# # Spenden
#
# Bei einer Spendenaktion hat der Fernsehsender ZRD zugesagt, jede eingehende
# Spende zu verdoppeln. Der Regionalsender YB3 erhöht jede eingehende Spende
# um 10 Euro. (ZRD verdoppelt bevor die 10 Euro von YB3 hinzugefügt werden.)
#
# Schreiben Sie eine Python Funktion `effektive_spende(n)`, die berechnet,
# welcher Betrag effektiv gespendet wird, wenn ein Zuschauer $N$ Euro spendet.

# %% [markdown] lang="en"
# # Donations
#
# At a fundraiser, the television broadcaster ZRD promised to double every incoming
# donation. Regional broadcaster YB3 increases every donation received
# by 10 euros. (ZRD doubles before adding YB3's €10.)
#
# Write a Python function `effective_donation(s)` that calculates
# the amount actually donated when a viewer donates $N$ euros.

# %% tags=["solution"]
def effektive_spende(spende):
    return 2 * spende + 10


# %% [markdown] lang="de"
# Wie hoch ist die effektive Spende, wenn ein Zuschauer 20 Euro spendet?

# %% [markdown] lang="en"
# What is the effective donation if a viewer donates 20 euros?

# %% tags=["solution"]
effektive_spende(20)

# %% [markdown] lang="de"
#
# Geben Sie die effektiven Spenden für 25, 50, 100 und 500 Euro auf dem
# Bildschirm aus.
#
# *Hinweis:* Sie können Eingaben mit der `Tab`-Taste vervollständigen. Es
# genügt also, wenn Sie
#
# `pri`-*Tab* `eff`-*Tab*
#
# eingeben bevor Sie die Argumente eintippen.

# %% [markdown] lang="en"
# Display the effective donations for 25, 50, 100 and 500 euros on the
# screen.
#
# *Note:* You can complete inputs with the `Tab` key. It is thus sufficient if you type
#
# `pri`-*Tab* `eff`-*Tab*
#
# before typing the arguments.

# %% tags=["solution"]
print(effektive_spende(10))
print(effektive_spende(25))
print(effektive_spende(50))
print(effektive_spende(100))
print(effektive_spende(500))
print(effektive_spende(1000))


# %% [markdown] lang="de"
# # Piraten, Teil 2
#
# Ihre Piraten-Crew droht zu meutern, weil die Berechnung der Beuteaufteilung
# zu lange dauert.
#
# Schreiben Sie eine Funktion `drucke_aufteilung_der_beute(dublonen, piraten)`,
# die die Aufteilung berechnet und in folgendem Format ausgibt:
#
# ```
# Piraten: 8
# Golddublonen: 17
# Jeder Pirat erhält: 2 Golddublone(n)
# Kapitän erhält extra: 1 Golddublone(n)
# ```

# %% [markdown] lang="en"
# # Pirates, part 2
#
# Your pirate crew is in danger of mutiny because of the calculation of the spoils
# takes too long.
#
# Write a function `print_division_of_loot(doubloons, pirates)`,
# which calculates the split and outputs it in the following format:
#
# ```
# Pirates: 8
# Gold Doubloons: 17
# Each pirate receives: 2 gold doubloon(s)
# Captain gains extra: 1 gold doubloon(s)
# ```

# %% tags=["solution"]
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    print("Piraten:", piraten)
    print("Golddublonen:", dublonen)
    print("Jeder Pirat erhält:", dublonen_pro_pirat, "Golddublone(n)")
    print("Kapitän erhält extra:", dublonen_kapitän, "Golddublone(n)")


drucke_aufteilung_der_beute(17, 8)


# %% [markdown] lang="de"
# # Piraten, Teil 3
#
# Nachdem die Gefahr der Meuterei gebannt ist haben Sie Zeit sich um die
# Verbesserung Ihrer Software zu kümmern.
#
# Schreiben Sie eine Funktion `teile_beute_auf(dublonen, piraten)` die den
# Beuteanteil jedes Piraten und die Extra-Beute des Kapitäns als zwei Werte
# zurückgibt.

# %% [markdown] lang="en"
# # Pirates, part 3
#
# After the threat of mutiny has passed, you have time to improve your software.
#
# Write a function `divide_loot(doubloons, pirates)` which returns
# each pirate's loot share and the captain's extra loot as two values.

# %% tags=["solution"]
def teile_beute_auf(dublonen, piraten):
    dublonen_pro_pirat = dublonen // piraten
    dublonen_kapitän = dublonen % piraten
    return dublonen_pro_pirat, dublonen_kapitän


# %% [markdown] lang="de"
#
# Schreiben Sie eine verbesserte Version der Funktion
# `drucke_aufteilung_der_beute()`, die `teile_beute_auf()` als Hilfsfunktion
# verwendet.

# %% [markdown] lang="en"
# Write an improved version of the function
# `print_division_of_loot()`, that uses `divide_loot()` as helper function.

# %% tags=["solution"]
def drucke_aufteilung_der_beute(dublonen, piraten):
    dublonen_pro_pirat, dublonen_kapitän = teile_beute_auf(dublonen, piraten)
    print("Piraten:", piraten)
    print("Golddublonen:", dublonen)
    print("Jeder Pirat erhält:", dublonen_pro_pirat, "Golddublone(n)")
    print("Kapitän erhält extra:", dublonen_kapitän, "Golddublone(n)")


drucke_aufteilung_der_beute(1000, 11)
