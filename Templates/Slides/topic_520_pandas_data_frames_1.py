# %% [markdown] {"lang": "de"}
# # Data Frames
#
# DataFrames sind die am häufigsten verwendete Datenstruktur in Pandas. Sie
# erlauben uns einfaches Lesen, Verarbeiten und Speichern von tabellenbasierten
# Daten.
#
# Konzeptionell besteht ein Datenrahmen aus mehreren Serieninstanzen, die sich
# einen gemeinsamen Index teilen.

# %% [markdown] {"lang": "en"}
# # Data Frames
#
# Data frames are the most commonly used Pandas data structure. They allow us to
# easily read, process and save table-based data
#
# Conceptually, a data frame consists of multiple series instances sharing a
# common index.

# %%
from pathlib import Path
import numpy as np
import pandas as pd


# %%
pandas_dir_path = Path(r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer\Data\Pandas")

# %% [markdown] {"lang": "de"}
# ## Erzeugen von Data Frames


# %% [markdown] {"lang": "en"}
# ## Creating Data Frames

# %% [markdown] {"lang": "de"}
# ### Aus einem NumPy Array

# %% [markdown] {"lang": "en"}
# ### From a NumPy Array

# %%
def create_data_frame():
    rng = np.random.default_rng(42)
    array = rng.normal(size=(5, 4), scale=5.0)
    index = "A B C D E".split()
    columns = "w x y z".split()
    return pd.DataFrame(array, index=index, columns=columns)


# %%
df = create_data_frame()
df


# %% {"tags": ["code-along"]}
type(df)

# %% [markdown] {"lang": "de"}
# ### Aus einer CSV Datei

# %% [markdown] {"lang": "en"}
# ### From a CSV File

# %% {"tags": ["code-along"]}
df_csv = pd.read_csv(pandas_dir_path / "example_data.csv")


# %% {"tags": ["code-along"]}
df_csv


# %% {"tags": ["code-along"]}
df_csv = pd.read_csv(pandas_dir_path / "example_data.csv", index_col=0)


# %% {"tags": ["code-along"]}
df_csv

# %% [markdown] {"lang": "de"}
# ### Aus einer Excel Datei

# %% [markdown] {"lang": "en"}
# ### From an Excel File

# %% {"tags": ["code-along"]}
df_excel = pd.read_excel(pandas_dir_path / "excel_data.xlsx", index_col=0)


# %% {"tags": ["code-along"]}
df_excel


# %% {"tags": ["code-along"]}
df_excel2 = pd.read_excel(pandas_dir_path / "excel_other_sheet.xlsx", index_col=0)


# %% {"tags": ["code-along"]}
df_excel2


# %% {"tags": ["code-along"]}
df_excel2 = pd.read_excel(
    pandas_dir_path / "excel_other_sheet.xlsx",
    index_col=0,
    sheet_name="Another Sheet",
    header=0,
    skiprows=[1]
)


# %% {"tags": ["code-along"]}
df_excel2.head()

# %% [markdown] {"lang": "de"}
#
# ### Andere Formate:
#
# - `pd.read_clipboard`
# - `pd.read_html`
# - `pd.read_json`
# - `pd.read_pickle`
# - `pd.read_sql` (verwendet SQLAlchemy um auf die Datenbank zuzugreifen)
# - ...

# %% [markdown] {"lang": "en"}
#
# ### Other Formats:
#
# - `pd.read_clipboard`
# - `pd.read_html`
# - `pd.read_json`
# - `pd.read_pickle`
# - `pd.read_sql` (uses SQLAlchemy to access a database)
# - ...

# %% [markdown] {"lang": "de"}
# ### Indizes und Operationen

# %% [markdown] {"lang": "en"}
# ### Indices and Operations

# %% {"tags": ["code-along"]}
df_csv.head()


# %% {"tags": ["code-along"]}
df_csv.tail()


# %% {"tags": ["code-along"]}
df = create_data_frame()
df["w"]


# %% {"tags": ["code-along"]}
type(df["w"])


# %% {"tags": ["code-along"]}
# Use only interactively
df.w


# %% {"tags": ["code-along"]}
df[["w", "y"]]


# %% {"tags": ["code-along"]}
df.index


# %% {"tags": ["code-along"]}
df.index.is_monotonic_increasing


# %% {"tags": ["code-along"]}
df.size


# %% {"tags": ["code-along"]}
df.ndim


# %% {"tags": ["code-along"]}
df.shape

# %% [markdown] {"lang": "de"}
# ### Erzeugen, Umbenennen und Löschen von Spalten

# %% [markdown] {"lang": "en"}
# ### Creating, renaming, deleting columns

# %% {"tags": ["code-along"]}
df = create_data_frame()
df["Sum of w and y"] = df["w"] + df["y"]


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.rename(columns={"Sum of w and y": "w + y"})


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.rename(columns={"Sum of w and y": "w + y"}, index={"E": "Z"}, inplace=True)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
type(df["y"])


# %% {"tags": ["code-along"]}
del df["y"]


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.drop("A")


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.drop("B", inplace=True)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.drop("z", axis=1)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.drop("z", axis=1, inplace=True)


# %% {"tags": ["code-along"]}
df

# %% [markdown] {"lang": "de"}
# ## Auswahl

# %% [markdown] {"lang": "en"}
# ## Selection

# %% {"tags": ["code-along"]}
df = create_data_frame()
df


# %% {"tags": ["code-along"]}
df["w"]


# %% {"tags": ["code-along"]}
# Error!
# df['A']


# %% {"tags": ["code-along"]}
df.loc["B"]


# %% {"tags": ["code-along"]}
type(df.loc["B"])


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.iloc[1]


# %% {"tags": ["code-along"]}
df.loc[["A", "C"]]


# %% {"tags": ["code-along"]}
df.loc[["A", "C"], ["x", "y"]]


# %% {"tags": ["code-along"]}
df.loc["B", "z"]


# %% {"tags": ["code-along"]}
df.iloc[[1, 2], [0, 3]]


# %% {"tags": ["code-along"]}
df.iloc[0, 0]

# %% [markdown] {"lang": "de"}
# ## Bedingte Auswahl

# %% [markdown] {"lang": "en"}
# ## Conditional Selection

# %% {"tags": ["code-along"]}
df = create_data_frame()
df


# %% {"tags": ["code-along"]}
df > 0  # noqa


# %% {"tags": ["code-along"]}
df[df > 0]


# %% {"tags": ["code-along"]}
df["w"] > 0  # noqa


# %% {"tags": ["code-along"]}
df[df["w"] > 0]


# %% {"tags": ["code-along"]}
df[df["w"] > 0][["x", "y"]]


# %% {"tags": ["code-along"]}
df[(df["w"] > 0) & (df["x"] < 0)]

# %% [markdown] {"lang": "de"}
#
# # Information über Data Frames

# %% [markdown] {"lang": "en"}
#
# # Information about Data Frames

# %% {"tags": ["code-along"]}
df = create_data_frame()
df["txt"] = "a b c d e".split()
df.iloc[1, 1] = np.nan
df


# %% {"tags": ["code-along"]}
df.describe()


# %% {"tags": ["code-along"]}
df.info()


# %% {"tags": ["code-along"]}
df.dtypes

# %% [markdown] {"lang": "de"}
# ## Der Index eines Data Frames

# %% [markdown] {"lang": "en"}
# ## Data Frame Index

# %% {"tags": ["code-along"]}
df = create_data_frame()
df["txt"] = "a b c d e".split()
df


# %% {"tags": ["code-along"]}
df.reset_index()


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.reset_index(inplace=True)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.rename(columns={"index": "old_index"}, inplace=True)


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.set_index("txt")


# %% {"tags": ["code-along"]}
df


# %% {"tags": ["code-along"]}
df.set_index("txt", inplace=True)
df


# %% {"tags": ["code-along"]}
df.set_index("old_index", inplace=True)
df


# %% {"tags": ["code-along"]}
df.info()


# %% {"tags": ["code-along"]}
df.index


# %% {"tags": ["code-along"]}
df.index.name = None


# %% {"tags": ["code-along"]}
df


# %%
