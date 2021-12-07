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
# # Tupel
#
# Tupel sind eine Datenstruktur, die sehr ähnlich zu Listen ist.
#
# Syntax:
#
# - Elemente durch Kommata getrennt: `1, 2, 3, 4`
# - In vielen Fällen müssen Tupel eingeklammert werden: `(1, 2, 3)`
#

# %%


# %%


# %%


# %%


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

# %%
values = 1, 2, 3
print(values + ("a", "b"))
print(values[1])
print("Length:", len(values))
values


# %%
for x in 1, 2, 3:
    print(x)


# %%
x, y = 1, 2


# %%
print(x, y)


# %%
def gehalt_und_bonus():
    return 40_000.0, 10_000.0


# %%
gehalt, bonus = gehalt_und_bonus()

# %%
print(gehalt)
print(bonus)
gehalt, bonus

# %%
(1, 2, 3).index(2)


# %%
(1, 2, 3, 1, 2, 1, 2).count(1)

