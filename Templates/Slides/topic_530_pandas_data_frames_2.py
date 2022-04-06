# %%
import numpy as np
import pandas as pd

# %% [markdown] {"lang": "de"}
# ## Fehlende Werte


# %% [markdown] {"lang": "en"}
# ## Missing Values

# %%
def create_data_frame_with_nans():
    return pd.DataFrame(
        {
            "A": [1, 2, np.nan, np.nan, 0],
            "B": [5, 6, 7, np.nan, 0],
            "C": [9, 10, 11, 12, 0],
            "D": [13, 14, 15, 16, 0],
            "E": [np.nan, 18, 19, 20, 0],
        }
    )


# %%
df = create_data_frame_with_nans()


# %%
df


# %% {"tags": ["code-along"]}
df.isna()


# %% {"tags": ["code-along"]}
df.count()


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.count(axis=1)


# %% {"tags": ["code-along"]}
df.isna().sum()


# %% {"tags": ["code-along"]}
df.isna().sum(axis=1)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.dropna()


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.dropna(axis=1, inplace=True)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df = create_data_frame_with_nans()
df


# %% {"tags": ["code-along"]}
df.fillna(value=1000)


# %% {"tags": ["code-along"]}
df.mean()

# %% {"tags": ["code-along"]}
df.fillna(value=df.mean())


# %% {"tags": ["code-along"]}
# df.fillna(value=df.mean(axis=1), axis=1)

# %% [markdown] {"lang": "de"}
# ## Gruppieren

# %% [markdown] {"lang": "en"}
# ## Grouping

# %%
def create_course_df():
    data = {
        "Course": [
            "Python",
            "Python",
            "Python",
            "Python",
            "Java",
            "Java",
            "Java",
            "C++",
            "C++",
        ],
        "Person": [
            "Jack",
            "Jill",
            "John",
            "Bill",
            "Jack",
            "Bill",
            "Davy",
            "Jack",
            "Diane",
        ],
        "Score": [97, 92, 38, 73, 81, 52, 62, 86, 98],
    }
    return pd.DataFrame(data)


# %% {"tags": ["code-along"]}
df = create_course_df()
df


# %% {"tags": ["code-along"]}
df.groupby("Course")


# %% {"tags": ["code-along"]}
df_by_course = df.groupby("Course")


# %% {"tags": ["code-along"]}
df_by_course.count()


# %% {"tags": ["code-along"]}
df_by_course["Person"].count()


# %% {"tags": ["code-along"]}
df_by_course.mean()


# %% {"tags": ["code-along"]}
df_by_course.std()


# %% {"tags": ["code-along"]}
df_by_course["Score"].aggregate(["mean", "std"])


# %% {"tags": ["code-along"]}
df_by_course.aggregate(["min", "max"])


# %% {"tags": ["code-along"]}
df_by_course["Score"].aggregate(["min", "max", "mean", "std"])


# %% {"tags": ["code-along"]}
df.groupby("Person").mean()


# %% {"tags": ["code-along"]}
df_by_course.describe()

# %% [markdown] {"lang": "de"}
# ## Operationen (Fortsetzung)

# %% [markdown] {"lang": "en"}
# ## Operations (Again)

# %% {"tags": ["code-along"]}
df = create_course_df()
df


# %% {"tags": ["code-along"]}
df.columns


# %% {"tags": ["code-along"]}
df.index


# %% {"tags": ["code-along"]}
df.sort_values(by="Course")


# %% {"tags": ["code-along"]}
df["Course"].values


# %% {"tags": ["code-along"]}
df["Person"].values


# %% {"tags": ["code-along"]}
df["Course"].unique()


# %% {"tags": ["code-along"]}
df["Person"].unique()


# %% {"tags": ["code-along"]}
df["Person"].nunique()


# %% {"tags": ["code-along"]}
df["Person"].value_counts()

# %% [markdown] {"lang": "de"}
# ## Auswahl

# %% [markdown] {"lang": "en"}
# ## Selection

# %% {"tags": ["code-along"]}
df[df["Score"] > 80]


# %% {"tags": ["code-along"]}
df[(df["Score"] > 60) & (df["Score"] <= 80)]

# %% [markdown] {"lang": "de"}
#
# ## Transformation von Daten

# %% [markdown] {"lang": "en"}
# ## Transforming Data

# %% {"tags": ["code-along"]}
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=["A", "B"])


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.apply(np.square)


# %% {"tags": ["code-along"]}
df.apply(np.sum)


# %% {"tags": ["code-along"]}
df.apply(np.sum, axis=1)


# %% {"tags": ["code-along"]}
df.apply(lambda n: [np.sum(n), np.mean(n)], axis=1)


# %% {"tags": ["code-along"]}
df.apply(lambda n: [np.sum(n), np.mean(n)], axis=1, result_type="expand")

# %% [markdown] {"lang": "de"}
# ## Elementweise Anwendung von Funktionen:

# %% [markdown] {"lang": "en"}
# ## Elementwise application of a function:

# %% {"tags": ["code-along"]}
df.applymap(lambda x: f"Value: {x}")


# %%
