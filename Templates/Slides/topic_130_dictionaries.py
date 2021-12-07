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


# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
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

# %% {{ doc.codealong() }}
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

# %% {{ doc.codealong() }}
sparse = {0: 1, 9: 1}


# %% {{ doc.codealong() }}
sparse


# %% {{ doc.codealong() }}
sparse[0]


# %%
# Fehler
# sparse[1]


# %% {{ doc.codealong() }}
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


# %% {{ doc.codealong() }}
print(translations["snake"])
print(translations.get("bat", "<unbekannt>"))
print(translations.get("monkey", "Affe"))
print(translations.get("tree"))


# %% {{ doc.codealong() }}
# Fehler:
# translations['monkey']
translations


# %% {{ doc.codealong() }}
translations["horse"] = "Pferd"
translations["horse"]


# %% {{ doc.codealong() }}
del translations["bird"]
print(translations.get("bird", "<unbekannt>"))
print(translations.setdefault("bird", "Vogel"))
print(translations.setdefault("bird", "<auch unbekannt>"))
print(translations.get("bird", "<unbekannt>"))


# %% {{ doc.codealong() }}
for key in translations:
    print(key, end=" ")


# %% {{ doc.codealong() }}
for key in translations.keys():
    print(key, end=" ")


# %% {{ doc.codealong() }}
for val in translations.values():
    print(val, end=" ")


# %% {{ doc.codealong() }}
for item in translations.items():
    print(item, end=" ")


# %% {{ doc.codealong() }}
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
