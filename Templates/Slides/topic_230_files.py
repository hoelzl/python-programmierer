# -*- coding: utf-8 -*-
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
# <div style="text-align:center; font-size:200%;"><b>Dateien</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Files</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet haben verloren.
#
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu speichern:


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Files
#
# So far, all data that we have calculated is lost at the end of the program execution.
#
# The easiest way to persist data is to save it in a file:

# %% {"tags": ["code-along"]}
import os


# %% {"tags": ["code-along"]}
os.getcwd()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
#  - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet
#    wird:
#    - `r`: Lesen
#    - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#    - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#    - `x`: Schreiben. Die Datei darf nicht existieren.
#    - `r+`: Lesen und Schreiben.
#  - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als
#    Binärdatei behandelt.
#  - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei
#    abgefragt oder verändert werden.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - With `open()` a file can be opened for reading or writing.
# - The `mode` parameter specifies whether the file is open for reading or writing
#   will:
#   - `r`: read
#   - `w`: writing. The content of the file is deleted
#   - `a`: writing. The new data is written at the end of the file.
#   - `x`: write. The file must not exist.
#   - `r+`: read and write.
# - If the letter `b` is appended to the end of `mode`, the file is saved as
#   binary file.
# - With the methods `tell()` and `seek()` the position in the file can
#   be queried or changed.

# %% {"slideshow": {"slide_type": "subslide"}}
file = open("my-data-file.txt", "w")
file.write("The first line.\n")
file.write("The second line.\n")
file.close()


# %%
file = open("my-data-file.txt", "r")
contents = file.read()
print(contents)
file.close()
contents


# %%
file = open("my-data-file.txt", mode="w")
file.write("Another line.\n")
file.write("Yet another line.\n")
file.close()


# %%
file = open("my-data-file.txt", mode="r")
contents = file.read()
print(contents)
file.close()


# %%
file = open("my-data-file.txt", mode="a")
file.write("Let's try this again.\n")
file.write("Until we succeed.\n")
file.close()


# %%
file = open("my-data-file.txt", "r")
contents = file.read()
print(contents)
file.close()


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  Dateien müssen immer mit `close` geschlossen werden, auch wenn der
#  Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen
#  wird. Das könnte mit `try ... finally` erfolgen.
#
#  Python bietet dafür ein eleganteres Konstrukt:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Files must always be closed with `close`, even if the the part of the program in which the file is used is left with an exception. This could be done with `try ... finally`.
#
# Python offers a more elegant construct for this:

# %%
with open("my-data-file.txt", "r") as file:
    contents = file.read()
print(contents)


# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File position before reading: {file.tell()}")
    contents = file.read()
    print(f"File position after reading: {file.tell()}")
    file.write("Another line.\nAnd another.")
    print(f"File position after writing: {file.tell()}")


# %%
with open("my-data-file.txt", "r+") as file:
    print(f"File has {len(file.readlines())} lines.")
    file.seek(40)
    file.write("overwrite a part of the file, yes?")
    file.seek(0)
    print(file.read())


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  ## Mini-Workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Abschnitt "Lesen und Schreiben in Dateien"
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_190_inheritance`
#  - Section "Reading and writing to files"

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# ## Objektorientierter Umgang mit Dateien: Pathlib
#
# Das `pathlib`-Modul bietet mit der Klasse `Path` einen sehr eleganten
# objektorientierten Ansatz zum Umgang mit Dateien:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Object-oriented handling of files: Pathlib
#
# The `pathlib` module offers a very elegant `Path` class
# that offers an object-oriented approach to handling files:

# %% {"tags": ["code-along"]}
from pathlib import Path

# %% {"tags": ["code-along"]}
my_path = Path()
print("relative path:", my_path)
print("absolute path:", my_path.absolute())
my_path

# %% {"tags": ["code-along"]}
my_file = my_path / "README.md"
print("Name:         ", my_file.name)
print("Parent:       ", my_file.parent.absolute())
print("Suffix:       ", my_file.suffix)
print("Change suffix:", my_file.with_suffix(".txt"))
print("Exists?       ", my_file.exists())

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
tmp_dir = Path.home() / "Tmp"
print(tmp_dir.absolute())
print(tmp_dir.exists())

# %% {"tags": ["code-along"]}
assert not tmp_dir.exists()
my_dir = tmp_dir / "subdir1/subdir2" / "subdir3"
my_dir.mkdir(parents=True, exist_ok=False)
my_dir.exists()

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
my_file = my_dir / "test.txt"
with my_file.open("w", encoding="utf-8") as file:
    file.write("Hello, world")
print("Exists?", my_file.exists())
print(list(my_dir.glob("*")))
my_file.unlink()
print("Exists?", my_file.exists())
print(list(my_dir.glob("*")))
my_file.unlink(missing_ok=True)

# %% {"tags": ["code-along"]}
if my_dir.exists():
    my_dir.rmdir()
print("Exists?", my_dir.exists())

# %% {"tags": ["code-along"]}
import shutil

shutil.rmtree(tmp_dir, ignore_errors=True)


# %% {"tags": ["code-along"]}
tmp_dir.exists()
