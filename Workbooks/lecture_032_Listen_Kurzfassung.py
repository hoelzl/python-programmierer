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
# <h1 style="text-align:center;">Python: Listen (Kurzfassung)</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Slicing
#
# Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
#
# - Das erste Element ist `liste[m]`
# - Das letzte Element ist `liste[n-1]`

# %% slideshow={"slide_type": "subslide"}
stringliste = ['a', 'b', 'c', 'd', 'e']

# %%
stringliste[1:3]

# %%
stringliste[1:1]

# %%
stringliste[0:len(stringliste)]

# %% slideshow={"slide_type": "subslide"}
stringliste[:3]

# %%
stringliste[1:]

# %%
stringliste[:]

# %%
stringliste[1:5:2]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen_und_For_Schleifen`
# - Abschnitt "Slicing"

# %% [markdown] slideshow={"slide_type": "slide"}
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

# %% slideshow={"slide_type": "subslide"}
liste[:] = [11, 22, 33]
liste

# %% [markdown] slideshow={"slide_type": "slide"}
#
# ## Slices als Objekte
#
# Slices sind selber Python Objekte. Außerhalb der Indexing-Operation `[]`
# können sie allerdings nicht mit der Notation `a:b` erzeugt werden, sondern mit
# der Konstruktor-Funktion `slice()`. 

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

# %% slideshow={"slide_type": "-"}
print(my_slice.indices(len(my_list)))

# %% [markdown] slideshow={"slide_type": "-"}
#
# Damit können wir eine Funktion schreiben, die alle Elemente eines Slices durch
# einen Wert ersetzt:

# %% slideshow={"slide_type": "subslide"}
import math
def replace_with(my_list, my_slice, value):
    start, stop, stride = my_slice.indices(len(my_list))
    num_values = math.ceil((stop - start) / stride)
    my_list[my_slice] = [value] * num_values


# %% slideshow={"slide_type": "subslide"}
my_list = [1, 2, 3, 4, 5, 6]
my_slice = slice(2, 4)
my_list[2:4]
replace_with(my_list, my_slice, 8)
my_list

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Identität von Objekten
#
# Die [Python Tutor](https://pythontutor.com/visualize.html) Website visualisiert die Zusammenhänge sehr anschaulich.

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% slideshow={"slide_type": "subslide"}
a[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
b[0] = 20

# %%
c[1] = 30

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Test der Identität von Objekten
#

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

# %% slideshow={"slide_type": "subslide"}
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

# %% slideshow={"slide_type": "subslide"}
hex(10), hex(78)

# %%
hex(id([1, 2, 3]))


# %% slideshow={"slide_type": "subslide"}
def modify_list(lst):
    print("modify_list: before", lst)
    lst.append("abc")
    print("modify_list: after", lst)


# %%
my_list = [1, 2, 3]
modify_list(my_list)

# %%
my_list

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Transformation von Listen

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%
my_list = [item + 1 for item in [1, 2, 3, 4]] 
my_list

# %% slideshow={"slide_type": "subslide"}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%
[f"Item {n}" for n in [1, 2, 3, 4]]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen_und_For_Schleifen`
# - Abschnitt "Quadratzahlen mit Listen-Komprehension"
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Filtern von Listen

# %% slideshow={"slide_type": "subslide"}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]

# %% slideshow={"slide_type": "subslide"}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]

# %% slideshow={"slide_type": "subslide"}
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result

# %%
[f"Item {item} in {list_1}"
 for list_1 in [[1, 2], ["a", "b", "c"]]
 for item in list_1]

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Mini-Workshop
#
# - Notebook `lecture_030x_Workshop_Listen_und_For_Schleifen`
# - Abschnitt "Filtern mit Listen-Komprehension"
#

# %%
