# %% [markdown] {"lang": "de"}
#
# # Pandas Typ `Series`
#
# Eine Pandas `Series` Instanz stellt eine Folge von Werten dar, ähnlich wie
# eine Python-Liste. Die Elemente einer Serie können über ihren numerischen
# Index abgerufen werden, aber zusätzlich kann eine Serie einen semantisch
# sinnvollen Index haben (z. B. für Zeitreihen).
#
# Intern wird eine Pandas-Serie durch ein Numpy-Array unterstützt, daher sind
# die meisten der Numpy-Operationen auch auf Serien anwendbar sind.
#
# Darüber hinaus ist es einfach (und billig), Serien nach Numpy zu konvertieren.

# %% [markdown] {"lang": "en"}
#
# # Pandas Type `Series`
#
# A series represents a sequence of values, similar to a Python list. Elements
# of their series can be retrieved by their numerical index, but in addition a
# series can have a semantically meaningful index (e.g., for time series).
#
# Internally, a Pandas series is backed by a numpy array, therefore most of the
# numpy operations are applicable to series as well.
#
# In addition it is easy (and cheap) to convert series to numpy.

# %%
import numpy as np
import pandas as pd

# %% [markdown] {"lang": "de"}
# ## Erzeugung
#
# ### Aus Listen

# %% [markdown] {"lang": "en"}
# ## Creation
#
# ### From Lists

# %% {"tags": ["code-along"]}
pd.Series(data=[10, 20, 30, 40])


# %% {"tags": ["code-along"]}
pd.Series(["a", "b", "c"])

# %% [markdown] {"lang": "de"}
# ### Aus Listen mit Index

# %% [markdown] {"lang": "en"}
# ### From Lists with Index

# %% {"tags": ["code-along"]}
pd.Series(data=[1, 2, 3, 4], index=["w", "x", "y", "z"])

# %% [markdown] {"lang": "de"}
# ### Aus Range oder Iterable

# %% [markdown] {"lang": "en"}
# ### From Range or Other Iterable

# %% {"tags": ["code-along"]}
pd.Series(data=range(1, 201, 2))

# %% {"tags": ["code-along"]}
data = pd.Series(data=range(1, 201, 2))
data.head()

# %% {"tags": ["code-along"]}
data.tail()

# %% [markdown] {"lang": "de"}
# ### Aus Dictionary

# %% [markdown] {"lang": "en"}
# ### From Dictionary

# %% {"tags": ["code-along"]}
pd.Series(data={"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})

# %% [markdown] {"lang": "de"}
# ## Indizes und Operationen

# %% [markdown] {"lang": "en"}
# ## Indices and Operations

# %%
food1 = pd.Series({"Ice Cream": 2.49, "Cake": 4.99, "Fudge": 7.99})
food2 = pd.Series({"Cake": 4.99, "Ice Cream": 3.99, "Pie": 3.49, "Cheese": 1.99})


# %% {"tags": ["code-along"]}
food1


# %% {"tags": ["code-along"]}
food1.index


# %% {"tags": ["code-along"]}
food1.size


# %% {"tags": ["code-along"]}
food1.sum()


# %% {"tags": ["code-along"]}
food1.mean()


# %% {"tags": ["code-along"]}
food1.name


# %% {"tags": ["code-along"]}
food1.name = "Deserts"


# %% {"tags": ["code-along"]}
food1.name


# %% {"tags": ["code-along"]}
food1


# %% {"tags": ["code-along"]}
food1.plot.bar(legend=True)


# %% {"tags": ["code-along"]}
import random
data = pd.Series(data=[random.gauss(0.0, 10.0) for _ in range(2_000)])
data.plot.hist(legend=False, bins=20)


# %% {"tags": ["code-along"]}
food1["Cake"]


# %% {"tags": ["code-along"]}
food1.loc["Cake"]


# %% {"tags": ["code-along"]}
# Error!
# food1["Pie"]


# %% {"tags": ["code-along"]}
food1.argmin()


# %% {"tags": ["code-along"]}
food1[0]


# %% {"tags": ["code-along"]}
food1.iloc[0]


# %% {"tags": ["code-along"]}
confusing = pd.Series(data=np.linspace(0, 5, 11), index=np.arange(-5, 6))
confusing


# %% {"tags": ["code-along"]}
confusing[0]


# %% {"tags": ["code-along"]}
confusing.loc[0]


# %% {"tags": ["code-along"]}
confusing.iloc[0]


# %% {"tags": ["code-along"]}
food_sum = food1 + food2
food_sum


# %% {"tags": ["code-along"]}
food1 + 0.5


# %% {"tags": ["code-along"]}
food1


# %% {"tags": ["code-along"]}
def discount(price):
    return price * 0.9

food1.apply(discount)


# %% {"tags": ["code-along"]}
food1


# %% {"tags": ["code-along"]}
food1.apply(lambda price: price * 0.9)


# %% {"tags": ["code-along"]}
pd.concat([food1, pd.Series({"Chocolate": 3.99, "Ice Cream": 1.99})])


# %% {"tags": ["code-along"]}
food1


# %% {"tags": ["code-along"]}
all_food = pd.concat([food1, food2])


# %% {"tags": ["code-along"]}
all_food

# %% [markdown] {"lang": "de"}
# ### Mehrfach vorkommende Index-Werte

# %% [markdown] {"lang": "en"}
# ### Multiple index values

# %% {"tags": ["code-along"]}
all_food.index


# %% {"tags": ["code-along"]}
all_food.is_unique


# %% {"tags": ["code-along"]}
food1.is_unique


# %% {"tags": ["code-along"]}
all_food["Cake"]


# %% {"tags": ["code-along"]}
type(all_food["Cake"])


# %% {"tags": ["code-along"]}
all_food["Pie"]


# %%
type(all_food["Pie"])


# %% {"tags": ["code-along"]}
all_food.groupby(all_food.index).max()

# %% [markdown] {"lang": "de"}
# ### Sortierte und unsortierte Indizes

# %% [markdown] {"lang": "en"}
# ### Sorted and unsorted Indices

# %% {"tags": ["code-along"]}
all_food.index.is_monotonic_increasing


# %% {"tags": ["code-along"]}
sorted_food = all_food.sort_index()


# %% {"tags": ["code-along"]}
sorted_food


# %% {"tags": ["code-along"]}
sorted_food.index.is_monotonic_increasing


# %% {"tags": ["code-along"]}
all_food.sort_values()


# %% {"tags": ["code-along"]}
all_food.sort_values().is_monotonic_increasing


# %% {"tags": ["code-along"]}
all_food[["Pie", "Cake"]]


# %% {"tags": ["code-along"]}
all_food


# %% {"tags": ["code-along"]}
all_food[1:3]


# %%
# all_food['Cake':'Fudge']


# %% {"tags": ["code-along"]}
sorted_food["Cake":"Fudge"]

# %% [markdown] {"lang": "de"}
#
# **Wichtig:** Der ober Wert der Slice, `"Fudge"` ist im Resultat enthalten!

# %% [markdown] {"lang": "en"}
#
# **Important:** The upper value of the slice, `"Fudge"` is contained in the
# result!

# %% [markdown] {"lang": "de"}
# ## Fehlende Werte

# %% [markdown] {"lang": "en"}
# ## Missing Values

# %% {"tags": ["code-along"]}
food = food1 + food2


# %% {"tags": ["code-along"]}
food.isna()


# %% {"tags": ["code-along"]}
food.isna().sum()


# %% {"tags": ["code-along"]}
food.dropna()

# %%
