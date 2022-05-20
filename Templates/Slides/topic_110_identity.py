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
# <div style="text-align:center; font-size:200%;"><b>Identität von Objekten</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Object Identity</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Identität von Objekten

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Objects identity

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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "en"}
#
#  <img src="img/identity.svg" style="display:block;width:70%;margin:auto;"/>

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
#  ## Test der Identität von Objekten

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Testing object identity

# %%
a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = c[:]

# %% [markdown] {"lang": "de"}
#
#  `==` testet Gleichheit der Werte, nicht (notwendigerweise) Objektidentität.

# %% [markdown] {"lang": "en"}
# `==` tests equality of values, not (necessarily) object identity.

# %%
a == b

# %%
b == c

# %%
c == d

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  Mit `is` kann man Objektidentität testen:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# You can use `is` to test object identity:

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

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
#  Die Funktion `id()` gibt die Adresse eines Objekts zurück:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The `id()` function returns the address of an object:

# %%
id([1, 2, 3])

# %% [markdown] {"lang": "de"}
#
#  Meistens stellt man Adressen in hexadezimaler Form dar:

# %% [markdown] {"lang": "en"}
# Addresses are usually represented in hexadecimal form:

# %%
hex(id([1, 2, 3]))

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# *Nur am Rande:* Gilt für Zahlen mit `x == y` immer `x is y`?

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# *Only as an aside:* Does `x is y` always apply to numbers with `x == y`?

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


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# ## Vorsicht mit veränderlichen Default-Argumenten!

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Be careful with mutable default arguments!

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


# %% {"slideshow": {"slide_type": "subslide"}}
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
