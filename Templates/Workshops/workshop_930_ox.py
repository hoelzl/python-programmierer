# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
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
# - Eine Möglichkeit, das Spiel zu implementieren ohne Klassen zu verwenden,
#   is als eine Funktion, die die zeichenweise
#   Übereinstimmung zweier Zeichenketten testet. Ein möglicher Ergebnistyp für
#   diese Funktion ist eine Liste der Form `['.', '+', '-', '.']`,
#   um auszudrücken, dass das erste und vierte Zeichen nicht übereinstimmen,
#   das zweite Zeichen ein perfekter Treffer ist und das dritte Zeichen in der
#   Lösung vorkommt, aber an einer anderen Stelle.
# - Aus einer Liste `list` mit Strings können Sie mittels `''.join(list)`
#   einen String erzeugen, der alle Elemente der Liste enthält.
# - Was passiert bei Ihrer Lösung, wenn der Benutzer ein Wort eingibt, das
#  länger oder kürzer ist als die Lösung?

# %% [markdown] lang="en"
# # Ox - A variant of Bulls and Cows
#
# Implement a variant of the game "Bulls and Cows"
#
# ## Gameplay
#
# - The computer chooses a word from a dictionary and tells the player
#   how many letters it contains
# - The player guesses a word and gets the following information for each letter:
#     - `+` if the letter is in the right place
#     - `–` if the letter occurs the solution, but in a different place
#     - `.` if the letter does not appear in the solution
# - If the player guesses the word in less than 10 tries he has
#   won, otherwise lost.
#
# ## Examples
#
# Successful game:
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
# Lost game:
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
# ## Implementation:
#
# Implement a function `ox()` that implements this game.
# You should define some auxiliary functions for this purpose,
# that encapsulate parts of the game logic.
#
# ## Hints
#
# - You can get user input using the function `input(quey: str)`.
#   `query` is the text to be displayed to the user;
#   the result of the function is the string entered by the user.
# - Save the "dictionary" as a list of words.
# - With `random.choice(list)` you can select a random item from a list.
# - One possibility to implement this game without using classes
#   is by defining a function that matches two strings
#   character-by-character. A possible result type for
#   this function is a list of the form `['.', '+', '-', '.']`,
#   to express that the first and fourth characters do not match,
#   the second character is a perfect match and the third character
#   appears in the solution, but in a different position.
# - Given a list `strings` of strings you can use `''.join(strings)`
#   to create a string containing all elements of the list.
# - What happens in your solution when the user enters a word that
#   is longer or shorter than the solution?

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
