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
# <div style="text-align:center; font-size:200%;"><b>Pickling</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Pickling</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de"}
#
# ## Pickles
#
# Das `pickle` Modul bietet die Möglichkeit, Python Objekte einfach zu speichern
# und zu laden.

# %% [markdown] {"lang": "en"}
# ## Pickle
#
# The `pickle` module provides a way to easily store and load Python objects.

# %% {"tags": ["code-along"]}
import pickle
from pprint import pprint

# %% {"tags": ["code-along"]}
my_list = [1, 2, 3, 4]
my_other_list = [3, 4, 5]
my_dict = {1: my_list, 2: my_other_list, 3: "a string", 4: ["some list"]}


# %% {"tags": ["code-along"]}
pprint(my_dict)


# %% {"tags": ["code-along"]}
my_pickle = pickle.dumps(my_dict)
pprint(my_pickle)

# %% {"tags": ["code-along"]}
restored_pickle = pickle.loads(my_pickle)

# %% {"tags": ["code-along"]}
pprint(restored_pickle)

# %% {"tags": ["code-along"]}
my_dict == restored_pickle

# %%
my_dict is restored_pickle

# %%
my_list.append(my_other_list)
my_other_list.append(my_list)

# %%
pprint(my_list)


# %%
pprint(my_dict)

# %%
my_pickle = pickle.dumps(my_dict)
restored_pickle = pickle.loads(my_pickle)

# %%
pprint(restored_pickle)

# %%
# Don't try this...
# my_dict == restored_pickle
