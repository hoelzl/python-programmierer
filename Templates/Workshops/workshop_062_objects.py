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
#
# # Kraftfahrzeuge (Teil 1)
#
# Definieren Sie eine Klasse `Kfz`, deren Instanzen Kraftfahrzeuge beschreiben.
# Jedes KFZ soll Attribute `hersteller` und `kennzeichen` haben.

# %% [markdown] lang="en"
# # Motor Vehicles (Part 1)
#
# Define a class `MotorVehicle` whose instances describe motor vehicles.
# Every car should have attributes `manufacturer` and `license_plate`.

# %% tags=["solution"]
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen


# %% tags=["solution"]
class MotorVehicle:
    def __init__(self, manufacturer, license_plate):
        self.manufacturer = manufacturer
        self.license_plate = license_plate


# %% [markdown] lang="de"
#
# Erzeugen Sie zwei Kraftfahrzeuge:
# - einen BMW mit Kennzeichen "M-BW 123"
# - einen VW mit Kennzeichen "WOB-VW 246"
# und speichern Sie sie in Variablen `bmw` und `vw`

# %% [markdown] lang="en"
# Create two motor vehicles:
# - a BMW with license plate "M-BW 123"
# - a VW with license plate "WOB-VW 246"
# and store them in variables `bmw` and `vw`

# %% tags=["solution"]
bmw = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% tags=["solution"]
bmw_en = MotorVehicle("BMW", "M-BW 123")
vw_en = MotorVehicle("VW", "WOB-VW 246")

# %% [markdown] lang="de"
#
# Erzeugen Sie eine neue Instanz von `Kfz` mit Hersteller BMW und Kennzeichen
# "M-BW 123" und speichern Sie sie in einer Variablen `bmw2`.

# %% [markdown] lang="en"
# Create a new instance of `MotorVehicle` with manufacturer BMW and registration number
# "M-BW 123" and store it in a variable `bmw2`.

# %% tags=["solution"]
bmw2 = Kfz("BMW", "M-BW 123")

# %% [markdown] lang="de"
#
# Wie können Sie feststellen, ob `bmw` und `bmw2` (bzw. `bmw` und `vw`) das
# gleiche Fahrzeug beschreiben?

# %% [markdown] lang="en"
# How can you determine whether `bmw` and `bmw2` (or `bmw` and `vw`) describe the same vehicle?

# %% tags=["solution"]
bmw.hersteller == bmw2.hersteller and bmw.kennzeichen == bmw2.kennzeichen

# %% tags=["solution"]
bmw.hersteller == vw.hersteller and bmw.kennzeichen == vw.kennzeichen

# %% tags=["solution"]
bmw_en.manufacturer == vw_en.manufacturer and bmw_en.license_plate == vw_en.license_plate


# %% [markdown] lang="de"
#
# # Kraftfahrzeuge (Teil 2)
#
# Erweitern Sie die Klasse `Kfz` um eine Methode `melde_um(self,
# neues_kennzeichen)`, die das Kennzeichen des Fahrzeugs ändert.

# %% [markdown] lang="en"
# # Motor Vehicles (Part 2)
#
# Extend the `MotorVehicle` class with a method `change_registration(self, new_license_plate)`, which changes the vehicle's license plate.

# %% tags=["solution"]
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen


# %% tags=["solution"]
class MotorVehicle:
    def __init__(self, manufacturer, license_plate):
        self.manufacturer = manufacturer
        self.license_plate = license_plate
    
    def change_registration(self, new_license_plate):
        self.license_plate = new_license_plate


# %% [markdown] lang="de"
#
# Erzeugen Sie neue Instanzen von `bmw`, `bmw2` und `vw` wie in der obigen
# Aufgabe:

# %% [markdown] lang="en"
# Create new instances of `bmw`, `bmw2` and `vw` as above:

# %% tags=["solution"]
bmw = Kfz("BMW", "M-BW 123")
bmw2 = Kfz("BMW", "M-BW 123")
vw = Kfz("VW", "WOB-VW 246")

# %% tags=["solution"]
bmw_en = MotorVehicle("BMW", "M-BW 123")
bmw2_en = MotorVehicle("BMW", "M-BW 123")
vw_en = MotorVehicle("VW", "WOB-VW 246")

# %% [markdown] lang="de"
#
# Melden Sie den obern erzeugten VW um, so dass er das neue Kennzeichen "BGL-A
# 9" hat. Wie können Sie feststellen ob das Ummelden die gewünschte Änderung
# hatte?

# %% [markdown] lang="en"
# Change the registation of the VW generated above so that it has the new license plate  "BGL-A 9". How can you tell if changing the registration resulted is the change you wanted?

# %% tags=["solution"]
vw.melde_um("BGL-A 9")

# %% tags=["solution"]
vw_en.change_registration("BGL-A 9")

# %% tags=["solution"]
# Z.B
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"
# Oder
print("Hersteller:", vw.hersteller, "\tKennzeichen:", vw.kennzeichen)

# %% tags=["solution"]
assert vw_en.license_plate == "BGL-A 9" and vw_en.manufacturer == "VW"

# %% [markdown] lang="de"
#
# Melden Sie den in `bmw` gespeicherten BMW um (mit Kennzeichen "F-B 21"). Wirkt
# sich die Änderung auf das in `bmw2` gespeicherte KFZ aus?

# %% [markdown] lang="en"
# Change the registration of the BMW saved in `bmw` (to the new registration number "F-B 21").
# Does the change affect the car saved in `bmw2`?

# %% tags=["solution"]
bmw.melde_um("F-B 21")
print("Hersteller:", bmw.hersteller, "\tKennzeichen:", bmw.kennzeichen)
print("Hersteller:", bmw2.hersteller, "\tKennzeichen:", bmw2.kennzeichen)


# %% [markdown] lang="de"
#
# # Kraftfahrzeuge (Teil 3)
#
# Verbessern Sie die Klasse `Kfz` indem Sie Methoden implementieren, die
# ein KFZ in einer geeigneten Form ausgeben.  Führen Sie die obigen Beispiele
# mit der verbesserten Klasse aus.


# %% [markdown] lang="en"
# # Motor Vehicles (Part 3)
#
# Enhance the `MotorVehicle` class by implementing methods that return a string representation of the vehicle in a suitable form. Repeat the above examples with the new class.

# %% tags=["solution"]
class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen

    def __repr__(self):
        return f"Kfz({self.hersteller!r}, {self.kennzeichen!r})"


# %% tags=["solution"]
bmw = Kfz("BMW", "M-BW 123")
bmw

# %% tags=["solution"]
bmw2 = Kfz("BMW", "M-BW 123")
bmw2

# %% tags=["solution"]
vw = Kfz("VW", "WOB-VW 246")
vw

# %% tags=["solution"]
vw.melde_um("BGL-A 9")
vw

# %% tags=["solution"]
assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"

# %% tags=["solution"]
bmw.melde_um("F-B 21")
bmw

# %% tags=["solution"]
bmw2

# %% [markdown] lang="de"
# # Einkaufsliste
#
# In dieser Aufgabe wollen wir eine  Einkaufsliste definieren, die geplante
# Einkäufe verwalten kann. Eine Einkaufsliste soll aus Einträgen bestehen, die
# ein Produkt und die davon benötigte Menge enthalten.
#
# Es sollen sowohl die Einkaufsliste selber als auch die Einträge durch
# benutzerdefinierte Datentypen repräsentiert werden.
#
# Definieren Sie zunächst eine Klasse `ShoppingListItem`, die Attribute `product` und
# `amount` hat. Verwenden Sie dazu den `@dataclass` Decorator

# %% [markdown] lang="en"
# # Shopping List
#
# In this workshop we want to define a shopping list, that can manage planned purchases. A shopping list should consist of items that contain a product and the required quantity of the product.
#
# Both the shopping list itself and the entries should be represented as user-defined data types.
#
# First define a class `ShoppingListItem` that has attributes `product` and `amount`. To do this, use the `@dataclass` decorator

# %% tags=["solution"]
from dataclasses import dataclass

@dataclass
class ShoppingListItem:
    product: str
    amount: str = "1"


# %% [markdown] lang="de"
# Erzeugen sie ein `ShoppingListItem`, das 500g Kaffee repräsentiert:

# %% [markdown] lang="en"
# Create a shopping list item that represents 500g of coffee:

# %% tags=["solution"]
ShoppingListItem("Kaffee", "500g")

# %% [markdown] lang="de"
#
# Definieren Sie eine Klasse `ShoppingList`, die eine Liste von `ShoppingListItem`-Instanzen
# beinhaltet:
#
# - Verwenden Sie den `@dataclass` Decorator
# - Die Klasse hat ein Attribut `items` vom Typ `list` (oder `list[ShoppingListItem]`, falls
#   Sie Python 3.9 oder neuer verwenden), das mit einer leeren Liste
#   Initialisiert wird.
# - Die Methode `add_item(self, item: ShoppingListItem)` fügt ein `ShoppingListItem` zur Einkaufsliste
#   hinzu.
#
# Implementieren Sie eine
# [`__str__()`-Methode](https://docs.python.org/3/reference/datamodel.html#object.__str__),
# so dass das folgende Programm:
#
# ```python
# meine_einkaufsliste = ShoppingList([ShoppingListItem('Tee', '2 Pakete'),
#                                     ShoppingListItem('Kaffee', '1 Paket')])
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
# ShoppingList(items=[ShoppingListItem(product='Tee', amount='2 Pakete'), ShoppingListItem(product='Kaffee', amount='1 Paket')])
# ```
#
# Implementieren Sie eine Methode für `__len__()`, die die Länge der
# Einkaufsliste zurückgibt, und für `__getitem__()`, die den Zugriff auf
# Einträge über ihren numerischen Index erlaubt.

# %% [markdown] lang="en"
# Define a class `ShoppingList` containing a list of `ShoppingListItem` instances:
#
# - Use the `@dataclass` decorator
# - The class has an attribute `items` of type `list` (or `list[ShoppingListItem]` if
#   you are using Python 3.9 or newer), initialized with an empty list.
# - The method `add_item(self, item: ShoppingListItem)` adds a `ShoppingListItem` to the shopping list.
#
# Implement a
# [`__str__()` method](https://docs.python.org/3/reference/datamodel.html#object.__str<_>_),
# so the following program:
#
# ```python
# my_shopping_list = ShoppingList([ShoppingListItem('Tea', '2 packets'),
#                                  ShoppingListItem('Coffee', '1 packet')])
# print(str(my_shopping_list))
# print(repr(my_shopping_list))
# ```
#
# Produces the following output:
#
# ```
# Shopping List
#   Tea, (2 packets)
#   Coffee, (1 packet)
#
# ShoppingList(items=[ShoppingListItem(product='Tea', amount='2 packets'), ShoppingListItem(product='Coffee', amount='1 packet')])
# ```
#
# Implement a method `__len__()` that returns the length of the shopping list, and a method `__getitem__()` that allows access to items via their numeric index.

# %% tags=["solution"]
from dataclasses import field

@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

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


# %% [markdown] lang="de"
#
# Definieren Sie Variable `meine_einkaufsliste`, die eine Einkaufsliste mit
# folgenden ShoppingListItems repräsentiert:
#
# - 2 Pakete Tee,
# - 1 Paket Kaffee
#
# Überprüfen Sie, dass sich `str()` und `repr()` wie oben beschrieben verhalten.

# %% [markdown] lang="en"
# Define a variable `my_shopping_list` containing a shopping list representing the following items:
#
# - 2 packets of tea,
# - 1 packet of coffee
#
# Check that `str()` and `repr()` behave as specified above.

# %% tags=["solution"]
meine_einkaufsliste = ShoppingList([ShoppingListItem("Tee", "2 Pakete"), ShoppingListItem("Kaffee", "1 Paket")])
print(str(meine_einkaufsliste))
print(repr(meine_einkaufsliste))

# %% [markdown] lang="de"
# Drucken Sie `meine_einkaufsliste` aus. Entspricht die Ausgabe Ihren Erwartungen?

# %% [markdown] lang="en"
# Print out `my_shopping_list`. Does the output look as expected?

# %% tags=["solution"]
print(meine_einkaufsliste)

# %% [markdown] lang="de"
#
# Stellen Sie fest, wie lange `meine_einkaufsliste` ist und was ihr erstes und zweites Element sind:

# %% [markdown] lang="en"
# Determine the length of `my_shopping_list` is and its first and second item.

# %% tags=["solution"]
print(len(meine_einkaufsliste))
print(meine_einkaufsliste[0])
print(meine_einkaufsliste[1])

# %% [markdown] lang="de"
#
# Was ist der Effekt des follgenden Ausdrucks?
# ```python
#   for item in meine_einkaufsliste:
#       print(item)
# ```

# %% [markdown] lang="en"
# What is the effect of the following expression?
# ```python
#   for item in my_shopping_list:
#       print(item)
# ```

# %% tags=["solution"]
for item in meine_einkaufsliste:
    print(item)

# %% [markdown] lang="de"
# Erweitern Sie die Definition der Klasse `ShoppingList`, so dass der Indexing Operator `[]` auch mit einem String aufgerufen werden kann, und das Shopping List Item mit dem entsprechenden `product` Attribut zurückgibt, falls es existiert, oder `None` falls kein solches Item existiert.
#
# Verifizieren Sie, dass ihre neue Implementierung des Indexing Operators für Integer und String Argumente funktioniert.
#
# *Hinweis:* Sie können die `isinstance()` Funktion verwenden um zu überprüfen, ob ein Objekt ein String ist:

# %% [markdown] lang="en"
# Extend the definition of the `ShoppingList` class so that the indexing operator `[]` can also be called with a string argument, and returns the shopping list item with the appropriate `product` attribute if such an item exists, or `None` if no such item exists.
#
# Verify that the new implementation of the indexing operators works for boths integer and string arguments.
#
# *Hint:* You can use the `isinstance()` function to check whether an object is a string:

# %% tags=["solution"]
print(isinstance("abc", str))
print(isinstance(123, str))


# %% tags=["solution"]
@dataclass
class ShoppingList:
    items: list[ShoppingListItem] = field(default_factory=list)

    def __str__(self):
        result = "Einkaufsliste\n"
        for item in self.items:
            result += f"  {item.product}, ({item.amount})\n"
        return result

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, n):
        if isinstance(n, str):
            return self.find_product(n)
        return self.items[n]

    def find_product(self, product):
        for item in self.items:
            if item.product == product:
                return item
        return None
    
    def add_item(self, item):
        self.items.append(item)


# %% tags=["solution"]
meine_einkaufsliste = ShoppingList([ShoppingListItem("Tee", "2 Pakete"), ShoppingListItem("Kaffee", "1 Paket")])
print(meine_einkaufsliste[0])
print(meine_einkaufsliste["Tee"])
print(meine_einkaufsliste["Marmelade"])

# %% [markdown] lang="de"
#
# Fügen Sie  250g Butter und  1 Laib Brot zur Einkaufsliste
# `meine_einkaufsliste` hinzu.

# %% [markdown] lang="en"
# Add 250g butter and 1 loaf of bread to the shopping list
# `my_shopping_list`.

# %% tags=["solution"]
meine_einkaufsliste.add_item(ShoppingListItem("Butter", "250g"))
meine_einkaufsliste.add_item(ShoppingListItem("Brot", "1 Laib"))
meine_einkaufsliste

# %% [markdown] lang="de"
# Drucken Sie die Einkaufsliste nochmal aus.

# %% [markdown] lang="en"
# Print out the shopping list again.

# %% tags=["solution"]
print(meine_einkaufsliste)

# %% [markdown] lang="de"
#
# Was passiert, wenn Sie `Butter` und `Brot` nochmals zur Einkaufsliste
# `meine_einkaufsliste` hinzufügen?

# %% [markdown] lang="en"
# What happens when you add `butter` and `bread` to the shopping list again?

# %% tags=["solution"]
meine_einkaufsliste.add_item(ShoppingListItem("Butter", "250g"))
meine_einkaufsliste.add_item(ShoppingListItem("Brot", "1 Laib"))
print(meine_einkaufsliste)

# %% [markdown] lang="de"
# *Diskussion:* Wie könnte das Verhalten der Klasse verbessert werden?

# %% [markdown] lang="en"
# *Discussion:* How could we improve the behavior of the class?
