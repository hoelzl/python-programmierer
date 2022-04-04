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
# <div style="text-align:center; font-size:200%;"><b>Tupel</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Tuples</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# # Tupel
#
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
#
# Syntax:
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Tuples
#
# Tuples are a data structure very similar to lists.
#
# Syntax:
#
# - Elements separated by commas: `1, 2, 3, 4`
# - In many cases, tuples must be enclosed in parens: `(1, 2, 3)`

# %% {"tags": ["code-along"]}
1, 2, 3


# %% {"tags": ["code-along"]}
non_tuple = 1
print(non_tuple)
type(non_tuple)

# %% {"tags": ["code-along"]}
singleton_tuple = (1,)
print(singleton_tuple)
type(singleton_tuple)


# %% {"tags": ["code-along"]}
x = "a", 1, True


# %% {"tags": ["code-along"]}
type(x)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Eigenschaften von Tupeln
#
#  - Tupel können beliebige Python-Werte speichern
#  - Elemente in einem Tupel haben eine feste Reihenfolge
#  - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
#  - Tupel können *nicht* modifiziert werden
#
#  Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Properties of tuples
#
#  - Tuples can store arbitrary Python values
#  - Elements in a tuple have a fixed order
#  - Elements of a tuple can be accessed by index
#  - Tuples can *not* be modified
#
#  Tuples are often used to store *heterogeneous* data.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Operationen auf Tupeln
#
#  - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
#  - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Operations on tuples
#
#  - Many of the operations on lists can be applied to tuples.
#  - The operations that change lists are not applicable.

# %% {"tags": ["code-along"]}
values = 1, 2, 3
print(values + ("a", "b"))
print(values[1])
print("Length:", len(values))
values


# %% {"tags": ["code-along"]}
for x in 1, 2, 3:
    print(x)


# %% {"tags": ["code-along"]}
x, y = 1, 2


# %% {"tags": ["code-along"]}
print(x, y)


# %% {"tags": ["code-along"]}
(1, 2, 3).index(2)


# %% {"tags": ["code-along"]}
(1, 2, 3, 1, 2, 1, 2).count(1)
