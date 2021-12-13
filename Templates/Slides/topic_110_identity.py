# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# j2 import 'macros.j2' as doc
# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# {{ doc.header("Identität von Objekten") }}

# %% [markdown]
#
#  ## Identität von Objekten

# %%
a = [1, 2, 3]
b = [1, 2, 3]
c = b

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
a[0] = 10

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %%
b[0] = 20

# %%
c[1] = 30

# %%
print(f"a = {a}, b = {b}, c = {c}")

# %% [markdown]
#
#  <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown]
#
#  ## Test der Identität von Objekten

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %% [markdown]
#
#  `==` testet Gleichheit der Werte, nicht (notwendigerweise) Objektidentität.

# %%
a == b

# %%
b == c

# %%
c == d

# %% [markdown]
#
#  Mit `is` kann man Objektidentität testen:

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]
e = c.copy()

# %%
a is b

# %%
b is c

# %%
c is d

# %%
c is e

# %%
c[0] = 2

# %%
d

# %%
e

# %% [markdown]
#
#  Die Funktion `id()` gibt die Adresse eines Objekts zurück:

# %%
id([1, 2, 3])

# %% [markdown]
#
#  Meistens stellt man Adressen in hexadezimaler Form dar:

# %%
hex(id([1, 2, 3]))

# %% [markdown]
# *Nur am Rande:* Gilt für Zahlen mit `x == y` immer `x is y`?

# %%
x = 1
y = 1
z = 1.0
print(x == y)
print(x is y)
print(x == z)
print(x is z)

# %%
x = 2560
y = 2560
print(x == y)
print(x is y)

# %%
import ctypes

x_refcount = ctypes.c_long.from_address(id(x)).value
x_int_value = ctypes.c_long.from_address(id(x) + 24).value

# %%
print(hex(id(x)))
print(x_refcount)
print(x_int_value)

# %%
print(hex(id(x)))
print(x_refcount)
print(x_int_value)


# %% [markdown]
# ## Vorsicht mit veränderlichen Default-Argumenten!

# %%
def f(lst=[]):
    lst.append(1)
    return lst


# %%
f([1, 2, 3])

# %%
f()

# %%
f()

# %%
f()


# %%
def f(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst


# %%
f()

# %%
f()

# %%
f()


# %%
def f(lst=[]):
    return lst


# %%
x = f()

# %%
x.append(2)

# %%
f()

# %%
a = [1, 2, 3]
b = a[1:2]
b[0] = "a"
print(a, b)

# %%
import numpy as np

a = np.array([1, 2, 3])
b = a[1:2]
b[0] = 4
print(a, b)

# %%
