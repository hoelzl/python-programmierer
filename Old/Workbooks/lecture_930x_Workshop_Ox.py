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
# # Ox - Eine Variante von Bulls and Cows
#
# Implementieren Sie eine Variante des Spiels "Bulls and Cows"
#
# ## Spielablauf
#
# - Der Computer wählt ein Wort aus einem Wörterbuch und teilt dem Spieler mit, wie viele Buchstaben es enthält
# - Der Spieler rät ein Wort und erhält als für jeden Buchstaben folgende Information
#     - Ein `+` wenn der Buchstabe an der richtigen Stelle vorkommt
#     - Ein `–` wenn der Buchstabe in der Lösung an einer anderen Stelle vorkommt
#     - Einen `.` wenn der Buchstabe nicht in der Lösung vorkommt
# = Wenn der Benutzer das Wort in weniger als 10 Versuchen errät hat er gewonnen, andernfalls verloren.
#
# ## Beispiele
#
# Erfolgreiches Spiel:
#
# ```
# Guess the word!
# The word to guess has 6 characters.
# Please enter your guess: something
# something
# .-..--
# Please enter your guess: postoffice
# postoffice
# +-.-+.
# Please enter your guess: python
# python
# ++++++
# Congratulations, you have won!
# ```
#
# Verlorenes Spiel:
#
# ```
# Guess the word!
# The word to guess has 4 characters.
# Please enter your guess: foobar
# foobar
# ....
# Please enter your guess: tango
# tango
# .+.-
# Please enter your guess: ohno
# ohno
# ....
# Please enter your guess: This game is stupid!
# This game is stupid!
# ....
# Please enter your guess: Let me out!
# Let me out!
# .-..
# Please enter your guess: exit
# exit
# -...
# Please enter your guess: quit
# quit
# ....
# Please enter your guess: QUIT
# QUIT
# ....
# Please enter your guess: 
#
#
# Please enter your guess: HOW DO I QUIT THIS STUPID GAME!!!!!
# HOW DO I QUIT THIS STUPID GAME!!!!!
# ....
# Better luck next time. The word was game.
# ```
#
# ## Implementierung:
#
# Implementieren Sie eine Funktion `ox()`, die dieses Spiel implementiert. Zwechmäßigerweise sollten Sie dazu einige Hilfsfunktionen definieren, die Teile der Spielelogik kapseln.
#
# ## Hinweise
#
# - Benutzereingaben können Sie mittels der Funktion `input(quey: str)` erhalten.  `query` ist der Text,
#   der dem Benutzer angezeigt wird; das Ergebnis der Funktion ist der vom Benutzer eingegebenee String.
# - Mit `random.choice(list)` können Sie aus einer Liste ein zufälliges Element auswählen.
# - Da wir noch keine benutzerdefinierten Datentypen kennengelernt haben bietet es sich an, eine Funktion
#   zu implementieren, die die zeichenweise Übereinstimmung zweier Zeichenketten testet. Ein möglicher
#   Ergebnistyp für diese Funktion ist eine Liste der Form `['.', '+', '-', '.']`, um auszudrücken, dass
#   das erste und vierte Zeichen nicht übereinstimmen, das zweite Zeichen ein perfekter Treffer ist und das
#   dritte Zeichen in der Lösung vorkommt, aber an einer anderen Stelle.
# - Aus einer Liste `list` mit Strings können Sie mittels `''.join(list)` einen String erzeugen, der alle Elemente
#   der Liste enthält.
# - Was passiert bei Ihrer Lösung, wenn der Benutzer ein Wort eingibt, das länger oder kürzer ist als die Lösung?

# %%
import random

# %%
