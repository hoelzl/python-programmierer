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

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Objektorientierung Teil 1: Klassen") }}


# %% [markdown]
# ## Properties
#
# Wie können wir es ermöglichen auf einen Punkt sowohl mittels der `x` und
# `y`-Koordinaten zuzugreifen, als auch mittels Radius und Winkel?

# %% {{ doc.codealong() }}
import math


class GeoPointV0:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_radius(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return f"GeoPointV0({self.x:.1f}, {self.y:.1f}, r={self.get_radius():.2f}, θ={self.get_angle():.2f})"


# %% {{ doc.codealong() }}
GeoPointV0()

# %% {{ doc.codealong() }}
GeoPointV0(1.0, 0.0)

# %% {{ doc.codealong() }}
GeoPointV0(0.0, 2.0)

# %% [markdown]
# Es ist unschön, dass bei der Verwendung von `GeoPointV0` die Attribute `x`
# und `y` anders behandelt werden müsseen als `radius` und `angle`:

# %% {{ doc.codealong() }}
p = GeoPointV0(1.0, 1.0)
print(p.x, p.y, p.get_radius(), p.get_angle())

# %% {{ doc.codealong() }}
import math


class GeoPointV1:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return f"GeoPointV1({self.x:.1f}, {self.y:.1f}, r={self.radius:.2f}, θ={self.angle:.2f})"


# %% {{ doc.codealong() }}
GeoPointV1()

# %% {{ doc.codealong() }}
GeoPointV1(1.0, 0.0)

# %% {{ doc.codealong() }}
GeoPointV1(0.0, 2.0)

# %% {{ doc.codealong() }}
p = GeoPointV1(1.0, 1.0)
print(p.x, p.y, p.radius, p.angle)

# %% [markdown]
#
# ## Setter für Properties:
#
# Properties können auch modifiziert werden:

# %% {{ doc.codealong() }}
import math


class GeoPointV2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def radius(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @radius.setter
    def radius(self, new_radius):
        old_radius = self.radius
        # Check for `old_radius == 0`...
        self.x *= new_radius / old_radius
        self.y *= new_radius / old_radius

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    def __repr__(self):
        return f"GeoPointV1({self.x:.1f}, {self.y:.1f}, r={self.radius:.2f}, θ={self.angle:.2f})"


# %% {{ doc.codealong() }}
p = GeoPointV2(3.0, 4.0)
print("Original point:  ", p)
p.radius = 10.0
print("Set radius to 10:", p)


# %% [markdown]
#
#  ## Attribute von Klassen
#  
# Die meisten Attribute werden auf der Instanz-Ebene definiert, d.h., jedes Objekt hat seine eigenen Werte für die Attribute. Manchmal ist es aber sinnvoll Attribute auch auf der Klassenebene zu definieren:

# %% {{ doc.codealong() }}
class CountedAdder:
    # Attribut der Klasse, wird von allen Instanzen geteilt
    num_counters = 0

    def __init__(self, value):
        CountedAdder.num_counters += 1
        # Instanzvariable (-attribut): Jede Instanz hat eigene Werte dafür
        self.value = value

    def describe(self):
        print(
            f"One of {CountedAdder.num_counters} adders. "
            f"This one adds {self.value} to its argument."
        )

    def add(self, n):
        return self.value + n


# %% {{ doc.codealong() }}
print(CountedAdder.num_counters)
a1 = CountedAdder(10)
print(CountedAdder.num_counters)
a2 = CountedAdder(20)
print(CountedAdder.num_counters)

# %% {{ doc.codealong() }}
print(a1.add(1))
print(a2.add(2))

# %% {{ doc.codealong() }}
a1.describe()
a2.describe()

# %% {{ doc.codealong() }}
print(CountedAdder.num_counters)
print(a1.num_counters)
print(a2.num_counters)

# %% {{ doc.codealong() }}
print(CountedAdder.add)
print(a1.add)
print(a2.add)


# ## Vererbung


# %% {{ doc.codealong() }}
class LoggingAdder(CountedAdder):
    def add(self, n):
        print(f"Adding {self.value} to {n}")
        return self.value + n


# %% {{ doc.codealong() }}
a3 = LoggingAdder(30)
print(a3.add(3))
print(a3.num_counters)

# %% {{ doc.codealong() }}
a1.describe()
a2.describe()
a3.describe()

# %% {{ doc.codealong() }}
# Method Resolution Order:
LoggingAdder.mro()

# %% {{ doc.codealong() }}
print(CountedAdder.add)
print(a1.add)
print(a2.add)
print(LoggingAdder.add)
print(a3.add)

# %% {{ doc.codealong() }}
print(CountedAdder.add)
print(a1.add.__func__)
print(a2.add.__func__)
print(LoggingAdder.add)
print(a3.add.__func__)

# %% {{ doc.codealong() }}
a1.__dict__["value"] = 15

# %% {{ doc.codealong() }}
a1.add(0)

# %% {{ doc.codealong() }}
LoggingAdder.__dict__


# %% [markdown]
#
#  ## Für Experten: Zugriff auf Attribute
#
#  Python ermöglicht es uns als Programmierer, an mehreren Stellen in den Zugriff auf Attribute einzugreifen und das Verhalten zu modifizieren.

# %% [markdown]
#
#  ## Attribute von Klassen
#
#  Beim Zugriff auf `C.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Key in `C.__dict__` ist:
#    - `v = C.__dict__['name']`
#    - Falls `v` ein Deskriptor ist (i.e., `type(v).__get__` definiert ist:
#      - Resultat ist `type(v).__get__(v, None, C)`
#    - Falls `v` kein Deskriptor ist:
#      - Resultat ist `v`
#  - Falls `name` kein Key in `C.__dict__` ist:
#    - Die Baisklassen von `C` werden in Method Resolution Order durchlaufen und
#      diese Verfahren wird für jede Klasse ausgeführt

# %% [markdown]
#
#  ## Attribute von Instanzen
#
#  Beim Zugriff auf `object.name` verfährt Python folgendermaßen:
#
#  - Falls `name` ein Overriding Descriptor `v` in `C` oder einer der
#    Basisklassen von `C` ist (`type(v)` hat Methoden `__get__()` und
#    `__set__()`:
#    - Das Resultat ist `type(v).__get__(v, object, C)`
#  - Andernfalls, falls `name` ein Schlüssel in `object.__dict__` ist:
#    - Das Resultat ist `object.__dict__['name']`
#  - Andernfalls delegiert `object.name` die Suche an die Klasse, wie oben
#    beschrieben
#    - Falls dadurch ein Deskriptor `v` gefunden wird, so ist das Ergebnis
#      `type(v).__get__(v, object, C)`
#    - Wenn ein Wert `v` gefunden wird, der kein Deskriptor ist, dann wird `v`
#      zurückgegeben
#  - Wenn kein Wert gefunden wird und `C.__getattr__` definiert ist, dann wird
#    `C.__getattr__(object, 'name')` aufgerufen um den Wert zu erhalten
#  - Andernfalls wird eine `AttributeError` Exception ausgelöst
#
#  Dieser Prozess kann durch die `__getattribute__` Methode überschrieben werden.

# %%
class LoggingDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"__get__({self}, {instance}, {owner})")
        print(f"  __dict__ == {instance.__dict__}")
        return instance.__dict__.get(self.name, "nothing")


# %%
class OverridingLoggingDescriptor(LoggingDescriptor):
    def __set__(self, instance, value):
        print(f"__set__({self}, {instance}, {value}")
        instance.__dict__[self.name] = value


# %%
class YourClass:
    f = LoggingDescriptor("f")
    g = OverridingLoggingDescriptor("g")


# %%
yc = YourClass()
print(yc.f, yc.g)

# %%
yc.f = 234
yc.g = 345

# %%
print(yc.f, yc.g)


# %%
class MyClass:
    def g(self, x):
        print(self, x)


def f(x, y):
    print(x, y)


# %%
mc = MyClass()
print(mc.__class__)

# %%
print(MyClass.g)
print(mc.g.__qualname__)
print(mc.g.__get__)

# %%
print(f.__get__)

# %%
bound_f = f.__get__(mc, MyClass)
bound_g = mc.g
print(bound_f)
print(bound_g)

# %%
bound_f(3)
bound_g(3)
mc.g(3)

# %% [markdown]
#
# ** Ende der Folien**

# Der Rest der Folien kann weitgehend entfallen, da Klassen jetzt in
# `introduction_part2` eingeführt werden.
#
# TODO: Überprüfen ob es noch nicht behandelte Inhalte gibt und diese
# extrahieren. Evtl. in eine kurze Wiederholung umarbeiten.


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
    "article_number":  "0713",
    "article_name":    "Netzkabel",
    "price_per_item:": 3.49,
    "total_price":     6.98,
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
shopping_cart_entry_1

# %%
type(shopping_cart_entry_1)

# %%
shopping_cart_entry_1.article_number = "9343"
shopping_cart_entry_1.article_name = "Strawberries"
shopping_cart_entry_1.price_per_item = 2.99

# %%
shopping_cart_entry_1.article_number

# %%
shopping_cart_entry_1.article_name

# %%
shopping_cart_entry_1.price_per_item

# %%
shopping_cart_entry_2 = ShoppingCartEntryV0()
shopping_cart_entry_2.article_number = "3742"
shopping_cart_entry_2.article_name = "Cream"

# %%
print(
    "shopping_cart_entry_1:",
    shopping_cart_entry_1.article_number,
    shopping_cart_entry_1.article_name,
    shopping_cart_entry_1.price_per_item,
)
print(
    "shopping_cart_entry_2:",
    shopping_cart_entry_2.article_number,
    shopping_cart_entry_2.article_name,
)


# %%
# Fehler:
# shopping_cart_entry_2.price_per_item


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
    def __init__(self, article_number, article_name, price_per_item,
                 number_of_items):
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
entry = ShoppingCartEntryV1("0713", "Netzkabel", 3.49, 2)
entry

# %%
entry.article_number, entry.article_name, entry.price_per_item, entry.number_of_items, entry.total_price

# %%
# Fehler!
# ShoppingCartEntryV1()


# %%
shopping_cart = [
    ShoppingCartEntryV1("9343", "Strawberries", price_per_item=2.99,
                        number_of_items=2),
    ShoppingCartEntryV1("3742", "Cream", price_per_item=1.99,
                        number_of_items=1),
]

# %% [markdown]
#
#  Die Ausgabe des Einkaufswagens ist mit der `ShoppingCartEntry` Klasse nicht sehr
#  vielsagend. Das werden wir später verbessern.

# %%
shopping_cart

# %% [markdown]
#
#  Wir können die Preise der einzelnen Entries im Einkaufswagen so berechnen:

# %%
[entry.total_price for entry in shopping_cart]


# %%
def total_price_of_shopping_cart(shopping_cart):
    result = 0.0
    for entry in shopping_cart:
        result += entry.total_price
    return result


# %%
total_price_of_shopping_cart(shopping_cart)


# %% [markdown]
#
#  ### ADT für Einkaufswagen
#
#  Der Einkaufswagen ist im Moment als Liste gespeichert. Es wäre möglicherweise
#  hilfreich dafür ebenfalls einen Typ zu definieren:

# %%
class ShoppingCartV0:
    def __init__(self, entries):
        self.entries = entries


# %%
shopping_cart_entry_1 = ShoppingCartEntryV1("9343", "Strawberries", 2.99, 2)
shopping_cart_entry_2 = ShoppingCartEntryV1("3742", "Cream", 1.99, 1)
shopping_cart = ShoppingCartV0([shopping_cart_entry_1, shopping_cart_entry_2])


# %%
def total_price_of_shopping_cart(shopping_cart):
    result = 0.0
    for entry in shopping_cart.entries:
        result += entry.total_price
    return result


# %%
total_price_of_shopping_cart(shopping_cart)


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
class ShoppingCartV2:
    def __init__(self, entries):
        self.entries = entries

    @property
    def total_price(self):
        result = 0.0
        for entry in self.entries:
            result += entry.total_price
        return result


# %%
shopping_cart = ShoppingCartV2([shopping_cart_entry_1, shopping_cart_entry_2])
print(shopping_cart_entry_1.total_price)
print(shopping_cart.total_price)

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
class ShoppingCart:
    def __init__(self, entries):
        self.entries = entries

    @property
    def total_price(self):
        result = 0.0
        for entry in self.entries:
            result += entry.total_price
        return result

    def __repr__(self):
        return f"ShoppingCart({self.entries!r})"

    # See real implementation
    def __str__(self):
        return f"Shopping Cart: {', '.join(str(e) for e in self.entries)}"


# %%
class ShoppingCartEntry:
    def __init__(self, article_number, article_name, price_per_item,
                 number_of_items):
        self.article_number = article_number
        self.article_name = article_name
        self.price_per_item = price_per_item
        self.number_of_items = number_of_items

    @property
    def total_price(self):
        return self.price_per_item * self.number_of_items

    def __repr__(self):
        return f"ShoppingCartEntry({self.article_number!r}, {self.article_name!r}, {self.price_per_item!r}, {self.number_of_items!r})"

    def __str__(self):
        return f"{self.article_name}"


# %%
shopping_cart = ShoppingCart(
    [
        ShoppingCartEntry("9343", "Strawberries", 2.99, 2),
        ShoppingCartEntry("3742", "Cream", 1.99, 1),
    ]
)

# %%
shopping_cart

# %%
print(shopping_cart)

# %%
print(f"{shopping_cart}")
print(f"{shopping_cart!s}")
print(f"{shopping_cart!r}")

# %% [markdown]
#
#  Siehe `Examples/ShoppingCart` für Implementierungsvariante.

# %%
sce1 = ShoppingCartEntry("1", "Item 1", 1.0, 1)
sce2 = ShoppingCartEntry("1", "Item 1", 1.0, 1)
sce1 == sce2

# %% [markdown]
#
#  ## Workshop
#
#  - Notebook `064x-Workshop Todo-Liste V2`
#  - Abschnitt "Grundlegende Funktionalität"
#  - Im Moment ohne die `__iter__()` Methode
