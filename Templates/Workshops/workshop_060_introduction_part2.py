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
# # Operatoren, Vergleiche
#
# Ist $2^{16}$ größer als $32\,000\,\,/\,\,2$?

# %% [markdown] lang="en"
# # Operators, comparisons
#
# Is $2^{16}$ larger than $32\,000\,\,/\,\,2$?

# %% tags=["solution"]
2 ** 16 > (32_000 / 2)

# %% [markdown] lang="de"
# Ist $72$ ohne Rest durch $3$ teilbar?

# %% [markdown] lang="en"
# Is $72$ divisible by $3$ without a remainder?

# %% tags=["solution"]
72 % 3 == 0

# %% [markdown] lang="de"
# Ist $72$ eine gerade Zahl (d.h. ohne Rest durch 2 teilbar)?

# %% [markdown] lang="en"
# Is $72$ an even number (i.e. divisible by 2 without remainder)?

# %% tags=["solution"]
72 % 2 == 0


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `ist_teilbar_durch(m, n)` die ( genau dann)
# `True` zurückgibt, wenn `m` durch `n` teilbar ist.

# %% [markdown] lang="en"
# Write a function `is_divisible_by(m,n)` which returns `True` if (and only if) `m` is divisible by `n`.

# %% tags=["solution"]
def ist_teilbar_durch(m, n):
    return m % n == 0


ist_teilbar_durch(6, 2)


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `ist_teilbar_durch_2_und_3(n)`, die genau dann
# `True` zurückgibt, wenn `n` ohne Rest durch $2$ und durch $3$ teilbar ist.

# %% [markdown] lang="en"
# Write a function `is_divisible_by_2_and_3(n)` that returns `True` if (and only if) `n` is divisible by $2$ and by $3$.

# %% tags=["solution"]
def ist_teilbar_durch_2_und_3(n):
    return ist_teilbar_durch(n, 2) and ist_teilbar_durch(n, 3)


# %% tags=["solution"]
def ist_teilbar_durch_2_und_3_v2(n):
    return n % 6 == 0


# %% [markdown] lang="de"
# Testen Sie, ob $72$ durch $2$ und durch $3$ teilbar ist.

# %% [markdown] lang="en"
# Test whether $72$ is divisible by $2$ and by $3$.

# %% tags=["solution"]
ist_teilbar_durch_2_und_3(72)


# %% [markdown] lang="de"
# # Volljährig
#
# Schreiben Sie eine Funktion `drucke_volljährig(alter)`, die `Volljährig`
# auf dem Bildschirm ausgibt, wenn `alter >= 18` ist und `Minderjährig` sonst.

# %% [markdown] lang="en"
# # Of legal age
#
# Write a function `print_of_age(age)` that prints `of_age` on the screen if `age >= 18` and `minor` otherwise.

# %% tags=["solution"]
def drucke_volljährig(alter):
    if alter < 18:
        print("Minderjährig")
    else:
        print("Volljährig")


# %% [markdown] lang="de"
# Testen Sie `drucke_volljährig(alter)` mit den Werten 17 und 18.

# %% [markdown] lang="en"
# Test `print_of age(age)` with the values ​​17 and 18.

# %% tags=["solution"]
drucke_volljährig(17)
drucke_volljährig(18)

# %% [markdown] lang="de"
# # Einkaufsliste
#
# Definieren Sie Variablen
# - `meine_einkaufsliste`, die eine Liste mit den Strings `Tee` und `Kaffee`
#   enthält,
# - `eine_andere_einkaufsliste`, die ebenfalls eine Liste mit den Strings
#   `Tee` und `Kaffee` enthält.

# %% [markdown] lang="en"
# # Shopping List
#
# Define variables
# - `my_shopping list` holding a list containing the strings `tea` and `coffee`
# - `another_shopping list`, holding a different list also containing the strings `tea` and `coffee`

# %% tags=["solution"]
meine_einkaufsliste = ["Tee", "Kaffee"]
eine_andere_einkaufsliste = ["Tee", "Kaffee"]


# %% [markdown] lang="de"
#
# Definieren Sie eine Funktion `drucke_einkaufsliste(einkaufsliste)`, die die
# als Argument übergebene Einkaufsliste ausdruckt:
#
# ```
# Einkaufsliste:
#   Tee
#   Kaffee
# ```

# %% [markdown] lang="en"
# Define a function `print_shopping_list(shopping_list)` that prints the shopping list passed as argument:
#
# ```
# Shopping List:
#   tea
#   coffee
# ```

# %% tags=["solution"]
def drucke_einkaufsliste(einkaufsliste):
    print("Einkaufsliste:")
    for item in einkaufsliste:
        print(" ", item)


# %% [markdown] lang="de"
#
# Testen Sie die Funktion `drucke_einkaufsliste(einkaufsliste)` mit beiden
# Einkaufslisten.

# %% [markdown] lang="en"
# Test the function `print_shopping list(shopping list)` with both
# shopping lists.

# %% tags=["solution"]
drucke_einkaufsliste(meine_einkaufsliste)

# %% tags=["solution"]
drucke_einkaufsliste(eine_andere_einkaufsliste)


# %% [markdown] lang="de"
# Definieren Sie eine Funktion `kaufe(produkt, einkaufsliste)`, das `produkt`
# zu  `einkaufsliste` hinzufügt.

# %% [markdown] lang="en"
# Define a function `buy(product, shopping_list)`, that adds `product` to `shopping_list`.

# %% tags=["solution"]
def kaufe(produkt, einkaufsliste):
    einkaufsliste.append(produkt)


# %% [markdown] lang="de"
# Fügen Sie `Butter` und `Brot` zur Einkaufsliste `meine_einkaufsliste` hinzu.

# %% [markdown] lang="en"
# Add `butter` and `bread` to the shopping list `my_shopping_list`.

# %% tags=["solution"]
kaufe("Butter", meine_einkaufsliste)
kaufe("Brot", meine_einkaufsliste)

# %% [markdown] lang="de"
# Drucken Sie beide Einkauslisten nochmal aus.

# %% [markdown] lang="en"
# Print out both shopping lists again.

# %% tags=["solution"]
drucke_einkaufsliste(meine_einkaufsliste)

# %% tags=["solution"]
drucke_einkaufsliste(eine_andere_einkaufsliste)

# %% [markdown] lang="de"
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %% [markdown] lang="en"
# What happens when you add `butter` and `bread` to the shopping list `my_shopping list` again?

# %% tags=["solution"]
kaufe("Butter", meine_einkaufsliste)
kaufe("Brot", meine_einkaufsliste)
drucke_einkaufsliste(meine_einkaufsliste)


# %% [markdown] lang="de"
# # Ausgabe von Quadratzahlen
#
# Schreiben Sie eine Funktion `drucke_quadrate(m, n)`, die die Quadrate der
# Zahlen zwischen `m` und `n` (einschließlich) in der folgenden Form ausgibt:
#
# ```
# Das Quadrat von 5 ist 25
# Das Quadrat von 6 ist 36
# Das Quadrat von 7 ist 49
# ```

# %% [markdown] lang="en"
# # Printing square numbers
#
# Write a function `print_squares(m, n)` that prints the squares of the
# numbers between `m` and `n` (inclusive) in the following form:
#
# ```
# The square of 5 is 25
# The square of 6 is 36
# The square of 7 is 49
# ```

# %% tags=["solution"]
def drucke_quadrate(m, n):
    for num in range(m, n + 1):
        print("Das Quadrat von", num, "ist", num ** 2)


# %% [markdown] lang="de"
# Testen Sie die Funktion mit Argumenten 5, 7

# %% [markdown] lang="en"
# Test the function with arguments 5, 7

# %% tags=["solution"]
drucke_quadrate(5, 7)


# %% [markdown] lang="de"
# # Verbesserte Einkaufsliste
#
# In dieser Aufgabe wollen wir eine verbesserte Version der Einkaufsliste
# definieren, in der sowohl die Einkaufsliste als auch die Einträge durch
# benutzerdefinierte Datentypen repräsentiert werden. Jeder Eintrag soll das
# Produkt und die davon benötigte Menge enthalten.
#
# Definieren Sie eine Klasse `Item`, die Attribute für das Produkt und Menge
# hat. `Item` soll eine `__repr__`-Methode haben, die das Item in einer
# angemessenen Form darstellt.

# %% [markdown] lang="en"
# # Improved shopping list
#
# In this exercise we want to define an improved version of the shopping list
# in which both the shopping list and the entries are represented by
# user-defined data types. Every entry in the shopping list should contain
# the product to buy and the required amount.
#
# Define a class `Item`, with attributes for the product and quantity.
# `Item` should have a `__repr__` method that returns a representation of the item in an
# appropriate form.

# %% tags=["solution"]
class Item:
    def __init__(self, product, amount="1"):
        self.product = product
        self.amount = amount

    def __repr__(self):
        return "Item(" + repr(self.product) + ", " + repr(self.amount) + ")"


# %% [markdown] lang="de"
# Erzeugen sie ein Item, das 500g Kaffee repräsentiert:

# %% [markdown] lang="en"
# Create an item that represents 500g of coffee:

# %% tags=["solution"]
Item("Kaffee", "500g")


# %% [markdown] lang="de"
# Definieren Sie eine Klasse `ShoppingList`, die eine Liste von `Item`-Instanzen
# beinhaltet:
#
# - Der Konstruktor `__init__(self, items=[])` erzeugt eine Einkaufsliste,
#   die die Einträge `items` enthält (jedes Element von `items` soll eine
#   `Item`-Instanz sein).
#
# - Die Methode `shopping_list.add_item(item: Item)` fügt ein `Item` zur
#   Einkaufsliste `shopping_list` hinzu.
#
# - Die Methode `shopping_list.print()` druckt die Einkaufsliste aus.
#
# `ShoppingList` soll eine `__repr__`-Methode haben, die die Einkaufsliste in
#   einer geeigneten Form darstellt.

# %% [markdown] lang="en"
# Define a class `ShoppingList` containing a list of `Item` instances:
#
# - The constructor `__init__(self, items=[])` creates a shopping list,
#   which contains the items `items` (each element of `items` should be an
#   `Item` instance).
#
# - The method `shopping_list.add_item(item: Item)` adds an `Item`
#   to `shopping_list`.
#
# - The `shopping_list.print()` method prints the shopping list.
#
# `ShoppingList` should have a `__repr__` method that converts the shopping list into
#   an appropriate form.

# %% tags=["solution"]
class ShoppingList:
    def __init__(self, items=[]):
        self.items = items

    def __repr__(self):
        return "ShoppingList(" + repr(self.items) + ")"

    def add_item(self, item):
        self.items.append(item)

    def print(self):
        print("Einkaufsliste")
        for item in self.items:
            print("  ", item.product, " (", item.amount, ")", sep="")


# %% [markdown] lang="de"
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit
# folgenden Items repräsentiert:
# - 2 Pakete Tee,
# - 1 Paket Kaffee

# %% [markdown] lang="en"
# Define a variable `my_shopping_list` containing a shopping list with the following items:
# - 2 packets of tea,
# - 1 packet of coffee

# %% tags=["solution"]
meine_einkaufsliste = ShoppingList([Item("Tee", "2 Pakete"), Item("Kaffee", "1 Paket")])
meine_einkaufsliste

# %% [markdown] lang="de"
# Drucken Sie `meine_einkaufsliste` aus.

# %% [markdown] lang="en"
# Print out `my_shopping list`.

# %% tags=["solution"]
meine_einkaufsliste.print()

# %% tags=["solution"]
drucke_einkaufsliste(eine_andere_einkaufsliste)

# %% [markdown] lang="de"
# Fügen Sie  250 g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

# %% [markdown] lang="en"
# Add 250g butter and 1 loaf of bread to the shopping list
# `my_shopping list`.

# %% tags=["solution"]
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
meine_einkaufsliste

# %% [markdown] lang="de"
# Drucken Sie die Einkaufsliste nochmal aus.

# %% [markdown] lang="en"
# Print out the shopping list again.

# %% tags=["solution"]
meine_einkaufsliste.print()

# %% [markdown] lang="de"
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %% [markdown] lang="en"
# What happens when you add `butter` and `bread` to `my_shopping list` again?

# %% tags=["solution"]
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
meine_einkaufsliste.print()

# %% tags=["solution"]
