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

# %%
# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Vertiefung zu Listen</h1>
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
def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
my_list = ['a', 'b', 'c', 'd', 'e']

# %% pycharm={"is_executing": false} slideshow={"slide_type": "-"}
find('a', my_list)

# %% pycharm={"is_executing": false}
find('d', my_list)

# %% pycharm={"is_executing": false}
print(find('x', my_list))

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
stringliste[1:3]

# %% pycharm={"is_executing": false}
stringliste[1:1]

# %% pycharm={"is_executing": false}
stringliste[0:len(stringliste)]

# %% pycharm={"is_executing": false} slideshow={"slide_type": "subslide"}
stringliste[:3]

# %% pycharm={"is_executing": false}
stringliste[1:]

# %% pycharm={"is_executing": false}
stringliste[:]

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
liste[1:3] = ['a', 'b', 'c']
liste

# %%
liste[2:2]

# %%
liste[2:2] = ['x']
liste

# %% pycharm={"name": "#%%\n"} slideshow={"slide_type": "subslide"}
liste[:] = [11, 22, 33]
liste

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slices als Objekte
#
# Slices sind selber Python Objekte. Außerhalb der Indexing-Operation `[]` können sie allerdings nicht mit der Notation `a:b` erzeugt werden, sondern mit der Konstruktor-Funktion `slice()`. 

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
# Die `indices()`-Methode eines Slice-Objekts kann dazu verwendet werden zu bestimmen, welche Indizes das Slice enthält:

# %% slideshow={"slide_type": "-"}
print(my_slice.indices(len(my_list)))

# %% [markdown] slideshow={"slide_type": "-"}
# Damit können wir eine Funktion schreiben, die alle Elemente eines Slices durch einen Wert ersetzt:

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