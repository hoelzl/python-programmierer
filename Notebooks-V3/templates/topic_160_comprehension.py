# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# %%


# j2 import 'macros.j2' as doc
# %% [markdown] {{ doc.slide() }}
# {{ doc.header (Listen-Komprehensione: Elegantere Iteration) }}


# %% [markdown]
#
# # Eleganter: Listen-Komprehension


# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# %%
my_list = [item + 1 for item in [1, 2, 3, 4]]
my_list


# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# %%
[f"Item {n}" for n in [1, 2, 3, 4]]


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
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]


# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result


# %%
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]


# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %%
[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitte "Filtern mit Listen-Komprehension"
#
