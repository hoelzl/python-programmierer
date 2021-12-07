# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---


# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Dictionaries</h1>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown]
#
#  ## Dictionaries
#
#  Indizes in Listen
#
#  - können nur Integer-Werte sein
#  - müssen ein Intervall von 0 bis `len(liste) - 1` umfassen
#
#  Elemente in einer Liste sind sortiert.

# %%
non_sparse = [0] * 10
non_sparse[0] = 1
non_sparse[9] = 1
non_sparse


# %% [markdown]
#
#  Dictionaries sind eine Datenstruktur, in der Indizes
#
#  - viele verschiedene Typen haben können:
#    - Integer-Werte
#    - Strings
#    - Tupel
#    - ...
#
#  Im Gegensatz zu Listen sind die Elemente in einem Dictionary nicht in einer
#  bestimmten Reihenfolge angeordnet.

# %%
sparse = {0: 1, 9: 1}


# %%
sparse


# %%
sparse[0]


# %%
# Fehler
# sparse[1]


# %%
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


# %%
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "Affe"))
print(translations.get("tree"))


# %%
# Fehler:
# translations['monkey']
translations


# %%
translations["horse"] = "Pferd"
translations["horse"]


# %%
del translations["bird"]
print(translations.get("bird", "<unbekannt>"))
print(translations.setdefault("bird", "Vogel"))
print(translations.setdefault("bird", "<auch unbekannt>"))
print(translations.get("bird", "<unbekannt>"))


# %%
for key in translations:
    print(key, end=" ")


# %%
for key in translations.keys():
    print(key, end=" ")


# %%
for val in translations.values():
    print(val, end=" ")


# %%
for item in translations.items():
    print(item, end=" ")


# %%
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `040x-Workshop Dictionaries`
#  - Abschnitt "Worthäufigkeiten"

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `042x-Workshop Todo-Liste V0`
#  - Abschnitt "TODO-Liste Version 0"