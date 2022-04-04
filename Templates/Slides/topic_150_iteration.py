# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Iteration</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Iteration</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# # Iteration über Listen
#
# Zur Iteration über Listen (und andere Datenstrukturen) bietet Python die
# bereits besprochene`for`-Schleife:


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Iteration over lists
#
# For iterating over lists (and other data structures), Python provides the
# already discussed `for` loop:

# %% {"tags": ["code-along"]}
my_list = [1, 2, 3, 4]
for n in my_list:
    print(f"Item {n}")


# %% {"tags": ["code-along"]}
index = 0
while index < len(my_list):
    n = my_list[index]
    print(f"Item {n}")
    index += 1


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Iteration über Listen von Listen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Iteration over lists of lists

# %% {"tags": ["code-along"]}
a, b = [1, 2]
print(a)
print(b)


# %%
my_list = [[1, 2], [3, 4], [5, 6]]


# %% {"tags": ["code-along"]}
for m, n in my_list:
    print(f"Items {m} and {n}")


# %% {"tags": ["code-along"]}
index = 0
while index < len(my_list):
    m, n = my_list[index]
    print(f"Items {m} and {n}")
    index += 1


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# # Finding items (again)
#
# Our previous version of `find` had to go through the list twice:
#
# - Once from `in` to test if the item you are looking for is in the list
# - Once from `index` to find the index.
#
# It would be nicer if we could do it in one go.

# %%
my_list = ["a", "b", "c", "d", "e"]

# %% {"tags": ["code-along"]}
enumerate(my_list)


# %% {"tags": ["code-along"]}
list(enumerate(my_list))


# %% {"tags": ["code-along"]}
for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def find(element, a_list):
    result = None
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            result = index
            break
    return result


# %%
my_list = ["a", "b", "c", "d", "a"]

# %% {"tags": ["code-along"]}
find("a", my_list)


# %% {"tags": ["code-along"]}
find("d", my_list)


# %% {"tags": ["code-along"]}
assert find("x", my_list) == None


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
# Alternative Implementierung:
def find_return(element, a_list):
    for index, list_entry in enumerate(a_list):
        if list_entry == element:
            return index
    return None


# %% {"tags": ["code-along"]}
# Mit assert können Invarianten dokumentiert werden:
assert find("a", my_list) == find_return("a", my_list)
assert find("d", my_list) == find_return("d", my_list)
assert find("x", my_list) == find_return("x", my_list)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitt "Finden in Listen"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - "Finding in lists" section

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Aggregation von Listenelementen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Aggregation of list items

# %% {"tags": ["code-along"]}
def summe(zahlen):
    ergebnis = 0
    for n in zahlen:
        ergebnis += n
    return ergebnis


# %% {"tags": ["code-along"]}
summe([1, 2, 3])


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitt "Mittelwert einer Liste"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Section "Average of a list"

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Transformation von Listen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Transformation of lists

# %% {"tags": ["code-along"]}
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# %% {"tags": ["code-along"]}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
# ## Mini-Workshop
#
# - Notebook `workshop_100_lists_part2`
# - Abschnitt "Quadratzahlen"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_100_lists_part2`
# - Section "Square numbers"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Filtern von Listen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Filtering lists

# %% {"tags": ["code-along"]}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# %% {"tags": ["code-along"]}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if "ab" in item:
        result.append(item)
result


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitt "Filtern"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Section "Filtering lists"

# %%
