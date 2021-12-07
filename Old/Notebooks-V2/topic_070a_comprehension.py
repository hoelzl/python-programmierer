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
# # Eleganter: Listen-Komprehension
#

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result

# %%

# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitte "Quadratzahlen mit Listen-Komprehension"
#

# %%
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result

# %%

# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result

# %%

# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result

# %%

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitte "Filtern mit Listen-Komprehension"
#
