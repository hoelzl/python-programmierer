# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Erste Schritte mit Python</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Getting Started with Python</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Einführung
#
# - Ausführung von Python Code
# - Notebooks und Entwicklungsumgebungen
# - Umgang mit Notebooks

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Introduction
#
# - Executing Python Code
# - Notebooks and development environments (IDEs)
# - Working with notebooks

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Python Interpreter und Jupyter Notebooks
#
# Wir beginnen mit einer kurzen Einführung in die Arbeitsweise von Python und
# Jupyter Notebooks.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# # Python and Jupyter notebooks
#
# We'll start with a brief introduction:
# - How does Python work?
# - What are Jupyter notebooks?

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>
#

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% {"slideshow": {"slide_type": "subslide"}}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Entwicklungsumgebungen
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interaktive Shell

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Development Environments
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interactive shell

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Arbeiten mit Notebooks
#
# - Kommando- und Edit-Modus
# - Einige Tastaturkürzel

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Working with notebooks
#
# - Command and edit mode
# - Some keyboard shortcuts

# %%
