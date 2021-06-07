
# %% [markdown]
#
# # Dateien
#
# Bislang gehen am Ende der Programmausführung alle Daten, die wir berechnet haben verloren.
#
# Die einfachste Varianten Daten zu persistieren ist sie in einer Datei zu speichern:

# %%
import os

# %%
os.getcwd()

# %% [markdown]
#
# - Mit `open()` kann eine Datei zum Lesen oder Schreiben geöffnet werden.
# - Der `mode` Parameter gibt an, ob die Datei zum Lesen oder Schreiben geöffnet
#   wird:
#   - `r`: Lesen
#   - `w`: Schreiben. Der Inhalt der Datei wird gelöscht
#   - `a`: Schreiben. Die neuen Daten werden ans Ende der Datei geschrieben.
#   - `x`: Schreiben. Die Datei darf nicht existieren.
#   - `r+`: Lesen und Schreiben.
# - Wird ans Ende von `mode` der Buchstabe `b` angehängt, so wird die Datei als
#   Binärdatei behandelt.
# - Mit den Methoden `tell()` und `seek()` kann die Position in der Datei
#   abgefragt oder verändert werden.

# %%
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

# %% [markdown]
#
# Dateien müssen immer mit `close` geschlossen werden, auch wenn der
# Programmteil, in dem die Datei verwendet wird durch eine Exception verlassen
# wird. Das könnte mit `try ... finally` erfolgen.
#
# Python bietet dafür ein eleganteres Konstrukt:

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

# %% [markdown]
#
# ## Mini-Workshop
#
# - Notebook `020x-Workshop Kontrollstrukturen`
# - Abschnitt "# Lesen und Schreiben in Dateien"
#

# %%
