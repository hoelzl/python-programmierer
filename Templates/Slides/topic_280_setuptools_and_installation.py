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
# {{ doc.header("Setuptools und Installation") }}

# %% [markdown]
#
#  # Setuptools: Distribution von Python Packeten
#
#  - Setuptools sind das Standard-Tool um installierbare Python-Pakete zu erzeugen.
#  - Das Wort "Packages" ist in der Python Welt überladen:
#      - Sammlung von Python Dateien wie in diesem Kapitel beschrieben
#      - Distribution einer installierbaren Version einer Bibliothek ("wheel"), die dann importiert werden kann.

# %% [markdown]
#
#  ### Beispiel: Erstellen einer Anwendung mit Bibliothek
#
#  - Hinzufügen von `setup.cfg` und `pyproject.toml`-Dateien mit Information über die zu installierenden Packages und Skripte
#  - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
#  - Erstellen der Distribution mit `python -m build` (Benötigt das PyPA `build` [package](https://github.com/pypa/build))
#  - Installation mit `pip` und dem generierten Wheel
#  - Installation während der Entwicklung: `pip install -e .`

# %% [markdown]
# ## Workshop
#
# - `Workshop_136_todo_list_v3`
# - Abschnitt "Packaging"
