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
# <div style="text-align:center; font-size:200%;"><b>Ausnahment und Fehlerbehandlung</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Exceptions and handling errors</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
#
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die
# "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m`
#   zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
#
# Einige Lösungsversuche:


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Error handling
#
# We want to write a function `int_sqrt(n: int) -> int` that calculates the
# "integer square root":
# - If `n` is a square number, i.e. has the form `m * m`, then `m` should
#   be returned.
# - What do we do if `n` is not a square number?
#
# Some attempted solutions:

# %% {"tags": ["code-along"]}
from typing import Tuple


# %% {"tags": ["code-along"]}
def int_sqrt_with_pair(n: int) -> Tuple[int, bool]:
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False


# %% {"tags": ["code-along"]}
int_sqrt_with_pair(9)


# %% {"tags": ["code-along"]}
int_sqrt_with_pair(8)


# %% {"tags": ["code-along"]}
int_sqrt_with_pair(0)


# %% {"tags": ["code-along"]}
int_sqrt_with_pair(1)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def print_int_sqrt_1(n):
    root, is_valid = int_sqrt_with_pair(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_1(8)


# %% {"tags": ["code-along"]}
def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1


# %% {"tags": ["code-along"]}
int_sqrt_with_negative_value(9)


# %% {"tags": ["code-along"]}
int_sqrt_with_negative_value(8)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def print_int_sqrt_2(n):
    root = int_sqrt_with_negative_value(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_2(8)


# %% {"tags": ["code-along"]}
def print_int_sqrt_2_better(n):
    root = int_sqrt_with_negative_value(8)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")


print_int_sqrt_2_better(8)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
#
#  Beide Ansätze haben mehrere Probleme:
#  - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit
#    einem falschen Wert weitergerechnet.
#  - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über
#    mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden. Das führt zu
#    unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur
#    Fehlerbehandlung getrennt ist.
#
#  Eine bessere Lösung:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Both approaches have several problems:
#  - Error handling is optional. If it is not carried out, the computation proceeds with
#    an incorrect value.
#  - If the caller cannot handle the error itself, the error must be passed through (possibly)
#    multiple levels of function calls. That leads to
#    confusing code because the "interesting" path is intermingled with code to
#    handle errors.
#
#  A better solution:

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# %% {"tags": ["code-along"]}
int_sqrt(9)


# %% {"tags": ["code-along"]}
int_sqrt(0)


# %% {"tags": ["code-along"]}
int_sqrt(1)


# %% {"tags": ["code-along"]}
# int_sqrt(8)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def print_int_sqrt(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %% {"tags": ["code-along"]}
# print_int_sqrt(8)


# %% {"tags": ["code-along"]}
def print_int_sqrt_no_error(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as err:
        print(str(err))


# %% {"tags": ["code-along"]}
print_int_sqrt_no_error(9)


# %% {"tags": ["code-along"]}
print_int_sqrt_no_error(8)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def print_int_sqrt_no_error_2(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError:
        print(f"{n} does not have a root!")
    finally:
        print("And that's all there is to say about this topic.")


# %% {"tags": ["code-along"]}
print_int_sqrt_no_error_2(9)


# %% {"tags": ["code-along"]}
print_int_sqrt_no_error_2(8)


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# ## Fehlerklassen
#
# In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene
# Fehlerarten signalisiert werden können:
# - `Exception`: Basisklasse aller behandelbaren Exceptions
# - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#   - OverflowError
#   - ZeroDivisionError
# - `LookupError`: Basisklasse wenn ein ungültiger Index für eine Datenstruktur
#   verwendet wurde
# - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
# - `EOFError`: Fehler wenn `intput()` unerwartet das Ende einer Datei erreicht
# - ...
#
# Die Liste der in der Standardbibliothek definierten Fehlerklassen ist
# [hier](https://docs.python.org/3/library/exceptions.html).

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Error classes
#
# In Python, there are many predefined classes that signal different types of error:
# - `Exception`: Base class of all exceptions that can be handled
# - `ArithmeticError`: Base class of all errors in arithmetic operations:
#   - OverflowError
#   - Zero Division Error
# - `LookupError`: base class when an invalid index for a data structure
#   has been used
# - `AssertionError`: error class used by `assert`
# - `EOFError`: Error when `intput()` unexpectedly reaches the end of a file
# - ...
#
# The list of error classes defined in the standard library is
# [here](https://docs.python.org/3/library/exceptions.html).

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
class NoRootError(ValueError):
    pass


# %% {"tags": ["code-along"]}
try:
    raise ValueError("ValueError")
    # raise NoRootError("This is a NoRootError.")
except NoRootError as error:
    print(f"Case 1: {error}")
except ValueError as error:
    print(f"Case 2: {error}")


# %% {"tags": ["code-along"]}
my_var = 1
assert my_var == 1


# %% {"tags": ["code-along"]}
def raise_and_handle_error():
    print("rahe() before")
    try:
        raise ValueError("ValueError was raised.")
        # raise NoRootError("Found no root.")
        # raise TypeError("Bad type")
    except NoRootError as error:
        print(f"Case NoRootError: {error}")
    except ValueError as error:
        print(f"Case ValueError: {error}")
    print("rahe() after")


# %%
def f2():
    print("f2() before")
    raise_and_handle_error()
    print("f2() after")


# %%
def f1():
    print("f1() before")
    try:
        f2()
    except Exception as error:
        print(f"Case Exception: {error}")
    print("f1() after")        


# %%
f1()

# %%

# %% [markdown] {"lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_190_inheritance`
# - Abschnitt "Bank Account"

# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
# - Notebook `workshop_190_inheritance`
# - Section "Bank Account"

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_090_control_structures`
# - Abschnitt "Knobeln"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
#  - Notebook `workshop_090_control_structures`
#  - Section "Rock Paper Scissors"

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `topic_900_othellite`
# - `compute_linear_index()`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `topic_900_othellite`
# - `compute_linear_index()`
