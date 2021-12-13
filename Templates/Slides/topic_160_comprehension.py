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
# {{ doc.header("Listen-Komprehensionen: Elegantere Iteration") }}


# %% [markdown]
#
# # Eleganter: Listen-Komprehension


# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# %% tags=["code-along"]
my_list = [item + 1 for item in [1, 2, 3, 4]]
my_list


# %%
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# %% tags=["code-along"]
[f"Item {n}" for n in [1, 2, 3, 4]]


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitte "Quadratzahlen mit Listen-Komprehension"
#

# %%
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# %% tags=["code-along"]
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]


# %%
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result


# %% tags=["code-along"]
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]


# %%
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %% tags=["code-along"]
[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitte "Filtern mit Listen-Komprehension"
#
