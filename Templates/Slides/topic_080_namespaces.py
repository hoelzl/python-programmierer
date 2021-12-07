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
# {{ doc.header("Namensräume") }}

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Namensräume
#
# Variablen und Funktionsnamen existieren in einem *Namensraum (Namespace)*.
#
# - Globale Variablen und Funktionsnamen sind im globalen Namensraum.
# - Mit `import` importierte Namen existieren im importierten Namensraum.
# - Namen, die innerhalb einer Funktion definiert werden sind im Namensraum dieser Funktion.
#     - Parameter
#     - lokale Variablen
#
# Der Namensraum einer Funktion "verschwindet" am Ende des Rumpfs.

# %% {"slideshow": {"slide_type": "subslide"}}
# Ohne Angabe der Namensräume, siehe nächste Folie
a = 1
def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)
f(2)
print(a)
# print(x)

# %% {"slideshow": {"slide_type": "subslide"}}
a = 1                   # Globaler Namespace
def f(x):               # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1           # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)            # Greift auf a aus dem Namespace von f zu
f(2)
print(a)                # Greift auf a aus dem globalen Namespace zu
# print(x)              # Fehler: x ist im Namespace von f

# %% {"slideshow": {"slide_type": "subslide"}}
a = 1
def f2():
    global a
    a = 4
    print(a)
f2()
print(a)
a = 5
print(a)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Vermeiden von langwierigen Berechnungen in Notebooks:
#
# **Warnung!** Hack!!!
# Manchmal hilfreich, aber auch eine große Fehlerquelle!

# %% {{ doc.codealong() }}
def slow_computation():
    import time
    # Increase this before demonstration!
    time.sleep(0.1)
    return 1


# %% {{ doc.codealong() }}
"slow_value" in globals()

# %% {{ doc.codealong() }}
slow_value = slow_computation()

# %% {{ doc.codealong() }}
"slow_value" in globals()

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
del slow_value

# %% {{ doc.codealong() }}
"slow_value" in globals()

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
if "slow_value" not in globals():
    slow_value = slow_computation()

# %% {{ doc.codealong() }}
if "slow_value" not in globals():
    slow_value = slow_computation()
