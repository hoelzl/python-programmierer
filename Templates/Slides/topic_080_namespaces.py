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
# @formatter:off

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
# @formatter:on

# %% {{ doc.codealong() }}
from dis import dis

# %% {{ doc.codealong() }}
dis(f)

# %% {{ doc.codealong() }}
dis(f2)

# %% {{ doc.codealong() }}
a = 1


def f_broken():
    # noinspection PyUnresolvedReferences
    print(a)
    a = 2


# %% {{ doc.codealong() }}
dis(f_broken)


# %% [markdown]
#
# ## Closures
#
# In Python ist es möglich Funktionen innerhalb von anderen Funktionen zu
# definieren. Diese können auf die Variablen der äußeren Funktion zugreifen.

# %% {{ doc.codealong() }}
def make_closure_1():
    from random import randint
    initial_value = randint(1, 10)

    def read_value():
        return initial_value

    return read_value()


# %% {{ doc.codealong() }}
make_closure_1()

# %% {{ doc.codealong() }}
dis(make_closure_1)


# %% {{ doc.codealong() }}
def make_closure_2():
    from random import randint
    initial_value = randint(1, 10)

    def read_value():
        return initial_value

    return read_value


# %% {{ doc.codealong() }}
make_closure_2()

# %% {{ doc.codealong() }}
dis(make_closure_2)

# %% {{ doc.codealong() }}
reader = make_closure_2()
reader()


# %% {{ doc.codealong() }}
def make_mean_fun_1():
    values: list[int] = []

    def compute_mean(new_value: int):
        values.append(new_value)
        return sum(values) / len(values)

    return compute_mean


# %% {{ doc.codealong() }}
my_mean = make_mean_fun_1()
your_mean = make_mean_fun_1()

# %% {{ doc.codealong() }}
print(my_mean(10))
print(my_mean(20))
print(your_mean(1))
print(your_mean(2))
print(my_mean(30))


# %% {{ doc.codealong() }}
def make_mean_fun_2():
    sum_of_values: int = 0
    num_values: int = 0

    def compute_mean(new_value: int):
        nonlocal sum_of_values, num_values
        sum_of_values += new_value
        num_values += 1
        return sum_of_values / num_values

    return compute_mean


# %% {{ doc.codealong() }}
my_mean = make_mean_fun_2()
your_mean = make_mean_fun_2()

# %% {{ doc.codealong() }}
print(my_mean(10))
print(my_mean(20))
print(your_mean(1))
print(your_mean(2))
print(my_mean(30))


# %% {{ doc.codealong() }}
dis(make_mean_fun_2)


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
