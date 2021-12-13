# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Pickling") }}

# %% [markdown]
#
# ## Pickles
#
# Das `pickle` Modul bietet die Möglichkeit, Python Objekte einfach zu speichern
# und zu laden.

# %% tags=["code-along"]
import pickle
from pprint import pprint

# %% tags=["code-along"]
my_list = [1, 2, 3, 4]
my_other_list = [3, 4, 5]
my_dict = {1: my_list, 2: my_other_list, 3: "a string", 4: ["some list"]}


# %% tags=["code-along"]
pprint(my_dict)


# %% tags=["code-along"]
my_pickle = pickle.dumps(my_dict)
pprint(my_pickle)

# %% tags=["code-along"]
restored_pickle = pickle.loads(my_pickle)

# %% tags=["code-along"]
pprint(restored_pickle)

# %% tags=["code-along"]
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
