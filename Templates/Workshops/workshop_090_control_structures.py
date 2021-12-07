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
# # Gerade Zahl
#
# Schreiben Sie eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt,
# falls `zahl` gerade ist und `False`, falls `zahl` ungerade ist.

# %% {{ doc.solution() }}
def ist_gerade(zahl):
    return zahl % 2 == 0


# %% [markdown]
# Schreiben Sie eine Funktion `drucke_ist_gerade(zahl)`, die 
#
# - `{zahl} ist gerade.` auf dem Bildschirm ausgibt, falls `zahl` gerade ist und
# - `{zahl} ist nicht gerade.` auf dem Bildschirm ausgibt, falls `zahl` nicht
#   gerade ist.

# %% {{ doc.solution() }}
def drucke_ist_gerade(zahl):
    if ist_gerade(zahl):
        print(f"{zahl} ist gerade.")
    else:
        print(f"{zahl} ist nicht gerade.")


# %% [markdown]
# Testen Sie `drucke_ist_gerade(zahl)` mit den Werten 0, 1 und 8.

# %% {{ doc.solution() }}
drucke_ist_gerade(0)
drucke_ist_gerade(1)
drucke_ist_gerade(8)


# %% [markdown]
# # Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die 
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %% {{ doc.solution() }}
def drucke_ist_positiv(zahl):
    if zahl > 0:
        print(f"{zahl} ist positiv.")
    elif zahl < 0:
        print(f"{zahl} ist negativ.")
    else:
        print("0 ist Null.")


# %% [markdown]
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %% {{ doc.solution() }}
drucke_ist_positiv(-3)
drucke_ist_positiv(0)
drucke_ist_positiv(2)


# %% {{ doc.solution() }}
def klassifiziere_positiv_negativ(zahl):
    if zahl > 0:
        return f"{zahl} ist positiv."
    elif zahl < 0:
        return f"{zahl} ist negativ."
    else:
        return "0 ist Null."


def drucke_ist_positiv_2(zahl):
    print(klassifiziere_positiv_negativ(zahl))


# %% {{ doc.solution() }}
drucke_ist_positiv_2(-3)
drucke_ist_positiv_2(0)
drucke_ist_positiv_2(2)


# %% [markdown]
# # Signum
#
# Schreiben Sie eine Funktion `signum(zahl)`, die
#
# - 1 zurückgibt, falls `zahl > 0` ist,
# - 0 zurückgibt, falls `zahl == 0` ist,
# - -1 zurückgibt, falls `zahl < 0` ist.

# %% {{ doc.solution() }}
def signum(zahl):
    if zahl > 0:
        return 1
    elif zahl == 0:
        return 0
    else:
        return -1


# %% [markdown]
# Testen Sie die Funktion für repräsentative Werte.

# %% {{ doc.solution() }}
signum(-10)

# %% {{ doc.solution() }}
signum(0)

# %% {{ doc.solution() }}
signum(2)


# %% [markdown]
# # Umrechnung in Meilen
#
# Schreiben Sie eine Funktion `konvertiere_km_nach_meilen(km)` die den Wert
# `km` von Kilometer in Meilen umrechnet (d.h. die den Wert in Meilen
# zurückgibt).
#
# *Hinweis:*
# - Ein Kilometer entspricht $0,621371$ Meilen

# %% {{ doc.solution() }}
def konvertiere_km_nach_meilen(km):
    return km * 0.621371


# %% [markdown]
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %% {{ doc.solution() }}
konvertiere_km_nach_meilen(1)

# %% {{ doc.solution() }}
konvertiere_km_nach_meilen(5)


# %% [markdown]
#
# Schreiben Sie eine Funktion `meilen_app()`, die eine Länge in Kilometern
# einliest und die äquivalente Entfernung in Meilen ausgibt.
#
# *Hinweise* 
# - Ein String kann mit `float()` in einen Float-Wert umgewandelt werden.

# %% {{ doc.solution() }}
def meilen_app():
    km = input("Bitte geben Sie eine Entfernung in km ein: ")
    if km != "":
        meilen = konvertiere_km_nach_meilen(float(km))
        print(f"{km} km sind {meilen} Meilen")
    else:
        print("Bitte geben Sie eine gültige Entfernung in km ein.")


# %% {{ doc.solution() }}
meilen_app()


# %% [markdown]
# # Umrechnung in Meilen mit Truthiness
#
# Schreiben Sie eine Funktion `meilen_app_2`, die sich wie `meilen_app`
# verhält, aber Truthiness von Strings ausnutzt.

# %% {{ doc.solution() }}
def meilen_app_2():
    km = input("Bitte geben Sie eine Entfernung in km ein: ")
    if km:
        meilen = konvertiere_km_nach_meilen(float(km))
        print(f"{km} km sind {meilen} Meilen")
    else:
        print("Bitte geben Sie eine gültige Entfernung in km ein.")


# %% {{ doc.solution() }}
# meilen_app_2()

# %% [markdown]
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

# %% {{ doc.solution() }}
def kinopreis(alter):
    if (alter < 2):
        return 0
    elif alter <= 12:
        return 2
    elif alter <= 17:
        return 5
    elif alter < 65:
        return 10
    else:
        return 6


# %% [markdown]
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %% {{ doc.solution() }}
kinopreis(1)

# %% {{ doc.solution() }}
kinopreis(7)

# %% {{ doc.solution() }}
kinopreis(15)

# %% {{ doc.solution() }}
kinopreis(25)

# %% {{ doc.solution() }}
kinopreis(70)


# %% [markdown] Schreiben Sie eine Funktion `drucke_kinopreis(alter)`,
# die einen Text der folgenden Art auf dem Bildschirm ausgibt:
#
# ```
# Sie sind 1 Jahr alt. Ihr Preis beträgt 0 Euro.
# Sie sind 15 Jahre alt. Ihr Preis beträgt 5 Euro.
# ```

# %% {{ doc.solution() }}
def drucke_kinopreis(alter):
    preis = kinopreis(alter)
    if alter == 1:
        print("Sie sind 1 Jahr alt. Ihr Preis beträgt {preis} Euro.")
    else:
        print(f"Sie sind {alter} Jahre alt. Ihr Preis beträgt {preis} Euro.")


# %% [markdown]
# Testen Sie `drucke_kinopreis(alter)` für repräsentative Werte.

# %% {{ doc.solution() }}
drucke_kinopreis(1)
drucke_kinopreis(7)
drucke_kinopreis(15)
drucke_kinopreis(25)
drucke_kinopreis(70)


# %% [markdown]
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

# %% {{ doc.solution() }}
def kino_app():
    alter = input("Wie alt sind Sie? ")
    if alter:
        drucke_kinopreis(int(alter))
    else:
        "Bitte geben Sie ein gültiges Alter ein."


# %%
# kino_app()

# %% [markdown]
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

# %% {{ doc.solution() }}
def rate_wort(lösung):
    geratenes_wort = input("Bitte geben Sie ein Wort ein: ")
    while geratenes_wort != lösung:
        geratenes_wort = input("Bitte versuchen Sie es nochmal: ")
    print("Genau!")


# %%
# rate_wort("Haus")

# %% [markdown]
# ### Zahlenraten
#
# Implementieren Sie eine Funktion `rate_zahl(lösung)`, die den Benutzer so
# lange nach einer Zahl fragt, bis er die Lösung erraten hat. Nach jeder
# Eingabe soll dem Benutzer angezeigt werden, ob die eingegebene Zahl zu
# groß, zu klein oder richtig ist.

# %% {{ doc.solution() }}
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

# %% [markdown]
#
# Wie müssen Sie Ihre Lösung modifizieren, damit der Spieler durch Eingabe
# einer leeren Zeichenkette das Spiel abbrechen kann?

# %% {{ doc.solution() }}
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


# %% {{ doc.solution() }}
# rate_zahl_1(23)

# %% [markdown]
# Lösung unter Zuhilfenahme der Funktion `klassifiziere_zahl`

# %% {{ doc.solution() }}
def klassifiziere_zahl(geratene_zahl, lösung):
    if geratene_zahl < lösung:
        return False, "Die geratene Zahl ist zu klein! "
    elif geratene_zahl > lösung:
        return False, "Die geratene Zahl ist zu groß! "
    else:
        return True, "Sie haben gewonnen!"


# %% {{ doc.solution() }}
def rate_zahl_2(lösung):
    geratene_zahl = input("Bitte geben Sie eine Zahl ein: ")
    erfolg, hinweis = klassifiziere_zahl(int(geratene_zahl), lösung)
    while not erfolg:
        geratene_zahl = input(hinweis)
        erfolg, hinweis = klassifiziere_zahl(int(geratene_zahl), lösung)
    print("Sie haben gewonnen!")


# %% {{ doc.solution() }}
# rate_zahl_2(23)

# %% [markdown]
# # Vererbung
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma
# erstellt werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein
#   Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn
#   gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des
#   Grundgehalts plus der Bezahlung für die Überstunden
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des
#   Grundgehalts plus Bonus
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager`
# mit geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt
# berechnet.

# %% {{ doc.solution() }}
class Mitarbeiter:
    def __init__(self, name, pers_nr, grundgehalt):
        self.name = name
        self.pers_nr = pers_nr
        self.grundgehalt = grundgehalt

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %% {{ doc.solution() }}
class Arbeiter(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, überstunden, stundensatz):
        super().__init__(name, pers_nr, grundgehalt)
        self.überstunden = überstunden
        self.stundensatz = stundensatz

    def __repr__(self):
        return (
            f"Arbeiter({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.überstunden}, {self.stundensatz})")

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %% {{ doc.solution() }}
class Manager(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, bonus):
        super().__init__(name, pers_nr, grundgehalt)
        self.bonus = bonus

    def __repr__(self):
        return (f"Manager({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
                f"{self.bonus})")

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% {{ doc.solution() }}
a = Arbeiter("Hans", 123, 36_000, 3, 40)
print(a.gehalt())
a

# %% {{ doc.solution() }}
m = Manager("Sepp", 666, 60_000, 30_000)
print(m.gehalt())
m


# %% [markdown]
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

# %% {{ doc.solution() }}
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


# %% [markdown]
# Testen Sie alle möglichen Pfade durch Ihre Funktion.

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("schere", "schere") == 0

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("papier", "papier") == 0

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("stein", "stein") == 0

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("schere", "papier") == 1

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("schere", "stein") == 2

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("papier", "schere") == 2

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("papier", "stein") == 1

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("stein", "schere") == 1

# %% {{ doc.solution() }}
assert evaluiere_eine_runde_knobeln("stein", "papier") == 2


# %% {{ doc.solution() }}
def assert_exception(lhs, rhs, invalid_player):
    try:
        evaluiere_eine_runde_knobeln(lhs, rhs)
        assert False, "No exception raised"
    except BadInputError as e:
        assert e.invalid_player == invalid_player, "Wrong invalid player"


# %% {{ doc.solution() }}
assert_exception("eisen", "schere", 1)

# %% {{ doc.solution() }}
assert_exception("schere", "eisen", 2)

# %% {{ doc.solution() }}
assert_exception("papier", "eisen", 2)

# %% {{ doc.solution() }}
assert_exception("stein", "eisen", 2)

# %% {{ doc.solution() }}
assert_exception("eisen", "eisen", 1)


# %% [markdown]
#
# Schreiben Sie eine Funktion `vergleiche_symbole(spieler1, spieler2)`,
# die folgende Information auf dem Bildschirm ausgibt:
#
# - `Unentschieden.`, wenn beide Spieler das gleiche Symbol gewählt haben,
# - `Spieler X gewinnt!`, wenn Spieler X (X = 1 oder 2) gewonnen hat,
# - `Ungültiges Symbol von Spieler X!`, wenn Spieler X ein ungültiges Symbol
#   eingegeben hat.

# %% {{ doc.solution() }}
def vergleiche_symbole(spieler1, spieler2):
    try:
        ergebniss = evaluiere_eine_runde_knobeln(spieler1, spieler2)
        if ergebniss == 0:
            print("Unentschieden.")
        else:
            print(f"Spieler {ergebniss} gewinnt!")
    except BadInputError as e:
        print(f"Ungültiges Symbol von Spieler {e.invalid_player}!")


# %% [markdown]
# Testen Sie `vergleiche_symbole` für geeignete Eingaben.

# %% {{ doc.solution() }}
vergleiche_symbole("papier", "papier")

# %% {{ doc.solution() }}
vergleiche_symbole("schere", "papier")

# %% {{ doc.solution() }}
vergleiche_symbole("papier", "stein")

# %% {{ doc.solution() }}
vergleiche_symbole("stein", "schere")

# %% {{ doc.solution() }}
vergleiche_symbole("papier", "schere")

# %% {{ doc.solution() }}
vergleiche_symbole("stein", "papier")

# %% {{ doc.solution() }}
vergleiche_symbole("schere", "stein")

# %% {{ doc.solution() }}
vergleiche_symbole("computer", "papier")

# %% {{ doc.solution() }}
vergleiche_symbole("papier", "computer")


# %% [markdown]
#
# Schreiben Sie eine Funktion `spiele_eine_runde_knobeln()`, die die Auswahl
# von Spieler 1 und Spieler 2 vom Terminal einliest und dann auf dem
# Bildschirm ausgibt, wer gewonnen hat.
#
# (Das ist natürlich kein benutzbares Spiel, da Spieler 2 sehen kann,
# was Spieler 1 gewählt hat.)

# %% {{ doc.solution() }}
def spiele_eine_runde_knobeln():
    spieler1 = input("Auswahl von Spieler 1: ")
    spieler2 = input("Auswahl von Spieler 2: ")
    vergleiche_symbole(spieler1.lower(), spieler2.lower())


# %% [markdown]
# Testen Sie die Funktion `spiele_eine_runde_knobeln()` interaktiv.

# %% {{ doc.solution() }}
# spiele_eine_runde_knobeln()

# %% [markdown]
#
# Schreiben Sie eine Funktion `spiele_knobeln()`, die zwei Spieler so lange
# gegeneinader knobeln lässt, bis ein Spieler 3 Spiele mehr gewonnen hat als
# der andere (z.B. wenn der erste Spieler 2 Spiele gewonnen hat, der zweite
# Spieler 5).

# %% {{ doc.solution() }}
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


# %% {{ doc.solution() }}
# spiele_knobeln()

# %% [markdown]
# # Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion `write_text_to_file(text: str, file_name: str)
# -> None`, die den String `text` in die Datei `file_name` schreibt, sofern
# diese *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft,
# falls die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von
# `open()`.

# %% {{ doc.solution() }}
def write_text_to_file(text, file_name):
    with open(file_name, 'x') as file:
        file.write(text)


# %% [markdown]
#
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den
# Text `Python 3.8` in die Datei `my-private-file.txt` zu schreiben.

# %% {{ doc.solution() }}
write_text_to_file('Python 3.8', 'my_private_file.txt')

# %% {{ doc.solution() }}
write_text_to_file('Python 3.8', 'my_private_file.txt')


# %% [markdown]
# Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die 
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)`
#   auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt
#   falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %% {{ doc.solution() }}
def annotate_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
            print('(annotated version)')
    except FileNotFoundError:
        print('No file found, we will bill the time we spent searching.')
    finally:
        print('Our invoice will be sent by mail.')


# %% {{ doc.solution() }}
annotate_file('my_private_file.txt')

# %% {{ doc.solution() }}
annotate_file('does-not-exist.txt')
