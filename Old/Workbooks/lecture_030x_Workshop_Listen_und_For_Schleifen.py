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
# # Farben
#
# Definieren Sie eine Variable `farben`, die eine Liste mit den Strings `Rot`, `Grün` und `Blau` enthält.

# %%

# %% [markdown]
# Überprüfen Sie, ob der String `Gelb` in `farben` enthalten ist

# %%

# %% [markdown]
# Fügen Sie `Gelb` zu den Farben hinzu.

# %%

# %% [markdown]
# Überprüfen Sie nochmals, ob `Gelb` in den Farben enthalten ist.

# %%

# %% [markdown]
# Wie viele Farben enthält die in `farben` gespeicherte Liste jetzt?

# %%

# %% [markdown]
# Ändern Sie das erste Element von `farben` in `Dunkelrot`

# %%

# %% [markdown]
# Fügen Sie `Lila` als zweites Element in die Liste ein.

# %%

# %% [markdown]
# Was ist das dritte Element der Liste `farben`?

# %%

# %% [markdown]
# Löschen Sie das zweite Element der Liste `farben`

# %%

# %% [markdown]
# Was ist das dritte Element der Liste `farben` jetzt?

# %%

# %% [markdown]
# # Slicing

# %%
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% [markdown]
# Extrahieren Sie von `liste` eine Liste mit allen Elementen außer den ersten beiden.

# %%

# %% [markdown]
# Extrahieren Sie von `liste` eine Liste, die aus dem 2. und 3. Element besteht.

# %%

# %% [markdown]
# Extrahieren Sie von `liste` eine neue Liste, die alle Elemente außer dem ersten und dem letzten enthält.

# %%

# %% [markdown]
# # Finden in Listen
#
# Schreiben Sie eine Funktion `finde_erste_gerade_zahl(liste)`, die den Index der ersten geraden Zahl in einer Liste von ganzen Zahlen zurückgibt. Falls die Liste keine gerade Zahl enthält soll die Funktion `None` zurückgeben.

# %%

# %% [markdown]
# Testen Sie die Funktion für geeignete Argumente.

# %%

# %% [markdown]
# ## Mittelwert einer Liste
#
# Der Mittelwert einer Liste mit $n$ Elementen $[x_0, \dots, x_{n-1}]$ ist definiert als
#
# $$\frac{x_0 + \dots + x_{n-1}}{n}$$
#
# Schreiben Sie eine Funktion `mittelwert(liste)`, die den Mittelwert einer Liste berechnet.

# %%

# %% [markdown]
# Testen Sie die Funktion für geeignete Argumente.

# %%

# %% [markdown] pycharm={"name": "#%% md\n"}
# **Zusatzaufgabe:** Der Mittelwert der Elemente einer Liste kann iterativ folgendermaßen berechnet werden:
#
# - Der Mittelwert $m$ der leeren Liste ist (per Definition für diese Lösung) 0
# - Wenn wir das $n+1$-te Element $x_{n+1}$ hinzufügen, so wird der neue Mittelwert berechnet als
#
# $$m \leftarrow m + \frac{1}{n+1}(x_{n+1} - m)$$
#
# Schreiben Sie eine Funktion `iterativer_mittelwert(liste)`, die den Mittelwert einer Liste iterativ berechnet.
#

# %% [markdown]
# # Quadratzahlen
#
# Gegeben sei die folgende Liste mit Zahlen.

# %%
zahlen = [1, 7, 4, 87, 23]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die die Quadrate der Zahlen in `zahlen` enthält.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die eine neue Liste mit den Quadraten der Zahlen in `zahlen` zurückgibt.

# %%

# %%

# %% [markdown]
# # Filtern
#
# Gegeben sei die folgende Liste mit Zahlen:

# %%
zahlen = [1, 183, 7, 4, 87, 10, 23, -12, 493, 11]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die alle Zahlen in `zahlen` enthält, die größer als 10 sind.

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `zahlen_größer_als_10(zahlen)`, die eine neue Liste zurückgibt, die die Zahlen aus `zahlen` enthält, die größer als 10 sind.

# %%

# %%

# %% [markdown]
# # Quadratzahlen mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste mit den Quadraten von `zahlen`. Verwenden Sie dazu eine Listen-Komprehension

# %%

# %% [markdown]
# Schreiben Sie die Funktion `quadriere(zahlen)` mit Listen-Komprehension.

# %%

# %%

# %% [markdown]
# # Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `zahlen` enthält, die größer als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %%

# %% [markdown]
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit Listen-Komprehension.

# %%

# %%

# %% [markdown]
# Schreiben Sie eine Funktion `quadrate_von_zahlen_kleiner_10(zahlen)`, die eine neue Liste zurückgibt, die die Quadrate aller Zahlen < 10 aus `zahlen` enthält.

# %%

# %%

# %% [markdown]
# # Generatoren

# %% [markdown]
# ## Generator für Quadratzahlen
#
# Schreiben Sie einen Generator, der die ersten 10 Quadratzahlen erzeugt.

# %%

# %% [markdown]
# ## Take
#
# Schreiben Sie eine Funktion `take(n: int, it)` die ein Iterable `it` als Argument bekommt und ein neues Iterable zurückgibt, das die ersten `n` Elemente von `it` liefert.

# %%
