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
# # Lesen und Schreiben in Dateien
#
# Schreiben Sie eine Funktion `write_text_to_file(text: str, file_name: str)
# -> None`, die den String `text` in die Datei `file_name` schreibt, sofern
# diese *nicht* existiert und eine Exception vom Typ `FileExistsError` wirft,
# falls die Datei existiert.
#
# *Hinweis:*  Beachten Sie die möglichen Werte für das `mode` Argument von
# `open()`.

# %% [markdown] lang="en"
# # Reading and writing to files
#
# Write a function `write_text_to_file(text: str, file_name: str) -> None`, which writes the string `text` to the file `file_name` if the file *does not* exist and throws an exception of type `FileExistsError`,
# if the file exists.
#
# *Note:* Note the possible values for the `mode` argument of `open()`.

# %% tags=["solution"]
def write_text_to_file(text, file_name):
    with open(file_name, "x") as file:
        file.write(text)


# %% [markdown] lang="de"
#
# Testen Sie die Funktion, indem Sie zweimal hintereinander versuchen den
# Text `Python 3.8` in die Datei `my-private-file.txt` zu schreiben.

# %% [markdown] lang="en"
# Test the function by trying to write the text `Python 3.8` to the file `my-private-file.txt` twice in a row.

# %% tags=["solution"]
write_text_to_file("Python 3.8", "my_private_file.txt")


# %% tags=["solution"]
# write_text_to_file("Python 3.8", "my_private_file.txt")

# %% [markdown] lang="de"
# Schreiben Sie eine Funktion `annotate_file(file_name: str) -> None`, die
# - den Inhalt der Datei `file_name` gefolgt von dem Text `(annotated version)`
#   auf dem Bildschirm ausgibt, falls sie existiert
# - den Text `No file found, we will bill the time we spent searching.` ausgibt
#   falls sie nicht existiert
# - in beiden Fällen den Text `Our invoice will be sent by mail.` ausgibt.

# %% [markdown] lang="en"
# Write a function `annotate_file(file_name: str) -> None` which
# - prints out the content of the file `file_name` followed by the text `(annotated version)`
#   if the file exists
# - prints out the text `No file found, we will bill the time we spent searching.`
#   if the file doesn't exist
#
# In both cases the text `Our invoice will be sent by mail.` is printed out.

# %% tags=["solution"]
def annotate_file(file_name):
    try:
        with open(file_name, "r") as file:
            print(file.read())
            print("(annotated version)")
    except FileNotFoundError:
        print("No file found, we will bill the time we spent searching.")
    finally:
        print("Our invoice will be sent by mail.")


# %% tags=["solution"]
annotate_file("my_private_file.txt")

# %% tags=["solution"]
annotate_file("does-not-exist.txt")
