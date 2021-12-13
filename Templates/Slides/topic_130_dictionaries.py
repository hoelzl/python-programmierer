# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%

# j2 import 'macros.j2' as doc
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Dictionaries") }}


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


# %% tags=["code-along"]
sparse[0]


# %% tags=["code-along"]
# Fehler
# sparse[1]


# %% tags=["code-along"]
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


# %% tags=["code-along"]
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "Affe"))
print(translations.get("tree"))


# %% tags=["code-along"]
# Fehler:
# translations['monkey']
translations


# %% tags=["code-along"]
translations["horse"] = "Pferd"
translations["horse"]


# %% tags=["code-along"]
del translations["bird"]
print(translations.get("bird", "<unbekannt>"))
print(translations.setdefault("bird", "Vogel"))
print(translations.setdefault("bird", "<auch unbekannt>"))
print(translations.get("bird", "<unbekannt>"))


# %% tags=["code-along"]
for key in translations:
    print(key, end=" ")


# %% tags=["code-along"]
for key in translations.keys():
    print(key, end=" ")


# %% tags=["code-along"]
for val in translations.values():
    print(val, end=" ")


# %% tags=["code-along"]
for item in translations.items():
    print(item, end=" ")


# %% tags=["code-along"]
for key, val in translations.items():
    print("Key:", key, "\tValue:", val)


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_130_dictionaries`
#  - Abschnitt "Worthäufigkeiten"

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `042x-Workshop Todo-Liste V0`
#  - Abschnitt "TODO-Liste Version 0"
