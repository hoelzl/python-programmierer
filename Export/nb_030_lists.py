#!/usr/bin/env python
# coding: utf-8

# %% [markdown]
#
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Listen und For-Schleifen</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <div style="text-align:center;">Allaithy Raed</div>
#

# %% [markdown]
#
# # Listen
#
# Wiederholung:
#
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden

# %%
["a", "b", "c"]

# %%
list(range(3))

# %% [markdown]
#
# ## Eigenschaften von Listen
#
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
#
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# %%
stringliste = ["a", "b", "c"]

# %%
stringliste[0]

# %%
stringliste[-1]

# %% [markdown]
#
# ### Überprüfen, ob ein Element in einer Liste enthalten ist

# %%
2 in [1, 2, 3]

# %%
not (2 in [1, 3, 5])

# %%
2 not in [1, 3, 5]

# %% [markdown]
#
# ### Finden der Position eines Elements

# %%
[1, 2, 3, 2, 4].index(2)

# %%
my_list = ["a", "b", "c", "d", "b", "d", "b"]
my_index = my_list.index("b")
print(my_index)
my_list[my_index]

# %%
# Fehler
# [1, 3, 5].index(2)

# %% [markdown]
#
# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in
# der Liste vorkommt. Wie können wir eine Funktion
# ```
# find(element, a_list)
# ```
# schreiben, die uns
#
# - einen Index zurückgibt, falls das Element `element` in der Liste vorkommt,
#   und die
# - `None` zurückgibt, falls es nicht vorkommt?

# %%
def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %%
my_list = ["a", "b", "c", "d", "e"]

# %%
find("a", my_list)

# %%
find("d", my_list)

# %%
print(find("x", my_list))

# %% [markdown]
#
# ### Modifikation von Elementen

# %%
stringliste

# %%
stringliste[0] = "A"

# %%
stringliste

# %% [markdown]
#
# ### Einfügen und Anhängen von Elementen

# %%
stringliste

# %%
stringliste.append("D")

# %%
stringliste

# %%
stringliste + ["E", "F"]

# %%
stringliste

# %%
stringliste.extend(["E", "F"])

# %%
stringliste

# %%
stringliste

# %%
stringliste.insert(1, "Y")

# %%
stringliste

# %%
stringliste.insert(0, "ANFANG")

# %%
stringliste

# %%
# Vorsicht!
stringliste.insert(-1, "ENDE")

# %%
stringliste

# %% [markdown]
#
# ### Entfernen von Elementen

# %%
stringliste

# %%
stringliste[7]

# %%
del stringliste[7]

# %%
stringliste

# %% [markdown]
#
# ### Länge einer Liste

# %%
stringliste

# %%
len(stringliste)

# %%
stringliste.insert(len(stringliste), "WIRKLICH DAS ENDE")

# %%
stringliste

# %%
# Vorsicht!
# stringliste[len(stringliste)]

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Farben"
#

# %% [markdown]
#
# ## Slicing
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %%
stringliste = ["a", "b", "c", "d", "e"]

# %%
stringliste[1:3]

# %%
stringliste[1:1]

# %%
stringliste[0 : len(stringliste)]

# %%
stringliste[:3]

# %%
stringliste[1:]

# %%
stringliste[:]

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Slicing"
#

# %% [markdown]
#
# ## Erzeugen von Listen
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste wiederholt werden:

# %%
[1, 2] * 3

# %%
3 * ["a", "b"]

# %%
[0] * 10

# %% [markdown]
#
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %%
liste = [1, 2, 3, 4]
liste[1:3]

# %%
liste[1:3] = ["a", "b", "c"]
liste

# %%
liste[2:2]

# %%
liste[2:2] = ["x"]
liste

# %%
liste[:] = [11, 22, 33]
liste

# %% [markdown]
#
# ## Identität von Objekten

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
a[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
b[0] = 20

# %%
c[1] = 30

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown]
#
# <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown]
#
# ## Test der Identität von Objekten

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %%
a == b

# %%
b == c

# %%
c == d

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %%
a is b

# %%
b is c

# %%
c is d

# %%
hex(id([1, 2, 3]))

# %%
def modify_list(lst):
    print("modify_list: before", lst)
    lst.append("abc")
    print("modify_list: after", lst)


# %%
my_list = [1, 2, 3]
modify_list(my_list)

# %%
my_list

# %% [markdown]
#
# # Iteration über Listen
#
# Zur Iteration über Listen (und andere Datenstrukturen) bietet Python die bereits besprochene`for`-Schleife:

# %%
my_list = [1, 2, 3, 4]
for n in my_list:
    print(f"Item {n}")

# %%
index = 0
while index < len(my_list):
    n = my_list[index]
    print(f"Item {n}")
    index += 1

# %% [markdown]
#
# ## Iteration über Listen von Listen

# %%
a, b = [1, 2]
print(a)
print(b)

# %%
my_list = [[1, 2], [3, 4], [5, 6]]

# %%
index = 0
while index < len(my_list):
    m, n = my_list[index]
    print(f"Items {m} and {n}")
    index += 1

# %%
for m, n in my_list:
    print(f"Items {m} and {n}")

# %% [markdown]
#
# # Nochmal Finden von Elementen
#
# Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen
# werden:
#
# - Einmal von `in` um zu testen, ob das gesuchte Element in der Liste vorkommt
# - Einmal von `index` um den Index zu finden.
#
# Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# %%
my_list = ["a", "b", "c", "d", "e"]
enumerate(my_list)

# %%
list(enumerate(my_list))

# %%
for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")

# %%
for index, element, other in [[1, 2, 3], ["a", "b", "c"]]:
    print(index, element, other)

# %%
def find(element, a_list):
    result = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            result = index
            break
    return result


# %%
my_list = ["a", "b", "c", "d", "a"]
find("a", my_list)

# %%
find("d", my_list)

# %%
assert find("x", my_list) == None

# %%
# Alternative Implementierung:
def find_return(element, a_list):
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            return index
    return None


# %%
# Mit assert können Invarianten dokumentiert werden:
assert find("a", my_list) == find_return("a", my_list)
assert find("d", my_list) == find_return("d", my_list)
assert find("x", my_list) == find_return("x", my_list)

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Finden in Listen"
#

# %% [markdown]
#
# ## Aggregation von Listenelementen

# %%
def summe(zahlen):
    ergebnis = 0
    for n in zahlen:
        ergebnis += n
    return ergebnis


# %%
summe([1, 2, 3])

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Mittelwert einer Liste"
#

# %% [markdown]
#
# ## Transformation von Listen

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Quadratzahlen"
#

# # Filtern von Listen

# %%
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if "ab" in item:
        result.append(item)
result

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitt "Filtern"
#

# %% [markdown]
#
# ## Eleganter: Listen-Komprehension

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
my_list = [item + 1 for item in [1, 2, 3, 4]]
my_list

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%
[f"Item {n}" for n in [1, 2, 3, 4]]

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitte "Quadratzahlen mit Listen-Komprehension"
#

# %%
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]

# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]

# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result

# %%
[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `030x-Workshop Listen und For-Schleifen`
# - Abschnitte "Filtern mit Listen-Komprehension"
#

# %% [markdown]
#
# # Tupel
#
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
#
# Syntax:
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`

# %%
1, 2, 3

# %%
(1,)

# %%
x = "a", 1, True

# %%
type(x)

# %% [markdown]
#
# ## Eigenschaften von Tupeln
#
# - Tupel können beliebige Python-Werte speichern
# - Elemente in einem Tupel haben eine feste Reihenfolge
# - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
# - Tupel können *nicht* modifiziert werden
#
# Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# %% [markdown]
#
# ## Operationen auf Tupeln
#
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# %%
values = 1, 2, 3
print(values + ("a", "b"))
print(values[1])
print("Length:", len(values))
values

# %%
for x in 1, 2, 3:
    print(x)

# %%
x, y = 1, 2

# %%
print(x, y)

# %%
(1, 2, 3).index(2)

# %%
(1, 2, 3, 1, 2, 1, 2).count(1)

# %%
[
    f"Item {item} in {tuple_1}"
    for tuple_1 in ((1, 2), ("a", "b", "c"))
    for item in tuple_1
]

# %% [markdown]
#
# # Generatoren
#
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum
#   Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar
#   sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:

# %%
gen = (n * n for n in range(10))
gen

# %%
for i in gen:
    print(i, end=" ")

# %%
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f"{i}, {j}, {k}")

# %%
r = range(3)
repr(r)

# %%
it = iter(r)
repr(it)

# %%
next(it)

# %%
next(it)

# %%
next(it)

# %%
# next(it)

# %%
for x in range(3):
    print(x, end=" ")

# %%
_r = range(3)
_temp_iter = iter(_r)
while True:
    try:
        x = next(_temp_iter)
    except StopIteration:
        break
    print(x, end=" ")

# %%
gen = (n * n for n in range(3))
repr(gen)

# %%
it = iter(gen)
repr(it)

# %%
next(it)

# %%
next(it)

# %%
next(it)

# %%
# next(it)

# %%
# `it` ist "erschöpft," man kann keine neuen Werte bekommen
# next(it)

# %% [markdown]
#
# ## Generator Funktionen
#
# Komplexere Fälle können von Generator Expressions nicht mehr abgedeckt werden.
#
# - Generator, der alle Zahlen erzeugt (ohne Obergrenze)
# - Generator, der ein Iterable modifiziert (z.B. mehrfach ausführt, eine fixe Anzahl an Elementen nimmt)
#
# Für diese Fälle gibt es Generator-Funktionen

# %%
def integers(start=0):
    n = start
    while True:
        yield n
        n += 1


# %%
for i in integers():
    if i > 3:
        break
    print(i, end=" ")

# %%
gen = integers()
print(repr(gen))
print(repr(iter(gen)))

# %%
gen = integers()

# %%
next(gen)

# %%

# %%
def repeat_n_times(n, it):
    for _ in range(n):
        for elt in it:
            yield elt


# %%
for num in repeat_n_times(3, range(5)):
    print(num, end=" ")

# %%
