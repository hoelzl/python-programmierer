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
# {{ doc.header("Kommandozeilenargumente") }}


# %% [markdown]
#
#  ## Verarbeiten von Command Line Arguments: Argparse und Typer
#
#  - Für viele Anwendungsfälle ist eine Kommandozeilenanwendung ausreichend
#  - Die manuelle Verarbeitung von Argumenten ist relativ aufwändig
#  - Python bietet mit `argparse` eine sehr gute Bibliothek, die viele häufige Anwendungsfälle deutlich vereinfacht
#  - Noch besser: [Typer](https://typer.tiangolo.com/)

# %% [markdown]
#
# ### Bestandteile von Typer:
#
# - Klasse `app = typer.Typer()` um die eigenen Klassen mit Typer zu verbinden.
# - Decorator `app.command()` um Funktionen Kommandos zu definieren.
# - Parametern von Funktionen werden zu positionalen Argumenten oder benannten Optionen.
# - Viele Funktionen von CLI-Applikationen werden von Typer automatisch erzeugt.

# %% [markdown]
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Bis Abschnitt "Kommandozeilenargumente"
