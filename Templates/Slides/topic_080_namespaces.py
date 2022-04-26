# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Namensräume</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Namespaces</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
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

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Namespaces
#
# Variables and function names exist in a *namespace*.
#
# - Global variables and function names are in the global namespace.
# - Names imported with `import` exist in the imported namespace.
# - Names defined within a function are in that function's namespace.
#     - parameters
#     - local variables
#
# A function's namespace "disappears" at the end of the body.

# %% {"slideshow": {"slide_type": "subslide"}}
# Ohne Angabe der Namensräume, siehe nächste Folie
# fmt: off
a = 1

def f(x):
    # print(a) # Was passiert, wenn diese Zeile einkommentiert wird?
    a = x + 1
    print(a)

f(2)
print(a)
# print(x)

# %% {"slideshow": {"slide_type": "subslide"}}
# fmt: off
a = 1         # Globaler Namespace

def f(x):     # Namespace von f - x ist im globalen Namespace *nicht* sichtbar
    a = x + 1 # Namespace von f - a ist im globalen Namespace *nicht* sichtbar
    print(a)  # Greift auf a aus dem Namespace von f zu

f(2)
print(a)      # Greift auf a aus dem globalen Namespace zu
# print(x)    # Fehler: x ist im Namespace von f
# fmt: on

# %% {"slideshow": {"slide_type": "subslide"}}
# fmt: off
a = 1

def f2(x):
    global a
    a = x + 1
    print(a)

f2(2)
print(a)
a = 5
print(a)
# fmt: on

# %% {"tags": ["code-along"]}
from dis import dis

# %% {"tags": ["code-along"]}
dis(f)

# %% {"tags": ["code-along"]}
dis(f2)

# %% {"tags": ["code-along"]}
# fmt: off
a = 1

def f_broken():
    # noinspection PyUnresolvedReferences
    print(a)
    a = 2
# fmt: on

# %%
# f_broken()

# %% {"tags": ["code-along"]}
dis(f_broken)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# ## Closures
#
# In Python ist es möglich Funktionen innerhalb von anderen Funktionen zu
# definieren. Diese können auf die Variablen der äußeren Funktion zugreifen.

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Closures
#
# In Python it is possible to define functions inside other functions. The inner functions can access the variables of the outer function.

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def make_closure_1():
    from random import randint

    initial_value = randint(1, 10)

    def read_value():
        return initial_value

    return read_value()


# %% {"tags": ["code-along"]}
make_closure_1()

# %% {"tags": ["code-along"]}
dis(make_closure_1)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def make_closure_2():
    from random import randint

    initial_value = randint(1, 10)

    def read_value():
        return initial_value

    return read_value


# %% {"tags": ["code-along"]}
make_closure_2()

# %% {"tags": ["code-along"]}
dis(make_closure_2)

# %% {"tags": ["code-along"]}
reader = make_closure_2()
reader()


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def make_mean_fun_1():
    values: list[int] = []

    def compute_mean(new_value: int):
        values.append(new_value)
        return sum(values) / len(values)

    return compute_mean


# %% {"tags": ["code-along"]}
my_mean = make_mean_fun_1()
your_mean = make_mean_fun_1()

# %% {"tags": ["code-along"]}
print(my_mean(10))
print(my_mean(20))
print(your_mean(1))
print(your_mean(2))
print(my_mean(30))


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def make_mean_fun_2():
    sum_of_values: int = 0
    num_values: int = 0

    def compute_mean(new_value: int):
        nonlocal sum_of_values, num_values
        sum_of_values += new_value
        num_values += 1
        return sum_of_values / num_values

    return compute_mean


# %% {"tags": ["code-along"]}
my_mean = make_mean_fun_2()
your_mean = make_mean_fun_2()

# %% {"tags": ["code-along"]}
print(my_mean(10))
print(my_mean(20))
print(your_mean(1))
print(your_mean(2))
print(my_mean(30))


# %% {"tags": ["code-along"]}
dis(make_mean_fun_2)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Vermeiden von langwierigen Berechnungen in Notebooks:
#
# **Warnung!** Hack!!!
# Manchmal hilfreich, aber auch eine große Fehlerquelle!

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Avoiding long-running calculations in notebooks:
#
# **Warning!** Hack!!!
# Sometimes helpful, but also a big source of errors!

# %% {"tags": ["code-along"]}
def slow_computation():
    import time

    # Increase this before demonstration!
    time.sleep(0.1)
    return 1


# %% {"tags": ["code-along"]}
"slow_value" in globals()

# %% {"tags": ["code-along"]}
slow_value = slow_computation()

# %% {"tags": ["code-along"]}
"slow_value" in globals()

# %% {"tags": ["code-along"]}
del slow_value

# %% {"tags": ["code-along"]}
"slow_value" in globals()

# %% {"tags": ["code-along"]}
if "slow_value" not in globals():
    slow_value = slow_computation()

# %% {"tags": ["code-along"]}
if "slow_value" not in globals():
    slow_value = slow_computation()

# %%
