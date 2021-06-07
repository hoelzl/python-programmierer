#!/usr/bin/env python
# coding: utf-8

# %% [markdown]
#
# # Vergleiche, Boole'sche Werte
#
# Gleichheit von Werten wird mit `==` getestet:

# %%
1 == 1

# %%
1 == 2

# %% [markdown]
#
# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %%
type(True)

# %% [markdown]
#
# ## Gleichheit von Zahlen

# %%
1 == 1.0

# %%
0.000_000_1 * 10_000_000 == 1

# %% [markdown]
#
# Vorsicht: Rundungsfehler!

# %%
(2 ** 0.5) ** 2 == 2

# %%
(2 ** 0.5) ** 2

# %% [markdown]
#
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %%
1 != 1.0

# %%
1 != 2

# %% [markdown]
#
# ## Vergleich von Zahlen

# %%
1 < 2

# %%
1 < 1

# %%
1 <= 1

# %%
1 > 2

# %%
2 >= 1

# %% [markdown]
#
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown]
#
# ## Operatoren auf Boole'schen Werten

# %%
1 < 2 and 3 < 2

# %%
1 < 2 or 3 < 2

# %%
not (1 < 2)

# %% [markdown]
#
# ### Wann ist ein logischer Ausdruck wahr?
#
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# %% [markdown]
#
# ### Verkettung von Vergleichen

# %%
1 < 2 < 3

# %%
1 < 2 and 2 < 3

# %%
1 < 3 <= 2

# %%
1 < 3 and 3 <= 2

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Operatoren, Vergleiche"

# %% [markdown]
#
# # `if`-Anweisungen
#
# - Wir wollen ein Programm schreiben, das bestimmt ob eine Zahl eine Glückszahl ist oder nicht:
#     - 7 ist eine Glückszahl
#     - Alle anderen Zahlen sind es nicht.
# - Mit den Python-Konstrukten, die wir bis jetzt kennen können wir das nicht machen.
# - Wir benötigen dazu die `if`-Anweisung:

# %%
def ist_glückszahl(zahl):
    print("Ist", zahl, "eine Glückszahl?")
    if zahl == 7:
        print("Ja!")
    else:
        print("Leider nein.")
    print("Wir wünschen Ihnen alles Gute.")


# %%
ist_glückszahl(1)

# %%
ist_glückszahl(7)

# %%
def ist_glückszahl_2(zahl):
    if zahl == 7:
        print(zahl, "ist eine Glückszahl!")
        print("Sie haben sicher einen super Tag!")
    else:
        print(zahl, "ist leider keine Glückszahl.")
        print("Vielleicht sollten Sie heute lieber im Bett bleiben.")
        print("Wir wünschen Ihnen trotzdem alles Gute.")


# %%
ist_glückszahl_2(1)

# %%
ist_glückszahl_2(7)

# %%
def einseitiges_if_1(zahl):
    print("Vorher")

    if zahl == 7:
        print(zahl, "ist eine Glückszahl")
        print("Glückwunsch!")

    print("Nachher")


# %%
einseitiges_if_1(1)

# %%
einseitiges_if_1(7)

# %%
def einseitiges_if_2(zahl):
    if zahl % 2 != 0:
        zahl += 1  # zahl = zahl + 1
    print(zahl)


# %%
einseitiges_if_2(1)

# %%
einseitiges_if_2(6)

# %% [markdown]
#
# ## Struktur einer `if`-Anweisung (unvollständig):
#
# ```python
# if <Bedingung>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein
#

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Volljährig"

# %% [markdown]
#
# # Listen
#
# - Bisher haben wir nur die Möglichkeit einzelne Werte in Variablen zu speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"

# %% [markdown]
#
# - Probleme damit:
#     - Außer den Variablennamen deutet nichts darauf hin, dass diese Werte z.B. zu einem Warenkorb gehören.
#     - Wir können nur eine fest vorgegebene Anzahl von Werten speichern.
#     - Es ist sehr schwer
#         - die Werte nach verschiedenen Kriterien zu sortieren
#         - Werte hinzuzufügen
#         - Werte zu löschen
#         - die Anzahl der Werte zu bestimmen
#         - ...

# %% [markdown]
#
# - Wir brauchen einen Datentyp, der es uns erlaubt mehrere "Dinge" zusammenzufassen.
# - In Python verwendet man häufig Listen um das zu erreichen.

# %%
warenkorb = ["Haferflocken", "Kaffeebohnen", "Orangenmarmelade"]

# %%
type(warenkorb)

# %% [markdown]
#
# ## Erzeugen von Listen
#
# - Listen werden erzeugt, indem man ihre Elemente in eckige Klammern einschließt.
# - Die Elemente einer Liste können beliebige Python-Werte sein.
# - Eine Liste kann Elemente mit verschiedenen Typen enthalten.

# %%
liste_1 = [1, 2, 3, 4, 5]
liste_2 = ["string1", "another string"]

# %%
print(liste_1)

# %%
print(liste_2)

# %%
liste_3 = []
liste_4 = [1, 0.4, "ein String", True, None]

# %%
print(liste_3)

# %%
print(liste_4)

# %% [markdown]
#
# Die Elemente einer Liste müssen keine Literale sein, man kann auch Werte von
# Variablen in einer Liste speichern:

# %%
produkt_1 = "Haferflocken"
produkt_2 = "Kaffeebohnen"
produkt_3 = "Orangenmarmelade"
warenkorb = [produkt_1, produkt_2, produkt_3, "Erdbeermarmelade"]

# %%
warenkorb

# %% [markdown]
#
# Der Typ von Listen ist `list`.

# %%
type([1, 2, 3])

# %% [markdown]
#
# Mit der Funktion `list` können manche andere Datentypen in Listen umgewandelt werden.
#
# Im Moment kennen wir nur Listen und Strings als mögliche Argumenttypen:

# %%
list("abc")

# %%
list([1, 2, 3])

# ## Zugriff auf Listenelemente

# %%
zahlenliste = [0, 1, 2, 3]

# %%
zahlenliste[0]

# %%
zahlenliste[3]

# %%
zahlenliste[-1]

# %% [markdown]
#
# ## Länge einer Liste

# %%
zahlenliste

# %%
len(zahlenliste)

# %% [markdown]
#
# ## Modifikation von Listeneinträgen

# %%
zahlenliste[1] = 10
zahlenliste

# %% [markdown]
#
# ## Anhängen von Elementen an eine Liste

# %%
zahlenliste.append(40)
zahlenliste

# %% [markdown]
#
# ## Iteration über Listen
#
# In Python kann man mit der `for`-Schleife über Listen iterieren.
#
# Die `for`-Schleife entspricht dem range-based for aus C++,
# `for-in`/`for-of` aus JavaScript oder der `for-each`-Schleife
# aus Java, nicht der klassischen `for`-Schleife
# aus C, C++ oder Java.

# %%
zahlenliste

# %%
for zahl in zahlenliste:
    print("Die Zahl ist:", zahl)

# %% [markdown]
#
# ## Syntax der `for`-Schleife
#
# ```python
# for <element-var> in <liste>:
#     <rumpf>
# ```

# %% [markdown]
#
# ## Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Einkaufsliste"

# %% [markdown]
#
# ## Simulation der klassischen `for`-Schleife
#
# Iteration mit einer `for`-Schleife ist auch über andere Datenstrukturen als Listen möglich.
#
# In Python stellt der Typ `range` eine Folge von ganzen Zahlen dar:
#
# - `range(n)` erzeugt das ganzzahlige Interval von $0$ bis $n-1$
# - `range(m, n)` erzeugt das ganzzahlige Interval von $m$ bis $n-1$
# - `range(m, n, k)` erzeugt die ganzzahlige Sequenz $m, m+k, m+2k, ..., p$,
#   wobei $p$ die größte Zahl der Form $m + jk$ mit $j \geq 0$ und $p < n$ ist

# %%
range(3)

# %%
list(range(3))

# %%
list(range(3, 23, 5))

# %%
for i in range(3):
    print(i)

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Ausgabe von Quadratzahlen"

# %% [markdown]
#
# # Umwandlung in Strings
#
# Python bietet zwei Funktionen an, mit denen beliebige Werte in Strings
# umgewandelt werden können:
#
# - `repr` für eine "programmnahe" Darstellung (wie könnte der Wert im Programm
#   erzeugt werden)
# - `str` für eine "benutzerfreundliche" Darstellung

# %%
print(str("Hallo!"))

# %%
print(repr("Hallo!"))

# %% [markdown]
#
# Für manche Datentypen liefern `str` und `repr` den gleichen String zurück:

# %%
print(str(["a", "b", "c"]))
print(repr(["a", "b", "c"]))

# %% [markdown]
#
# # Benutzerdefinierte Datentypen
#
# In Python können benutzerdefinierte Datentypen definiert werden:

# %%
class PointV0:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %%
p = PointV0(2, 3)
p

# %%
print("x =", p.x)
print("y =", p.y)

# %% [markdown]
#
# ## Methoden
#
# Klassen können Methoden enthalten. Im Gegensatz zu vielen anderen Sprachen hat
# Python bei der Definition keinen impliziten `this` Parameter; das Objekt auf dem
# die Methode aufgerufen wird muss als erster Parameter angegeben werden.
#
# Per Konvention hat dieser Parameter den Namen `self`.

# %%
class PointV1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = PointV1(2, 3)
print("x =", p.x)
print("y =", p.y)

# %%
p.move(3, 5)
print("x =", p.x)
print("y =", p.y)

# %% [markdown]
#
# ## Das Python-Objektmodell
#
# Mit Dunder-Methoden können benutzerdefinierten Datentypen benutzerfreundlicher
# gestaltet werden:

# %%
print(str(p))
print(repr(p))

# %% [markdown]
#
# Durch Definition der Methode `__repr__(self)` kann der von `repr` zurückgegebene
# String für benutzerdefinierte Klassen angepasst werden: Der Funktionsaufruf
# `repr(x)` überprüft, ob `x` eine Methode `__repr__` hat und ruft diese auf,
# falls sie existiert.

# %%
class PointV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "PointV2(" + repr(self.x) + ", " + repr(self.y) + ")"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p = PointV2(2, 5)
print(repr(p))

# %% [markdown]
#
# Standardmäßig delegiert die Funktion `str` an `repr`, falls keine `__str__`-Methode
# definiert ist:
#

# %%
print(str(p))

# %% [markdown]
#
# Python bietet viele Dunder-Methoden an: siehe das
# [Python Datenmodell](https://docs.python.org/3/reference/datamodel.html)
# in der Dokumentation

# %%
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(" + repr(self.x) + ", " + repr(self.y) + ")"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


# %%
p1 = Point(1, 2)
p2 = Point(2, 4)
p = p1 + p2
p

# %%
p += p1
p

# %%
p3 = p - Point(3, 2)
p3

# %% [markdown]
#
# ## Workshop
#
# - Notebook `012x-Workshop Einführung in Python (Teil 2)`
# - Abschnitt "Verbesserte Einkaufsliste"

# %%
