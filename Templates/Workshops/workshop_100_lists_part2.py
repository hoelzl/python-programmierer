# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# j2 import 'macros.j2' as doc
# %% [markdown]
# # Farben
#
# Definieren Sie eine Variable `farben`, die eine Liste mit den Strings
# `Rot`, `Grün` und `Blau` enthält.

# %% tags=["solution"]
farben = ["Rot", "Grün", "Blau"]

# %% [markdown]
# Überprüfen Sie, ob der String `Gelb` in `farben` enthalten ist

# %% tags=["solution"]
"Gelb" in farben

# %% [markdown]
# Fügen Sie `Gelb` zu den Farben hinzu.

# %% tags=["solution"]
farben.append("Gelb")

# %% [markdown]
# Überprüfen Sie nochmals, ob `Gelb` in den Farben enthalten ist.

# %% tags=["solution"]
"Gelb" in farben

# %% [markdown]
# Wie viele Farben enthält die in `farben` gespeicherte Liste jetzt?

# %% tags=["solution"]
len(farben)

# %% [markdown]
# Ändern Sie das erste Element von `farben` in `Dunkelrot`

# %% tags=["solution"]
farben[0] = "Dunkelrot"

# %% [markdown]
# Fügen Sie `Lila` als zweites Element in die Liste ein.

# %% tags=["solution"]
farben.insert(1, "Lila")

# %% [markdown]
# Was ist das dritte Element der Liste `farben`?

# %% tags=["solution"]
farben[2]

# %% [markdown]
# Löschen Sie das zweite Element der Liste `farben`

# %% tags=["solution"]
del farben[1]

# %% [markdown]
# Was ist das dritte Element der Liste `farben` jetzt?

# %% tags=["solution"]
farben[2]

# %% [markdown]
# # Slicing

# %%
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% [markdown]
# Extrahieren Sie von `liste` eine Liste mit allen Elementen außer den ersten
# beiden.

# %% tags=["solution"]
liste[2:]

# %% [markdown]
# Extrahieren Sie von `liste` eine Liste, die aus dem 2. und 3. Element besteht.

# %% tags=["solution"]
liste[1:3]

# %% [markdown]
# Extrahieren Sie von `liste` eine neue Liste, die alle Elemente außer dem
# ersten und dem letzten enthält.

# %% tags=["solution"]
liste[1:-1]


# %% [markdown]
# # Finden in Listen
#
# Schreiben Sie eine Funktion `finde_erste_gerade_zahl(liste)`, die den Index
# der ersten geraden Zahl in einer Liste von ganzen Zahlen zurückgibt. Falls
# die Liste keine gerade Zahl enthält soll die Funktion `None` zurückgeben.

# %% tags=["solution"]
def finde_erste_gerade_zahl(liste):
    result = None
    for index, zahl in enumerate(liste):
        if zahl % 2 == 0:
            result = index
            break
    return result


# %% [markdown]
# Testen Sie die Funktion für geeignete Argumente.

# %% tags=["solution"]
assert finde_erste_gerade_zahl([1, 3, 5, 2, 4, 6]) == 3
assert finde_erste_gerade_zahl([1, 3]) is None
assert finde_erste_gerade_zahl([0, 1, 2, 3]) == 0


# %% [markdown]
# ## Mittelwert einer Liste
#
# Der Mittelwert einer Liste mit $n$ Elementen $[x_0, \dots, x_{n-1}]$ ist
# definiert als
#
# $$\frac{x_0 + \dots + x_{n-1}}{n}$$
#
# Schreiben Sie eine Funktion `mittelwert(liste)`, die den Mittelwert einer
# Liste berechnet.

# %% tags=["solution"]
def mittelwert(zahlen):
    if zahlen:
        ergebnis = 0
        for zahl in zahlen:
            ergebnis += zahl
        return ergebnis / len(zahlen)
    return 0


# %% [markdown] pycharm={"name": "#%% md\n"}
# Testen Sie die Funktion für geeignete Argumente.

# %% tags=["solution"]
assert mittelwert([1, 2, 3]) == 2.0

# %% tags=["solution"]
assert mittelwert([]) == 0


# %% [markdown]
# **Zusatzaufgabe:** Der Mittelwert der Elemente einer Liste kann iterativ
# folgendermaßen berechnet werden:
#
# - Der Mittelwert $m$ der leeren Liste ist (per Definition für diese Lösung) 0
# - Wenn wir das $n+1$-te Element $x_{n+1}$ hinzufügen, so wird der neue
#   Mittelwert berechnet als
#
# $$m \leftarrow m + \frac{1}{n+1}(x_{n+1} - m)$$
#
# Schreiben Sie eine Funktion `iterativer_mittelwert(liste)`, die den
# Mittelwert einer Liste iterativ berechnet.
#

# %% tags=["solution"]
def iterativer_mittelwert(zahlen):
    ergebnis = 0
    for index, value in enumerate(zahlen):
        ergebnis += (value - ergebnis) / (index + 1)
    return ergebnis


# %% tags=["solution"]
assert iterativer_mittelwert([]) == 0.0

# %% tags=["solution"]
assert iterativer_mittelwert([1]) == 1.0

# %% tags=["solution"]
assert iterativer_mittelwert([1, 2, 3]) == 2.0

# %% tags=["solution"]
assert iterativer_mittelwert(range(11)) == 5.0


# %% tags=["solution"]
def assert_mittelwert_equal(liste):
    assert iterativer_mittelwert(liste) == mittelwert(liste)


# %% tags=["solution"]
assert_mittelwert_equal([])
assert_mittelwert_equal([1, 2, 3])
assert_mittelwert_equal(list(range(10)))

# %% [markdown]
# # Quadratzahlen
#
# Gegeben sei die folgende Liste mit Zahlen.

# %%
zahlen = [1, 7, 4, 87, 23]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die die Quadrate der Zahlen in `zahlen` enthält.

# %% tags=["solution"]
result = []
for n in zahlen:
    result.append(n * n)
result


# %% [markdown]
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die eine neue Liste mit den
# Quadraten der Zahlen in `zahlen` zurückgibt.

# %% tags=["solution"]
def quadriere(zahlen):
    result = []
    for n in zahlen:
        result.append(n * n)
    return result


# %% tags=["solution"]
assert quadriere(zahlen) == [1, 49, 16, 7569, 529]

# %% [markdown]
# # Quadratzahlen mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste mit den Quadraten von `zahlen`. Verwenden Sie
# dazu eine Listen-Komprehension

# %% tags=["solution"]
[n * n for n in zahlen]


# %% [markdown]
# Schreiben Sie die Funktion `quadriere(zahlen)` mit Listen-Komprehension.

# %% tags=["solution"]
def quadriere(zahlen):
    return [n * n for n in zahlen]


# %% tags=["solution"]
quadriere(zahlen)

# %% [markdown]
# # Filtern
#
# Gegeben sei die folgende Liste mit Zahlen:

# %%
zahlen = [1, 183, 7, 4, 87, 10, 23, -12, 493, 11]

# %% [markdown]
# Erzeugen Sie eine neue Liste, die alle Zahlen in `zahlen` enthält, die größer als 10 sind.

# %% tags=["solution"]
result = []
for n in zahlen:
    if n > 10:
        result.append(n)
result


# %% [markdown]
# Schreiben Sie eine Funktion `zahlen_größer_als_10(zahlen)`, die eine neue
# Liste zurückgibt, die die Zahlen aus `zahlen` enthält, die größer als 10 sind.

# %% tags=["solution"]
def zahlen_größer_als_10(zahlen):
    result = []
    for n in zahlen:
        if n > 10:
            result.append(n)
    return result


# %% tags=["solution"]
assert zahlen_größer_als_10(zahlen) == [183, 87, 23, 493, 11]

# %% [markdown]
# # Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `zahlen` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %% tags=["solution"]
[n for n in zahlen if n > 10]


# %% [markdown]
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %% tags=["solution"]
def zahlen_größer_als_10(zahlen):
    return [n for n in zahlen if n > 10]


# %% tags=["solution"]
assert zahlen_größer_als_10(zahlen) == [183, 87, 23, 493, 11]


# %% [markdown]
#
# Schreiben Sie eine Funktion `quadrate_von_zahlen_kleiner_10( zahlen)`,
# die eine neue Liste zurückgibt, die die Quadrate aller Zahlen < 10 aus
# `zahlen` enthält.

# %% tags=["solution"]
def quadrate_von_zahlen_kleiner_10(zahlen):
    return [n * n for n in zahlen if n < 10]


# %%
zahlen

# %% tags=["solution"]
assert quadrate_von_zahlen_kleiner_10(zahlen) == [1, 49, 16, 144]

# %% [markdown]
# # Generatoren

# %% [markdown]
# ## Generator für Quadratzahlen
#
# Schreiben Sie einen Generator, der die ersten 10 Quadratzahlen erzeugt.

# %% tags=["solution"]
gen = (i * i for i in range(1, 11))

# %% tags=["solution"]
for i in gen:
    print(i, end=" ")


# %% [markdown]
# ## Take
#
# Schreiben Sie eine Funktion `take(n: int, it)` die ein Iterable `it` als
# Argument bekommt und ein neues Iterable zurückgibt, das die ersten `n`
# Elemente von `it` liefert.

# %% tags=["solution"]
def take(n, it):
    for i, elt in enumerate(it):
        if i >= n:
            break
        yield elt


# %% tags=["solution"]
for i in take(4, range(20)):
    print(i, end=" ")

# %% tags=["solution"]
for i in take(100, range(5)):
    print(i, end=" ")
