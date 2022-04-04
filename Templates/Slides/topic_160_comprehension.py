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
# <div style="text-align:center; font-size:200%;"><b>Komprehensionen: Elegantere Iteration</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Comprehensions: More elegant iteration</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# # Eleganter: Listen-Komprehension


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # More elegant: list comprehension

# %%
result = []
for item in [1, 2, 3, 4]:
    result.append(item + 1)
result


# %% {"tags": ["code-along"]}
my_list = [item + 1 for item in [1, 2, 3, 4]]
my_list


# %% {"slideshow": {"slide_type": "subslide"}}
result = []
for n in [1, 2, 3, 4]:
    result.append(f"Item {n}")
result


# %% {"tags": ["code-along"]}
[f"Item {n}" for n in [1, 2, 3, 4]]


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitte "Quadratzahlen mit Listen-Komprehension"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Sections "Square numbers with list comprehension"

# %% {"slideshow": {"slide_type": "subslide"}}
result = []
for item in [1, 2, 3, 4, 5, 6]:
    if item % 2 == 0:
        result.append(item)
result


# %% {"tags": ["code-along"]}
[item for item in [1, 2, 3, 4, 5, 6] if item % 2 == 0]


# %% {"slideshow": {"slide_type": "subslide"}}
result = []
for item in ["abc", "def", "asd", "qwe", "bab"]:
    if item[0] == "a":
        result.append(item)
result


# %% {"tags": ["code-along"]}
[item for item in ["abc", "def", "asd", "qwe"] if item[0] == "a"]


# %% {"slideshow": {"slide_type": "subslide"}}
result = []
for list_1 in [[1, 2], ["a", "b", "c"]]:
    for item in list_1:
        result.append(f"Item {item} in {list_1}")
result


# %% {"tags": ["code-along"]}
[f"Item {item} in {list_1}" for list_1 in [[1, 2], ["a", "b", "c"]] for item in list_1]


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Abschnitte "Filtern mit Listen-Komprehension"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_100_lists_part2`
#  - Sections "Filtering with list comprehension"
