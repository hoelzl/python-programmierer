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
# <div style="text-align:center; font-size:200%;"><b>Kommandozeilenargumente: Typer</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Command line arguments: Typer</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Verarbeiten von Command Line Arguments: Argparse und Typer
#
#  - Für viele Anwendungsfälle ist eine Kommandozeilenanwendung ausreichend
#  - Die manuelle Verarbeitung von Argumenten ist relativ aufwändig
#  - Python bietet mit `argparse` eine sehr gute Bibliothek, die viele häufige Anwendungsfälle deutlich vereinfacht
#  - Noch besser: [Typer](https://typer.tiangolo.com/)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Processing Command Line Arguments: Argparse and Typer
#
#  - A command line application is sufficient for many applications
#  - Manual processing of command-line arguments is relatively time-consuming
#  - With `argparse`, Python offers a very good library that significantly simplifies many common use cases
#  - Even better: [Typer](https://typer.tiangolo.com/)

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
# ### Bestandteile von Typer:
#
# - Klasse `app = typer.Typer()` um die eigenen Klassen mit Typer zu verbinden.
# - Decorator `app.command()` um Funktionen als Kommandos zu definieren.
# - Parametern von Funktionen werden zu positionalen Argumenten oder benannten Optionen.
# - Viele Funktionen von CLI-Applikationen werden von Typer automatisch erzeugt.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### Components of Typer:
#
# - Class `app = typer.Typer()` to connect your own classes to Typer.
# - Decorator `app.command()` to define function commands.
# - Function parameters become positional arguments or named options.
# - Many functions of CLI applications are generated automatically by Typer.

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Bis Abschnitt "Kommandozeilenargumente"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Up to section "Command Line Arguments"
