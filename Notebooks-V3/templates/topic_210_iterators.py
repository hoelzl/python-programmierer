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

# %%

# j2 import 'macros.j2' as doc
# %% [markdown] {"incorrectly_encoded_metadata": "{{ doc.slide() }}"}
# {{ doc.header (Iteratoren und Generatoren) }}


# %% [markdown]
#
# # Generatoren
#
# - Es ist nicht effizient eine Liste zu konstruieren, wenn wir sie nur zum
#   Iterieren über ihre Elemente verwenden wollen
# - Python bietet die Möglichkeit Generatoren zu definieren, die iterierbar
#   sind, aber nicht den Overhead einer Liste haben
# - Die einfachste Form ist mit Generator Expressions:


# %%
gen = (n * n for n in range(10))
gen


# %%
for i in gen:
    print(i, end=" ")


# %%
for i, j, k in ((n, m, n * m) for n in range(2, 5) for m in range(n, 5)):
    print(f"{i}, {j}, {k}")


# %%
r = range(3)
repr(r)


# %%
it = iter(r)
repr(it)


# %%
next(it)


# %%
next(it)


# %%
next(it)


# %%
# next(it)


# %%
for x in range(3):
    print(x, end=" ")


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
gen = (n * n for n in range(3))
repr(gen)


# %%
it = iter(gen)
repr(it)


# %%
next(it)


# %%
next(it)


# %%
next(it)


# %%
# next(it)


# %%
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

# %%
def integers(start=0):
    n = start
    while True:
        yield n
        n += 1



# %%
for i in integers():
    if i > 3:
        break
    print(i, end=" ")


# %%
gen = integers()
print(repr(gen))
print(repr(iter(gen)))


# %%
gen = integers()


# %%
next(gen)


# %%
def repeat_n_times(n, it):
    for _ in range(n):
        for elt in it:
            yield elt



# %%
for num in repeat_n_times(3, range(5)):
    print(num, end=" ")

