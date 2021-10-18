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
# # Gerade Zahl
#
# Schreiben Sie eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt, falls `zahl` gerade ist und `False`, falls `zahl` ungerade ist.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `drucke_ist_gerade(zahl)`, die 
#
# - `{zahl} ist gerade.` auf dem Bildschirm ausgibt, falls `zahl` gerade ist und
# - `{zahl} ist nicht gerade.` auf dem Bildschirm ausgibt, falls `zahl` nicht gerade ist.

# %%

# %% [markdown]
# Testen Sie `drucke_ist_gerade(zahl)` mit den Werten 0, 1 und 8.

# %%

# %% [markdown]
# # Positiv / Negativ
#
# Schreiben Sie eine Funktion `drucke_ist_positiv(zahl)`, die 
#
# - `{zahl} ist positiv.` auf dem Bildschirm ausgibt, falls `zahl > 0` ist,
# - `{zahl} ist Null.` auf dem Bildschirm ausgibt, falls `zahl == 0` ist,
# - `{zahl} ist negativ.` auf dem Bildschirm ausgibt, falls `zahl < 0` ist.

# %%

# %% [markdown]
# Testen Sie `drucke_ist_positiv(zahl)` mit den Werten -3, 0 und 2.

# %%

# %% [markdown]
# # Signum
#
# Schreiben Sie eine Funktion `signum(zahl)`, die
#
# - 1 zurückgibt, falls `zahl > 0` ist,
# - 0 zurückgibt, falls `zahl == 0` ist,
# - -1 zurückgibt, falls `zahl < 0` ist.

# %%

# %% [markdown]
# Testen Sie die Funktion für repräsentative Werte.

# %%

# %%

# %%

# %% [markdown]
# # Umrechnung in Meilen
#
# Schreiben Sie eine Funktion `konvertiere_km_nach_meilen(km)` die den Wert `km` von Kilometer in Meilen umrechnet (d.h. die den Wert in Meilen zurückgibt).
#
# *Hinweis:*
# - Ein Kilometer entspricht $0,621371$ Meilen

# %%

# %% [markdown]
# Testen Sie `konvertiere_km_nach_meilen(km)` für 1 und 5 km.

# %%

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `meilen_app()`, die eine Länge in Kilometern einliest und die äquivalente Entfernung in Meilen ausgibt.
#
# *Hinweise* 
# - Ein String kann mit `float()` in einen Float-Wert umgewandelt werden.

# %%

# %%
# meilen_app()

# %% [markdown]
# # Umrechnung in Meilen mit Truthiness
#
# Schreiben Sie eine Funktion `meilen_app_2`, die sich wie `meilen_app` verhält, aber Truthiness von Strings ausnutzt.

# %%

# %%
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
# Schreiben Sie eine Funktion `kinopreis(alter)`, die den Preis in Abhängigkeit vom Alter berechnet und zurückgibt.

# %%

# %% [markdown]
# Testen Sie die Funktion `kinopreis()` für einige repräsentative Werte.

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `drucke_kinopreis(alter)`, die einen Text der folgenden Art auf dem Bildschirm ausgibt:
#
# ```
# Sie sind 1 Jahr alt. Ihr Preis beträgt 5 Euro.
# Sie sind 15 Jahre alt. Ihr Preis beträgt 5 Euro.
# ```

# %%

# %% [markdown]
# Testen Sie `drucke_kinopreis(alter)` für repräsentative Werte.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `kino_app()`, die ein Alter einliest und den Kinopreis für eine Person dieses Alters im gerade beschriebenen Format ausgibt. Zwei Beispielinteraktionen:
#
# ```
# Wie alt sind Sie? 37
# Sie sind 37 Jahre alt. Ihr Preis beträgt 10 Euro.
#
# Wie alt sind Sie? 12
# Sie sind 12 Jahre alt. Ihr Preis beträgt 2 Euro.
# ```

# %%

# %% [markdown]
# Testen Sie die Funktion `kino_app()` interaktiv.

# %%
# kino_app()

# %% [markdown]
# # Shout
#
# Schreiben Sie eine Funktion `shout(text)`, die `text` in Großbuchstaben, gefolgt von drei Außrufezeichen auf dem Bildschirm ausgibt.

# %%

# %% [markdown]
# Testen Sie die Funktion mit Argument `"Hallo"`

# %%

# %% [markdown]
# # Ratespiele
#
# Die folgenden einfachen "Spiele" erlauben dem Spieler unbegrenzt viele Eingaben. Daher ist es sinnvoll, sie mit einer While-Schleife zu implementieren.
#
# ### Raten eines Wortes
#
# Implementieren Sie eine Funktion `rate_wort(lösung)`, die den Benutzer so lange nach einem Wort fragt, bis das eingegebene Wort der Lösung entspricht.

# %%

# %% [markdown]
# Testen Sie die Funktion `rate_wort("Haus")` interaktiv.

# %%

# %% [markdown]
# ### Zahlenraten
#
# Implementieren Sie eine Funktion `rate_zahl(lösung)`, die den Benutzer so lange nach einer Zahl fragt, bis er die Lösung erraten hat. Nach jeder Eingabe soll dem Benutzer angezeigt werden, ob die eingegebene Zahl zu groß, zu klein oder richtig ist.

# %%

# %% [markdown]
# Testen Sie die Funktion `rate_zahl(17)` interaktiv.

# %%

# %% [markdown]
# Wie müssen Sie Ihre Lösung modifizieren, damit der Spieler durch Eingabe einer leeren Zeichenkette das Spiel abbrechen kann?

# %%

# %% [markdown]
# # Vererbung
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma erstellt werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des Grundgehalts plus der Bezahlung für die Überstunden 
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des Grundgehalts plus Bonus
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager` mit geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt berechnet.

# %%

# %% [markdown]
# # Knobeln
#
# (Auch Schere, Stein, Papier; Schnick, Schnack, Schnuck; Fli, Fla, Flu; usw.)
#
# Beim Knobeln spielen zwei Spieler gegeneinander. Jeder der beiden Spieler wählt eines der drei Symbole "Schere", "Stein" oder "Papier" aus (ohne die Wahl des anderen Spielers zu kennen). Haben beide Spieler das gleiche Symbol gewählt, so ist das Spiel unentschieden. Andernfalls gilt:
#
# - Schere schlägt Papier
# - Papier schlägt Stein
# - Stein schlägt Schere
#
# Schreiben Sie eine Funktion `evaluiere_eine_runde_knobeln(spieler1, spieler2)`, die bewertet, ob die Runde unentschieden ausgegangen ist oder ob einer der Spieler gewonnen hat. Dazu soll die Funktion folgende Werte zurückgeben:
#
# - 0, wenn die Runde unentschieden war
# - 1, wenn Spieler 1 gewonnen hat
# - 2, wenn Spieler 2 gewonnen hat
#
# Wenn einer der Spieler eine ungültige Eingabe vorgenommen hat soll die Funktion eine Exception vom benutzerdefinierten Typ `BadInputException` auslösen, in der die Nummer des Spielers gespeichert ist, dessen Eingabe ungültig war. (Wenn beide Spieler eine ungültige Eingabe vorgenommen haben kann ein beliebiger Spieler gespeichert werden.)

# %%

# %% [markdown]
# Testen Sie alle möglichen Pfade durch Ihre Funktion.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `vergleiche_symbole(spieler1, spieler2)`, die folgende Information auf dem Bildschirm ausgibt:
#
# - `Unentschieden.`, wenn beide Spieler das gleiche Symbol gewählt haben,
# - `Spieler X gewinnt!`, wenn Spieler X (X = 1 oder 2) gewonnen hat,
# - `Ungültiges Symbol von Spieler X!`, wenn Spieler X ein ungültiges Symbol eingegeben hat.

# %%

# %% [markdown]
# Testen Sie `vergleiche_symbole` für geeignete Eingaben.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `spiele_eine_runde_knobeln()`, die die Auswahl von Spieler 1 und Spieler 2 vom Terminal einliest und dann auf dem Bildschirm ausgibt, wer gewonnen hat.
#
# (Das ist natürlich kein benutzbares Spiel, da Spieler 2 sehen kann, was Spieler 1 gewählt hat.)

# %%

# %% [markdown]
# Testen Sie die Funktion `spiele_eine_runde_knobeln()` interaktiv.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `spiele_knobeln()`, die zwei Spieler so lange gegeneinader knobeln lässt, bis ein Spieler 3 Spiele mehr gewonnen hat als der andere (z.B. wenn der erste Spieler 2 Spiele gewonnen hat, der zweite Spieler 5).

# %%

# %%

# %% [markdown]
# Testen Sie ihre modifizierte Lösung interaktiv.

# %% [markdown]
# # Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion `write_text_to_file(text: str, file_name: str) -> None`, die den String `text` in die Datei `file_name` schreibt, sofern diese *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft, falls die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von `open()`.

# %%

# %% [markdown]
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den Text `Python 3.8` in die Datei `my-private-file.txt` zu schreiben.

# %%

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die 
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)` auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %%

# %% [markdown]
# Testen Sie die Funktion mit einer existierenden und einer nicht existierenden Datei.

# %%

# %%
