# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Vertiefung zu Listen</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Lists in Depth</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Listen
#
# Wiederholung:
#
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Lists
#
# Recall:
#
# - List literals are enclosed in square brackets
# - Other sequences can be converted to lists using `list`

# %%
["a", "b", "c"]

# %% {"tags": ["code-along"]}
list("abcde")

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# ## Ranges

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
#
# ## Ranges

# %%
range(1, 4)

# %%
list(range(1, 4))

# %%
range(4)

# %%
list(range(4))

# %%
list(range(1, 9, 2))

# %%
for x in range(1, 4):
    print(x)

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Ausgabe von Quadratzahlen"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Section "Printing square numbers"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Eigenschaften von Listen
#
# - Listen können beliebige Python-Werte speichern
# - Elemente in einer Liste haben eine feste Reihenfolge
# - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
# - Listen können modifiziert werden
#
# Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
# enthalten aber Elemente eines einzigen Typs.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Properties of lists
#
# - Lists can store arbitrary Python values
# - Elements in a list have a fixed order
# - Elements of a list can be accessed by index
# - Lists can be modified
#
# Lists can contain elements of different types, but most lists contain elements of a single type.

# %% {"slideshow": {"slide_type": "subslide"}}
stringliste = ["a", "b", "c"]

# %% {"tags": ["code-along"]}
stringliste[0]

# %% {"tags": ["code-along"]}
stringliste[-1]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Überprüfen, ob ein Element in einer Liste enthalten ist

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Check if an item is in a list

# %% {"tags": ["code-along"]}
2 in [1, 2, 3]

# %% {"tags": ["code-along"]}
not (2 in [1, 3, 5])

# %% {"tags": ["code-along"]}
2 not in [1, 3, 5]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Finden der Position eines Elements

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Find the position of an element

# %% {"tags": ["code-along"]}
[1, 2, 3, 2, 4].index(2)

# %%
my_list = ["a", "b", "c", "d", "b", "d", "b"]

# %% {"tags": ["code-along"]}
my_index = my_list.index("b")
print(my_index)
my_list[my_index]


# %% {"tags": ["code-along"]}
# Fehler
# [1, 3, 5].index(2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Micro workshop:
#
# The `index` method throws an exception if the searched object does not
# appear in the list. Write a function
# ```
# find(item, a_list)
# ```
#
# - which returns an index if the element `element` is in the list, and
# - returns `None` if it is not

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %% {"slideshow": {"slide_type": "subslide"}}
my_list = ["a", "b", "c", "d", "e"]

# %% {"slideshow": {"slide_type": "-"}, "tags": ["code-along"]}
find("a", my_list)

# %% {"tags": ["code-along"]}
find("d", my_list)

# %% {"tags": ["code-along"]}
print(find("x", my_list))

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Modifikation von Elementen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Modification of elements

# %%
stringliste

# %% {"tags": ["code-along"]}
stringliste[0] = "A"

# %%
stringliste

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Einfügen und Anhängen von Elementen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Inserting and appending elements

# %%
stringliste

# %% {"tags": ["code-along"]}
stringliste.append("D")

# %%
stringliste

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
stringliste + ["E", "F"]

# %%
stringliste

# %% {"tags": ["code-along"]}
stringliste.extend(["E", "F"])

# %% {"slideshow": {"slide_type": "subslide"}}
stringliste

# %% {"tags": ["code-along"]}
stringliste.insert(1, "Y")

# %%
stringliste

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
stringliste.insert(0, "ANFANG")

# %%
stringliste

# %% {"tags": ["code-along"]}
# Vorsicht!
stringliste.insert(-1, "ENDE")

# %%
stringliste

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Entfernen von Elementen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Removing elements

# %%
stringliste = ["ANFANG", "A", "Y", "b", "c", "D", "E", "ENDE", "F"]
stringliste[7]

# %% {"tags": ["code-along"]}
del stringliste[7]

# %%
stringliste

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Länge einer Liste

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Length of a list

# %%
stringliste

# %% {"tags": ["code-along"]}
len(stringliste)

# %% {"tags": ["code-along"]}
stringliste.insert(len(stringliste), "WIRKLICH DAS ENDE")

# %%
stringliste

# %% {"tags": ["code-along"]}
# Vorsicht
# stringliste[len(stringliste)]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Farben"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_100_lists_part2`
# - Section Colors

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Erzeugen von Listen
#
# Durch den Multiplikationsoperator `*` können die Elemente einer Liste
# wiederholt werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Creating lists
#
# The multiplication operator `*` allows the elements of a list
# be repeated:

# %% {"tags": ["code-along"]}
[1, 2] * 3

# %% {"tags": ["code-along"]}
3 * ["a", "b"]

# %% {"tags": ["code-along"]}
[0] * 10

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Slicing
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste`
# extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Slicing
#
# With the notation `list[m:n]` you can extract a "sublist" of `list`.
#
# - The first element is `list[m]`
# - The last element is `list[n-1]`

# %% {"slideshow": {"slide_type": "subslide"}}
stringliste = ["a", "b", "c", "d", "e"]

# %% {"tags": ["code-along"]}
stringliste[1:3]

# %% {"tags": ["code-along"]}
stringliste[1:1]

# %% {"tags": ["code-along"]}
stringliste[0 : len(stringliste)]

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
stringliste[:3]

# %% {"tags": ["code-along"]}
stringliste[1:]

# %% {"tags": ["code-along"]}
stringliste[:]

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Slicing"
#

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
# - Notebook `workshop_100_lists_part2`
# - Section "Slicing"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Zuweisung an Slices
#
# Man kann Werte an Slices zuweisen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Assignment to slices
#
# You can assign values to slices:

# %% {"tags": ["code-along"]}
liste = [1, 2, 3, 4]
liste[1:3]

# %% {"tags": ["code-along"]}
liste[1:3] = ["a", "b", "c"]
liste

# %% {"tags": ["code-along"]}
liste[2:2]

# %% {"tags": ["code-along"]}
liste[2:2] = ["x"]
liste

# %% {"slideshow": {"slide_type": "subslide"}, "tags": ["code-along"]}
liste[:] = [11, 22, 33]
liste

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Slices als Objekte
#
# Slices sind selber Python Objekte. Außerhalb der Indexing-Operation `[]`
# können sie allerdings nicht mit der Notation `a:b` erzeugt werden, sondern
# mit der Konstruktor-Funktion `slice()`.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Slices as objects
#
# Slices are themselves Python objects. However, outside the indexing operation `[]`
# they cannot be created with the notation `a:b`, but only
# with the constructor function `slice()`.

# %% {"slideshow": {"slide_type": "-"}}
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[2:4])


# %% {"tags": ["code-along"]}
my_slice = slice(2, 4)
print(my_list[my_slice])

# %% {"slideshow": {"slide_type": "subslide"}}
print(my_list[:3])

# %% {"tags": ["code-along"]}
my_slice = slice(None, 3)
print(my_list[my_slice])

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# Die `indices()`-Methode eines Slice-Objekts kann dazu verwendet werden zu
# bestimmen, welche Indizes das Slice enthält:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The `indices()` method of a slice object can be used to
# determine which indices the slice contains:

# %%
my_slice = slice(None, 3)
print(my_slice.indices(len(my_list)))


# %% [markdown] {"lang": "de"}
#
# Damit können wir eine Funktion schreiben, die alle Elemente eines Slices
# durch einen Wert ersetzt:

# %% [markdown] {"lang": "en"}
# With this we can write a function that replaces all the elements of a slice
# with a given value:

# %% {"slideshow": {"slide_type": "subslide"}}
def replace_with(my_list, my_slice, value):
    import math

    start, stop, stride = my_slice.indices(len(my_list))
    num_values = math.ceil((stop - start) / stride)
    my_list[my_slice] = [value] * num_values


# %% {"slideshow": {"slide_type": "subslide"}}
my_list = [1, 2, 3, 4, 5, 6]
my_slice = slice(2, 6)
replace_with(my_list, my_slice, 8)
my_list
