# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Vertiefung zu Listen") }}


# %% [markdown]
# # Listen
#
# Wiederholung:
#
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden

# %%
['a', 'b', 'c']

# %% {{ doc.codealong() }}
list('abcde')

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Simulation der klassischen `for`-Schleife
#
# Iteration mit einer `for`-Schleife ist auch über andere Datenstrukturen als Listen möglich.
#
# In Python stellt der Typ `range` eine Folge von ganzen Zahlen dar:
#
# - `range(n)` erzeugt das ganzzahlige Interval von $0$ bis $n-1$
# - `range(m, n)` erzeugt das ganzzahlige Interval von $m$ bis $n-1$
# - `range(m, n, k)` erzeugt die ganzzahlige Sequenz $m, m+k, m+2k, ..., p$, wobei $p$ die größte Zahl der Form $m + jk$ mit $j \geq 0$ und $p < n$ ist

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
range(3)

# %% {{ doc.codealong() }}
list(range(3))

# %% {{ doc.codealong() }}
list(range(3, 23, 5))

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
for i in range(3):
    print(i)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Ausgabe von Quadratzahlen"


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

# %% slideshow={"slide_type": "subslide"}
stringliste = ["a", "b", "c"]

# %% {{ doc.codealong() }}
stringliste[0]

# %% {{ doc.codealong() }}
stringliste[-1]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Überprüfen, ob ein Element in einer Liste enthalten ist

# %% {{ doc.codealong() }}
2 in [1, 2, 3]


# %% {{ doc.codealong() }}
not (2 in [1, 3, 5])

# %% {{ doc.codealong() }}
2 not in [1, 3, 5]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Finden der Position eines Elements

# %% {{ doc.codealong() }}
[1, 2, 3, 2, 4].index(2)

# %% {{ doc.codealong() }}
my_list = ['a', 'b', 'c', 'd', 'b', 'd', 'b']
my_index = my_list.index('b')
print(my_index)
my_list[my_index]


# %% {{ doc.codealong() }}
# Fehler
# [1, 3, 5].index(2)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Micro-Workshop:
#
# Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in
# der Liste vorkommt. Schreiben Sie eine Funktion
# ```
# find(element, a_list)
# ```
#
# - die einen Index zurückgibt, falls das Element `element` in der Liste
#   vorkommt, und
# - die `None` zurückgibt, falls es nicht vorkommt

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
my_list = ['a', 'b', 'c', 'd', 'e']

# %% slideshow={"slide_type": "-"} {{ doc.codealong() }}
find('a', my_list)

# %% {{ doc.codealong() }}
find('d', my_list)

# %% {{ doc.codealong() }}
print(find('x', my_list))

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Modifikation von Elementen

# %%
stringliste

# %% {{ doc.codealong() }}
stringliste[0] = "A"

# %% {{ doc.codealong() }}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Einfügen und Anhängen von Elementen

# %%
stringliste

# %% {{ doc.codealong() }}
stringliste.append("D")

# %% {{ doc.codealong() }}
stringliste

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
stringliste + ["E", "F"]

# %% {{ doc.codealong() }}
stringliste

# %% {{ doc.codealong() }}
stringliste.extend(["E", "F"])

# %% {{ doc.codealong() }}
stringliste

# %% slideshow={"slide_type": "subslide"}
stringliste

# %% {{ doc.codealong() }}
stringliste.insert(1, "Y")

# %% {{ doc.codealong() }}
stringliste

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
stringliste.insert(0, "ANFANG")

# %% {{ doc.codealong() }}
stringliste

# %% {{ doc.codealong() }}
# Vorsicht!
stringliste.insert(-1, "ENDE")

# %% {{ doc.codealong() }}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Entfernen von Elementen

# %%
stringliste = ['ANFANG', 'A', 'Y', 'b', 'c', 'D', 'E', 'ENDE', 'F']
stringliste[7]

# %% {{ doc.codealong() }}
del stringliste[7]

# %% {{ doc.codealong() }}
stringliste

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Länge einer Liste

# %%
stringliste

# %% {{ doc.codealong() }}
len(stringliste)

# %%  {{ doc.codealong() }}
stringliste.insert(len(stringliste), "WIRKLICH DAS ENDE")

# %% {{ doc.codealong() }}
stringliste

# %% {{ doc.codealong() }}
# Vorsicht
# stringliste[len(stringliste)]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Farben"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Erzeugen von Listen
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste wiederholt werden:

# %% {{ doc.codealong() }}
[1, 2] * 3

# %% {{ doc.codealong() }}
3 * ["a", "b"]

# %% {{ doc.codealong() }}
[0] * 10

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slicing
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% slideshow={"slide_type": "subslide"}
stringliste = ['a', 'b', 'c', 'd', 'e']

# %% {{ doc.codealong() }}
stringliste[1:3]

# %% {{ doc.codealong() }}
stringliste[1:1]

# %% {{ doc.codealong() }}
stringliste[0:len(stringliste)]

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
stringliste[:3]

# %% {{ doc.codealong() }}
stringliste[1:]

# %% {{ doc.codealong() }}
stringliste[:]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Slicing"
#

# %% [markdown] pycharm={"name": "#%% md\n"} slideshow={"slide_type": "slide"}
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %% {{ doc.codealong() }}
liste = [1, 2, 3, 4]
liste[1:3]

# %% {{ doc.codealong() }}
liste[1:3] = ['a', 'b', 'c']
liste

# %% {{ doc.codealong() }}
liste[2:2]

# %% {{ doc.codealong() }}
liste[2:2] = ['x']
liste

# %% slideshow={"slide_type": "subslide"} {{ doc.codealong() }}
liste[:] = [11, 22, 33]
liste

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slices als Objekte
#
# Slices sind selber Python Objekte. Außerhalb der Indexing-Operation `[]`
# können sie allerdings nicht mit der Notation `a:b` erzeugt werden, sondern
# mit der Konstruktor-Funktion `slice()`.

# %% slideshow={"slide_type": "-"}
my_list = [1, 2, 3, 4, 5, 6]
my_slice = slice(2, 4)
print(my_list[2:4])
print(my_list[my_slice])

# %% slideshow={"slide_type": "subslide"}
my_slice = slice(None, 3)
print(my_list[:3])
print(my_list[my_slice])

# %% [markdown] slideshow={"slide_type": "subslide"}
#
# Die `indices()`-Methode eines Slice-Objekts kann dazu verwendet werden zu
# bestimmen, welche Indizes das Slice enthält:

# %%
print(my_slice.indices(len(my_list)))

# %% [markdown]
#
# Damit können wir eine Funktion schreiben, die alle Elemente eines Slices
# durch einen Wert ersetzt:

# %% slideshow={"slide_type": "subslide"}
import math
def replace_with(my_list, my_slice, value):
    start, stop, stride = my_slice.indices(len(my_list))
    num_values = math.ceil((stop - start) / stride)
    my_list[my_slice] = [value] * num_values


# %% slideshow={"slide_type": "subslide"}
my_list = [1, 2, 3, 4, 5, 6]
my_slice = slice(2, 6)
replace_with(my_list, my_slice, 8)
my_list
