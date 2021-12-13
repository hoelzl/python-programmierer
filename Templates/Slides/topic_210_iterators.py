# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Iteratoren und Generatoren") }}


# %% [markdown]
#
# # Generatoren
#
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum
#   Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar
#   sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:


# %% tags=["code-along"]
gen = (n * n for n in range(10))
gen

# %% tags=["code-along"]
for i in gen:
    print(i, end=" ")

# %% tags=["code-along"]
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f"{i}, {j}, {k}")

# %% tags=["code-along"]
r = range(3)
repr(r)

# %% tags=["code-along"]
it = iter(r)
repr(it)

# %% tags=["code-along"]
next(it)

# %% tags=["code-along"]
next(it)

# %% tags=["code-along"]
next(it)

# %% tags=["code-along"]
# next(it)


# %% tags=["code-along"]
for x in range(3):
    print(x, end=" ")

# %% tags=["code-along"]
_r = range(3)
_temp_iter = iter(_r)
while True:
    try:
        x = next(_temp_iter)
    except StopIteration:
        break
    print(x, end=" ")

# %% tags=["code-along"]
gen = (n * n for n in range(3))
repr(gen)

# %% tags=["code-along"]
it = iter(gen)
repr(it)

# %% tags=["code-along"]
next(it)

# %% tags=["code-along"]
next(it)

# %% tags=["code-along"]
next(it)


# %% tags=["code-along"]
# next(it)


# %% tags=["code-along"]
# `it` ist "erschöpft," man kann keine neuen Werte bekommen
# next(it)


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

# %% tags=["code-along"]
def integers(start=0):
    n = start
    while True:
        yield n
        n += 1


# %% tags=["code-along"]
for i in integers():
    if i > 3:
        break
    print(i, end=" ")

# %% tags=["code-along"]
gen = integers()
print(repr(gen))
print(repr(iter(gen)))

# %% tags=["code-along"]
gen = integers()

# %% tags=["code-along"]
next(gen)


# %% tags=["code-along"]
def repeat_n_times(n, it):
    for _ in range(n):
        for elt in it:
            yield elt


# %% tags=["code-along"]
for num in repeat_n_times(3, range(5)):
    print(num, end=" ")
