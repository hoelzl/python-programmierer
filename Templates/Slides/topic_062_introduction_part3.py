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
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# j2 import 'macros.j2' as doc
# %% [markdown] slideshow={"slide_type": "slide"}
# {{ doc.header("Einführung in Python: Grundlagen Teil 3") }}


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Beliebig viele Argumente:
#
# Man kann Funktionen definieren, die beliebig viele Argumente bekommen können:

# %% tags=["code-along"]
def my_add(*args):
    result = 0
    for i in args:
        result += i
    return result


# %% tags=["code-along"]
my_add(1, 2, 3, 4, 5, 6)


# %% [markdown]
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

# %% tags=["code-along"]
def print_lines(*args):
    for arg in args:
        print(arg)


# %% tags=["code-along"]
print_lines("hey", "you")


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Das kann auch mit anderen Argumenten kombiniert werden:

# %% tags=["code-along"]
def add_more_than_two(x, y, *more_args):
    result = x + y
    for i in more_args:
        result += i
    return result


# %% tags=["code-along"]
add_more_than_two(1, 2, 3, 4, 5, 6)

# %% tags=["code-along"]
add_more_than_two(1, 2)


# %% tags=["code-along"]
# add_more_than_two(1)

# %% [markdown]
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %% tags=["code-along"]
def my_keys(**kwargs):
    print("Keyword arguments:", kwargs)


# %% tags=["code-along"]
my_keys(x=1, y=2)


# %% [markdown]
# Es ist möglich diese beiden Features zu kombinieren:

# %% tags=["code-along"]
def takes_arbitrary_args(*args, **kwargs):
    print("Positional argsuments:", args)
    print("Keyword arguments:    ", kwargs)


# %% tags=["code-along"]
takes_arbitrary_args(1, "foo", a="alpha", b="beta")


# %% [markdown]
#
# ## Micro-Workshop
#
# Schreiben Sie eine Funktion `print_named_lines(**kwargs)`, die beliebig viele
# Keyword-Argumente bekommt und sie in folgender Form auf dem Bildschirm
# ausgibt:
# >>> print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")
# Key: foo -- value: My Foo
# Key: bar -- value: My Bar
# Key: quux -- value: My Quux


# %% tags=["code-along"]
def print_named_lines(**kwargs):
    for k, v in kwargs.items():
        print("Key:", k, "-- value:", v)


# %% tags=["code-along"]
print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")


# %% [markdown]
# ## "Splicing" von Argumenten
#
# - Wenn man eine Liste `args` hat, kann man die darin enthaltenen Werte mit
#   der Syntax `*args` als positionale Argumente übergeben.
# - Wenn man ein Dictionary `kwargs` hat, kann man die Key/Value-Paare mit der
#   Syntax `**kwargs` als benannte Argumente übergeben:

# %% tags=["code-along"]
def add(x, y):
    return x + y


# %% tags=["code-along"]
my_list = [3, 4]

# %% tags=["code-along"]
# add(my_list)

# %% tags=["code-along"]
add(my_list[0], my_list[1])

# %% tags=["code-along"]
add(*my_list)

# %% tags=["code-along"]
my_dict = {"a": "alpha", "b": "beta"}

# %% tags=["code-along"]
takes_arbitrary_args(my_list, my_dict)

# %% tags=["code-along"]
takes_arbitrary_args(*my_list, **my_dict)

# %% tags=["code-along"]
takes_arbitrary_args(3, 4, a="alpha", b="beta")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Mehrere Rückgabewerte
#
# Wie oben gezeigt kann man mehrere Variablen in einem Schritt definieren:

# %% tags=["code-along"]
ergebnis, rest = 10, 2

# %% tags=["code-along"]
print(ergebnis)
print(rest)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Besonders hilfreich ist das für Funktionen die mehrere eng zusammenhängende
#   Werte berechnen.
# - Man kann mit `return wert1, wert2` mehrere Werte zurückgeben

# %% tags=["code-along"]
def zwei_werte(a, b):
    return a + 1, b + 2


# %% tags=["code-along"]
erster_wert, zweiter_wert = zwei_werte(1, 2)
print(erster_wert)
print(zweiter_wert)


# %% tags=["code-along"]
def division_mit_rest(m, n):
    ergebnis = m // n
    rest = m % n
    return ergebnis, rest


# %% tags=["code-along"]
e, r = division_mit_rest(17, 7)
print(e)
print(r)


# %% tags=["code-along"]
# Kürzer
def division_mit_rest_2(m, n):
    return m // n, m % n


# %% tags=["code-along"]
e, r = division_mit_rest_2(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# (In Python gibt es die eingebaute Funktion `divmod`, die diese Berechnung
# ausführt:)

# %% tags=["code-along"]
e, r = divmod(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_050_introduction_part1`
# - Abschnitt "Piraten, Teil 3"


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Vergleiche, Boole'sche Werte

# %% [markdown]
# Gleichheit von Werten wird mit `==` getestet:

# %% tags=["code-along"]
1 == 1

# %% tags=["code-along"]
1 == 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %% tags=["code-along"]
type(True)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Gleichheit von Zahlen

# %% tags=["code-along"]
1 == 1.0

# %% [markdown]
# Mit Unterstrichen lassen sich Zahlen übersichtlicher schreiben.

# %% tags=["code-along"]
0.000_000_1 * 10_000_000 == 1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Vorsicht: Rundungsfehler!

# %% tags=["code-along"]
1 / 10

# %% tags=["code-along"]
1 / 100

# %% tags=["code-along"]
(1 / 10) * (1 / 10) == (1 / 100)

# %% tags=["code-along"]
0.1 * 0.1

# %% tags=["code-along"]
0.1 - 0.01

# %% tags=["code-along"]
100 * 1.1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %% tags=["code-along"]
1 != 1.0

# %% tags=["code-along"]
1 != 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Vergleich von Zahlen

# %% tags=["code-along"]
1 < 2

# %% tags=["code-along"]
1 < 1

# %% tags=["code-along"]
1 <= 1

# %% {"slideshow": {"slide_type": "subslide"}} tags=["code-along"]
1 > 2

# %% tags=["code-along"]
2 >= 1

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Operatoren auf Boole'schen Werten
#

# %% tags=["code-along"]
1 < 2 and 3 < 2

# %% tags=["code-along"]
1 < 2 or 3 < 2

# %% tags=["code-along"]
not (1 < 2)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Wann ist ein logischer Ausdruck wahr?
#
# | Operator | Operation                      | `True` wenn...                 |
# |:--------:|:-------------------------------|:-------------------------------|
# | and      | logisches "Und" (Konjunktion)  | beide Argumente `True`         |
# | or       | logisches "Oder" (Disjunktion) | mindestens ein Argument `True` |
# | not      | logisches "Nicht" (Negation)   | Argument `False`               |

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Verkettung von Vergleichen

# %% tags=["code-along"]
1 < 2 < 3

# %% tags=["code-along"]
# noinspection PyChainedComparisons
1 < 2 and 2 < 3

# %% tags=["code-along"]
1 < 3 <= 2

# %% tags=["code-along"]
# noinspection PyChainedComparisons
1 < 3 and 3 <= 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Operatoren, Vergleiche"


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Mini-Workshop
#
# - Notebook `workshop_060_introduction_part2`
# - Abschnitt "Volljährig"
