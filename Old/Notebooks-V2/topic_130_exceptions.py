# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
# ---

# %%

# %% [markdown]
#
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m` zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
#
# Einige Lösungsversuche:


# %%
from typing import Tuple



# %%
def int_sqrt_with_pair(n: int) -> Tuple[int, bool]:
    for m in range(n + 1):
        if m * m == n:
            return m, True
    return 0, False



# %%
int_sqrt_with_pair(9)


# %%
int_sqrt_with_pair(8)


# %%
int_sqrt_with_pair(0)


# %%
int_sqrt_with_pair(1)


# %%
def print_int_sqrt_1(n):
    root, is_valid = int_sqrt_with_pair(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_1(8)


# %%
def int_sqrt_with_negative_value(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    return -1



# %%
int_sqrt_with_negative_value(9)


# %%
int_sqrt_with_negative_value(8)


# %%
def print_int_sqrt_2(n):
    root = int_sqrt_with_negative_value(8)
    print(f"The root of {n} is {root}.")


print_int_sqrt_2(8)


# %%
def print_int_sqrt_2_better(n):
    root = int_sqrt_with_negative_value(8)
    if root < 0:
        print(f"{n} does not have a root!")
    else:
        print(f"The root of {n} is {root}.")


print_int_sqrt_2_better(8)


# %% [markdown]
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

# %%
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")



# %%
int_sqrt(9)


# %%
int_sqrt(0)


# %%
int_sqrt(1)


# %%
# int_sqrt(8)


# %%
def print_int_sqrt(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")



# %%
# print_int_sqrt(8)


# %%
def print_int_sqrt_no_error(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(str(error))



# %%
print_int_sqrt_no_error(9)


# %%
print_int_sqrt_no_error(8)


# %%
def print_int_sqrt_no_error_2(n):
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError:
        print(f"{n} does not have a root!")
    finally:
        print("And that's all there is to say about this topic.")



# %%
print_int_sqrt_no_error_2(9)


# %%
print_int_sqrt_no_error_2(8)


# %% [markdown]
#
#  ## Fehlerklassen
#
#  In Python gibt es viele vordefinierte Fehlerklassen, mit denen verschiedene
#  Fehlerarten signalisiert werden können:
#  - `Exception`: Basisklasse aller behandelbaren Exceptions
#  - `ArithmeticError`: Basisklasse aller Fehler bei Rechenoperationen:
#    - OverflowError
#    - ZeroDivisionError
#  - `LookupError`: Basisklasse wenn ein ungültiger Index für eine Datenstruktur
#    verwendet wurde
#  - `AssertionError`: Fehlerklasse, die von `assert` verwendet wird
#  - `EOFError`: Fehler wenn `intput()` unerwartet das Ende einer Datei erreicht
#  - ...
#
#  Die Liste der in der Standardbibliothek definierten Fehlerklassen ist
#  [hier](https://docs.python.org/3/library/exceptions.html).

# %%
class NoRootError(ValueError):
    pass



# %%
try:
    raise ValueError("ValueError")
    # raise NoRootError("This is a NoRootError.")
except NoRootError as error:
    print(f"Case 1: {error}")
except ValueError as error:
    print(f"Case 2: {error}")


# %%
my_var = 1
assert my_var == 1


# %% [markdown]
#
#  ## Mini-Workshop
#
#  - Notebook `020x-Workshop Kontrollstrukturen`
#  - Abschnitt "Knobeln"
#
