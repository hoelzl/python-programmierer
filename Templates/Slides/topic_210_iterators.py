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
# %% [markdown] {{ doc.slide() }}
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


# %% {{ doc.codealong() }}
gen = (n * n for n in range(10))
gen

# %% {{ doc.codealong() }}
for i in gen:
    print(i, end=" ")

# %% {{ doc.codealong() }}
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f"{i}, {j}, {k}")

# %% {{ doc.codealong() }}
r = range(3)
repr(r)

# %% {{ doc.codealong() }}
it = iter(r)
repr(it)

# %% {{ doc.codealong() }}
next(it)

# %% {{ doc.codealong() }}
next(it)

# %% {{ doc.codealong() }}
next(it)

# %% {{ doc.codealong() }}
# next(it)


# %% {{ doc.codealong() }}
for x in range(3):
    print(x, end=" ")

# %% {{ doc.codealong() }}
_r = range(3)
_temp_iter = iter(_r)
while True:
    try:
        x = next(_temp_iter)
    except StopIteration:
        break
    print(x, end=" ")

# %% {{ doc.codealong() }}
gen = (n * n for n in range(3))
repr(gen)

# %% {{ doc.codealong() }}
it = iter(gen)
repr(it)

# %% {{ doc.codealong() }}
next(it)

# %% {{ doc.codealong() }}
next(it)

# %% {{ doc.codealong() }}
next(it)


# %% {{ doc.codealong() }}
# next(it)


# %% {{ doc.codealong() }}
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

# %% {{ doc.codealong() }}
def integers(start=0):
    n = start
    while True:
        yield n
        n += 1


# %% {{ doc.codealong() }}
for i in integers():
    if i > 3:
        break
    print(i, end=" ")

# %% {{ doc.codealong() }}
gen = integers()
print(repr(gen))
print(repr(iter(gen)))

# %% {{ doc.codealong() }}
gen = integers()

# %% {{ doc.codealong() }}
next(gen)


# %% {{ doc.codealong() }}
def repeat_n_times(n, it):
    for _ in range(n):
        for elt in it:
            yield elt


# %% {{ doc.codealong() }}
for num in repeat_n_times(3, range(5)):
    print(num, end=" ")
