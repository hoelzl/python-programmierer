# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# %% [markdown]
#
#  # Namensräume
#
#  Variablen und Funktionsnamen existieren in einem *Namensraum (Namespace)*.
#
#  - Globale Variablen und Funktionsnamen sind im globalen Namensraum.
#  - Mit `import` importierte Namen existieren im importierten Namensraum.
#  - Namen, die innerhalb einer Funktion definiert werden sind im Namensraum
#    dieser Funktion.
#      - Parameter
#      - lokale Variablen
#
#  Der Namensraum einer Funktion "verschwindet" am Ende des Rumpfs.

# %%
# Ohne Angabe der Namensräume, siehe nächste Folie
a = 1


def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)


f(2)
print(a)
# print(x)


# %%
a = 1  # Globaler Namespace


def f(x):  # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1  # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)  # Greift auf a aus dem Namespace von f zu


f(2)
print(a)  # Greift auf a aus dem globalen Namespace zu
# print(x)              # Fehler: x ist im Namespace von f


# %%
a = 1


# %%
def f2():
    global a
    a = 4
    print(a)



# %%
f2()
print(a)
a = 5
print(a)

