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
# # Generatoren
#
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum
#   Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar
#   sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:
#

# %%

# %%

# %%
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f"{i}, {j}, {k}")


# %%

# %%

# %%

# %%



# %%

# %%

# %%

# %%
_r = range(3)
_temp_iter = iter(_r)
while True:
    try:
        x = next(_temp_iter)
    except StopIteration:
        break
    print(x, end=" ")

# %%

# %%

# %%

# %%

# %%

# %%

# %%
# `it` ist "erschöpft," man kann keine neuen Werte bekommen


# %% [markdown]
#
#  ## Generator Funktionen
#
#  Komplexere Fälle können von Generator Expressions nicht mehr abgedeckt werden.
#
#  - Generator, der alle Zahlen erzeugt (ohne Obergrenze)
#  - Generator, der ein Iterable modifiziert (z.B. mehrfach ausführt, eine fixe Anzahl an Elementen nimmt)
#
#  Für diese Fälle gibt es Generator-Funktionen

# %%

# %%

# %%

# %%

# %%

# %%

# %%
