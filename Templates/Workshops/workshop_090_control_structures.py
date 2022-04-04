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
# # Gerade Zahl
#
# Schreiben Sie eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt,
# falls `zahl` gerade ist und `False`, falls `zahl` ungerade ist.

# %% [markdown] lang="en"
# # Even number
#
# Write a function `is_even(number)` that returns `True`,
# if `number` is even and `False` if `number` is odd.

# %% tags=["solution"]
def ist_gerade(zahl):
    return zahl % 2 == 0


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `drucke_ist_gerade(zahl)`, die
#
# - `{zahl} ist gerade.` auf dem Bildschirm ausgibt, falls `zahl` gerade ist und
# - `{zahl} ist nicht gerade.` auf dem Bildschirm ausgibt, falls `zahl` nicht
#   gerade ist.

# %% [markdown] lang="en"
# Write a function `print_is_even(number)` that
#
# - prints `{number} is even.` on the screen if `number` is even and
# - Prints `{number} is not even.` to the screen if `number` is not
#   is straight.

# %% tags=["solution"]
def drucke_ist_gerade(zahl):
    if ist_gerade(zahl):
        print(f"{zahl} ist gerade.")
    else:
        print(f"{zahl} ist nicht gerade.")


# %% [markdown] lang="de"
# Testen Sie `drucke_ist_gerade(zahl)` mit den Werten 0, 1 und 8.

# %% [markdown] lang="en"
# Test `print_is_even(number)` with the values ​​0, 1 and 8.

# %% tags=["solution"]
drucke_ist_gerade(0)
drucke_ist_gerade(1)
drucke_ist_gerade(8)


# %% [markdown] lang="de"
# # Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %% [markdown] lang="en"
# # Positive / Negative
#
# Write a function `print_is_positive(number)` that
#
# - prints `{number} is positive.` on the screen if `number > 0`,
# - prints `{number} is zero.` on the screen if `number == 0`,
# - Print `{number} is negative.` to the screen if `number < 0`.

# %% tags=["solution"]
def drucke_ist_positiv(zahl):
    if zahl > 0:
        print(f"{zahl} ist positiv.")
    elif zahl < 0:
        print(f"{zahl} ist negativ.")
    else:
        print("0 ist Null.")


# %% [markdown] lang="de"
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %% [markdown] lang="en"
# Test `print_is_positive(number)` with the values ​​-3, 0 and 2.

# %% tags=["solution"]
drucke_ist_positiv(-3)
drucke_ist_positiv(0)
drucke_ist_positiv(2)


# %% tags=["solution"]
def klassifiziere_positiv_negativ(zahl):
    if zahl > 0:
        return f"{zahl} ist positiv."
    elif zahl < 0:
        return f"{zahl} ist negativ."
    else:
        return "0 ist Null."


def drucke_ist_positiv_2(zahl):
    print(klassifiziere_positiv_negativ(zahl))


# %% tags=["solution"]
drucke_ist_positiv_2(-3)
drucke_ist_positiv_2(0)
drucke_ist_positiv_2(2)


# %% [markdown] lang="de"
# # Signum
#
# Schreiben Sie eine Funktion `signum(zahl)`, die
#
# - 1 zurückgibt, falls `zahl > 0` ist,
# - 0 zurückgibt, falls `zahl == 0` ist,
# - -1 zurückgibt, falls `zahl < 0` ist.

# %% [markdown] lang="en"
# # Signum
#
# Write a function `signum(number)` that
#
# - returns 1 if `number > 0`,
# - returns 0 if `number == 0`,
# - returns -1 if `number < 0`.

# %% tags=["solution"]
def signum(zahl):
    if zahl > 0:
        return 1
    elif zahl == 0:
        return 0
    else:
        return -1


# %% [markdown] lang="de"
# Testen Sie die Funktion für repräsentative Werte.

# %% [markdown] lang="en"
# Test the function for representative values.

# %% tags=["solution"]
signum(-10)

# %% tags=["solution"]
signum(0)

# %% tags=["solution"]
signum(2)


# %% [markdown] lang="de"
# # Umrechnung in Meilen
#
# Schreiben Sie eine Funktion `konvertiere_km_nach_meilen(km)` die den Wert
# `km` von Kilometer in Meilen umrechnet (d.h. die den Wert in Meilen
# zurückgibt).
#
# *Hinweis:*
# - Ein Kilometer entspricht $0,621371$ Meilen

# %% [markdown] lang="en"
# # Conversion to miles
#
# Write a function `convert_km_to_miles(km)` that converts the value `km` from kilometers to miles (i.e. the value in miles is returned).
#
# *Note:*
# - One kilometer equals $0,621371$ miles

# %% tags=["solution"]
def konvertiere_km_nach_meilen(km):
    return km * 0.621371


# %% [markdown] lang="de"
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %% [markdown] lang="en"
# Test `convert_km_to_miles(km)` for 1 and 5 km.

# %% tags=["solution"]
konvertiere_km_nach_meilen(1)

# %% tags=["solution"]
konvertiere_km_nach_meilen(5)


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `meilen_app()`, die eine Länge in Kilometern
# einliest und die äquivalente Entfernung in Meilen ausgibt. Wenn die Eingabe ein leerer String ist, soll der String `Bitte geben Sie eine gültige Entfernung in km ein.` ausgegeben werden.
#
# *Hinweise*
# - Ein String kann mit `float()` in einen Float-Wert umgewandelt werden.

# %% [markdown] lang="en"
# Write a function `miles_app()` that reads a length in kilometers from the user and prints out the equivalent distance in miles. If the user enters an empty string, `Please enter a valid distance in km.` should be printed on the screen.
#
# *Notes*
# - A string can be converted to a float value with `float()`.

# %% tags=["solution"]
def meilen_app():
    km = input("Bitte geben Sie eine Entfernung in km ein: ")
    if km != "":
        meilen = konvertiere_km_nach_meilen(float(km))
        print(f"{km} km sind {meilen} Meilen")
    else:
        print("Bitte geben Sie eine gültige Entfernung in km ein.")


# %% tags=["solution"]
meilen_app()


# %% [markdown] lang="de"
# # Umrechnung in Meilen mit Truthiness
#
# Schreiben Sie eine Funktion `meilen_app_2`, die sich wie `meilen_app`
# verhält, aber Truthiness von Strings ausnutzt.

# %% [markdown] lang="en"
# # Conversion to miles with Truthiness
#
# Write a function `miles_app_2` that behaves similar to `miles_app` but exploits the truthiness of strings. Are there any inputs for which the behavior differs?

# %% tags=["solution"]
def meilen_app_2():
    km = input("Bitte geben Sie eine Entfernung in km ein: ")
    if km:
        meilen = konvertiere_km_nach_meilen(float(km))
        print(f"{km} km sind {meilen} Meilen")
    else:
        print("Bitte geben Sie eine gültige Entfernung in km ein.")


# %% tags=["solution"]
# meilen_app_2()

# %% [markdown] lang="de"
# # Kino-Preis
#
# Das Python-Lichtspielhaus hat folgende Eintrittspreise:
#
# - Kleinkinder unter 2 Jahren sind frei.
# - Kinder von 2-12 Jahren zahlen 2 Euro.
# - Teenager von 13-17 Jahren zahlen 5 Euro.
# - Erwachsene zahlen 10 Euro.
# - Rentner (ab 65) zahlen 6 Euro.
#
# Schreiben Sie eine Funktion `kinopreis(alter)`, die den Preis in
# Abhängigkeit vom Alter berechnet und zurückgibt.

# %% [markdown] lang="en"
# # Cinema price
#
# The Python-Cinema has the following entrance fees:
#
# - Infants under 2 years are free.
# - Children from 2-12 years pay 2 euros.
# - Teenagers aged 13-17 pay 5 euros.
# - Adults pay 10 euros.
# - Pensioners (over 65) pay 6 euros.
#
# Write a function `cinema_price(age)` that returns the price in Euros a person with age `age` has to pay.

# %% tags=["solution"]
def kinopreis(alter):
    if alter < 2:
        return 0
    elif alter <= 12:
        return 2
    elif alter <= 17:
        return 5
    elif alter < 65:
        return 10
    else:
        return 6


# %% [markdown] lang="de"
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %% [markdown] lang="en"
# Test the function `cinema_price()` for some representative values.

# %% tags=["solution"]
kinopreis(1)

# %% tags=["solution"]
kinopreis(7)

# %% tags=["solution"]
kinopreis(15)

# %% tags=["solution"]
kinopreis(25)

# %% tags=["solution"]
kinopreis(70)


# %% Schreiben Sie eine Funktion `drucke_kinopreis(alter)`, [markdown] lang="de"
# Schreiben Sie eine Funktion `drucke_kinopreis(alter)`, 
# die einen Text der folgenden Art auf dem Bildschirm ausgibt:
#
# ```
# Sie sind 1 Jahr alt. Ihr Preis beträgt 0 Euro.
# Sie sind 15 Jahre alt. Ihr Preis beträgt 5 Euro.
# ```

# %% [markdown] lang="en"
# Write a function `print_cinema_price(age)`, that prints a text of the following type on the screen:
#
# ```
# You are 1 year old. Their price is 0 euros.
# You are 15 years old. Their price is 5 euros.
# ```

# %% tags=["solution"]
def drucke_kinopreis(alter):
    preis = kinopreis(alter)
    if alter == 1:
        print("Sie sind 1 Jahr alt. Ihr Preis beträgt {preis} Euro.")
    else:
        print(f"Sie sind {alter} Jahre alt. Ihr Preis beträgt {preis} Euro.")


# %% [markdown] lang="de"
# Testen Sie `drucke_kinopreis()` für repräsentative Werte.

# %% [markdown] lang="en"
# Test `print_cinema_price()` for representative values.

# %% tags=["solution"]
drucke_kinopreis(1)
drucke_kinopreis(7)
drucke_kinopreis(15)
drucke_kinopreis(25)
drucke_kinopreis(70)


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `kino_app()`, die ein Alter einliest und den
# Kinopreis für eine Person dieses Alters im gerade beschriebenen Format
# ausgibt. Zwei Beispielinteraktionen:
#
# ```
# Wie alt sind Sie? 37
# Sie sind 37 Jahre alt. Ihr Preis beträgt 10 Euro.
#
# Wie alt sind Sie? 12
# Sie sind 12 Jahre alt. Ihr Preis beträgt 2 Euro.
# ```

# %% [markdown] lang="en"
# Write a function `cinema_app()` that reads an age and prints the
# cinema price for a person of this age in the format just described. Two example interactions:
#
# ```
# How old are they? 37
# You are 37 years old. Their price is 10 euros.
#
# How old are they? 12
# You are 12 years old. Their price is 2 euros.
# ```

# %% tags=["solution"]
def kino_app():
    alter = input("Wie alt sind Sie? ")
    if alter:
        drucke_kinopreis(int(alter))
    else:
        "Bitte geben Sie ein gültiges Alter ein."


# %%
# kino_app()

# %% [markdown] lang="de"
# # Ratespiele
#
# Die folgenden einfachen "Spiele" erlauben dem Spieler unbegrenzt viele
# Eingaben. Daher ist es sinnvoll, sie mit einer While-Schleife zu
# implementieren.
#
# ### Raten eines Wortes
#
# Implementieren Sie eine Funktion `rate_wort(lösung)`, die den Benutzer so
# lange nach einem Wort fragt, bis das eingegebene Wort der Lösung entspricht.

# %% [markdown] lang="en"
# # Guessing games
#
# The following simple "games" allow the player unlimited number of
# inputs. Therefore, it makes sense to use a while loop
# to implement them.
#
# ### Guess a word
#
# Implement a function `guess_word(solution)` that prompts the user for a word and
# keeps asking until the word typed by the user matches `solution`.

# %% tags=["solution"]
def rate_wort(lösung):
    geratenes_wort = input("Bitte geben Sie ein Wort ein: ")
    while geratenes_wort != lösung:
        geratenes_wort = input("Bitte versuchen Sie es nochmal: ")
    print("Genau!")


# %%
# rate_wort("Haus")

# %% [markdown] lang="de"
# ### Zahlenraten
#
# Implementieren Sie eine Funktion `rate_zahl(lösung)`, die den Benutzer so
# lange nach einer Zahl fragt, bis er die Lösung erraten hat. Nach jeder
# Eingabe soll dem Benutzer angezeigt werden, ob die eingegebene Zahl zu
# groß, zu klein oder richtig ist.

# %% [markdown] lang="en"
# ### Number guesses
#
# Implement a function `guess_number(solution)` that asks the user for a number and keeps asking until the user has guessed the solution. After every input the function should display whether the entered number
# is too big, too small or the correct number.

# %% tags=["solution"]
def rate_zahl(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    while int(geratene_zahl) != lösung:
        if int(geratene_zahl) < lösung:
            print(f"{geratene_zahl} ist zu klein.")
        else:
            print(f"{geratene_zahl} ist zu groß.")
        geratene_zahl = input("Bitte versuchen Sie es noch einmal: ")
    print("Sie haben gewonnen!")


# %%
# rate_zahl(23)

# %% [markdown] lang="de"
#
# Wie müssen Sie Ihre Lösung modifizieren, damit der Spieler durch Eingabe
# einer leeren Zeichenkette das Spiel abbrechen kann?

# %% [markdown] lang="en"
# How do you have to modify your solution to allow the player to input
# an empty string to abort the game?

# %% tags=["solution"]
def rate_zahl_1(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    while geratene_zahl and int(geratene_zahl) != lösung:
        if int(geratene_zahl) < lösung:
            print(f"{geratene_zahl} ist zu klein.")
        else:
            print(f"{geratene_zahl} ist zu groß.")
        geratene_zahl = input("Bitte versuchen Sie es noch einmal: ")
    if geratene_zahl:
        print("Sie haben gewonnen!")
    else:
        print("Aufgeben ist feige!")


# %% tags=["solution"]
# rate_zahl_1(23)

# %% [markdown] lang="de"
# Lösung unter Zuhilfenahme der Funktion `klassifiziere_zahl`

# %% [markdown] lang="en"
# Solution using the `classify_number` function

# %% tags=["solution"]
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        return False, "Die geratene Zahl ist zu klein! "
    elif geratene_zahl > lösung:
        return False, "Die geratene Zahl ist zu groß! "
    else:
        return True, "Sie haben gewonnen!"


# %% tags=["solution"]
def rate_zahl_2(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    erfolg, hinweis = klassifiziere_zahl(int(geratene_zahl), lösung)
    while not erfolg:
        geratene_zahl = input(hinweis)
        erfolg, hinweis = klassifiziere_zahl(int(geratene_zahl), lösung)
    print("Sie haben gewonnen!")


# %% tags=["solution"]
# rate_zahl_2(23)

# %% [markdown] lang="de"
# # Knobeln
#
# (Auch Schere, Stein, Papier; Schnick, Schnack, Schnuck; Fli, Fla, Flu; usw.)
#
# Beim Knobeln spielen zwei Spieler gegeneinander. Jeder der beiden Spieler
# wählt eines der drei Symbole "Schere", "Stein" oder "Papier" aus (ohne die
# Wahl des anderen Spielers zu kennen). Haben beide Spieler das gleiche
# Symbol gewählt, so ist das Spiel unentschieden. Andernfalls gilt:
#
# - Schere schlägt Papier
# - Papier schlägt Stein
# - Stein schlägt Schere
#
# Schreiben Sie eine Funktion `evaluiere_eine_runde_knobeln(spieler1,
# spieler2)`, die bewertet, ob die Runde unentschieden ausgegangen ist oder
# ob einer der Spieler gewonnen hat. Dazu soll die Funktion folgende Werte
# zurückgeben:
#
# - 0, wenn die Runde unentschieden war
# - 1, wenn Spieler 1 gewonnen hat
# - 2, wenn Spieler 2 gewonnen hat
#
# Wenn einer der Spieler eine ungültige Eingabe vorgenommen hat soll die
# Funktion eine Exception vom benutzerdefinierten Typ `BadInputException`
# auslösen, in der die Nummer des Spielers gespeichert ist, dessen Eingabe
# ungültig war. (Wenn beide Spieler eine ungültige Eingabe vorgenommen haben
# kann ein beliebiger Spieler gespeichert werden.)

# %% [markdown] lang="en"
# # Rock, Paper, Scissors
#
# In Rock, Paper, Scissors, two players play against each other. Each of the two players
# selects one of the three symbols "scissors", "rock" or "paper" (without knowing the other player's
# choice). If both players have chosen the same
# symbol, the game is a tie. Otherwise:
#
# - Scissors beats paper
# - Paper beats stone
# - Rock beats scissors
#
# Write a function `evaluate_a_round_of_rps(player1, player2)`, which evaluates whether the round ended in a draw or
# whether one of the players won. To do this, the function should return one of the following values:
#
# - 0 if the round was a draw
# - 1 if player 1 won
# - 2 if player 2 won
#
# If one of the players has made an invalid entry, the
# Function should throw an exception of user-defined type `BadInputException`, in which the number of the player who is at fault is stored. (If both players made an invalid entry any player can be stored.)

# %% tags=["solution"]
class BadInputError(ValueError):
    def __init__(self, msg, invalid_player):
        super().__init__(msg)
        self.invalid_player = invalid_player


def evaluiere_eine_runde_knobeln(spieler1, spieler2):
    if spieler1 == spieler2 and spieler1 in ["schere", "papier", "stein"]:
        return 0
    elif spieler1 == "schere":
        if spieler2 == "papier":
            return 1
        elif spieler2 == "stein":
            return 2
        else:
            raise BadInputError("Ungültiges Symbol von Spieler 2", 2)
    elif spieler1 == "papier":
        if spieler2 == "stein":
            return 1
        elif spieler2 == "schere":
            return 2
        else:
            raise BadInputError("Ungültiges Symbol von Spieler 2", 2)
    elif spieler1 == "stein":
        if spieler2 == "schere":
            return 1
        elif spieler2 == "papier":
            return 2
        else:
            raise BadInputError("Ungültiges Symbol von Spieler 2", 2)
    else:
        raise BadInputError("Ungültiges Symbol von Spieler 1", 1)


# %% [markdown] lang="de"
# Testen Sie alle möglichen Pfade durch Ihre Funktion.

# %% [markdown] lang="en"
# Test all possible paths through your function.

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("schere", "schere") == 0

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("papier", "papier") == 0

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("stein", "stein") == 0

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("schere", "papier") == 1

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("schere", "stein") == 2

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("papier", "schere") == 2

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("papier", "stein") == 1

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("stein", "schere") == 1

# %% tags=["solution"]
assert evaluiere_eine_runde_knobeln("stein", "papier") == 2


# %% tags=["solution"]
def assert_exception(lhs, rhs, invalid_player):
    try:
        evaluiere_eine_runde_knobeln(lhs, rhs)
        assert False, "No exception raised"
    except BadInputError as e:
        assert e.invalid_player == invalid_player, "Wrong invalid player"


# %% tags=["solution"]
assert_exception("eisen", "schere", 1)

# %% tags=["solution"]
assert_exception("schere", "eisen", 2)

# %% tags=["solution"]
assert_exception("papier", "eisen", 2)

# %% tags=["solution"]
assert_exception("stein", "eisen", 2)

# %% tags=["solution"]
assert_exception("eisen", "eisen", 1)


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `vergleiche_symbole(spieler1, spieler2)`,
# die folgende Information auf dem Bildschirm ausgibt:
#
# - `Unentschieden.`, wenn beide Spieler das gleiche Symbol gewählt haben,
# - `Spieler X gewinnt!`, wenn Spieler X (X = 1 oder 2) gewonnen hat,
# - `Ungültiges Symbol von Spieler X!`, wenn Spieler X ein ungültiges Symbol
#   eingegeben hat.

# %% [markdown] lang="en"
# Write a function `compare_symbols(player1, player2)`,
# that outputs the following information on the screen:
#
# - `Tie.` if both players have chosen the same symbol,
# - `Player X wins!` if player X (X = 1 or 2) won,
# - `Invalid symbol from player X!` if player X has entered an invalid symbol.

# %% tags=["solution"]
def vergleiche_symbole(spieler1, spieler2):
    try:
        ergebniss = evaluiere_eine_runde_knobeln(spieler1, spieler2)
        if ergebniss == 0:
            print("Unentschieden.")
        else:
            print(f"Spieler {ergebniss} gewinnt!")
    except BadInputError as e:
        print(f"Ungültiges Symbol von Spieler {e.invalid_player}!")


# %% [markdown] lang="de"
# Testen Sie `vergleiche_symbole` für geeignete Eingaben.

# %% [markdown] lang="en"
# Test `compare_symbols` for appropriate input.

# %% tags=["solution"]
vergleiche_symbole("papier", "papier")

# %% tags=["solution"]
vergleiche_symbole("schere", "papier")

# %% tags=["solution"]
vergleiche_symbole("papier", "stein")

# %% tags=["solution"]
vergleiche_symbole("stein", "schere")

# %% tags=["solution"]
vergleiche_symbole("papier", "schere")

# %% tags=["solution"]
vergleiche_symbole("stein", "papier")

# %% tags=["solution"]
vergleiche_symbole("schere", "stein")

# %% tags=["solution"]
vergleiche_symbole("computer", "papier")

# %% tags=["solution"]
vergleiche_symbole("papier", "computer")


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `spiele_eine_runde_knobeln()`, die die Auswahl
# von Spieler 1 und Spieler 2 vom Terminal einliest und dann auf dem
# Bildschirm ausgibt, wer gewonnen hat.
#
# (Das ist natürlich kein benutzbares Spiel, da Spieler 2 sehen kann,
# was Spieler 1 gewählt hat.)

# %% [markdown] lang="en"
# Write a function `play_a_round_of_rps()` that reads the selections
# of player 1 and player 2 from the terminal and prints out who won.
#
# (Of course this is not a usable game as player 2 can see
# the choice player 1 made.)

# %% tags=["solution"]
def spiele_eine_runde_knobeln():
    spieler1 = input("Auswahl von Spieler 1: ")
    spieler2 = input("Auswahl von Spieler 2: ")
    vergleiche_symbole(spieler1.lower(), spieler2.lower())


# %% [markdown] lang="de"
# Testen Sie die Funktion `spiele_eine_runde_knobeln()` interaktiv.

# %% [markdown] lang="en"
# Test the function `play_a_round_of_rps()` interactively.

# %% tags=["solution"]
# spiele_eine_runde_knobeln()

# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `spiele_knobeln()`, die zwei Spieler so lange
# gegeneinader knobeln lässt, bis ein Spieler 3 Spiele mehr gewonnen hat als
# der andere (z.B. wenn der erste Spieler 2 Spiele gewonnen hat, der zweite
# Spieler 5).

# %% [markdown] lang="en"
# Write a function `play_rps()` that lets two players play against each other until one player has won 3 games more than
# the other (e.g. if the first player has won 2 games and the second player 5).

# %% tags=["solution"]
def spiele_knobeln():
    gewinne1 = 0
    gewinne2 = 0
    while abs(gewinne1 - gewinne2) < 3:
        spieler1 = input("Auswahl von Spieler 1: ")
        spieler2 = input("Auswahl von Spieler 2: ")
        try:
            ergebnis = evaluiere_eine_runde_knobeln(spieler1, spieler2)
            if ergebnis == 1:
                print("Spieler 1 gewinnt diese Runde!")
                gewinne1 += 1
            elif ergebnis == 2:
                print("Spieler 2 gewinnt diese Runde!")
                gewinne2 += 1
            else:
                print("Unentschieden!")
        except BadInputError as e:
            print(e)
    print(f"Spieler {1 if gewinne1 > gewinne2 else 2} gewinnt!")


# %% tags=["solution"]
# spiele_knobeln()
