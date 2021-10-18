# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <h1 style="text-align:center;">Python Quickstart</h1>
# <h2 style="text-align:center;">Coding Akademie München GmbH</h2>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Python und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und
# Jypyter Notebooks.

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Variablen und Datentypen
#
# Zahlen und Arithmetik:

# %%

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Zeichenketten

# %%

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Variablen

# %%

# %%


# %% [markdown] slideshow={"slide_type": "slide"}
# ## Jupyter Notebooks: Anzeige von Werten
#
# - Jupyter Notebooks geben den letzten Wert jeder Zelle auf dem Bildschirm aus
# - Das passiert in "normalen" Python-Programmen nicht!
#   - Wenn sie als Programme ausgeführt werden
#   - Der interaktive Interpreter verhält sich ähnlich wie Notebooks

# %% slideshow={"slide_type": "subslide"}

# %% [markdown]
# Um die Ausgabe des letzten Wertes einer Zeile in Jupyter zu unterbinden kann man
# die Zeile mit einem Strichpunkt beenden:

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# Jupyter zeigt auch den Wert von Variablen an:

# %%

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# Um mehrere Werte anzuzeigen kann man die `print()`-Funktion verwenden:
#
# `print(...)` gibt den in Klammern eingeschlossenen Text auf dem Bildschirm aus.

# %%

# %%

# %%

# %%


# %% slideshow={"slide_type": "subslide"}


# %% [markdown]
# Vergleichen Sie die Ausgabe mit der folgenden Zelle:

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Typen

# %%

# %%

# %%


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Vordefinierte Funktionen

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Funktionen

# %%


# %%

# %%

# %%


# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `greeting(name)`, die eine Begrüßung in der Form
# "Hallo *name*!" auf dem Bildschirm ausgibt, z.B.
# ```python
# >>> greeting("Max")
# Hallo Max!
# >>>
# ```

# %%


# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Methoden

# %%

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Mehrere Parameter, Default Argumente

# %%


# %%


# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Verschachtelte Funktionsaufrufe

# %%


# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Typannotationen

# %%


# %%

# %%
# Typannotationen dienen lediglich zur Dokumentation und werden von Python
# ignoriert:

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Listen und Tupel

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Boole'sche Werte und `if`-Anweisungen

# %%

# %%

# %%

# %%

# %% slideshow={"slide_type": "subslide"}


# %% slideshow={"slide_type": "subslide"}

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `fits_in_line(text: str, line_length: int = 72)`,
# die `True` oder `False` zurückgibt, je nachdem ob `text` in einer Zeile der
# Länge `line_length` ausgegeben werden kann oder nicht:
# ```python
# >>> fits_in_line("Hallo")
# True
# >>> fits_in_line("Hallo", 3)
# False
# >>>
# ```
#
# Schreiben Sie eine Funktion `print_line(text: str, line_length:int = 72)`,
# die
# * `text` auf dem Bildschirm ausgibt, falls das in einer Zeile der Länge `line_length` möglich ist
# * `...` ausgibt, falls das nicht möglich ist.
# ```python
# >>> print_line("Hallo")
# Hallo
# >>> print_line("Hallo", 3)
# ...
# >>>
# ```

# %%


# %%

# %%

# %%

# %%

# %%


# %% [markdown] slideshow={"slide_type": "subslide"}
# ## `for`-Schleifen

# %% slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `print_all(items: list)`, die die Elemente der
# Liste `items` auf dem Bildschirm ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_all([1, 2, 3])
# 1
# 2
# 3
# >>>
# ```
# Was passiert, wenn Sie die Funktion mit einem String als Argument aufrufen,
# z.B. `print_all("abc")`

# %%

# %%

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Micro-Workshop
#
# Schreiben Sie eine Funktion `print_squares(n: int)`, die die Quadrate der
# Zahlen von 1 bis n ausgibt, jeweils ein Element pro Zeile:
#
# ```python
# >>> print_square(3)
# 1**2 = 1
# 2**2 = 4
# 3**2 = 9
# >>>
# ```

# %%

# %%

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Dictionaries

# %%

# %%

# %%
# Fehler:
# translations['monkey']

# %% slideshow={"slide_type": "subslide"}

# %% slideshow={"slide_type": "subslide"}

# %% slideshow={"slide_type": "subslide"}

# %%

# %% slideshow={"slide_type": "subslide"}

# %%

# %%
