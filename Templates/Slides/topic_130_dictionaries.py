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
# <div style="text-align:center; font-size:200%;"><b>Dictionaries</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Dictionaries</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Dictionaries
#
#  Indizes in Listen
#
#  - können nur Integer-Werte sein
#  - müssen ein Intervall von 0 bis `len(liste) - 1` umfassen
#
#  Elemente in einer Liste sind sortiert.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Dictionaries
#
# Indices in lists
#
# - can only be integer values
# - must span an interval from 0 to `len(list) - 1`
#
# Items in a list are sorted.

# %%
non_sparse = [0] * 10
non_sparse[0] = 1
non_sparse[9] = 1
non_sparse


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# Dictionaries sind eine Datenstruktur, in der Indizes
#
# - viele verschiedene Typen haben können:
#   - Integer-Werte
#   - Strings
#   - Tupel
#   - ...
#
# Im Gegensatz zu Listen sind die Elemente in einem Dictionary nicht in einer
# bestimmten Reihenfolge angeordnet.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Dictionaries are a data structure whose indidex values
#
#  - can be of many different types:
#    - integer values
#    - Strings
#    - Tuple
#    - ...
#
# Unlike lists, the elements in a dictionary are not arranged in a specific order.

# %% {"slideshow": {"slide_type": "subslide"}}
sparse = {0: 1, 9: 1}


# %%
sparse


# %% {"tags": ["code-along"]}
sparse[0]


# %% {"tags": ["code-along"]}
# Fehler
# sparse[1]


# %% {"tags": ["code-along"]}
sparse[12] = 3
print(sparse[12])
sparse


# %%
translations = {
    "snake": "Schlange",
    "bat": "Fledermaus",
    "horse": "Hose",
    "bird": "Vogel",
}


# %% {"tags": ["code-along"]}
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "Affe"))
print(translations.get("tree"))


# %% {"tags": ["code-along"]}
# Fehler:
# translations['monkey']
translations


# %% {"tags": ["code-along"]}
translations["horse"] = "Pferd"
translations["horse"]


# %% {"tags": ["code-along"]}
del translations["bird"]
print(translations.get("bird", "<unbekannt>"))
print(translations.setdefault("bird", "Vogel"))
print(translations.setdefault("bird", "<auch unbekannt>"))
print(translations.get("bird", "<unbekannt>"))


# %% {"tags": ["code-along"]}
for key in translations:
    print(key, end=" ")


# %% {"tags": ["code-along"]}
for key in translations.keys():
    print(key, end=" ")


# %% {"tags": ["code-along"]}
for val in translations.values():
    print(val, end=" ")


# %% {"tags": ["code-along"]}
for item in translations.items():
    print(item, end=" ")


# %% {"tags": ["code-along"]}
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_130_dictionaries`
#  - Abschnitt "Worthäufigkeiten"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_130_dictionaries`
# - Section "Word frequencies"

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Mini-Workshop
#
#  - Notebook `042x-Workshop Todo-Liste V0`
#  - Abschnitt "TODO-Liste Version 0"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `042x workshop todo list V0`
#  - Section "TODO list version 0"
