# -*- coding: utf-8 -*-
# %% [markdown]
#
# # Kraftfahrzeuge (Teil 1)
#
# Definieren Sie eine Klasse `Kfz`, deren Instanzen Kraftfahrzeuge beschreiben.
# Jedes KFZ soll Attribute `hersteller` und `kennzeichen` haben.

# %%
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

# %% [markdown]
#
# Erzeugen Sie zwei Kraftfahrzeuge:
# - einen BMW mit Kennzeichen "M-BW 123"
# - einen VW mit Kennzeichen "WOB-VW 246"
# und speichern Sie sie in Variablen `bmw` und `vw`

# %%
bmw = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown]
#
# Erzeugen Sie eine neue Instanz von `Kfz` mit Hersteller BMW und Kennzeichen
# "M-BW 123" und speichern Sie sie in einer Variablen `bmw2`.

# %%
bmw2 = Kfz("BMW", "M-BW 123")

# %% [markdown]
#
# Wie können Sie feststellen, ob `bmw` und `bmw2` (bzw. `bmw` und `vw`) das
# gleiche Fahrzeug beschreiben?

# %%
bmw.hersteller == bmw2.hersteller and bmw.kennzeichen == bmw2.kennzeichen

# %%
bmw.hersteller == vw.hersteller and bmw.kennzeichen == vw.kennzeichen

# %% [markdown]
#
# # Kraftfahrzeuge (Teil 2)
#
# Erweitern Sie die Klasse `Kfz` um eine Methode `melde_um(self,
# neues_kennzeichen)`, die das Kennzeichen des Fahrzeugs ändert.

# %%
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen

# %% [markdown]
#
# Erzeugen Sie neue Instanzen von `bmw`, `bmw2` und `vw` wie in der obigen
# Aufgabe:

# %%
bmw = Kfz("BMW", "M-BW 123")
bmw2 = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% [markdown]
#
# Melden Sie den obern erzeugten VW um, so dass er das neue Kennzeichen "BGL-A
# 9" hat. Wie können Sie feststellen ob das Ummelden die gewünschte Änderung
# hatte?

# %%
vw.melde_um("BGL-A 9")

# %%
# Z.B
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"
# Oder
print("Hersteller:", vw.hersteller, "\tKennzeichen:", vw.kennzeichen)

# %% [markdown]
#
# Melden Sie den in `bmw` gespeicherten BMW um (mit Kennzeichen "F-B 21"). Wirkt
# sich die Änderung auf das in `bmw2` gespeicherte KFZ aus?

# %%
bmw.melde_um("F-B 21")
print("Hersteller:", bmw.hersteller, "\tKennzeichen:", bmw.kennzeichen)
print("Hersteller:", bmw2.hersteller, "\tKennzeichen:", bmw2.kennzeichen)

# %% [markdown]
# # Einkaufsliste
#
# In dieser Aufgabe wollen wir eine  Einkaufsliste definieren, die geplante
# Einkäufe verwalten kann. Eine Einkaufsliste soll aus Einträgen bestehen, die
# ein Produkt und die davon benötigte Menge enthalten.
#
# Es sollen sowohl die Einkaufsliste selber als auch die Einträge durch
# benutzerdefinierte Datentypen repräsentiert werden. 
#
# Definieren Sie zunächst eine Klasse `Item`, die Attribute `product` und
# `amount` hat. Verwenden Sie dazu den `@dataclass` Decorator

# %%
from dataclasses import dataclass

@dataclass
class Item:
    product: str
    amount: int = 1

# %% [markdown]
# Erzeugen sie ein Item, das 500g Kaffee repräsentiert:

# %%
Item("Kaffee", "500g")


# %% [markdown]
#
# Definieren Sie eine Klasse `ShoppingList`, die eine Liste von `Item`-Instanzen
# beinhaltet:
#
# - Verwenden Sie den `@dataclass` Decorator
# - Die Klasse hat ein Attribut `items` vom Typ `list` (oder `list[Item]`, falls
#   Sie Python 3.9 oder neuer verwenden), das mit einer leeren Liste
#   Initialisiert wird.
# - Die Methode `add_item(self, item: Item)` fügt ein `Item` zur Einkaufsliste
#   hinzu.
#
# Implementieren Sie eine
# [`__str__()`-Methode](https://docs.python.org/3/reference/datamodel.html#object.__str__),
# so dass das folgende Programm:
#
# ```python
# meine_einkaufsliste = ShoppingList([Item('Tee', '2 Pakete'),
#                                     Item('Kaffee', '1 Paket')])
# print(str(meine_einkaufsliste))
# print(repr(meine_einkaufsliste))
# ```
#
# Folgende Ausgabe erzeugt:
#
# ```
# Einkaufsliste
#   Tee, (2 Pakete)
#   Kaffee, (1 Paket)
#
# ShoppingList(items=[Item(product='Tee', amount='2 Pakete'), Item(product='Kaffee', amount='1 Paket')])
# ```
#
# Implementieren Sie eine Methode für `__len__()`, die die Länge der
# Einkaufsliste zurückgibt, und für `__getitem__()`, die den Zugriff auf
# Einträge über ihren numerischen Index erlaubt.

# %%
from dataclasses import field

@dataclass
class ShoppingList:
    items: list[Item] = field(default_factory=list)

    def __str__(self):
        result = "Einkaufsliste\n"
        for item in self.items:
            result += f"  {item.product}, ({item.amount})\n"
        return result

    def __len__(self):
        return len(self.items)

    def __getitem__(self, n):
        return self.items[n]

    def add_item(self, item):
        self.items.append(item)


# %% [markdown]
#
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit
# folgenden Items repräsentiert:
# - 2 Pakete Tee,
# - 1 Paket Kaffee

# %%
meine_einkaufsliste = ShoppingList([Item('Tee', '2 Pakete'),
                                    Item('Kaffee', '1 Paket')])
print(str(meine_einkaufsliste))
print(repr(meine_einkaufsliste))


# %% [markdown]
#
# Drucken Sie `meine_einkaufsliste` aus.

# %%
print(meine_einkaufsliste)


# %% [markdown]
#
# Stellen Sie fest, wie lange `meine_einkaufsliste` ist und welches Element an
# Index 1 ist:

# %%
print(len(meine_einkaufsliste))
print(meine_einkaufsliste[0])

# %% [markdown]
#
# Was ist der Effekt des follgenden Ausdrucks?
# ```python 
#   for item in meine_einkaufsliste:
#       print(item)
# ```

# %%
for item in meine_einkaufsliste:
    print(item)

# %% [markdown]
#
# Fügen Sie  250 g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

# %%
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
meine_einkaufsliste

# %% [markdown]
# Drucken Sie die Einkausliste nochmal aus.

# %%
print(meine_einkaufsliste)

# %% [markdown]
#
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %%
meine_einkaufsliste.add_item(Item("Butter", "250g"))
meine_einkaufsliste.add_item(Item("Brot", "1 Laib"))
print(meine_einkaufsliste)

# %%
