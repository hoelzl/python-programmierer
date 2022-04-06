# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# %% [markdown] lang="de"
# # Hauspreise in Californien

# %% [markdown] lang="en"
# # California Housing Prices

# %%
from pathlib import Path
import pandas as pd

# %%
pandas_data_path = Path(r"C:\Users\tc\Programming\Python\Courses\Own\python-programmierer\Data\Pandas")
california_housing_csv_path = pandas_data_path / "california-housing.csv"

# %% [markdown] lang="de"
# ## Laden des Datensatzes
#
# Laden Sie die CSV-Datei `california_housing_csv_path` als 
# Pandas DataFrame. Importieren Sie dabei keine
# Spalten ohne Informationsgehalt.

# %% [markdown] lang="en"
# ## Loading the data set
#
# Load the csv file `california_housing_csv_path` as
# pandas DataFrame. Do not import any columns without information content.

# %% tags=["solution"]
df = pd.read_csv(california_housing_csv_path, index_col=0)

# %% tags=["solution"]
df


# %% [markdown] lang="de"
# Wie viele Zeilen hat der DataFrame?

# %% [markdown] lang="en"
# How many rows does the DataFrame have?

# %% tags=["solution"]
len(df)


# %% [markdown] lang="de"
# Welche Spalten hat der DataFrame? 
# Gibt es Spalten im DataFrame die undefinierte Werte (NA) enthalten?

# %% [markdown] lang="en"
# Which columns does the DataFrame have?
# Are there columns in the DataFrame that contain undefined values ​​(NA)?

# %% tags=["solution"]
df.columns

# %%
# This is true if `notna()` drops rows, i.e., if 
df.isna().sum()


# %% [markdown] lang="de"
#
# Was sind Minimum, Maximum, Mittelwert und
# Standardabweichung der einzelnen Spalten?

# %% [markdown] lang="en"
# What are minimum, maximum, mean and standard deviation of each column?

# %% tags=["solution"]
df.describe()

# %% [markdown] lang="de"
# Erzeugen Sie Histogramme der einzelnen Spalten.
# Welche Auffälligkeiten gibt es dabei?

# %% [markdown] lang="en"
# Generate histograms of the individual columns.
# Are there any features that stick out?

# %% tags=["solution"]
df.hist(bins=30, figsize=(12, 8))

# %% [markdown] lang="de"
#
# Erzeugen Sie einen neuen DataFrame, der nur die Zeilen enthält, deren `Target`
# Wert größer als 4 ist. Wie viele einträge hat dieser DataFrame?

# %% [markdown] lang="en"
# Create a new DataFrame containing only the rows whose `Target`
# value is greater than 4. How many entries does this DataFrame have?

# %% tags=["solution"]
df_expensive = df[df["Target"] > 4]

# %% tags=["solution"]
df_expensive


# %% [markdown] lang="de"
#
# Plotten Sie Longitude vs. Latitude als Scatterplot. Was können Sie aus diesem
# Plot ablesen?
#
# Mit dem Keyword-Argument `c` können Sie einen Spaltennamen angeben, deren
# Werte die Farbe der Ausgabe bestimmen. Mit `cmap` können Sie eine Colormap
# dafür angeben. Mit dem Keyword-Argument `alpha` können Sie die Transparenz der
# Ausgabe steuern.
#
# Experimentieren Sie mit diesen Werten um die Ausgabe informativer zu
# gestalten.

# %% [markdown] lang="en"
# Plot longitude vs. latitude as a scatterplot. What can you infer from this
# plot?
#
# The `c` keyword argument allows you to specify a column name whose
# values determine the color of the output. With `cmap` you can create a colormap
# for these colors. With the keyword argument `alpha` you can set the transparency of the output.
#
# Experiment with these values to make the output more informative.

# %% tags=["solution"]
df.plot(
    kind="scatter",
    x="Longitude",
    y="Latitude",
    figsize=(10, 8),
    alpha=0.4,
    c="Target",
    cmap="hot",
)

# %% [markdown] lang="de"
# Wie sieht die entsprechende Ausgabe für den DataFrame aus, der nur
# teure Häuser enthält?


# %% [markdown] lang="en"
# What does the corresponding output look like for the DataFrame that only
# contains expensive houses?

# %% tags=["solution"]
df_expensive.plot(
    kind="scatter",
    x="Longitude",
    y="Latitude",
    figsize=(10, 8),
    alpha=0.4,
    c="Target",
    cmap="hot",
)


# %% [markdown] lang="de"
#
# Falls Sie Seaborn installiert haben können Sie mit `seaborn.pairplot()` ein
# Grid mit Scatterplots aus allen möglichen Kombinationen von Spalten erzeugen.
# Mit dem Keyword-Argument `hue` können Sie dabei eine Spalte angeben, die die
# Farbe der Ausgabe bestimmt.
#
# Welche der Plots liefern interessante Informationen? Welche Werte sind für
# `hue` interessant?
#
# *Hinweis:* Es empfiehlt sich, die Anzahl der Werte auf z.B. 500 oder 1000 zu
# beschränken um die Zeit, die die Erzeugung der Plots dauert in Grenzen zu
# halten.

# %% [markdown] lang="en"
# If you have installed seaborn you can use `seaborn.pairplot()` to
# create a grid of scatterplots with all possible combinations of columns.
# With the keyword argument `hue` you can specify a column that contains the
# color of the output.
#
# Which of the plots provide interesting information? What values might be interesting as value of `hue`?
#
# *Note:* It is advisable to decrease the number of rows being plotted to e.g. 500 or 1000 to limit the time it takes to generate the plots.

# %% tags=["solution"]
import seaborn as sns
sns.pairplot(df.iloc[:500])

# %% tags=["solution"]
sns.pairplot(df.iloc[:500], hue="Target")


# %% tags=["solution"]
sns.pairplot(df.iloc[:500], hue="MedInc")

# %% tags=["solution"]
sns.pairplot(df_expensive)
