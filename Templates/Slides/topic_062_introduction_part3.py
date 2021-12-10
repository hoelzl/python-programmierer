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
# %% [markdown] {{ doc.slide() }}
# {{ doc.header("Einführung in Python: Grundlagen Teil 3") }}


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Beliebig viele Argumente:
#
# Man kann Funktionen definieren, die beliebig viele Argumente bekommen können:

# %% {{ doc.codealong() }}
def my_add(*args):
    result = 0
    for i in args:
        result += i
    return result


# %% {{ doc.codealong() }}
my_add(1, 2, 3, 4, 5, 6)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Das kann auch mit anderen Argumenten kombiniert werden:

# %% {{ doc.codealong() }}
def add_more_than_two(x, y, *more_args):
    result = x + y
    for i in more_args:
        result += i
    return result


# %% {"slideshow": {"slide_type": "slide"}} {{ doc.codealong() }}
add_more_than_two(1, 2, 3, 4, 5, 6)

# %% {{ doc.codealong() }}
add_more_than_two(1, 2)


# %% {{ doc.codealong() }}
# add_more_than_two(1)

# %% [markdown]
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %% {{ doc.codealong() }}
def my_keys(**kwargs):
    print("Keyword arguments:", kwargs)


# %% {{ doc.codealong() }}
my_keys(x=1, y=2)


# %% [markdown]
# Es ist möglich diese beiden Features zu kombinieren:

# %% {{ doc.codealong() }}
def takes_arbitrary_args(*args, **kwargs):
    print("Positional argsuments:", args)
    print("Keyword arguments:    ", kwargs)


# %% {{ doc.codealong() }}
takes_arbitrary_args(1, "foo", a="alpha", b="beta")


# %% [markdown]
# ## "Splicing" von Argumenten
#
# - Wenn man eine Liste `args` hat, kann man die darin enthaltenen Werte mit
#   der Syntax `*args` als positionale Argumente übergeben.
# - Wenn man ein Dictionary `kwargs` hat, kann man die Key/Value-Paare mit der
#   Syntax `**kwargs` als benannte Argumente übergeben:

# %% {{ doc.codealong() }}
def add(x, y):
    return x + y


# %% {{ doc.codealong() }}
my_list = [3, 4]

# %% {{ doc.codealong() }}
# add(my_list)

# %% {{ doc.codealong() }}
add(my_list[0], my_list[1])

# %% {{ doc.codealong() }}
add(*my_list)

# %% {{ doc.codealong() }}
my_dict = {"a": "alpha", "b": "beta"}

# %% {{ doc.codealong() }}
takes_arbitrary_args(my_list, my_dict)

# %% {{ doc.codealong() }}
takes_arbitrary_args(*my_list, **my_dict)

# %% {{ doc.codealong() }}
takes_arbitrary_args(3, 4, a="alpha", b="beta")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Mehrere Rückgabewerte
#
# Wie oben gezeigt kann man mehrere Variablen in einem Schritt definieren:

# %% {{ doc.codealong() }}
ergebnis, rest = 10, 2

# %% {{ doc.codealong() }}
print(ergebnis)
print(rest)


# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# - Besonders hilfreich ist das für Funktionen die mehrere eng zusammenhängende
#   Werte berechnen.
# - Man kann mit `return wert1, wert2` mehrere Werte zurückgeben

# %% {{ doc.codealong() }}
def zwei_werte(a, b):
    return a + 1, b + 2


# %% {{ doc.codealong() }}
erster_wert, zweiter_wert = zwei_werte(1, 2)
print(erster_wert)
print(zweiter_wert)


# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
def division_mit_rest(m, n):
    ergebnis = m // n
    rest = m % n
    return ergebnis, rest


# %% {{ doc.codealong() }}
e, r = division_mit_rest(17, 7)
print(e)
print(r)


# %% {"slideshow": {"slide_type": ""}} {{ doc.codealong() }}
# Kürzer
def division_mit_rest_2(m, n):
    return m // n, m % n


# %% {{ doc.codealong() }}
e, r = division_mit_rest_2(17, 7)
print(e)
print(r)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# (In Python gibt es die eingebaute Funktion `divmod`, die diese Berechnung
# ausführt:)

# %% {{ doc.codealong() }}
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

# %% {{ doc.codealong() }}
1 == 1

# %% {{ doc.codealong() }}
1 == 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Das Ergebnis eines Vergleichs ist ein Boole'scher Wert (Wahrheitswert)
#
# - `True`
# - `False`

# %% {{ doc.codealong() }}
type(True)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Gleichheit von Zahlen

# %% {{ doc.codealong() }}
1 == 1.0

# %% [markdown]
# Mit Unterstrichen lassen sich Zahlen übersichtlicher schreiben.

# %% {{ doc.codealong() }}
0.000_000_1 * 10_000_000 == 1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# Vorsicht: Rundungsfehler!

# %% {{ doc.codealong() }}
1 / 10

# %% {{ doc.codealong() }}
1 / 100

# %% {{ doc.codealong() }}
(1 / 10) * (1 / 10) == (1 / 100)

# %% {{ doc.codealong() }}
0.1 * 0.1

# %% {{ doc.codealong() }}
0.1 - 0.01

# %% {{ doc.codealong() }}
100 * 1.1

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Ungleichheit von Zahlen
#
# Der Operator `!=` testet, ob zwei Zahlen verschieden sind

# %% {{ doc.codealong() }}
1 != 1.0

# %% {{ doc.codealong() }}
1 != 2

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Vergleich von Zahlen

# %% {{ doc.codealong() }}
1 < 2

# %% {{ doc.codealong() }}
1 < 1

# %% {{ doc.codealong() }}
1 <= 1

# %% {"slideshow": {"slide_type": "subslide"}} {{ doc.codealong() }}
1 > 2

# %% {{ doc.codealong() }}
2 >= 1

# %% [markdown] {"pycharm": {"name": "#%% md\n"}, "slideshow": {"slide_type": "slide"}}
# ## Vergleichsoperatoren auf anderen Typen
#
# Die Vergleichsoperatoren lassen sich auch auf viele andere Typen anwenden
# (genaueres später).

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Operatoren auf Boole'schen Werten
#

# %% {{ doc.codealong() }}
1 < 2 and 3 < 2

# %% {{ doc.codealong() }}
1 < 2 or 3 < 2

# %% {{ doc.codealong() }}
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

# %% {{ doc.codealong() }}
1 < 2 < 3

# %% {{ doc.codealong() }}
# noinspection PyChainedComparisons
1 < 2 and 2 < 3

# %% {{ doc.codealong() }}
1 < 3 <= 2

# %% {{ doc.codealong() }}
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
