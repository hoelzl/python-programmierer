# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Listen
#
# Wiederholung:
#
# - Listen-Literale werden in eckige Klammern eingeschlossen
# - Andere Sequenzen können mittels `list` in Listen umgewandelt werden
#

# %%
["a", "b", "c"]

# %%
range(3)

# %%
list(range(3))

# %% [markdown]
#
#  ## Eigenschaften von Listen
#
#  - Listen können beliebige Python-Werte speichern
#  - Elemente in einer Liste haben eine feste Reihenfolge
#  - Auf Elemente einer Liste kann mit einem Index zugegriffen werden
#  - Listen können modifiziert werden
#
#  Listen können Elemente mit verschiedenen Typen enthalten, die meisten Listen
#  enthalten aber Elemente eines einzigen Typs.

# %%
stringliste = ["a", "b", "c"]

# %%
stringliste[0]

# %%
stringliste[-1]

# %% [markdown]
#
#  ### Überprüfen, ob ein Element in einer Liste enthalten ist

# %%
2 in [1, 2, 3]

# %%
"a" in stringliste

# %%
"x" in stringliste

# %%
not (2 in [1, 3, 5]) # Don't do this

# %%
2 not in [1, 3, 5]

# %% [markdown]
#
#  ### Finden der Position eines Elements

# %%
[1, 2, 3, 4, 5].index(2)

# %%
my_list = ["a", "b", "c", "d", "b", "d", "b"]
my_index = my_list.index("b")
print(my_index)
my_list[my_index]

# %%
# Fehler
[1, 3, 5].index(2)


# %% [markdown]
#
#  Die Methode `index` wirft eine Exception, wenn das gesuchte Objekt nicht in
#  der Liste vorkommt. Wie können wir eine Funktion
#  ```
#  find(element, a_list)
#  ```
#  schreiben, die uns
#
#  - einen Index zurückgibt, falls das Element `element` in der Liste vorkommt,
#    und die
#  - `None` zurückgibt, falls es nicht vorkommt?

# %%
def find(element, a_list):
    if element in a_list:
        return a_list.index(element)
    else:
        return None


# %%
my_list = ["a", "b", "c", "d", "e"]

# %%
find("a", my_list)

# %%
find("d", my_list)

# %%
find("x", my_list) == None

# %% [markdown]
#
#  ### Modifikation von Elementen

# %%
stringliste

# %%
stringliste[0] = "A"

# %%
stringliste

# %% [markdown]
#
#  ### Einfügen und Anhängen von Elementen

# %%
stringliste

# %%
stringliste.append("D")

# %%
stringliste

# %%
stringliste + ["E", "F"]

# %%
stringliste

# %%
stringliste.extend(["E", "F"])

# %%
stringliste

# %%
stringliste.insert(0, "ANFANG")

# %%
stringliste

# %%
stringliste.insert(-1, "ENDE")

# %%
stringliste

# %% [markdown]
#
#  ### Entfernen von Elementen

# %%
stringliste

# %%
stringliste[6]

# %%
del stringliste[6]

# %%
stringliste


# %% [markdown]
#
#  ### Länge einer Liste

# %%
stringliste

# %%
len(stringliste)

# %%
stringliste.insert(len(stringliste), "Wirklich das Ende")

# %%
stringliste

# %%
# Vorsicht!
stringliste[len(stringliste)]

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Farben"
#

# %% [markdown]
#
#  ## Slicing
#
#  Mit der Notation `liste[m:n]` kann man eine "Teilliste" von `liste` extrahieren.
#
#  - Das erste Element ist `liste[m]`
#  - Das letzte Element ist `liste[n-1]`

# %%
stringliste = ["a", "b", "c", "d", "e"]

# %%
stringliste[1:3]

# %%
stringliste[1:1]

# %%
stringliste[0:len(stringliste)]

# %%
stringliste[:3]

# %%
stringliste[1:]

# %%
stringliste[:]

# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `030x-Workshop Listen und For-Schleifen`
#  - Abschnitt "Slicing"
#

# %% [markdown]
#
#  ## Erzeugen von Listen
#
#  Durch den Multiplikationsoperator `*` können die Elemente einer Liste
#  wiederholt werden:

# %%
[1, 2] * 3

# %%
3 * ["a", "b"]

# %%
[0] * 10

# %% [markdown]
#
#  ## Zuweisung an Slices
#
#  Man kann Werte an Slices zuweisen:

# %%
liste = [1, 2, 3, 4]
liste[1:3]

# %%
liste[1:3] = ["a", "b", "c"]
liste

# %%
liste[1:3] = 123

# %%
liste[2:2]

# %%
liste[2:2] = ["x"]
liste

# %%
liste[:] = [11, 22, 33]
liste

# %%
