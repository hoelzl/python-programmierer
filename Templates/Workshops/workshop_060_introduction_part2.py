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
# # Operatoren, Vergleiche
#
# Ist $2^{16}$ größer als $32\,000\,\,/\,\,2$?

# %% {{ solution() }}
2 ** 16 > (32_000 / 2)

# %% [markdown]
# Ist $72$ ohne Rest durch $3$ teilbar?

# %% {{ solution() }}
72 % 3 == 0

# %% [markdown]
# Ist $72$ eine gerade Zahl (d.h. ohne Rest durch 2 teilbar)?

# %% {{ solution() }}
72 % 2 == 0


# %% [markdown]
#
# Schreiben Sie eine Funktion `ist_teilbar_durch(m, n)` die ( genau dann)
# `True` zurückgibt, wenn `m` durch `n` teilbar ist

# %% {{ solution() }}
def ist_teilbar_durch(m, n):
    return m % n == 0


ist_teilbar_durch(6, 2)


# %% [markdown]
#
# Schreiben Sie eine Funktion `ist_teilbar_durch_2_und_3(n)`, die genau dann
# `True` zurückgibt, wenn `n` ohne Rest durch $2$ und durch $3$ teilbar ist.

# %% {{ solution() }}
def ist_teilbar_durch_2_und_3(n):
    return ist_teilbar_durch(n, 2) and ist_teilbar_durch(n, 3)


# %% {{ solution() }}
def ist_teilbar_durch_2_und_3_v2(n):
    return n % 6 == 0


# %% [markdown]
# Testen Sie, ob $72$ durch $2$ und durch $3$ teilbar ist.

#  {{ solution() }}
ist_teilbar_durch_2_und_3(72)


# %% [markdown] 
# # Volljährig
#
# Schreiben Sie eine Funktion `drucke_volljährig(alter)`, die `Volljährig`
# auf dem Bildschirm ausgibt, wenn `alter >= 18` ist und `Minderjährig` sonst.

#  {{ solution() }}
def drucke_volljährig(alter):
    if alter < 18:
        print("Minderjährig")
    else:
        print("Volljährig")


# %% [markdown]
# Testen Sie `drucke_volljährig(alter)` mit den Werten 17 und 18.

#  {{ solution() }}
drucke_volljährig(17)
drucke_volljährig(18)

# %% [markdown]
# # Einkaufsliste
#
# Definieren Sie Variablen
# - `meine_einkaufsliste`, die eine Liste mit den Strings `Tee` und `Kaffee`
#   enthält,
# - `eine_andere_einkaufsliste`, die ebenfalls eine Liste mit den Strings
#   `Tee` und `Kaffee` enthält.

#  {{ solution() }}
meine_einkaufsliste = ["Tee", "Kaffee"]
eine_andere_einkaufsliste = ["Tee", "Kaffee"]


# %% [markdown]
#
# Definieren Sie eine Funktion `drucke_einkaufsliste(einkaufsliste)`, die die
# als Argument übergebene Einkaufsliste ausdruckt:
#
# ```
# Einkaufsliste:
#   Tee
#   Kaffee
# ```

#  {{ solution() }}
def drucke_einkaufsliste(einkaufsliste):
    print("Einkaufsliste:")
    for item in einkaufsliste:
        print(" ", item)


# %% [markdown]
#
# Testen Sie die Funktion `drucke_einkaufsliste(einkaufsliste)` mit beiden
# Einkaufslisten.

#  {{ solution() }}
drucke_einkaufsliste(meine_einkaufsliste)

#  {{ solution() }}
drucke_einkaufsliste(eine_andere_einkaufsliste)


# %% [markdown]
# Definieren Sie eine Funktion `kaufe(produkt, einkaufsliste)`, das `produkt`
# zu  `einkaufsliste` hinzufügt.

#  {{ solution() }}
def kaufe(produkt, einkaufsliste):
    einkaufsliste.append(produkt)


# %% [markdown]
# Fügen Sie `Butter` und `Brot` zur Einkaufsliste `meine_einkaufsliste` hinzu.

#  {{ solution() }}
kaufe("Butter", meine_einkaufsliste)
kaufe("Brot", meine_einkaufsliste)

# %% [markdown]
# Drucken Sie beide Einkauslisten nochmal aus.

#  {{ solution() }}
drucke_einkaufsliste(meine_einkaufsliste)

#  {{ solution() }}
drucke_einkaufsliste(eine_andere_einkaufsliste)

# %% [markdown]
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

#  {{ solution() }}
kaufe("Butter", meine_einkaufsliste)
kaufe("Brot", meine_einkaufsliste)
drucke_einkaufsliste(meine_einkaufsliste)


# %% [markdown]
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

# %% {{ solution() }}
def drucke_quadrate(m, n):
    for num in range(m, n + 1):
        print("Das Quadrat von", num, "ist", num ** 2)


# %% [markdown]
# Testen Sie die Funktion mit Argumenten 5, 7

# %% {{ solution() }}
drucke_quadrate(5, 7)


# %% [markdown]
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

#  {{ solution() }}
class Item:
    def __init__(self, product, amount='1'):
        self.product = product
        self.amount = amount

    def __repr__(self):
        return "Item(" + repr(self.product) + ", " + repr(self.amount) + ")"


# %% [markdown] 
# Erzeugen sie ein Item, das 500g Kaffee repräsentiert:

#  {{ solution() }}
Item("Kaffee", "500g")


# %% [markdown] 
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
# - Die Methode `print()` druckt die Einkaufsliste aus.
#
# `ShoppingList` soll eine `__repr__`-Methode haben, die die Einkaufsliste in
#   einer geeigneten Form darstellt.

#  {{ solution() }}
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
            print("  ", item.product, " (", item.amount, ")", sep='')


# %% [markdown]
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit
# folgenden Items repräsentiert:
# - 2 Pakete Tee,
# - 1 Paket Kaffee

#  {{ solution() }}
meine_einkaufsliste = ShoppingList([Item('Tee', '2 Pakete'),
                                    Item('Kaffee', '1 Paket')])
meine_einkaufsliste

# %% [markdown]
# Drucken Sie `meine_einkaufsliste` aus.

#  {{ solution() }}
meine_einkaufsliste.print()

#  {{ solution() }}
drucke_einkaufsliste(eine_andere_einkaufsliste)

# %% [markdown]
# Fügen Sie  250 g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

#  {{ solution() }}
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
meine_einkaufsliste

# %% [markdown]
# Drucken Sie die Einkaufsliste nochmal aus.

#  {{ solution() }}
meine_einkaufsliste.print()

# %% [markdown]
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

#  {{ solution() }}
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
meine_einkaufsliste.print()

#  {{ solution() }}
