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
# <div style="text-align:center; font-size:200%;"><b>Setuptools und Installation</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Setuptools and installation</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  # Setuptools: Distribution von Python Packeten
#
#  - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.
#  - Das Wort "Packages" ist in der Python Welt überladen:
#      - Sammlung von Python Dateien wie im Kapitel über Module und Packages beschrieben.
#      - Distribution einer installierbaren Version einer Bibliothek ("wheel"), die dann importiert werden kann.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Setuptools: Distribution of Python packages
#
#  - Setuptools are the default tool to create installable Python packages.
#  - The word "Packages" is overloaded in the Python world:
#      - Collection of Python files as described in the lesson about modules and packages.
#      - Distribution of an installable version of a library ("wheel"), which can then be imported.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ### Beispiel: Erstellen einer Anwendung mit Bibliothek
#
#  - Hinzufügen von `setup.cfg` und `pyproject.toml`-Dateien mit Information über die zu installierenden Packages und Skripte
#  - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
#  - Erstellen der Distribution mit `python -m build` (Benötigt das PyPA `build` [package](https://github.com/pypa/build))
#  - Installation mit `pip` und dem generierten Wheel
#  - Installation während der Entwicklung: `pip install -e .`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Example: Creating an application with a library
#
#  - Add `setup.cfg` and `pyproject.toml` files with information about packages and scripts to be installed
#  - Add some help files (`README.md`, `LICENSE`)
#  - Build the distribution with `python -m build` (Requires the PyPA `build` [package](https://github.com/pypa/build))
#  - Installation with `pip` and the generated wheel
#  - Install during development: `pip install -e .`

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Abschnitt "Packaging"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Section "Packaging"
