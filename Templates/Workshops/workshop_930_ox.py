# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# j2 import 'macros.j2' as doc
# %% [markdown]
# # Ox - Eine Variante von Bulls and Cows
#
# Implementieren Sie eine Variante des Spiels "Bulls and Cows"
#
# ## Spielablauf
#
# - Der Computer wählt ein Wort aus einem Wörterbuch und teilt dem Spieler mit,
#   wie viele Buchstaben es enthält
# - Der Spieler rät ein Wort und erhält als für jeden Buchstaben folgende
#   Information
#     - Ein `+` wenn der Buchstabe an der richtigen Stelle vorkommt
#     - Ein `–` wenn der Buchstabe in der Lösung an einer anderen Stelle
#       vorkommt
#     - Einen `.` wenn der Buchstabe nicht in der Lösung vorkommt
# - Wenn der Spieler das Wort in weniger als 10 Versuchen errät hat er
#   gewonnen, andernfalls verloren.
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
# Implementieren Sie eine Funktion `ox()`, die dieses Spiel implementiert.
# Zwechmäßigerweise sollten Sie dazu einige Hilfsfunktionen definieren,
# die Teile der Spielelogik kapseln.
#
# ## Hinweise
#
# - Benutzereingaben können Sie mittels der Funktion `input(quey: str)`
#   erhalten.  `query` ist der Text, der dem Benutzer angezeigt wird; das
#   Ergebnis der Funktion ist der vom Benutzer eingegebenee String.
# - Speichern Sie das "Wörterbuch" als eine Liste von Wörtern.
# - Mit `random.choice(list)` können Sie aus einer Liste ein zufälliges
#   Element auswählen.
# - Da wir noch keine benutzerdefinierten Datentypen kennengelernt haben
#   bietet es sich an, eine Funktion zu implementieren, die die zeichenweise
#   Übereinstimmung zweier Zeichenketten testet. Ein möglicher Ergebnistyp für
#   diese Funktion ist eine Liste der Form `['.', '+', '-', '.']`,
#   um auszudrücken, dass das erste und vierte Zeichen nicht übereinstimmen,
#   das zweite Zeichen ein perfekter Treffer ist und das dritte Zeichen in der
#   Lösung vorkommt, aber an einer anderen Stelle.
# - Aus einer Liste `list` mit Strings können Sie mittels `''.join(list)`
#   einen String erzeugen, der alle Elemente der Liste enthält.
# - Was passiert bei Ihrer Lösung, wenn der Benutzer ein Wort eingibt, das
#  länger oder kürzer ist als die Lösung?

# %% tags=["solution"]
import random


# %% tags=["solution"]
def match_char(char, index, solution):
    """
    Checks whether `char` is a perfect match for position `index` in `solution`.
    Returns `'+'` if `solution[index] == char`, `'-'` if `char` occurs at another
    position in `solution` and `'.'` otherwise.
    """
    if index >= len(solution):
        return ""
    elif solution[index] == char:
        return "+"
    elif char in solution:
        return "-"
    else:
        return "."


# %% tags=["solution"]
match_char("b", 1, "abc")

# %% tags=["solution"]
match_char("a", 1, "abc")

# %% tags=["solution"]
match_char("x", 1, "abc")

# %% tags=["solution"]
match_char("x", 10, "abc")


# %% tags=["solution"]
def match_chars(chars, solution):
    return [match_char(char, index, solution) for index, char in enumerate(chars)]


# %% tags=["solution"]
match_chars("cbx", "abc")


# %% tags=["solution"]
def evaluate_guess(guess, solution):
    return "".join(match_chars(guess, solution))


# %% tags=["solution"]
evaluate_guess("cbx", "abc")

# %% tags=["solution"]
evaluate_guess("b", "abc")

# %% tags=["solution"]
evaluate_guess("bbcdea", "abc")


# %% tags=["solution"]
def is_perfect_result(result):
    if result == "":
        return False
    for c in result:
        if c != "+":
            return False
    return True


# %% tags=["solution"]
is_perfect_result("+++")

# %% tags=["solution"]
is_perfect_result("+++-+")

# %% tags=["solution"]
is_perfect_result("")

# %% tags=["solution"]
dictionary = ["game", "gate", "teatime", "python"]


# %% tags=["solution"]
def print_header(word):
    print(
        f"""Guess the word!
The word to guess has {len(word)} characters."""
    )


# %% tags=["solution"]
print_header("foo")


# %% tags=["solution"]
def ox():
    word = random.choice(dictionary)
    has_won = False
    print_header(word)
    for _ in range(10):
        if not has_won:
            guess = input("Please enter your guess: ")
            result = evaluate_guess(guess, word)
            print(guess)
            print(result)
            if is_perfect_result(result):
                has_won = True
    if has_won:
        print("Congratulations, you have won!")
    else:
        print(f"Better luck next time. The word was {word}.")


# %% tags=["solution"]
ox()
