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
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python: Listen und For-Schleifen</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown]
# # Listen
#
# Wiederholung:
#
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden

# %%
['a', 'b', 'c']

# %% pycharm={"name": "#%%\n"}
list(range(3))


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Eigenschaften von Listen
#
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
#
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste = ["a", "b", "c"]

# %% pycharm={"is_executing": false}
stringliste[0]

# %% pycharm={"is_executing": false}
stringliste[-1]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Überprüfen, ob ein Element in einer Liste enthalten ist

# %% pycharm={"is_executing": false}
2 in [1, 2, 3]


# %%
not (2 in [1, 3, 5])

# %% pycharm={"is_executing": false}
2 not in [1, 3, 5]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Finden der Position eines Elements

# %% pycharm={"is_executing": false}
[1, 2, 3, 2, 4].index(2)

# %%
my_list = ['a', 'b', 'c', 'd', 'b', 'd', 'b']
my_index = my_list.index('b')
print(my_index)
my_list[my_index]

# %% pycharm={"is_executing": false}
# Fehler
# [1, 3, 5].index(2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Micro-Workshop:
#
# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in der Liste vorkommt. Schreiben Sie eine Funktion
# ```
# find(element, a_list)
# ```
#
# - die einen Index zurückgibt, falls das Element `element` in der Liste vorkommt, und
# - die `None` zurückgibt, falls es nicht vorkommt

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
my_list = ['a', 'b', 'c', 'd', 'e']

# %% pycharm={"is_executing": false} slideshow={"slide_type": "-"}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Modifikation von Elementen

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false}
stringliste[0] = "A"

# %% pycharm={"is_executing": false}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Einfügen und Anhängen von Elementen

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false}
stringliste.append("D")

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste + ["E", "F"]

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false}
stringliste.extend(["E", "F"])

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste

# %% pycharm={"is_executing": false}
stringliste.insert(1, "Y")

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste.insert(0, "ANFANG")

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false}
# Vorsicht!
stringliste.insert(-1, "ENDE")

# %% pycharm={"is_executing": false}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Entfernen von Elementen

# %% pycharm={"is_executing": false}
stringliste = ['ANFANG', 'A', 'Y', 'b', 'c', 'D', 'E', 'ENDE', 'F']
stringliste[7]

# %% pycharm={"is_executing": false}
del stringliste[7]

# %% pycharm={"is_executing": false}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Länge einer Liste

# %% slideshow={"slide_type": "subslide"}
stringliste

# %% pycharm={"is_executing": false}
len(stringliste)

# %% pycharm={"is_executing": false} slideshow={"slide_type": "-"}
stringliste.insert(len(stringliste), "WIRKLICH DAS ENDE")

# %% pycharm={"is_executing": false}
stringliste

# %% pycharm={"is_executing": false}
# Vorsicht
# stringliste[len(stringliste)]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Farben"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Erzeugen von Listen
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste wiederholt werden:

# %%
[1, 2] * 3

# %%
3 * ["a", "b"]

# %%
[0] * 10

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slicing
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste = ['a', 'b', 'c', 'd', 'e']

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Slicing"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %%
liste = [1, 2, 3, 4]
liste[1:3]

# %%

# %%

# %%

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slices als Objekte
#
# Slices sind selber Python Objekte. Außerhalb der Indexing-Operation `[]` können sie allerdings nicht mit der Notation `a:b` erzeugt werden, sondern mit der Konstruktor-Funktion `slice()`. 

# %% slideshow={"slide_type": "-"}

# %% slideshow={"slide_type": "subslide"}

# %% [markdown] slideshow={"slide_type": "subslide"}
# Die `indices()`-Methode eines Slice-Objekts kann dazu verwendet werden zu bestimmen, welche Indizes das Slice enthält:

# %% slideshow={"slide_type": "-"}

# %% [markdown] slideshow={"slide_type": "-"}
# Damit können wir eine Funktion schreiben, die alle Elemente eines Slices durch einen Wert ersetzt:

# %% slideshow={"slide_type": "subslide"}

# %% slideshow={"slide_type": "subslide"}

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Identität von Objekten
#
# Die [Python Tutor](https://pythontutor.com/visualize.html) Website visualisiert die Zusammenhänge sehr anschaulich.

# %% pycharm={"is_executing": false}
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %% pycharm={"is_executing": false}
print(f"a = {a}, b = {b}, c = {c}")

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
a[0] = 10

# %% pycharm={"is_executing": false}
print(f"a = {a}, b = {b}, c = {c}")

# %% pycharm={"is_executing": false}
b[0] = 20

# %%
c[1] = 30

# %% pycharm={"is_executing": false}
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Test der Identität von Objekten

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% slideshow={"slide_type": "subslide"}

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %% pycharm={"name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# # Nochmal Finden von Elementen
#
# Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen werden:
#
# - Einmal von `in` um zu testen, ob das gesuchte Element in der Liste vorkommt
# - Einmal von `index` um den Index zu finden.
#
# Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten. (Mini-Workshop...)

# %% pycharm={"is_executing": false, "name": "#%%\n"} slideshow={"slide_type": "subslide"}
my_list = ['a', 'b', 'c', 'd', 'e']


# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}

# %% pycharm={"is_executing": false, "name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
my_list = ['a', 'b', 'c', 'd', 'a']


# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %%
# Mit assert können Invarianten dokumentiert werden:


# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Finden in Listen"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Aggregation von Listenelementen

# %% slideshow={"slide_type": "-"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Mittelwert einer Liste"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Transformation von Listen

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false}

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Quadratzahlen"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Eleganter: Listen-Komprehension

# %% pycharm={"is_executing": false}
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false, "name": "#%%\n"} slideshow={"slide_type": "subslide"}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitte "Quadratzahlen mit Listen-Komprehension"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# # Filtern von Listen

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitt "Filtern"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Eleganter: Listen-Komprehension

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %% pycharm={"is_executing": false}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %% pycharm={"is_executing": false}

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result

# %% pycharm={"name": "#%%\n"}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen und For-Schleifen`
# - Abschnitte "Filtern mit Listen-Komprehension"
#

# %% [markdown]
# ## Workshop
#
# - Notebook `lecture_930x_Workshop_Ox`

# %% [markdown] slideshow={"slide_type": "slide"}
# # Tupel
#
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
#
# Syntax:
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`
# - Tupel mit einem Element müssen in der Form `(1,)` geschrieben werden.

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %%

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %% pycharm={"name": "#%%\n"}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Eigenschaften von Tupeln
#
# - Tupel können beliebige Python-Werte speichern
# - Elemente in einem Tupel haben eine feste Reihenfolge
# - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
# - Tupel können *nicht* modifiziert werden
#
# Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Operationen auf Tupeln
#
# - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
# - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"name": "#%%\n"}

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}

# %%

# %% pycharm={"is_executing": false}

# %% [markdown] slideshow={"slide_type": "slide"}
# # Generatoren
#
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:

# %% slideshow={"slide_type": "subslide"}

# %%

# %% slideshow={"slide_type": "subslide"}
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f'{i}, {j}, {k}')

# %% slideshow={"slide_type": "subslide"}

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %% slideshow={"slide_type": "subslide"}

# %%
_r = range(3)
_temp_iter = iter(_r)
while True:
    try: x = next(_temp_iter)
    except StopIteration: break
    print(x, end=' ')

# %% slideshow={"slide_type": "subslide"}

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %% slideshow={"slide_type": "-"}
# `it` ist "erschöpft," man kann keine neuen Werte bekommen


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Generator-Funktionen
#
# Komplexere Fälle können von Generator Expressions nicht mehr abgedeckt werden.
#
# - Generator, der alle Zahlen erzeugt (ohne Obergrenze)
# - Generator, der ein Iterable modifiziert (z.B. mehrfach ausführt, eine fixe Anzahl an Elementen nimmt)
#
# Für diese Fälle gibt es Generator-Funktionen

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%
