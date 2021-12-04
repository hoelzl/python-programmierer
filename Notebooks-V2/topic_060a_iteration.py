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

# %% [markdown]
# # Iteration über Listen
#
# Zur Iteration über Listen (und andere Datenstrukturen) bietet Python die
# bereits besprochene`for`-Schleife:
#

# %%
my_list = [1, 2, 3, 4]
for n in my_list:
    print(f"Item {n}")

# %%
index = 0
while index < len(my_list):
    n = my_list[index]
    print(f"Item {n}")
    index += 1

# %% [markdown]
#
#  ## Iteration über Listen von Listen

# %%
a, b = [1, 2]
print(a)
print(b)

# %%
my_list = [[1, 2], [3, 4], [5, 6]]

# %%
for m, n in my_list:
    print(f"Items {m} and {n}")

# %%
index = 0
while index < len(my_list):
    m, n = my_list[index]
    print(f"Items {m} and {n}")
    index += 1

# %% [markdown]
#
#  # Nochmal Finden von Elementen
#
#  Bei unserer bisherigen Version von `find` muss die Liste zweimal durchlaufen
#  werden:
#
#  - Einmal von `in` um zu testen, ob das gesuchte Element in der Liste vorkommt
#  - Einmal von `index` um den Index zu finden.
#
#  Schöner wäre es, wenn wir das in einem Durchlauf erledigen könnten.

# %%
my_list = ["a", "b", "c", "d", "e"]
enumerate(my_list)

# %%
list(enumerate(my_list))

# %%
for index, element in enumerate(my_list):
    print(f"index = {index}, element = {element}")

# %%

# %%
my_list = ["a", "b", "c", "d", "a"]

# %%

# %%

# %%

# %%
# Mit assert können Invarianten dokumentiert werden:
assert find("a", my_list) == find_return("a", my_list)
assert find("d", my_list) == find_return("d", my_list)
assert find("x", my_list) == find_return("x", my_list)

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Finden in Listen"
#

# %% [markdown]
#
#  ## Aggregation von Listenelementen

# %%

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Mittelwert einer Liste"

# %% [markdown]
#
#  ## Transformation von Listen

# %%

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Quadratzahlen"
#
#  # Filtern von Listen

# %%

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Filtern"
#
