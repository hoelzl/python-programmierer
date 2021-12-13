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
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Tupel") }}

# %% [markdown]
# # Tupel
#
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
#
# Syntax:
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`
#

# %% tags=["code-along"]
1, 2, 3


# %% tags=["code-along"]
non_tuple = 1
print(non_tuple)
type(non_tuple)

# %% tags=["code-along"]
singleton_tuple = (1,)
print(singleton_tuple)
type(singleton_tuple)


# %% tags=["code-along"]
x = "a", 1, True


# %% tags=["code-along"]
type(x)


# %% [markdown]
#
#  ## Eigenschaften von Tupeln
#
#  - Tupel können beliebige Python-Werte speichern
#  - Elemente in einem Tupel haben eine feste Reihenfolge
#  - Auf Elemente eines Tupels kann mit einem Index zugegriffen werden
#  - Tupel können *nicht* modifiziert werden
#
#  Oft werden Tupel zum Speichern *heterogener* Daten verwendet.

# %% [markdown]
#
#  ## Operationen auf Tupeln
#
#  - Viele der Operationen auf Listen lassen sich auf Tupel anwenden.
#  - Die Operationen, die Listen verändern sind nicht anwendbar.

# %% tags=["code-along"]
values = 1, 2, 3
print(values + ("a", "b"))
print(values[1])
print("Length:", len(values))
values


# %% tags=["code-along"]
for x in 1, 2, 3:
    print(x)


# %% tags=["code-along"]
x, y = 1, 2


# %% tags=["code-along"]
print(x, y)


# %% tags=["code-along"]
(1, 2, 3).index(2)


# %% tags=["code-along"]
(1, 2, 3, 1, 2, 1, 2).count(1)
