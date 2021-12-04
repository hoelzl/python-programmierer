# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
#
#  <img src="img/python-logo-notext.svg"
#       style="display:block;margin:auto;width:10%"/>
#  <h1 style="text-align:center;">Python: Kurze Einführung in Klassen</h1>
#  <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
#  <br/>
#  <div style="text-align:center;">Dr. Matthias Hölzl</div>
#  <div style="text-align:center;">Allaithy Raed</div>

# %% [markdown]
#
#  # Klassen
#
#  Wie können wir einen Eintrag in einem Warenkorb darstellen?
#
#  - Artikelnummer
#  - Artikelname
#  - Preis pro Stück
#  - Anzahl
#  - Gesamtpreis
#
#  Vorschlag: Liste, (Tupel, Dictionaries)

# %%
entry = ["0713", "Netzkabel", 3.49, 2, 6.98]

# %%
entry

# %% [markdown]
#
#  ## Problem
#
#  - Schwer zu erkennen, welcher Bedeutung ein Eintrag hat
#  - Listenoperationen sind für Entries möglich, aber nicht sinnvoll
#  - Bedeutung nur implizit; für Python ist es einfach eine Liste
#  - Berechnete Werte (Gesamtpreis) müssen explizit angegeben werden

# %%
entry = {
    "article_number": "0713",
    "article_name": "Netzkabel",
    "price_per_item:": 3.49,
    "number_of_items": 2,
    "total_price": 6.98,
}

# %%
entry


# %% [markdown]
#
#  ## Verbesserungen und noch vorhandene Probleme
#
#  - Bedeutung der einzelnen "Attribute" ist klarer
#  - Dictionary-Operationen für Eintrag sinnvoller als Listenoperationen
#    (passen aber immer noch nicht komplett)
#  - Bedeutung des Eintrags selber nur implizit; für Python ist es einfach ein Dictionary
#  - Berechnete Werte (Gesamtpreis) müssen explizit angegeben werden

# %% [markdown]
#
#  # Klassen und Objekte
#
#  Wie können wir in Python Objekte erzeugen, in denen wir zusammengehörige Daten Speichern können?
#
#  - Listen
#  - Tupel
#  - Dictionaries
#  - *(Instanzen von) benutzerdefinierten Klassen*

# %%
class ShoppingCartEntryV0:
    pass


# %%
shopping_cart_entry_1 = ShoppingCartEntryV0()
shopping_cart_entry_2 = ShoppingCartEntryV0()
shopping_cart_entry_1

# %%
type(shopping_cart_entry_1)

# %%
shopping_cart_entry_1 == shopping_cart_entry_2

# %%
shopping_cart_entry_1.article_number = "9343"
shopping_cart_entry_1.article_name = "Strawberries"
shopping_cart_entry_1.price_per_item = 2.99

# %%
shopping_cart_entry_1.article_number

# %%
shopping_cart_entry_2.article_number

# %%
shopping_cart_entry_1.article_name

# %%
shopping_cart_entry_1.price_per_item

# %%
shopping_cart_entry_2.article_number = "3852"
shopping_cart_entry_2.article_name = "Cream"
shopping_cart_entry_2.price_per_item = 1.99

# %%
shopping_cart_entry_2.article_number

# %%
shopping_cart_entry_2.article_name

# %%
print("ShoppingCartEntryV0",
      shopping_cart_entry_1.article_number,
      shopping_cart_entry_1.article_name,
      shopping_cart_entry_1.price_per_item)


# %% [markdown]
#
#  ## Bessere Variante: "Abstrakter Datentyp"
#
#  Wir definieren uns einen Typ, der für "entries in einem Warenkorb" steht.
#  Alle Instanzen dieses Typs haben die gleiche Struktur:
#
#  - `article_number`, `article_name`
#  - `price_per_item`, `number_of_items`
#  - `total_price`, berechnet aus den vorhergehenden Werten
#

# %% [markdown]
#
#  ### Konstruktoren
#
#  Die benötigten Werte werden bei der Konstruktion eines entries angegeben.
#
#  In Python definiert man dazu die `__init__()` Methode:

# %%
class ShoppingCartEntryV1:
    def __init__(self, article_number, article_name, price_per_item, number_of_items):
        self.article_number = article_number
        self.article_name = article_name
        self.price_per_item = price_per_item
        self.number_of_items = number_of_items
        self.total_price = price_per_item * number_of_items


# %% [markdown]
#
#  - Die `__init__()` Methode wird von Python nach dem Erzeugen einer Instanz
#    aufgerufen
#  - Das erste Argument ist dabei immer die neu erzeugte Instanz und hat
#    per Konvention den Namen `self`
#  - Die restlichen Argumente müssen an den Konstruktor übergeben werden:

# %%
shopping_cart_entry_1 = ShoppingCartEntryV1("0713", "Netzkabel", 3.49, 2)
shopping_cart_entry_1

# %%
(shopping_cart_entry_1.article_number,
 shopping_cart_entry_1.article_name,
 shopping_cart_entry_1.number_of_items,
 shopping_cart_entry_1.price_per_item,
 shopping_cart_entry_1.total_price)

# %%
shopping_cart = [ShoppingCartEntryV1("9343", "Strawberries", price_per_item=2.99, number_of_items=2),
                 ShoppingCartEntryV1("3742", "Cream", price_per_item=1.99, number_of_items=3)]

# %%
shopping_cart

# %% [markdown]
#
#  Die Ausgabe des Einkaufswagens ist mit der `ShoppingCartEntry` Klasse nicht sehr
#  vielsagend. Das werden wir später verbessern.

# %%
for entry in shopping_cart:
    print(entry.total_price)


# %% [markdown]
#
#  Wir können die Preise der einzelnen Entries im Einkaufswagen so berechnen:

# %%
def total_price_of_shopping_cart(shopping_cart):
    result = 0.0
    for entry in shopping_cart:
        result += entry.total_price
    return result


# %%
total_price_of_shopping_cart(shopping_cart)


# %%

# %% [markdown]
#
#  ### ADT für Einkaufswagen
#
#  Der Einkaufswagen ist im Moment als Liste gespeichert. Es wäre möglicherweise
#  hilfreich dafür ebenfalls einen Typ zu definieren:

# %%
class ShoppingCartV0:
    def __init__(self, entries):
        if isinstance(entries, list):
            self.entries = entries
        else:
            self.entries = [entries]


# %%
shopping_cart_entry_1 = ShoppingCartEntryV1("9343", "Strawberries", price_per_item=2.99, number_of_items=2)
shopping_cart_entry_2 = ShoppingCartEntryV1("3742", "Cream", price_per_item=1.99, number_of_items=3)
shopping_cart = ShoppingCartV0([shopping_cart_entry_1, shopping_cart_entry_2])


# %%
def total_price_of_shopping_cart(shopping_cart):
    result = 0.0
    for entry in shopping_cart.entries:
        result += entry.total_price
    return result


# %%
total_price_of_shopping_cart(shopping_cart)

# %%
total_price_of_shopping_cart(ShoppingCartV0(shopping_cart_entry_1))


# %% [markdown]
#
#  ## Mini Workshop
#
#  - Notebook `062x-Workshop Todo-Liste V1`
#  - Abschnitt "TODO-Liste Version 1"

# %% [markdown]
#
#  ### Methoden
#
#  - Beim `ShoppingCartEntry` haben wir den Gesamtpreis als Attribut gespeichert.
#  - Beim `ShoppingCart` berechnen wir den Gesamtpreis durch eine Top-Level
#    Funktion, die auf die `entries` zugreift.
#  - Das ist inkonsistent und daher unschön.
#  - Es wäre hilfreich, wenn wir die Funktionen, die zu einer Klasse gehören in
#    der Klasse definieren könnten:
#  - Wir haben bei der `__init__()` Methode schon eine Funktionsdefinition in den Rumpf einer Klasse geschrieben
#  - Das geht nicht nur für `__init__()` sondern auch für benutzerdefinierte Funktionen
#  - Funktionen, die innerhalb einer Klasse definiert werden heißen *Methoden*
#  - Methoden haben immer mindestens einen Parameter
#    - per Konvention `self`
#    - steht für das Objekt in dessen Kontext die Methode aufgerufen wird

# %%
class ShoppingCartV1:
    def __init__(self, entries):
        self.entries = entries
        
    def get_total_price(self):
        result = 0.0
        for entry in self.entries:
            result += entry.total_price
        return result


# %%
shopping_cart = ShoppingCartV1([shopping_cart_entry_1, shopping_cart_entry_2])
shopping_cart

# %% [markdown]
#
#  - Methoden werden mit der Syntax
#
#    ```python
#    object.method(arg1, arg2, ...)
#    ```
#
#    aufgerufen.
#  - Das Argument des `self`-Parameters ist `object`
#  - `arg1`, `arg2`, ... werden an die folgenden Parameter gebunden.

# %%
shopping_cart.get_total_price()

# %% [markdown]
#
#  Eine Methode wird durch die `object.`-Operation an `object` *gebunden*, d.h.,
#  dem `self` Parameter wird bei nachfolgenden Aufrufen `object` als Argument
#  übergebben:

# %%
print(shopping_cart.get_total_price())
my_method = shopping_cart.get_total_price
print(shopping_cart)
print(my_method)
print(my_method())

# %% [markdown]
#
#  ### Dunder-Methoden
#
#  Zur Erinnerung:

# %%
print(str("Foo"))

# %%
print(repr("Foo"))

# %%
foo = "Foo"
print(f"{foo}")
print(f"{foo!s}")
print(f"{foo!r}")

# %%
print(f"{shopping_cart}")
print(f"{shopping_cart!s}")
print(f"{shopping_cart!r}")


# %%
class ShoppingCartEntryV2:    
    def __init__(self, article_number: str, article_name: str, price_per_item: float, number_of_items: int):
        self.article_number = article_number
        self.article_name = article_name
        self.price_per_item = price_per_item
        self.number_of_items = number_of_items
        self.total_price = price_per_item * number_of_items
    
    def __repr__(self):
        return (f"ShoppingCartEntryV2({self.article_number!r}, {self.article_name!r}, "
                f"{self.price_per_item!r}, {self.number_of_items!r})")
    
    def __str__(self):
        return f"{self.article_name}"


# %%
from typing import List

class ShoppingCartV2:
    def __init__(self, entries: List[ShoppingCartEntryV2]):
        self.entries = entries
    
    def __repr__(self):
        return f"ShoppingCartV2({self.entries!r})"
    
    def __str__(self):
        return f"Shopping Cart: {', '.join([str(e) for e in self.entries])}"
        
    def get_total_price(self):
        result = 0.0
        for entry in self.entries:
            result += entry.total_price
        return result


# %%
shopping_cart_entry_1 = ShoppingCartEntryV2("9343", "Strawberries", price_per_item=2.99, number_of_items=2)
shopping_cart_entry_2 = ShoppingCartEntryV2("3742", "Cream", price_per_item=1.99, number_of_items=3)
shopping_cart = ShoppingCartV2([shopping_cart_entry_1, shopping_cart_entry_2])
shopping_cart

# %%
str(shopping_cart)

# %%

# %%

# %%

# %% [markdown]
#
#  Siehe `Examples/ShoppingCart` für Implementierungsvariante.

# %%

# %% [markdown]
#
#  ## Workshop
#
#  - Notebook `064x-Workshop Todo-Liste V2`
#  - Abschnitt "Grundlegende Funktionalität"
#  - Im Moment ohne die `__iter__()` Methode

# %% [markdown]
#
#  ### Properties
#
#  In `ShoppingCartV1` ist `get_total_price()` eine Funktion, in
#  `ShoppingCartEntryV1` hatten wir den Gesamtpreis in einem Attribut
#  gespeichert.
#
#  Das ergibt immer noch ein inkonsistentes Benutzerinterface:

# %%
print(shopping_cart_entry_1.total_price)
print(shopping_cart.get_total_price())


# %% [markdown]
#
#  Eine Möglichkeit das zu vermeiden:
#
#  - Getter für alle Instanzvariablen (siehe Java)
#  - Viel Boilerplate-Code

# %% [markdown]
#
#  In Python können wir diesen Unterschied durch Definition einer `total_price`
#  Property vermeiden. Eine Property
#
#  - Ist eine Methode, die wie jede andere Methode evaluiert wird
#  - Sieht syntaktisch wie der Zugriff auf ein Attribut aus
#  - Wird durch den *Decorator* `@property` eingeführt

# %%

# %%
