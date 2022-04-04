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
# # Farben
#
# Definieren Sie eine Variable `farben`, die eine Liste mit den Strings
# `Rot`, `Grün` und `Blau` enthält.

# %% [markdown] lang="en"
# # Colours
#
# Define a variable `colors` containing a list of the strings
# `Red`, `Green` and `Blue`.

# %% tags=["solution"]
farben = ["Rot", "Grün", "Blau"]

# %% [markdown] lang="de"
# Überprüfen Sie, ob der String `Gelb` in `farben` enthalten ist

# %% [markdown] lang="en"
# Check if the string `yellow` is in `colors`

# %% tags=["solution"]
"Gelb" in farben

# %% [markdown] lang="de"
# Fügen Sie `Gelb` zu den Farben hinzu.

# %% [markdown] lang="en"
# Add `Yellow` to the colors.

# %% tags=["solution"]
farben.append("Gelb")

# %% [markdown] lang="de"
# Überprüfen Sie nochmals, ob `Gelb` in den Farben enthalten ist.

# %% [markdown] lang="en"
# Check again if `yellow` is included in the colors.

# %% tags=["solution"]
"Gelb" in farben

# %% [markdown] lang="de"
# Wie viele Farben enthält die in `farben` gespeicherte Liste jetzt?

# %% [markdown] lang="en"
# How many colors does the list stored in `colors` contain now?

# %% tags=["solution"]
len(farben)

# %% [markdown] lang="de"
# Ändern Sie das erste Element von `farben` in `Dunkelrot`

# %% [markdown] lang="en"
# Change the first element in `colors` to `dark red`

# %% tags=["solution"]
farben[0] = "Dunkelrot"

# %% [markdown] lang="de"
# Fügen Sie `Lila` als zweites Element in die Liste ein.

# %% [markdown] lang="en"
# Add `Purple` as the second item in the list.

# %% tags=["solution"]
farben.insert(1, "Lila")

# %% [markdown] lang="de"
# Was ist das dritte Element der Liste `farben`?

# %% [markdown] lang="en"
# What is the third element of the `colors` list?

# %% tags=["solution"]
farben[2]

# %% [markdown] lang="de"
# Löschen Sie das zweite Element der Liste `farben`

# %% [markdown] lang="en"
# Delete the second item of the `colors` list

# %% tags=["solution"]
del farben[1]

# %% [markdown] lang="de"
# Was ist das dritte Element der Liste `farben` jetzt?

# %% [markdown] lang="en"
# What is the third element of the `colors` list now?

# %% tags=["solution"]
farben[2]

# %% [markdown] lang="de"
# # Slicing

# %% [markdown] lang="en"
# # Slicing

# %%
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% [markdown] lang="de"
# Extrahieren Sie von `my_list` eine Liste mit allen Elementen außer den ersten beiden.

# %% [markdown] lang="en"
# Extract from `my_list` a list with all elements except the first two.

# %% tags=["solution"]
my_list[2:]

# %% [markdown] lang="de"
# Extrahieren Sie von `my_list` eine Liste, die aus dem 2. und 3. Element besteht.

# %% [markdown] lang="en"
# From `my_list` extract a list consisting of the 2nd and 3rd elements.

# %% tags=["solution"]
my_list[1:3]

# %% [markdown] lang="de"
# Extrahieren Sie von `my_list` eine neue Liste, die alle Elemente außer dem
# ersten und dem letzten enthält.

# %% [markdown] lang="en"
# Extract from `my_list` a new list containing all elements except the
# first and last contains.

# %% tags=["solution"]
my_list[1:-1]


# %% [markdown] lang="de"
# # Finden in Listen
#
# Schreiben Sie eine Funktion `finde_erste_gerade_zahl(liste)`, die den Index
# der ersten geraden Zahl in einer Liste von ganzen Zahlen zurückgibt. Falls
# die Liste keine gerade Zahl enthält soll die Funktion `None` zurückgeben.

# %% [markdown] lang="en"
# # Finding in lists
#
# Write a function `find_first_even_number(list)` that returns the index of the first even number in a list of integers. If the list does not contain an even number, the function should return `None`.

# %% tags=["solution"]
def finde_erste_gerade_zahl(liste):
    result = None
    for index, zahl in enumerate(liste):
        if zahl % 2 == 0:
            result = index
            break
    return result


# %% [markdown] lang="de"
# Testen Sie die Funktion für geeignete Argumente.

# %% [markdown] lang="en"
# Test the function for appropriate arguments.

# %% tags=["solution"]
assert finde_erste_gerade_zahl([1, 3, 5, 2, 4, 6]) == 3
assert finde_erste_gerade_zahl([1, 3]) is None
assert finde_erste_gerade_zahl([0, 1, 2, 3]) == 0


# %% [markdown] lang="de"
# ## Mittelwert einer Liste
#
# Der Mittelwert einer Liste mit $n$ Elementen $[x_0, \dots, x_{n-1}]$ ist
# definiert als
#
# $$\frac{x_0 + \dots + x_{n-1}}{n}$$
#
# Schreiben Sie eine Funktion `mittelwert(liste)`, die den Mittelwert einer
# Liste berechnet.

# %% [markdown] lang="en"
# ## Mean value of a list
#
# The mean of a list with $n$ elements $[x_0, \dots, x_{n-1}]$ is
# defined as
#
# $$\frac{x_0 + \dots + x_{n-1}}{n}$$
#
# Write a function `mean(list)` that calculates the mean of a list.

# %% tags=["solution"]
def mittelwert(zahlen):
    if zahlen:
        ergebnis = 0
        for zahl in zahlen:
            ergebnis += zahl
        return ergebnis / len(zahlen)
    return 0


# %% [markdown] pycharm={"name": "#%% md\n"} lang="de"
# Testen Sie die Funktion für geeignete Argumente.

# %% [markdown] lang="en"
# Test the function for appropriate arguments.

# %% tags=["solution"]
assert mittelwert([1, 2, 3]) == 2.0

# %% tags=["solution"]
assert mittelwert([]) == 0


# %% [markdown] lang="de"
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

# %% [markdown] lang="en"
# **Additional task:** The mean of the elements of a list can be calculated iteratively as follows:
#
# - The mean $m$ of the empty list is (by definition for this solution) 0
# - If we add the $n+1$-th element $x_{n+1}$, then the new mean is calculated as
#
# $$m \leftarrow m + \frac{1}{n+1}(x_{n+1} - m)$$
#
# Write a function `iterative_average(list)` that calculates the mean of a list iteratively.

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

# %% [markdown] lang="de"
# # Quadratzahlen
#
# Gegeben sei die folgende Liste mit Zahlen.

# %% [markdown] lang="en"
# # Square numbers
#
# Given the following list of numbers.

# %%
numbers = [1, 7, 4, 87, 23]

# %% [markdown] lang="de"
# Erzeugen Sie eine neue Liste, die die Quadrate der Zahlen in `numbers` enthält.

# %% [markdown] lang="en"
# Create a new list containing the squares of the numbers in `numbers`.

# %% tags=["solution"]
result = []
for n in numbers:
    result.append(n * n)
result


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `quadriere(zahlen)`, die eine neue Liste mit den
# Quadraten der Zahlen in `zahlen` zurückgibt.

# %% [markdown] lang="en"
# Write a function `square(numbers)` that returns a new list with the
# squares the numbers in `numbers`.

# %% tags=["solution"]
def quadriere(zahlen):
    result = []
    for n in zahlen:
        result.append(n * n)
    return result


# %% tags=["solution"]
assert quadriere(numbers) == [1, 49, 16, 7569, 529]

# %% [markdown] lang="de"
# # Quadratzahlen mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste mit den Quadraten von `numbers`. Verwenden Sie
# dazu eine Listen-Komprehension

# %% [markdown] lang="en"
# # Square numbers with list comprehension
#
# Create a new list with the squares of `numbers` using list comprehension.

# %% tags=["solution"]
[n * n for n in numbers]


# %% [markdown] lang="de"
# Schreiben Sie die Funktion `quadriere(zahlen)` mit Listen-Komprehension.

# %% [markdown] lang="en"
# Implement the function `square(numbers)` using list comprehension.

# %% tags=["solution"]
def quadriere(zahlen):
    return [n * n for n in zahlen]


# %% tags=["solution"]
quadriere(numbers)

# %% [markdown] lang="de"
# # Filtern
#
# Gegeben sei die folgende Liste mit Zahlen:

# %% [markdown] lang="en"
# # Filtering lists
#
# Given the following list of numbers:

# %%
numbers = [1, 183, 7, 4, 87, 10, 23, -12, 493, 11]

# %% [markdown] lang="de"
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer als 10 sind.

# %% [markdown] lang="en"
# Create a new list containing all numbers in `numbers` that are greater than 10.

# %% tags=["solution"]
result = []
for n in numbers:
    if n > 10:
        result.append(n)
result


# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `zahlen_größer_als_10(zahlen)`, die eine neue
# Liste zurückgibt, die die Zahlen aus `zahlen` enthält, die größer als 10 sind.

# %% [markdown] lang="en"
# Write a function `numbers_greater_than_10(numbers)` that returns a list containing the numbers from `numbers` that are greater than 10.

# %% tags=["solution"]
def zahlen_größer_als_10(zahlen):
    result = []
    for n in zahlen:
        if n > 10:
            result.append(n)
    return result


# %% tags=["solution"]
assert zahlen_größer_als_10(numbers) == [183, 87, 23, 493, 11]

# %% [markdown] lang="de"
# # Filtern mit Listen-Komprehension
#
# Erzeugen Sie eine neue Liste, die alle Zahlen in `numbers` enthält, die größer
# als 10 sind. Verwenden Sie dazu Listen-Komprehension.

# %% [markdown] lang="en"
# # Filtering with list comprehension
#
# Create a new list containing all numbers in `numbers` that are larger
# than 10. Use list comprehension to do this.

# %% tags=["solution"]
[n for n in numbers if n > 10]


# %% [markdown] lang="de"
# Schreiben Sie die Funktion `zahlen_größer_als_10(zahlen)` mit
# Listen-Komprehension.

# %% [markdown] lang="en"
# Implement the function `numbers_greater_than_10(numbers)` using list comprehension.

# %% tags=["solution"]
def zahlen_größer_als_10(zahlen):
    return [n for n in zahlen if n > 10]


# %% tags=["solution"]
assert zahlen_größer_als_10(numbers) == [183, 87, 23, 493, 11]


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `quadrate_von_zahlen_kleiner_10( zahlen)`,
# die eine neue Liste zurückgibt, die die Quadrate aller Zahlen < 10 aus
# `zahlen` enthält.

# %% [markdown] lang="en"
# Write a function `square_of_numbers_less than_10(numbers)`,
# which returns a new list containing the squares of all numbers < 10
# contained in `numbers`.

# %% tags=["solution"]
def quadrate_von_zahlen_kleiner_10(zahlen):
    return [n * n for n in zahlen if n < 10]


# %%
numbers

# %% tags=["solution"]
assert quadrate_von_zahlen_kleiner_10(numbers) == [1, 49, 16, 144]

# %% [markdown] lang="de"
# # Generatoren

# %% [markdown] lang="en"
# # Generators

# %% [markdown] lang="de"
# ## Generator für Quadratzahlen
#
# Schreiben Sie einen Generator, der die ersten 10 Quadratzahlen erzeugt.

# %% [markdown] lang="en"
# ## Square number generator
#
# Write a generator that produces the first 10 square numbers.

# %% tags=["solution"]
gen = (i * i for i in range(1, 11))

# %% tags=["solution"]
for i in gen:
    print(i, end=" ")


# %% [markdown] lang="de"
# ## Take
#
# Schreiben Sie eine Funktion `take(n: int, it)` die ein Iterable `it` als
# Argument bekommt und ein neues Iterable zurückgibt, das die ersten `n`
# Elemente von `it` liefert.

# %% [markdown] lang="en"
# ## Take
#
# Write a function `take(n: int, it)` which takes an Iterable `it` as
# argument and returns a new iterable that successively returns the first `n`
# elements that `it` supplies.

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
