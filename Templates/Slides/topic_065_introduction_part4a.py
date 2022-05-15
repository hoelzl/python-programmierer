# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: py:percent
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
# <div style="text-align:center; font-size:200%;"><b>Einführung in Python: Grundlagen Teil 3</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Introduction to Python: Part 3</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Beliebig viele Argumente:
#
# Man kann Funktionen definieren, die beliebig viele Argumente bekommen können:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Any number of arguments:
#
# You can define functions that can take any number of arguments:

# %% {"tags": ["code-along"]}
def my_add(*args):
    result = 0
    for i in args:
        result += i
    return result


# %% {"tags": ["code-along"]}
my_add(1, 2, 3, 4, 5, 6)


# %% [markdown] {"lang": "de"}
#
# ## Micro-Workshop
#
# Schreiben Sie eine Funktion `print_lines(*args)`, die beliebig viele
# Argumente bekommt und ein Argument pro Zeile ausgibt:
# ```
# >>> print_lines("hey", "you")
# hey
# you
# ```

# %% [markdown] {"lang": "en"}
# ## Micro workshop
#
# Write a function `print_lines(*args)` that can take any number of arguments and prints them all, one argument per line:
# ```
# >>> print_lines("hey", "you")
# hey
# you
# ```

# %% {"tags": ["code-along"]}
def print_lines(*args):
    for arg in args:
        print(arg)


# %% {"tags": ["code-along"]}
print_lines("hey", "you")


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# Das kann auch mit anderen Argumenten kombiniert werden:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# This can also be combined with other arguments:

# %% {"tags": ["code-along"]}
def add_more_than_two(x, y, *more_args):
    result = x + y
    for i in more_args:
        result += i
    return result


# %% {"tags": ["code-along"]}
add_more_than_two(1, 2, 3, 4, 5, 6)

# %% {"tags": ["code-along"]}
add_more_than_two(1, 2)


# %% {"tags": ["code-along"]}
# add_more_than_two(1)

# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "slide"}}
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Any number of named arguments:
#
# Likewise, a function can have any number of named arguments:

# %% {"tags": ["code-along"]}
def my_keys(**kwargs):
    print("Keyword arguments:", kwargs)


# %% {"tags": ["code-along"]}
my_keys(x=1, y=2)


# %% [markdown] {"lang": "de"}
# Es ist möglich diese beiden Features zu kombinieren:

# %% [markdown] {"lang": "en"}
# It is possible to combine these two features:

# %% {"tags": ["code-along"]}
def takes_arbitrary_args(*args, **kwargs):
    print("Positional argsuments:", args)
    print("Keyword arguments:    ", kwargs)


# %% {"tags": ["code-along"]}
takes_arbitrary_args(1, "foo", a="alpha", b="beta")


# %% [markdown] {"lang": "de", "slideshow": {"slide_type": "subslide"}}
#
# ## Micro-Workshop
#
# Schreiben Sie eine Funktion `print_named_lines(**kwargs)`, die beliebig viele
# Keyword-Argumente bekommt und sie in folgender Form auf dem Bildschirm
# ausgibt:
# ```python
# >>> print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")
# Key: foo -- value: My Foo
# Key: bar -- value: My Bar
# Key: quux -- value: My Quux
# ```


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Micro workshop
#
# Write a function `print_named_lines(**kwargs)` that can take any number of
# Keyword arguments and prints them in the following form:
# ```python
# >>> print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")
# Key: foo -- value: My Foo
# Key: bar -- value: My Bar
# Key: quux -- value: My Quux
# ```

# %% {"tags": ["code-along"]}
def print_named_lines(**kwargs):
    for k, v in kwargs.items():
        print("Key:", k, "-- value:", v)


# %% {"tags": ["code-along"]}
print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")


# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## "Splicing" von Argumenten
#
# - Wenn man eine Liste `args` hat, kann man die darin enthaltenen Werte mit
#   der Syntax `*args` als positionale Argumente übergeben.
# - Wenn man ein Dictionary `kwargs` hat, kann man die Key/Value-Paare mit der
#   Syntax `**kwargs` als benannte Argumente übergeben:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## "Splicing" of arguments
#
# - If you have a list `args`, you can pass its values as positional arguments using the syntax `*args`.
# - If you have a dictionary `kwargs`, you can pass its key-value pairs as named arguments with the syntax `**kwargs`:

# %% {"tags": ["code-along"]}
def add(x, y):
    return x + y


# %% {"tags": ["code-along"]}
my_list = [3, 4]

# %% {"tags": ["code-along"]}
# add(my_list)

# %% {"tags": ["code-along"]}
add(my_list[0], my_list[1])

# %% {"tags": ["code-along"]}
add(*my_list)

# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
my_dict = {"a": "alpha", "b": "beta"}

# %% {"tags": ["code-along"]}
takes_arbitrary_args(my_list, my_dict)

# %% {"tags": ["code-along"]}
takes_arbitrary_args(*my_list, **my_dict)

# %% {"tags": ["code-along"]}
takes_arbitrary_args(3, 4, a="alpha", b="beta")

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Mehrere Rückgabewerte
#
# Wie oben gezeigt kann man mehrere Variablen in einem Schritt definieren:

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Multiple return values
#
# As shown above, you can define multiple variables in one step:

# %% {"tags": ["code-along"]}
ergebnis, rest = 10, 2

# %% {"tags": ["code-along"]}
print(ergebnis)
print(rest)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# - Besonders hilfreich ist das für Funktionen die mehrere eng zusammenhängende
#   Werte berechnen.
# - Man kann mit `return wert1, wert2` mehrere Werte zurückgeben

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# - This is particularly useful for functions that are closely related
#   calculate values.
# - You can return multiple values ​​with `return value1, value2`

# %% {"tags": ["code-along"]}
def zwei_werte(a, b):
    return a + 1, b + 2


# %% {"tags": ["code-along"]}
erster_wert, zweiter_wert = zwei_werte(1, 2)
print(erster_wert)
print(zweiter_wert)


# %% {"tags": ["code-along"], "slideshow": {"slide_type": "subslide"}}
def division_mit_rest(m, n):
    ergebnis = m // n
    rest = m % n
    return ergebnis, rest


# %% {"tags": ["code-along"]}
e, r = division_mit_rest(17, 7)
print(e)
print(r)


# %% {"tags": ["code-along"]}
# Kürzer
def division_mit_rest_2(m, n):
    return m // n, m % n


# %% {"tags": ["code-along"]}
e, r = division_mit_rest_2(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# (In Python gibt es die eingebaute Funktion `divmod`, die diese Berechnung ausführt)

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# (Python has a built-in function `divmod` that performs this calculation)

# %% {"tags": ["code-along"]}
e, r = divmod(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Piraten, Teil 3"


# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Section "Pirates, Part 3"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# # Vergleiche, Boole'sche Werte

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# # Comparisons, Boolean values

# %% [markdown] {"lang": "de"}
# Gleichheit von Werten wird mit `==` getestet:

# %% [markdown] {"lang": "en"}
# Equality of values ​​is tested with `==`:

# %% {"tags": ["code-along"]}
1 == 1

# %% {"tags": ["code-along"]}
1 == 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# The result of a comparison is a boolean value
#
# - `True`
# - `False`

# %% {"tags": ["code-along"]}
type(True)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Gleichheit von Zahlen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Equality of numbers

# %% {"tags": ["code-along"]}
1 == 1.0

# %% [markdown] {"lang": "de"}
# Mit Unterstrichen lassen sich Zahlen übersichtlicher schreiben.

# %% [markdown] {"lang": "en"}
# Numbers can be written more clearly with underscores.

# %% {"tags": ["code-along"]}
0.000_000_1 * 10_000_000 == 1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# Vorsicht: Rundungsfehler!

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# Caution: rounding errors!

# %% {"tags": ["code-along"]}
1 / 10

# %% {"tags": ["code-along"]}
1 / 100

# %% {"tags": ["code-along"]}
(1 / 10) * (1 / 10) == (1 / 100)

# %% {"tags": ["code-along"]}
0.1 * 0.1

# %% {"tags": ["code-along"]}
0.1 - 0.01

# %% {"tags": ["code-along"]}
100 * 1.1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Inequality of numbers
#
# The `!=` operator tests whether two numbers are different

# %% {"tags": ["code-along"]}
1 != 1.0

# %% {"tags": ["code-along"]}
1 != 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Vergleich von Zahlen

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Comparison of numbers

# %% {"tags": ["code-along"]}
1 < 2

# %% {"tags": ["code-along"]}
1 < 1

# %% {"tags": ["code-along"]}
1 <= 1

# %% {"incorrectly_encoded_metadata": "{\"slideshow\": {\"slide_type\": \"subslide\"}} tags=[\"code-along\"]"}
1 > 2

# %% {"tags": ["code-along"]}
2 >= 1

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Comparison operators on other types
#
# The comparison operators can also be applied to many other types
# (more details later).

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Operatoren auf Boole'schen Werten
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Operators on Boolean values

# %% {"tags": ["code-along"]}
1 < 2 and 3 < 2

# %% {"tags": ["code-along"]}
1 < 2 or 3 < 2

# %% {"tags": ["code-along"]}
not (1 < 2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Wann ist ein logischer Ausdruck wahr?
#
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ### When is a logical expression true?
#
# | Operator | Operation                      | `True` if...                   |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logical "and" (conjunction)    | both arguments `True`          |
# | or       | logical "or" (disjunction)     | at least one argument `True`   |
# | not      | logical "not" (negation)       | argument `False`               |

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ### Verkettung von Vergleichen

# %% [markdown] {"lang": "en"}
# ### Chaining comparisons

# %% {"tags": ["code-along"]}
1 < 2 < 3

# %% {"tags": ["code-along"]}
# noinspection PyChainedComparisons
1 < 2 and 2 < 3

# %% {"tags": ["code-along"]}
1 < 3 <= 2

# %% {"tags": ["code-along"]}
# noinspection PyChainedComparisons
1 < 3 and 3 <= 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Operatoren, Vergleiche"


# %% [markdown] {"lang": "en"}
# ## Mini workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Section "Operators, Comparisons"

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Struktur einer `if`-Anweisung (unvollständig):
#
# ```python
# if <Bedingung>:
#     Rumpf, der ausgeführt wird, wenn Bedingung 1 wahr ist
# else:
#     Rumpf, der ausgeführt wird, wenn keine der Bedingungen wahr ist
# ```
# - Nur das `if` und der erste Rumpf sind notwendig
# - Falls ein `else` vorhanden ist, so darf der entsprechende Rumpf nicht leer sein
#

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "slide"}}
# ## Structure of an `if` statement (incomplete):
#
# ```python
# if <Bedingung>:
#     # Body that runs if condition 1 is true
# else:
#     # Body that is executed if none of the conditions are true
# ```
# - Only the `if` and the first body are necessary
# - If an `else` is present, the corresponding body must not be empty

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "lang": "de"}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Volljährig"

# %% [markdown] {"lang": "en", "slideshow": {"slide_type": "subslide"}}
# ## Mini workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Section "Adult"
